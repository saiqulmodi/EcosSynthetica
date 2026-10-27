"""Builds games/saiqulmodi-ecos-synthetica/ for stratos-games-site.

EcosSynthetica is a pure Three.js game (no pygbag), so the box just:
  - bundles three.module.js locally (no CDN call at runtime)
  - strips Google Fonts links (system fonts fallback)
  - strips Firebase Analytics (loads from gstatic.com — external)

Run:  python tools/make_stratos_box.py [box folder]
"""
import os, re, shutil, sys, urllib.request

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.expanduser("~"), "OneDrive", "Desktop", "stratos-games-site", "games",
    "saiqulmodi-ecos-synthetica")
CACHE = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
                     "EcosSynthetica", "engine_cache")
os.makedirs(CACHE, exist_ok=True)

THREE_URL   = "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"
THREE_CACHE = os.path.join(CACHE, "three.module.js")

if not os.path.exists(THREE_CACHE):
    print("Downloading three.module.js …")
    with urllib.request.urlopen(THREE_URL, timeout=180) as r, \
         open(THREE_CACHE + ".part", "wb") as f:
        shutil.copyfileobj(r, f)
    os.replace(THREE_CACHE + ".part", THREE_CACHE)

os.makedirs(BOX, exist_ok=True)
cdn_dir = os.path.join(BOX, "cdn")
os.makedirs(cdn_dir, exist_ok=True)
shutil.copyfile(THREE_CACHE, os.path.join(cdn_dir, "three.module.js"))

for folder in ("js", "data"):
    dst = os.path.join(BOX, folder)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(os.path.join(PROJECT, folder), dst)

html = open(os.path.join(PROJECT, "index.html"), encoding="utf-8").read()

html = html.replace(
    '"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"',
    '"./cdn/three.module.js"'     # an import map needs ./ (a bare cdn/ path is refused)
)

html = re.sub(r'<link rel="preconnect" href="https://fonts\.[^"]*"[^>]*>\n?', '', html)
html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^"]*"[^>]*>\n?', '', html)

html = re.sub(
    r'[ \t]*<!-- Firebase Analytics.*?</script>\n?',
    '',
    html,
    flags=re.DOTALL
)

open(os.path.join(BOX, "index.html"), "w", encoding="utf-8").write(html)

leftover = re.findall(r"https?://(?!www\.w3\.org)[^\s\"'<>)]+", html)
total = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(BOX) for f in fs)
print("remaining external URLs in index.html:", leftover)
print(f"box size: {total / 1024 / 1024:.2f} MB")
