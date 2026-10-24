"""Upgraded build_quiz.py: builds js/quizbank.js from the NEET Data Hub.

Extracts questions across Classes 1-12 with structured coverage of:
- Biology (Microbiology, Cell, Genetics, Ecology, Physiology)
- Chemistry (Solutions, Acids/Bases, Biomolecules, Equilibrium)
- Physics (Motion, Optics/Microscopy, Energy, Fluids)

Outputs UTF-8 encoded JavaScript with options and explanations intact.
"""
import json
import random
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HUB = Path(r"C:\Users\saiqu\Projects\NEET_Data_Hub\output\neet_hub.db")
OUT = ROOT / "js" / "quizbank.js"

# Number of questions per gameplay form (increased from 80 to 200 for deep variety)
PER_FORM = 200

# Mapping of curriculum chapters to Ecos-Synthetica forms:
# Form 0: Micro-world, Cytology, Microbial Biochemistry & Optics
# Form 1: Plant Ecology, Photosynthesis, Thermodynamics & Solutions
# Form 2: Animalia, Invertebrates, Mechanics, Acids & Bases
# Form 3: Genetics, Evolution, Human Health, Organic Biomolecules
FORM_SPECS = {
    0: {
        "neet_prefixes": ["b11-02", "b11-08", "b12-08", "b12-09", "c11-01", "p12-09"],
        "class9_10": [
            "Cell: structure and functions",
            "Cell division (counting cells and chromosomes)",
            "Mirrors and lenses",
            "Refraction and refractive index",
            "Concentration of solutions",
            "Structure of the atom"
        ],
        "lower_foundations": [
            "Microorganisms: friend and foe",
            "Cell: structure and functions",
            "Materials around us"
        ]
    },
    1: {
        "neet_prefixes": ["b11-03", "b11-05", "b11-11", "b11-13", "b12-01", "b12-11", "b12-12", "c11-06", "c12-02"],
        "class9_10": [
            "Life processes",
            "Our environment: food chains and energy flow",
            "Work, energy and power",
            "Improvement in food resources",
            "Matter and its states"
        ],
        "lower_foundations": [
            "Photosynthesis and respiration in plants",
            "Nutrition in plants",
            "Crop production and management",
            "Seeds and germination"
        ]
    },
    2: {
        "neet_prefixes": ["b11-04", "b11-07", "b12-11", "b12-12", "b12-13", "p11-05", "p11-07"],
        "class9_10": [
            "Diversity in living organisms",
            "Density, pressure and buoyancy",
            "Force, momentum and Newton's laws",
            "Acids, bases and salts",
            "Displacement reactions (reactivity series)"
        ],
        "lower_foundations": [
            "Honeybees",
            "Insects and small creatures",
            "Flowers and pollination",
            "Food habits of animals",
            "Where animals live (habitats)"
        ]
    },
    3: {
        "neet_prefixes": ["b12-05", "b12-06", "b12-07", "b11-14", "b11-15", "b11-16", "c12-14", "c11-08"],
        "class9_10": [
            "Heredity: Mendelian crosses",
            "Heredity: ratios and sex determination",
            "Evolution",
            "Why do we fall ill (diseases)",
            "Carbon compounds: homologous series and naming",
            "Control and coordination"
        ],
        "lower_foundations": [
            "Why do we fall ill (diseases)",
            "Good habits, health and hygiene",
            "Famous Indians in science and environment"
        ]
    }
}


def clean_text(val):
    if not val:
        return ""
    # Standardize quotes and dashes to prevent encoding glitches
    s = str(val).strip()
    s = s.replace("\u2014", "—").replace("\u2013", "–")
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return s


