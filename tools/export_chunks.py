import sqlite3
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "tools", "academic_master.db")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "chapters")
MANIFEST_PATH = os.path.join(BASE_DIR, "data", "manifest.json")

def export_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Generate Manifest
    cur.execute("""
    SELECT batch_id, batch_name, sub_batch_id, chapter_key, chapter_title, subject, grade, target_volume
    FROM syllabus_catalog
    ORDER BY batch_id, sub_batch_id;
    """)
    rows = cur.fetchall()

    manifest = []
    for r in rows:
        cur.execute("SELECT COUNT(*) FROM questions WHERE chapter_key = ?", (r[3],))
        current_count = cur.fetchone()[0]

        manifest.append({
            "batch_id": r[0],
            "batch_name": r[1],
            "sub_batch_id": r[2],
            "chapter_key": r[3],
            "chapter_title": r[4],
            "subject": r[5],
            "grade": r[6],
            "target_volume": r[7],
            "current_volume": current_count,
            "file": f"data/chapters/{r[3]}.json"
        })

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Manifest written to: {MANIFEST_PATH}")

    # 2. Export Each Chapter's Questions to JSON
    total_exported = 0
    for item in manifest:
        ckey = item["chapter_key"]
        cur.execute("""
        SELECT id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty
        FROM questions
        WHERE chapter_key = ?;
        """, (ckey,))
        q_rows = cur.fetchall()

        q_list = []
        for q in q_rows:
            q_list.append({
                "id": q[0],
                "chapter_key": q[1],
                "subject": q[2],
                "grade": q[3],
                "type": q[4],
                "question": q[5],
                "options": [q[6], q[7], q[8], q[9]],
                "answer": q[10],
                "explanation": q[11],
                "difficulty": q[12],
                "reward": { "energy": 25, "xp": 15 }
            })

        out_file = os.path.join(OUTPUT_DIR, f"{ckey}.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(q_list, f, indent=2)

        if len(q_list) > 0:
            print(f"Exported {len(q_list)} questions -> {out_file}")
            total_exported += len(q_list)

    conn.close()
    print(f"Finished chunk export. Total questions ready for game: {total_exported}")

if __name__ == "__main__":
    export_all()