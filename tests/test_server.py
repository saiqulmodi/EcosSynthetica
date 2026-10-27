"""Checks the optional school server: sync works on and off, teacher-only routes,
personal data stripped, live AI off -> 503 (game falls back), AI request shape.
Run: python tests/test_server.py   (no real API call is made: the AI client is a stand-in)
"""
import json
import sys
import tempfile
import threading
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "server"))
import ecos_server as es  # noqa: E402

fails = 0
def check(name, ok, info=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + (f"  ({info})" if info else ""))
    fails += 0 if ok else 1

tmp = tempfile.mkdtemp()
es.Handler.store = es.Store(str(Path(tmp) / "t.db"))
es.Handler.ai = es.AI.__new__(es.AI)
es.Handler.ai.client = None
es.Handler.ai.calls = {}
es.Handler.teacher_key = "secret-teacher"
es.Handler.origins = set()
srv = ThreadingHTTPServer(("127.0.0.1", 0), es.Handler)
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()

def req(method, path, body=None, token=None, teacher=False):
    h = {"Content-Type": "application/json"}
    if token: h["Authorization"] = "Bearer " + token
    if teacher: h["X-Teacher-Key"] = "secret-teacher"
    r = urllib.request.Request(f"http://127.0.0.1:{port}/api/v1{path}", method=method, headers=h,
                               data=None if body is None else json.dumps(body).encode())
    try:
        with urllib.request.urlopen(r) as res:
            return res.status, json.loads(res.read() or b"null")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"null")

s, h = req("GET", "/health")
check("health answers, live AI reported off", s == 200 and h["ai"] is False)
s, _ = req("POST", "/classes", {"name": "7B"})
check("only a teacher can create a class", s == 403)
s, c = req("POST", "/classes", {"name": "7B", "grade": "7"}, teacher=True)
check("teacher creates a class and gets a join code", s == 200 and len(c["joinCode"]) == 9, c.get("joinCode"))
s, _ = req("POST", "/auth/join", {"classCode": "NOPE-0000", "displayName": "Asha"})
check("unknown class code is refused", s == 404)
s, j = req("POST", "/auth/join", {"classCode": c["joinCode"].lower(), "displayName": "Asha"})
check("student joins with the class code", s == 200 and j["token"] and j["classId"] == c["id"])
s, _ = req("PUT", "/progress", [{"moduleId": "ex_plants", "status": "done", "stars": 3, "bestScore": 0.95}])
check("progress needs a student token", s == 401)
s, r = req("PUT", "/progress", [{"moduleId": "ex_plants", "status": "done", "stars": 3, "bestScore": 0.95}, {"moduleId": "pro_dengue", "status": "tried", "stars": 9, "bestScore": 4}], token=j["token"])
check("student syncs results", s == 200 and r["saved"] == 2)
s, r = req("PUT", "/progress", [{"moduleId": "ex_plants", "status": "done", "stars": 2, "bestScore": 0.7}], token=j["token"])
s, t = req("GET", f"/classes/{c['id']}/progress", teacher=True)
rows = {x["module_id"]: x for x in t["rows"]}
check("teacher sees one row per student and module (upsert)", len(t["rows"]) == 2 and rows["ex_plants"]["stars"] == 2)
check("stars and scores are clamped to valid ranges", rows["pro_dengue"]["stars"] == 3 and rows["pro_dengue"]["best_score"] == 1.0)
s, _ = req("GET", f"/classes/{c['id']}/progress", token=j["token"])
check("students cannot read the class table", s == 403)
req("POST", f"/classes/{c['id']}/assignments", {"moduleId": "pro_aqi", "dueOn": "2026-11-15"}, teacher=True)
s, a = req("GET", f"/classes/{c['id']}/assignments", token=j["token"])
check("student sees class assignments", s == 200 and a == [{"moduleId": "pro_aqi", "dueOn": "2026-11-15"}])
s, _ = req("POST", "/mentor/ask", {"question": "why", "register": "scientist", "lang": "en", "concepts": []}, token=j["token"])
check("live AI off -> 503, so the game uses the offline Mentor", s == 503)

# Live AI on, with a stand-in client that records the request.
seen = {}
class FakeMessages:
    def create(self, **kw):
        seen.update(kw)
        return SimpleNamespace(stop_reason="end_turn", content=[SimpleNamespace(type="text", text="Leaves use light to make sugar.")])
fake = SimpleNamespace(messages=FakeMessages(), beta=SimpleNamespace(messages=FakeMessages()))
es.Handler.ai.client = fake
concept = {"id": "photosynthesis", "title": "Photosynthesis", "text": "6CO2 + 12H2O ...", "source": "NCERT Class 11"}
s, r = req("POST", "/mentor/ask", {"question": "Asha here, mail me at asha@example.com or 9876543210: why light?", "register": "scientist", "lang": "hi", "concepts": [concept]}, token=j["token"])
check("live AI answers through the proxy", s == 200 and r["answer"].startswith("Leaves") and r["sources"] == ["NCERT Class 11"])
user_text = seen["messages"][0]["content"]
check("student name, email and phone never reach the API", "Asha" not in user_text and "asha@" not in user_text and "9876543210" not in user_text)
check("AI Teacher uses the design document's tutoring model", seen["model"] == "claude-haiku-5-5")
check("system prompt limits answers to the checked notes", "Answer only from the concept notes" in seen["system"] and "hi" in seen["system"])
s, r = req("POST", "/mentor/ask", {"question": "x", "register": "professional", "lang": "en", "concepts": [concept]}, token=j["token"])
check("Research Assistant model with refusal fallbacks", seen["model"] == "claude-sonnet-5-5" and seen.get("fallbacks") == "default" and "server-side-fallback-2026-07-01" in seen.get("betas", []))
s, _ = req("POST", "/mentor/ask", {"question": "x", "register": "explorer", "lang": "en", "concepts": []}, token=j["token"])
check("no live AI for Explorer (Class 1-10)", s == 400)
class Refuse(FakeMessages):
    def create(self, **kw):
        return SimpleNamespace(stop_reason="refusal", content=[])
es.Handler.ai.client = SimpleNamespace(messages=Refuse(), beta=SimpleNamespace(messages=Refuse()))
s, _ = req("POST", "/mentor/ask", {"question": "x", "register": "scientist", "lang": "en", "concepts": []}, token=j["token"])
check("a refusal returns no answer (offline Mentor takes over)", s == 502)
es.Handler.ai.calls = {c["joinCode"]: [__import__("time").time()] * es.ASKS_PER_HOUR}
s, _ = req("POST", "/mentor/ask", {"question": "x", "register": "scientist", "lang": "en", "concepts": []}, token=j["token"])
check("per-class hourly limit", s == 429)
with urllib.request.urlopen(f"http://127.0.0.1:{port}/index.html") as res:
    check("server also serves the game", res.status == 200)
try:
    urllib.request.urlopen(f"http://127.0.0.1:{port}/server/ecos_server.py"); check("server files are not served", False)
except urllib.error.HTTPError as e:
    check("server files and the database are not served", e.code == 404)

srv.shutdown()
print(f"\n{fails} check(s) failed" if fails else "\nall checks passed")
sys.exit(1 if fails else 0)
