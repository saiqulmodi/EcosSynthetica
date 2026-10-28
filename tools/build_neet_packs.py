"""Builds the NEET & MBBS question packs for the Eco Professional Q/A Bank from neet_hub.db.

Ships only the Class 11-12 NEET questions that are not already in the Scientist form
packs or data/ (qa-bank.html loads those too), so the game stays under 20 MB.
Writes content/questions/professional/neet-<subject>-<class>.json and index.json.
Run again after tools/build_quiz.py rebuilds the Scientist packs.

Run:  python tools/build_neet_packs.py
"""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HUB = Path(r"C:\Users\saiqu\Projects\NEET_Data_Hub\output\neet_hub.db")
OUT = ROOT / "content" / "questions" / "professional"


def shipped_texts():
    have = set()
    for f in (ROOT / "content" / "questions" / "scientist").glob("form-*.json"):
        have.update(q["q"] for q in json.loads(f.read_text(encoding="utf-8")))
    for f in [ROOT / "data" / "neet_academic_bank.json", *(ROOT / "data" / "chapters").glob("*.json")]:
        have.update(q["question"] for q in json.loads(f.read_text(encoding="utf-8-sig")))
    return have


def main():
    have = shipped_texts()
    con = sqlite3.connect(HUB)
    rows = con.execute(
        """select qu.id, qu.class_level, qu.subject, ch.title, qu.question,
                  qu.option_a, qu.option_b, qu.option_c, qu.option_d, qu.correct_option, qu.explanation
           from questions qu join chapters ch on ch.id = qu.chapter_id
           where qu.class_level >= 11 and ch.in_neet = 1 order by qu.id""").fetchall()
    packs, seen = {}, set()
    for qid, cls, subject, topic, text, a, b, c, d, right, why in rows:
        if text in have or text in seen or right not in "ABCD" or not all((a, b, c, d)):
            continue
        seen.add(text)
        packs.setdefault(f"neet-{subject.lower()}-{cls}", []).append(
            {"id": qid, "cls": cls, "subject": subject, "topic": topic, "q": text,
             "opts": [a, b, c, d], "ans": "ABCD".index(right), "why": why or ""})
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("neet-*.json"):
        old.unlink()
    for name, items in sorted(packs.items()):
        (OUT / f"{name}.json").write_text(json.dumps(items, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"{name}.json  {len(items)}")
    (OUT / "index.json").write_text(json.dumps(sorted(f"{n}.json" for n in packs)), encoding="utf-8")
    print("total", sum(len(v) for v in packs.values()))


if __name__ == "__main__":
    main()
