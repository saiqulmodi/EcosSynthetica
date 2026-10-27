"""Ecos-Synthetica school server (optional, Advanced).

One small program a school runs on a teacher's laptop or a server:
  * serves the game itself, so students open http://<this-computer>:8770/
  * school sync: class codes, students join with a code, module results only
    (no clicks, no events, no location, no email) - SQLite file
  * live AI proxy for Eco Scientist / Eco Professional: holds the Claude API
    key (never sent to browsers), rate-limits per class, strips personal data,
    and answers only from the checked concept texts the game sends

Nothing here is needed to play: if the server is off or unreachable the game
uses its offline Mentor and keeps progress on the device.

Run:
  set ECOS_TEACHER_KEY=choose-a-secret          (needed to create classes and read class progress)
  set ANTHROPIC_API_KEY=...                       (only for the live AI; leave unset to keep it off)
  python server/ecos_server.py [--port 8770] [--db server/ecos_school.db]

REST API (/api/v1, JSON):
  GET  /health                                   -> { ok, ai }
  POST /classes            (teacher key)  { name, grade }               -> { id, joinCode }
  POST /auth/join                         { classCode, displayName }    -> { token, userId, classId }
  GET  /classes/<id>/assignments                                        -> [ { moduleId, dueOn } ]
  POST /classes/<id>/assignments (teacher) { moduleId, dueOn }          -> { ok }
  PUT  /progress           (student token) [ { moduleId, status, stars, bestScore } ]  -> { saved }
  GET  /classes/<id>/progress (teacher key)                             -> { students, modules, rows }
  POST /mentor/ask         (student token) { question, register, lang, concepts: [ {id, title, text, source} ] }
                                                                        -> { answer, sources } or 503 when the AI is off
  GET  /content/manifest                                                -> { files: { path: size } }
"""
import argparse
import hashlib
import json
import os
import re
import secrets
import sqlite3
import sys
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
GAME_DIRS = ("js", "css", "content", "vendor", "data", "fonts")
GAME_FILES = ("index.html", "teacher.html", "sw.js", "questions.json")

SCHEMA = """
CREATE TABLE IF NOT EXISTS class_group (id INTEGER PRIMARY KEY, name TEXT NOT NULL, grade TEXT, join_code TEXT UNIQUE NOT NULL, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS app_user (id INTEGER PRIMARY KEY, class_id INTEGER NOT NULL REFERENCES class_group(id), display_name TEXT NOT NULL,
  token_hash TEXT UNIQUE NOT NULL, created_at TEXT NOT NULL, UNIQUE (class_id, display_name));
CREATE TABLE IF NOT EXISTS progress_snapshot (user_id INTEGER NOT NULL REFERENCES app_user(id), module_id TEXT NOT NULL, status TEXT, stars INTEGER,
  best_score REAL, synced_at TEXT NOT NULL, PRIMARY KEY (user_id, module_id));
CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY, class_id INTEGER NOT NULL REFERENCES class_group(id), module_id TEXT NOT NULL, due_on TEXT);
"""

# Models from the design document: a fast, low-cost model for the AI Teacher,
# a stronger one for the Research Assistant.
MODELS = {"scientist": "claude-haiku-5-5", "professional": "claude-sonnet-5-5"}
ASKS_PER_HOUR = 60          # per class code
MAX_QUESTION = 500          # characters

PERSONA = {
    "scientist": "You are the AI Teacher in Ecos-Synthetica for Class 11-12 students in India. Use NCERT terms, give equations where useful, and end with one short question back to the student.",
    "professional": "You are the AI Research Assistant in Ecos-Synthetica for college students and professionals (MBBS, engineering, agriculture, forestry, environmental science). Use professional terms and numbers with units.",
}
RULES = (
    "Answer only from the concept notes provided in the user's message and cite their sources by name. "
    "If the notes do not cover the question, say that you do not have a checked answer and suggest a related topic from the notes. "
    "Never invent figures. Keep to 120 words. Answer in the language code given ({lang}: en English, hi Hindi, bn Bengali). "
    "Respect nature-first framing: organisms are described by their own survival story first; countered organisms are contained, never destroyed."
)

