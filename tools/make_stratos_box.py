"""Builds games/saiqulmodi-ecos-synthetica/ for stratos-games-site.

The box gets exactly the files the game ships (the same list tools/check_size.py
counts), with nothing loaded from outside the folder:
  - Three.js is already local (vendor/three.module.min.js)
  - Google Fonts links are removed (system fonts take over)
game.json and thumbnail.png in the box are kept as they are (this script updates
game.json's text only when --game-json is given). Then it runs the stratos.games
checks it can run: size under 20 MB, no outside scripts or tracking, no mobile
app ad IDs, title / how_to_play / 800x500 cover present.

Run:  python tools/make_stratos_box.py [box folder] [--game-json]
"""
import fnmatch
import json
import os
import re
import shutil
import struct
import subprocess
import sys

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
BOX = args[0] if args else os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop", "stratos-games-site", "games",
                                        "saiqulmodi-ecos-synthetica")
KEEP = {"game.json", "thumbnail.png"}

sys.path.insert(0, os.path.join(PROJECT, "tools"))
from check_size import shipped  # noqa: E402  (same file list as the 20 MB check)

files = [rel for rel, _ in shipped()]

# Fresh box: remove every old file except the box's own game.json and cover
# (file by file: OneDrive can lock folders; empty folders are tidied when possible).
os.makedirs(BOX, exist_ok=True)
want = {os.path.normcase(os.path.join(BOX, *rel.split("/"))) for rel in files}
for root, dirs, fs in os.walk(BOX, topdown=False):
    for f in fs:
        p = os.path.join(root, f)
        if os.path.relpath(p, BOX) in KEEP or os.path.normcase(p) in want:
            continue
        os.remove(p)
    for d in dirs:
        try:
            os.rmdir(os.path.join(root, d))
        except OSError:
            pass

for rel in files:
    dst = os.path.join(BOX, *rel.split("/"))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(os.path.join(PROJECT, *rel.split("/")), dst)

for page in ("index.html", "teacher.html"):
    path = os.path.join(BOX, page)
    if not os.path.exists(path):
        continue
    html = open(path, encoding="utf-8").read()
    html = re.sub(r'<link rel="preconnect" href="https://fonts\.[^"]*"[^>]*>\n?', "", html)
    html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^"]*"[^>]*>\n?', "", html)
    open(path, "w", encoding="utf-8", newline="\n").write(html)

if "--game-json" in sys.argv:
    gj_path = os.path.join(BOX, "game.json")
    gj = json.load(open(gj_path, encoding="utf-8")) if os.path.exists(gj_path) else {}
    gj.update(json.load(open(os.path.join(PROJECT, "tools", "stratos_game.json"), encoding="utf-8")))
    json.dump(gj, open(gj_path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=2)

# ---------- stratos.games checks ----------
problems = []
total = 0
outside = set()
for root, _, fs in os.walk(BOX):
    for f in fs:
        p = os.path.join(root, f)
        total += os.path.getsize(p)
        if f.endswith((".html", ".js", ".css")):
            text = open(p, encoding="utf-8", errors="ignore").read()
            if "ca-app-pub-" in text:
                problems.append(f"mobile app ad ID in {os.path.relpath(p, BOX)}")
            # Script or stylesheet loaded from another site (plain links the player taps are fine).
            for m in re.finditer(r"""(?:<script[^>]+src|<link[^>]+href|import\s*\(?\s*|\.src\s*=\s*|fetch\s*\(\s*)['"](https?://[^'"]+)""", text):
                outside.add(f"{os.path.relpath(p, BOX)}: {m.group(1)}")
            if re.search(r"googletagmanager|google-analytics|(?<![A-Za-z])gtag\(|goatcounter|firebase", text, re.I):
                problems.append(f"tracking code in {os.path.relpath(p, BOX)}")
if total > 20 * 1024 * 1024:
    problems.append(f"box is {total / 1048576:.1f} MB (limit 20 MB)")
problems += [f"outside script/style: {o}" for o in sorted(outside)]
gj = json.load(open(os.path.join(BOX, "game.json"), encoding="utf-8")) if os.path.exists(os.path.join(BOX, "game.json")) else {}
for k in ("title", "how_to_play"):
    if not str(gj.get(k, "")).strip():
        problems.append(f"game.json has no {k}")
thumb = os.path.join(BOX, "thumbnail.png")
if not os.path.exists(thumb):
    problems.append("no thumbnail.png")
else:
    w, h = struct.unpack(">II", open(thumb, "rb").read(24)[16:24])
    if (w, h) != (800, 500):
        problems.append(f"thumbnail.png is {w}x{h} (want 800x500)")

print(f"box: {BOX}")
print(f"files: {len(files)}  size: {total / 1048576:.2f} MB")
print("checks:", "all passed" if not problems else "")
for p in problems:
    print("  PROBLEM", p)
sys.exit(1 if problems else 0)
