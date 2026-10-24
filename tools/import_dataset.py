import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic_master.db")

def import_external_json(file_path, chapter_key, subject, grade):
    """Imports raw question arrays from public Kaggle/GitHub dumps into SQLite."""
    if not os.path.exists(file_path):
        print(f"File {file_path} not found. Skipping.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = 0

    for idx, item in enumerate(data):
        qid = item.get("id", f"EXT_{chapter_key.upper()}_{idx+1:05d}")
        qtext = item.get("question")
        opts = item.get("options", [item.get("opa"), item.get("opb"), item.get("opc"), item.get("opd")])
        ans = item.get("answer", item.get("cop", 0))
        expl = item.get("explanation", item.get("exp", "Refer to standard NCERT explanation."))

        if not qtext or len(opts) < 4:
            continue

        cur.execute("""
        INSERT OR REPLACE INTO questions
        (id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (qid, chapter_key, subject, grade, "mcq_fact", qtext, opts[0], opts[1], opts[2], opts[3], ans, expl, 2))
        inserted += 1

    conn.commit()
    conn.close()
    print(f"Bulk imported {inserted} questions into chapter '{chapter_key}'.")

if __name__ == "__main__":
    print("Dataset importer ready. Pass any downloaded JSON to import_external_json().")