now = lambda: time.strftime("%Y-%m-%dT%H:%M:%S")
token_hash = lambda t: hashlib.sha256(t.encode()).hexdigest()

# Personal data a student might type by mistake is removed before anything leaves the school.
PII = [re.compile(p) for p in (r"[\w.+-]+@[\w-]+\.[\w.]+", r"(?<!\d)(?:\+?91[\s-]?)?[6-9]\d{9}(?!\d)", r"\b\d{4}\s?\d{4}\s?\d{4}\b")]


def strip_pii(text, names=()):
    for p in PII:
        text = p.sub("[removed]", text)
    for n in names:
        if n and len(n) > 1:
            text = re.sub(re.escape(n), "[student]", text, flags=re.IGNORECASE)
    return text


class Store:
    def __init__(self, path):
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)
        self.lock = threading.Lock()

    def q(self, sql, args=(), one=False):
        with self.lock:
            cur = self.db.execute(sql, args)
            self.db.commit()
            rows = cur.fetchall()
        return (rows[0] if rows else None) if one else rows

    def create_class(self, name, grade):
        code = "-".join(secrets.token_hex(2).upper() for _ in range(2))
        self.q("INSERT INTO class_group (name, grade, join_code, created_at) VALUES (?,?,?,?)", (name, grade, code, now()))
        return self.q("SELECT id, join_code FROM class_group WHERE join_code=?", (code,), one=True)

    def join(self, code, name):
        c = self.q("SELECT id FROM class_group WHERE join_code=?", (code.upper().strip(),), one=True)
        if not c:
            return None
        token = secrets.token_urlsafe(24)
        existing = self.q("SELECT id FROM app_user WHERE class_id=? AND display_name=?", (c["id"], name), one=True)
        if existing:  # re-joining on a new device: the old token stops working
            self.q("UPDATE app_user SET token_hash=? WHERE id=?", (token_hash(token), existing["id"]))
            uid = existing["id"]
        else:
            self.q("INSERT INTO app_user (class_id, display_name, token_hash, created_at) VALUES (?,?,?,?)", (c["id"], name, token_hash(token), now()))
            uid = self.q("SELECT id FROM app_user WHERE class_id=? AND display_name=?", (c["id"], name), one=True)["id"]
        return {"token": token, "userId": uid, "classId": c["id"]}

    def user(self, token):
        if not token:
            return None
        return self.q("SELECT u.id, u.class_id, u.display_name, c.join_code FROM app_user u JOIN class_group c ON c.id=u.class_id WHERE token_hash=?",
                      (token_hash(token),), one=True)


class AI:
    """Live model through the official Anthropic SDK. Off when no key is set."""

    def __init__(self):
        self.client = None
        self.calls = {}
        if os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"):
            try:
                import anthropic
                self.anthropic = anthropic
                self.client = anthropic.Anthropic(max_retries=2, timeout=30.0)
            except Exception as e:  # SDK missing: stay offline
                print("Live AI off:", e, file=sys.stderr)

    def allowed(self, class_code):
        t = time.time()
        recent = [x for x in self.calls.get(class_code, []) if t - x < 3600]
        if len(recent) >= ASKS_PER_HOUR:
            self.calls[class_code] = recent
            return False
        recent.append(t)
        self.calls[class_code] = recent
        return True

    def request(self, question, register, lang, concepts):
        notes = "\n\n".join(f"[{c.get('title', c.get('id', ''))}] (source: {c.get('source', '')})\n{c.get('text', '')}" for c in concepts[:4])
        system = PERSONA[register] + " " + RULES.format(lang=lang)
        user = f"Concept notes:\n{notes or '(none matched)'}\n\nStudent question ({lang}):\n{question}"
        return {"model": MODELS[register], "system": system, "messages": [{"role": "user", "content": user}]}

    def ask(self, question, register, lang, concepts):
        req = self.request(question, register, lang, concepts)
        if register == "professional":
            # Claude Sonnet 5.5: if a safety classifier declines, the API retries on a fallback model in the same call.
            resp = self.client.beta.messages.create(max_tokens=2000, output_config={"effort": "low"},
                                                     betas=["server-side-fallback-2026-07-01"], fallbacks="default", **req)
        else:
            resp = self.client.messages.create(max_tokens=2000, output_config={"effort": "low"}, **req)
        if resp.stop_reason == "refusal":
            return None
        text = "".join(b.text for b in resp.content if b.type == "text").strip()
        return {"answer": text, "sources": [c.get("source", "") for c in concepts[:4] if c.get("source")]} if text else None