def build_form_bank(con, spec, rng, limit=PER_FORM):
    questions = []

    # 1. Fetch NEET Class 11-12 questions matching chapter prefixes
    neet_clauses = " OR ".join(["q.chapter_id LIKE ?" for _ in spec["neet_prefixes"]])
    params = [f"{p}%" for p in spec["neet_prefixes"]]
    query_neet = f"""
        SELECT q.id, q.class_level, c.title, c.subject,
               q.question, q.option_a, q.option_b, q.option_c, q.option_d,
               q.correct_option, q.explanation
        FROM questions q
        JOIN chapters c ON c.id = q.chapter_id
        WHERE q.class_level >= 11 AND ({neet_clauses})
    """
    rows_neet = con.execute(query_neet, params).fetchall()

    # 2. Fetch Class 9 & 10 Foundations
    placeholders_9_10 = ",".join(["?"] * len(spec["class9_10"]))
    query_9_10 = f"""
        SELECT q.id, q.class_level, c.title, c.subject,
               q.question, q.option_a, q.option_b, q.option_c, q.option_d,
               q.correct_option, q.explanation
        FROM questions q
        JOIN chapters c ON c.id = q.chapter_id
        WHERE q.class_level IN (9, 10) AND c.title IN ({placeholders_9_10})
    """
    rows_9_10 = con.execute(query_9_10, spec["class9_10"]).fetchall()

    # 3. Fetch Class 1-8 Lower Foundations
    placeholders_lower = ",".join(["?"] * len(spec["lower_foundations"]))
    query_lower = f"""
        SELECT q.id, q.class_level, c.title, c.subject,
               q.question, q.option_a, q.option_b, q.option_c, q.option_d,
               q.correct_option, q.explanation
        FROM questions q
        JOIN chapters c ON c.id = q.chapter_id
        WHERE q.class_level <= 8 AND c.title IN ({placeholders_lower})
    """
    rows_lower = con.execute(query_lower, spec["lower_foundations"]).fetchall()

    # Quota allocation to ensure high-yield balance:
    # 50% NEET (11-12), 30% Foundation (9-10), 20% Basics (1-8)
    n_neet = int(limit * 0.50)
    n_9_10 = int(limit * 0.30)
    n_lower = limit - n_neet - n_9_10

    sample_neet = rng.sample(rows_neet, min(n_neet, len(rows_neet))) if rows_neet else []
    sample_9_10 = rng.sample(rows_9_10, min(n_9_10, len(rows_9_10))) if rows_9_10 else []
    sample_lower = rng.sample(rows_lower, min(n_lower, len(rows_lower))) if rows_lower else []

    all_sampled = sample_neet + sample_9_10 + sample_lower
    rng.shuffle(all_sampled)

    for row in all_sampled:
        qid, cls, topic, subject, q_text, opt_a, opt_b, opt_c, opt_d, corr, expl = row
        opt_map = {"A": opt_a, "B": opt_b, "C": opt_c, "D": opt_d}
        correct_text = opt_map.get(str(corr).strip().upper(), opt_a)
        wrong_opts = [clean_text(v) for k, v in opt_map.items() if k != str(corr).strip().upper() and v]

        # Put correct answer first (Quiz.js options() shuffles opts dynamically at runtime)
        opts = [clean_text(correct_text)] + wrong_opts[:3]
        if len(opts) < 4:
            continue

        questions.append({
            "id": int(qid),
            "cls": int(cls),
            "subject": clean_text(subject),
            "topic": clean_text(topic),
            "q": clean_text(q_text),
            "opts": opts,
            "ans": 0,
            "why": clean_text(expl) or f"Correct answer: {opts[0]}."
        })

    return questions[:limit]


def main():
    if not HUB.exists():
        print(f"Error: Database not found at {HUB}")
        sys.exit(1)

    con = sqlite3.connect(HUB)
    rng = random.Random(42)
    bank_data = {}

    print("Building multi-subject question bank...")
    for form_id, spec in FORM_SPECS.items():
        bank_data[str(form_id)] = build_form_bank(con, spec, rng, limit=PER_FORM)
        print(f"  Form {form_id}: {len(bank_data[str(form_id)])} questions compiled.")

    con.close()

    # Write output file in UTF-8
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// Generated by tools/build_quiz.py from NEET Data Hub. Do not edit by hand.\n")
        f.write("export const BANK = ")
        json.dump(bank_data, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"\nSuccessfully generated {OUT} with UTF-8 encoding.")


if __name__ == "__main__":
    main()