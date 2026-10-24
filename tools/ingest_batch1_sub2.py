import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic_master.db")

QUESTIONS = [
    (
        "BIO_11_CYCLE_001",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "In a typical human cell cycle lasting 24 hours, what percentage of the total duration is spent in interphase?",
        "About 25%",
        "About 50%",
        "More than 95%",
        "Exactly 75%",
        2,
        "According to NCERT, human cells divide once every 24 hours. The M-phase lasts for only about an hour, meaning interphase lasts more than 95% of the cell cycle duration.",
        1
    ),
    (
        "BIO_11_CYCLE_002",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "During which sub-stage of interphase does DNA replication take place and the centriole duplicate in the cytoplasm?",
        "G1 Phase (Gap 1)",
        "S Phase (Synthesis)",
        "G2 Phase (Gap 2)",
        "G0 Phase (Quiescent stage)",
        1,
        "During S phase, DNA replication doubles the amount of DNA per cell (from 2C to 4C, chromosome number remains 2n), and centrioles duplicate in the cytoplasm of animal cells.",
        1
    ),
    (
        "BIO_11_CYCLE_003",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "Cells that do not divide further exit G1 phase to enter an inactive stage called:",
        "M Phase",
        "G2 Phase",
        "Quiescent stage (G0)",
        "S Phase",
        2,
        "Cells in the G0 stage remain metabolically active but no longer proliferate unless called upon to do so based on organism requirements.",
        1
    ),
    (
        "BIO_11_CYCLE_004",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "At which stage of mitosis do chromosomes align along the equatorial plate (metaphase plate)?",
        "Prophase",
        "Metaphase",
        "Anaphase",
        "Telophase",
        1,
        "Metaphase is characterized by all replicated chromosomes lying at the equator, with kinetochores attached to spindle fibers from opposite poles.",
        1
    ),
    (
        "BIO_11_CYCLE_005",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "What is the key event that distinguishes Anaphase of mitosis?",
        "Condensation of chromatin",
        "Splitting of centromeres and separation of sister chromatids",
        "Reformation of nuclear envelope",
        "Attachment of spindle fibers to kinetochores",
        1,
        "During anaphase, centromeres split simultaneously and sister chromatids separate, migrating toward opposite spindle poles.",
        2
    ),
    (
        "BIO_11_CYCLE_006",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "Synapsis—the pairing of homologous chromosomes accompanied by the formation of a synaptonemal complex—occurs in which stage of Prophase I?",
        "Leptotene",
        "Zygotene",
        "Pachytene",
        "Diplotene",
        1,
        "Chromosomes start pairing together during zygotene; this pairing process is called synapsis, mediated by the synaptonemal complex.",
        2
    ),
    (
        "BIO_11_CYCLE_007",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "The X-shaped structures formed by non-sister chromatids during the dissolution of the synaptonemal complex in Diplotene are called:",
        "Kinetochores",
        "Centrosomes",
        "Chiasmata",
        "Chromocenters",
        2,
        "The dissolution of the synaptonemal complex occurs in diplotene, leaving homologous chromosomes attached only at the points of crossing over (chiasmata).",
        2
    ),
    (
        "BIO_11_CYCLE_008",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "Terminalisation of chiasmata is the hallmark event of which final stage of Meiosis I Prophase?",
        "Diakinesis",
        "Diplotene",
        "Pachytene",
        "Zygotene",
        0,
        "Diakinesis represents the final stage of meiotic prophase I, marked by terminalisation of chiasmata and disappearance of the nucleolus.",
        2
    ),
    (
        "BIO_11_CYCLE_009",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "assertion_reason",
        "Statement I: Meiosis reduces the chromosome number by half in the resulting gametes.\nStatement II: Meiosis increases genetic variability in populations of organisms from one generation to the next.",
        "Both Statement I and Statement II are correct",
        "Both Statement I and Statement II are incorrect",
        "Statement I is correct, but Statement II is incorrect",
        "Statement I is incorrect, but Statement II is correct",
        0,
        "Both statements are true: Meiosis conserves species chromosome number via halving during gametogenesis and generates variation through crossing over and independent assortment.",
        2
    ),
    (
        "BIO_11_CYCLE_010",
        "bio_11_cell_cycle_division",
        "Biology",
        11,
        "mcq_fact",
        "The short stage between Meiosis I and Meiosis II where DNA replication does NOT occur is known as:",
        "Interphase",
        "Interkinesis",
        "Diakinesis",
        "Metaphase II",
        1,
        "Interkinesis is generally short-lived and occurs between Telophase I and Prophase II. No replication of DNA takes place during interkinesis.",
        2
    )
]

def ingest():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executemany("""
    INSERT OR REPLACE INTO questions 
    (id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, QUESTIONS)

    conn.commit()
    cur.execute("SELECT COUNT(*) FROM questions WHERE chapter_key = 'bio_11_cell_cycle_division';")
    count = cur.fetchone()[0]
    conn.close()
    print(f"Ingested {len(QUESTIONS)} questions. Total in bio_11_cell_cycle_division: {count}")

if __name__ == "__main__":
    ingest()