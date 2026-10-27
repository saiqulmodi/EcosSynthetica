"""Builds the question packs the game loads on demand (content/questions/...).

  scientist/form-0..3.json   the evolve-quiz bank, one file per form
                             (from js/quizbank.js if it is still there, else
                             from the packs already written by build_quiz.py)
  explorer/class-1..10.json  nature questions for Class 1-10 from the
                             School MCQ Bank, tagged with an Explorer module

Run:  python tools/build_packs.py
"""
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "questions"
SCHOOL = Path(r"C:\Users\saiqu\Projects\School_MCQ_Bank\output\mcq_bank.db")
PER_CLASS = 160

# Explorer module for a School MCQ Bank topic (first match wins).
MODULES = [
    ("pollution", r"pollut|waste|garbage|natural resources|clean|recycl|plastic|conserv"),
    ("water", r"water|rain|cloud|river|evaporat|condens"),
    ("foodchain", r"food chain|food web|food habits|producer|consumer|ecosystem|herbivor|carnivor|omnivor"),
    ("biodiversity", r"biodiversity|wildlife|forest|extinct|endanger|species|national park|sanctuar|where animals are found"),
    ("climate", r"climate|weather|season|global warming|energy|sun\b|sun,|greenhouse"),
    ("plants", r"plant|seed|root|leaf|leaves|flower|tree|crop|spice|fruit|vegetable|photosynth|germinat"),
    ("animals", r"animal|bird|insect|honeybee|young ones|habitat|homes|sounds|body covering|ears|creature|egg"),
]
SUBJECTS = ("EVS", "Biology", "Geography", "General Safety")


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return path.stat().st_size


def write_scientist_packs(bank):
    """bank: {"0": [...], ...} in the quizbank.js item format."""
    total = 0
    for form, items in bank.items():
        total += dump(OUT / "scientist" / f"form-{form}.json", items)
        print(f"  scientist form {form}: {len(items)} questions")
    return total


def scientist_from_quizbank():
    src = ROOT / "js" / "quizbank.js"
    if not src.exists():
        print("  js/quizbank.js not present: scientist packs left as they are")
        return 0
    s = src.read_text(encoding="utf-8")
    return write_scientist_packs(json.loads(s[s.index("{"): s.rindex("}") + 1]))


def module_of(topic, question):
    text = f"{topic} {question}".lower()
    for mod, pat in MODULES:
        if re.search(pat, text):
            return mod
    return None


def explorer_packs():
    if not SCHOOL.exists():
        print(f"  School MCQ Bank not found at {SCHOOL}: explorer packs skipped")
        return 0
    con = sqlite3.connect(SCHOOL)
    total = 0
    for cls in range(1, 11):
        rows = con.execute(
            f"SELECT id, subject, topic, question, option_a, option_b, option_c, option_d, correct_option, explanation "
            f"FROM questions WHERE class_level=? AND subject IN ({','.join('?' * len(SUBJECTS))}) ORDER BY id",
            (cls, *SUBJECTS),
        ).fetchall()
        picked, per_mod = [], {}
        for rid, subj, topic, q, a, b, c, d, corr, why in rows:
            mod = module_of(topic, q)
            if not mod:
                continue
            ans = "ABCD".index(str(corr).strip().upper()[:1]) if str(corr).strip()[:1].upper() in "ABCD" else None
            if ans is None:
                continue
            per_mod.setdefault(mod, []).append({"id": rid, "cls": cls, "subject": subj, "topic": topic, "m": mod,
                                                "q": q, "opts": [a, b, c, d], "ans": ans, "why": why or ""})
        # Spread the class's cap across modules so every module has questions.
        mods = sorted(per_mod)
        i = 0
        while len(picked) < PER_CLASS and any(per_mod.values()):
            m = mods[i % len(mods)]
            if per_mod[m]:
                picked.append(per_mod[m].pop(0))
            i += 1
        total += dump(OUT / "explorer" / f"class-{cls}.json", picked)
        counts = {}
        for p in picked:
            counts[p["m"]] = counts.get(p["m"], 0) + 1
        print(f"  explorer class {cls}: {len(picked)} {counts}")
    con.close()
    return total


def main():
    total = scientist_from_quizbank() + explorer_packs()
    print(f"question packs: {total / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    sys.exit(main())
