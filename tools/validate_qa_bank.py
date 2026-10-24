import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "neet_academic_bank.json")

def validate():
    if not os.path.exists(DATA_FILE):
        print(f"File not found: {DATA_FILE}")
        sys.exit(1)

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    ids = set()
    errors = 0

    for i, item in enumerate(data):
        qid = item.get("id")
        if not qid:
            print(f"[Error] Item at index {i} has no 'id'")
            errors += 1
        elif qid in ids:
            print(f"[Error] Duplicate ID detected: {qid}")
            errors += 1
        else:
            ids.add(qid)

        opts = item.get("options", [])
        if len(opts) != 4:
            print(f"[Error] {qid} does not have exactly 4 options")
            errors += 1

        ans = item.get("answer")
        if ans not in [0, 1, 2, 3]:
            print(f"[Error] {qid} has invalid answer index: {ans}")
            errors += 1

    if errors == 0:
        print(f"Success: {len(data)} questions validated cleanly with 0 errors.")
    else:
        print(f"Validation finished with {errors} errors.")

if __name__ == "__main__":
    validate()