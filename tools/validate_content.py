"""Checks the content packs in content/text/: every English text also exists in
Hindi and Bengali, no text is empty, and every concept and case names a source.

Run:  python tools/validate_content.py        (exit code 1 on any problem)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("en", "hi", "bn")
problems = []


def walk(node, where):
    if isinstance(node, dict):
        if "en" in node and isinstance(node["en"], str):
            for l in LANGS:
                if not str(node.get(l, "")).strip():
                    problems.append(f"{where}: missing or empty '{l}'")
            return
        if "en" in node and isinstance(node["en"], dict) and all(isinstance(v, str) for v in node["en"].values()):
            # a block of UI strings: { en: {key: text}, hi: {...}, bn: {...} }
            for l in LANGS[1:]:
                other = node.get(l, {})
                for k in node["en"]:
                    if not str(other.get(k, "")).strip():
                        problems.append(f"{where}.{l}: missing key '{k}'")
            for k, v in node["en"].items():
                if not v.strip():
                    problems.append(f"{where}.en: empty key '{k}'")
            return
        for k, v in node.items():
            walk(v, f"{where}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{where}[{i}]")


def main():
    files = sorted((ROOT / "content" / "text").rglob("*.json"))
    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except ValueError as e:
            problems.append(f"{rel}: not valid JSON ({e})")
            continue
        walk(data, rel)
        for i, c in enumerate(data.get("concepts", [])):
            if not str(c.get("source", "")).strip():
                problems.append(f"{rel}: concept {c.get('id', i)} has no source")
        for i, c in enumerate(data.get("cases", [])):
            if not c.get("sources"):
                problems.append(f"{rel}: case {c.get('id', i)} has no sources")
    for p in problems:
        print("PROBLEM", p)
    print(f"{len(files)} files checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