class Handler(SimpleHTTPRequestHandler):
    store = None
    ai = None
    teacher_key = ""
    origins = set()

    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def log_message(self, fmt, *args):  # no request logs: nothing about students is written out
        pass

    # ---------- helpers ----------
    def cors(self):
        origin = self.headers.get("Origin", "")
        if origin and origin in self.origins:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Teacher-Key")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")

    def send_json(self, code, data):
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.cors()
        self.end_headers()
        self.wfile.write(body)

    def body(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n > 64 * 1024:
            raise ValueError("too large")
        return json.loads(self.rfile.read(n) or b"null")

    def bearer(self):
        h = self.headers.get("Authorization", "")
        return self.store.user(h[7:].strip()) if h.startswith("Bearer ") else None

    def is_teacher(self):
        k = self.headers.get("X-Teacher-Key", "")
        return bool(self.teacher_key) and secrets.compare_digest(k, self.teacher_key)

    # ---------- routing ----------
    def do_OPTIONS(self):
        self.send_response(204)
        self.cors()
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path.startswith("/api/v1/"):
            return self.api("GET", path[7:])
        first = path.strip("/").split("/")[0]
        if path in ("/", "") or first in GAME_DIRS or first in GAME_FILES:
            return super().do_GET()
        self.send_error(404)

    def do_POST(self):
        path = urlparse(self.path).path
        return self.api("POST", path[7:]) if path.startswith("/api/v1/") else self.send_error(404)

    def do_PUT(self):
        path = urlparse(self.path).path
        return self.api("PUT", path[7:]) if path.startswith("/api/v1/") else self.send_error(404)

    def api(self, method, route):
        try:
            return self.route(method, route)
        except (ValueError, KeyError, TypeError, json.JSONDecodeError):
            return self.send_json(400, {"error": "bad request"})

    def route(self, method, route):
        s = self.store
        m = re.fullmatch(r"/classes/(\d+)/(assignments|progress)", route)
        if method == "GET" and route == "/health":
            return self.send_json(200, {"ok": True, "ai": bool(self.ai.client)})
        if method == "POST" and route == "/classes":
            if not self.is_teacher():
                return self.send_json(403, {"error": "teacher key needed"})
            b = self.body()
            c = s.create_class(str(b["name"])[:60], str(b.get("grade", ""))[:12])
            return self.send_json(200, {"id": c["id"], "joinCode": c["join_code"]})
        if method == "POST" and route == "/auth/join":
            b = self.body()
            name = re.sub(r"\s+", " ", str(b["displayName"])).strip()[:24]
            if not name:
                return self.send_json(400, {"error": "name needed"})
            r = s.join(str(b["classCode"]), name)
            return self.send_json(200, r) if r else self.send_json(404, {"error": "unknown class code"})
        if m and m.group(2) == "assignments":
            cid = int(m.group(1))
            if method == "GET":
                u = self.bearer()
                if not (self.is_teacher() or (u and u["class_id"] == cid)):
                    return self.send_json(403, {"error": "not in this class"})
                rows = s.q("SELECT module_id, due_on FROM assignment WHERE class_id=? ORDER BY due_on", (cid,))
                return self.send_json(200, [{"moduleId": r["module_id"], "dueOn": r["due_on"]} for r in rows])
            if method == "POST":
                if not self.is_teacher():
                    return self.send_json(403, {"error": "teacher key needed"})
                b = self.body()
                s.q("INSERT INTO assignment (class_id, module_id, due_on) VALUES (?,?,?)", (cid, str(b["moduleId"])[:60], str(b.get("dueOn", ""))[:10]))
                return self.send_json(200, {"ok": True})
        if m and m.group(2) == "progress" and method == "GET":
            if not self.is_teacher():
                return self.send_json(403, {"error": "teacher key needed"})
            cid = int(m.group(1))
            rows = s.q("SELECT u.display_name, p.module_id, p.status, p.stars, p.best_score, p.synced_at FROM app_user u "
                       "LEFT JOIN progress_snapshot p ON p.user_id=u.id WHERE u.class_id=? ORDER BY u.display_name, p.module_id", (cid,))
            students = sorted({r["display_name"] for r in rows})
            modules = sorted({r["module_id"] for r in rows if r["module_id"]})
            return self.send_json(200, {"students": students, "modules": modules, "rows": [dict(r) for r in rows if r["module_id"]]})
        if method == "PUT" and route == "/progress":
            u = self.bearer()
            if not u:
                return self.send_json(401, {"error": "join a class first"})
            rows = self.body()
            if not isinstance(rows, list) or len(rows) > 200:
                raise ValueError
            for r in rows:
                status = str(r.get("status", ""))[:12]
                if status not in ("done", "tried", "open", "locked"):
                    status = "tried"
                s.q("INSERT INTO progress_snapshot (user_id, module_id, status, stars, best_score, synced_at) VALUES (?,?,?,?,?,?) "
                    "ON CONFLICT(user_id, module_id) DO UPDATE SET status=excluded.status, stars=excluded.stars, best_score=excluded.best_score, synced_at=excluded.synced_at",
                    (u["id"], str(r["moduleId"])[:60], status, max(0, min(3, int(r.get("stars") or 0))), max(0.0, min(1.0, float(r.get("bestScore") or 0))), now()))
            return self.send_json(200, {"saved": len(rows)})
        if method == "POST" and route == "/mentor/ask":
            u = self.bearer()
            if not u:
                return self.send_json(401, {"error": "join a class first"})
            if not self.ai.client:
                return self.send_json(503, {"error": "live AI is off"})
            b = self.body()
            register = b.get("register")
            if register not in MODELS:
                return self.send_json(400, {"error": "live AI is only for Eco Scientist and Eco Professional"})
            if not self.ai.allowed(u["join_code"]):
                return self.send_json(429, {"error": "class limit reached, try later"})
            question = strip_pii(str(b["question"])[:MAX_QUESTION], [u["display_name"]])
            lang = b.get("lang") if b.get("lang") in ("en", "hi", "bn") else "en"
            concepts = [{k: strip_pii(str(c.get(k, ""))[:3000]) for k in ("id", "title", "text", "source")} for c in (b.get("concepts") or [])[:4]]
            try:
                r = self.ai.ask(question, register, lang, concepts)
            except Exception as e:  # any API problem: the game falls back to the offline Mentor
                print("AI error:", type(e).__name__, file=sys.stderr)
                return self.send_json(502, {"error": "live AI unavailable"})
            return self.send_json(200, r) if r else self.send_json(502, {"error": "no answer"})
        if method == "GET" and route == "/content/manifest":
            files = {}
            for d in ("content",):
                for f in (ROOT / d).rglob("*.json"):
                    files[f.relative_to(ROOT).as_posix()] = f.stat().st_size
            return self.send_json(200, {"files": files})
        return self.send_json(404, {"error": "not found"})


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--port", type=int, default=8770)
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--db", default=str(Path(__file__).with_name("ecos_school.db")))
    ap.add_argument("--allow-origin", action="append", default=[], help="extra web origin allowed to call the API (e.g. the GitHub Pages address)")
    a = ap.parse_args()
    Handler.store = Store(a.db)
    Handler.ai = AI()
    Handler.teacher_key = os.environ.get("ECOS_TEACHER_KEY", "")
    Handler.origins = set(a.allow_origin)
    srv = ThreadingHTTPServer((a.host, a.port), Handler)
    print(f"Ecos-Synthetica school server on http://localhost:{a.port}/  (live AI {'on' if Handler.ai.client else 'off'}; "
          f"teacher key {'set' if Handler.teacher_key else 'NOT set: classes cannot be created'})")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
