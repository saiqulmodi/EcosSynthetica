"""Checks the 20 MB limit: adds up every file the game ships (website, zip, app)
and fails if the total is over 20 MB or any part is over its budget.

Run:  python tools/check_size.py        (exit code 1 when over)
"""
import fnmatch
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MB = 1024 * 1024
LIMIT = 20 * MB

# Not shipped: tools, docs, servers, native app projects, build files.
SKIP_DIRS = {".git", "tools", "docs", "server", "android", "www", "node_modules", "__pycache__"}
SKIP_FILES = ["*.py", "*.pyc", "*.bat", "*.bak", "package.json", "package-lock.json",
              "capacitor.config.json", "README.md", ".gitignore", "*.md"]

# Budget rows: first matching pattern wins.
ROWS = [
    ("engine", 1.3, ["vendor/three*"]),
    ("audio", 6.0, ["content/audio/*"]),
    ("fonts", 0.6, ["fonts/*"]),
    ("datasets", 1.5, ["content/datasets/*"]),
    ("questions", 5.0, ["content/questions/*", "data/*", "questions.json"]),
    ("text", 2.5, ["js/lang/*", "content/text/*", "js/tiers/*/text*.js", "js/ai/concepts*.js"]),
    ("images", 0.5, ["*.svg", "*.png", "*.jpg", "*.webp", "*.ico"]),
    ("code", 1.5, ["*"]),
]


def shipped():
    # Files git tracks plus new files git would add (respects .gitignore).
    out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout.splitlines()
    for rel in sorted(set(out)):
        parts = rel.split("/")
        if parts[0] in SKIP_DIRS or any(fnmatch.fnmatch(parts[-1], pat) for pat in SKIP_FILES):
            continue
        f = ROOT / rel
        if f.is_file():
            yield rel, f.stat().st_size


def main():
    totals = {name: 0 for name, _, _ in ROWS}
    biggest = []
    for rel, size in shipped():
        for name, _, pats in ROWS:
            if any(fnmatch.fnmatch(rel, p) for p in pats):
                totals[name] += size
                break
        biggest.append((size, rel))
    total = sum(totals.values())
    bad = False
    print(f"{'part':<10} {'used':>8} {'budget':>8}")
    for name, budget, _ in ROWS:
        over = totals[name] > budget * MB
        bad |= over
        print(f"{name:<10} {totals[name] / MB:>7.2f}M {budget:>7.1f}M {'OVER' if over else ''}")
    print(f"{'TOTAL':<10} {total / MB:>7.2f}M {LIMIT / MB:>7.1f}M {'OVER' if total > LIMIT else 'ok'}")
    print("largest files:", ", ".join(f"{r} {s / MB:.2f}M" for s, r in sorted(biggest, reverse=True)[:5]))
    return 1 if bad or total > LIMIT else 0


if __name__ == "__main__":
    sys.exit(main())
