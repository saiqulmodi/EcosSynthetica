"""Builds the Extra-Edge Q/A bank (Class 8-12 + NEET/MBBS) and removes the Class 1-7 Q/A.

  tools/extraedge/xe_*.py   hand-written questions: SETS = [(subject, topic, [(q, right, [3 wrong], why)])]
  -> content/questions/extraedge/class-8..12.json, neet-mbbs.json, index.json

Every question is checked: 4 different options, the right answer is not among the wrong
ones, and no question repeats, either inside the new bank or against any question already
in the game (explorer, scientist, professional packs and data/*). Repeats are dropped and listed.

Class 1-7: content/questions/explorer/class-1..7.json become empty lists (file names kept,
so the game code is unchanged) and Class 1-7 items are taken out of the scientist packs.

Run:  python tools/build_extraedge.py
"""
import hashlib
import importlib.util
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
Q = ROOT / "content" / "questions"
SRC = ROOT / "tools" / "extraedge"
OUT = Q / "extraedge"
SUBJECT_ORDER = ["Physics", "Chemistry", "Biology", "Botany", "Maths"]


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", str(s).lower())


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def remove_class_1_to_7():
    for c in range(1, 8):
        dump(Q / "explorer" / f"class-{c}.json", [])
    for f in sorted((Q / "scientist").glob("form-*.json")):
        items = load(f)
        kept = [x for x in items if int(x.get("cls", 99)) >= 8]
        if len(kept) != len(items):
            dump(f, kept)
            print(f"  {f.relative_to(ROOT).as_posix()}: removed {len(items) - len(kept)} Class 1-7 items ({len(kept)} left)")
    print("  explorer/class-1..7.json: emptied")


def existing_questions():
    seen = set()
    files = list((Q / "explorer").glob("*.json")) + list((Q / "scientist").glob("*.json")) + list((Q / "professional").glob("neet-*.json"))
    files += [ROOT / "data" / "neet_academic_bank.json", *(ROOT / "data" / "chapters").glob("*.json"), ROOT / "questions.json"]
    for f in files:
        if not f.exists():
            continue
        data = load(f)
        if isinstance(data, dict):
            data = [q for s in data.get("stages", []) for q in s.get("questions", [])]
        for x in data:
            if isinstance(x, dict):
                seen.add(norm(x.get("q") or x.get("question") or x.get("prompt") or ""))
    seen.discard("")
    return seen


def main():
    print("Removing Class 1-7 Q/A")
    remove_class_1_to_7()
    old = existing_questions()
    banks, problems, repeats, mine = {}, [], [], set()
    for f in sorted(SRC.glob("xe_*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        level = getattr(mod, "LEVEL", "")
        key = "neet-mbbs" if level else f"class-{mod.CLS}"
        for subject, topic, items in mod.SETS:
            for n, (q, right, wrong, why) in enumerate(items):
                where = f"{f.name} {subject}/{topic} #{n + 1}"
                opts = [right, *wrong]
                if len(wrong) != 3 or len({str(o).strip() for o in opts}) != 4 or not all(str(o).strip() for o in opts) or not q.strip() or not why.strip():
                    problems.append(where)
                    continue
                k = norm(q)
                if k in mine or k in old:
                    repeats.append(f"{where}: {q}")
                    continue
                mine.add(k)
                rnd = random.Random(int(hashlib.md5(q.encode("utf-8")).hexdigest(), 16))
                rnd.shuffle(opts)
                item = {"id": f"xe-{key}-{hashlib.md5(q.encode('utf-8')).hexdigest()[:8]}", "cls": mod.CLS, "subject": subject,
                        "topic": topic, "q": q, "opts": opts, "ans": opts.index(right), "why": why}
                if level:
                    item["lvl"] = level
                banks.setdefault(key, []).append(item)
    for p in problems:
        print("PROBLEM", p)
    if problems:
        raise SystemExit("fix the questions above")
    for r in repeats:
        print("REPEAT dropped:", r)
    order = [f"class-{c}" for c in range(8, 13)] + ["neet-mbbs"]
    index = []
    for key in order:
        items = sorted(banks.get(key, []), key=lambda x: (SUBJECT_ORDER.index(x["subject"]), x["topic"]))
        dump(OUT / f"{key}.json", items)
        index.append(f"{key}.json")
        by = {s: sum(1 for x in items if x["subject"] == s) for s in SUBJECT_ORDER}
        print(f"  extraedge/{key}.json: {len(items)}  " + ", ".join(f"{s} {n}" for s, n in by.items()))
    dump(OUT / "index.json", index)
    print(f"Extra-Edge total: {sum(len(v) for v in banks.values())} questions, {len(repeats)} repeat(s) dropped")


if __name__ == "__main__":
    main()
