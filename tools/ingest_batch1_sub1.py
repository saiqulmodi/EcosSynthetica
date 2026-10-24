import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic_master.db")

QUESTIONS = [
    (
        "BIO_11_CELL_001",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "Who proposed the cell theory modification stating 'Omnis cellula-e cellula' (all cells arise from pre-existing cells)?",
        "Matthias Schleiden",
        "Theodore Schwann",
        "Rudolf Virchow",
        "Robert Brown",
        2,
        "Rudolf Virchow in 1855 first explained that cells divide and new cells are formed from pre-existing cells ('Omnis cellula-e cellula').",
        1
    ),
    (
        "BIO_11_CELL_002",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "Which of the following cellular components is non-membrane bound and found in both prokaryotic and eukaryotic cells?",
        "Lysosome",
        "Ribosome",
        "Peroxisome",
        "Endoplasmic Reticulum",
        1,
        "Ribosomes are non-membrane bound organelles found in all living cells—both prokaryotes (70S) and eukaryotes (80S).",
        1
    ),
    (
        "BIO_11_CELL_003",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "What is the typical diameter range of mitochondria according to NCERT?",
        "0.2 - 1.0 µm (average 0.5 µm)",
        "1.0 - 4.1 µm",
        "0.02 - 0.2 µm",
        "5.0 - 10.0 µm",
        0,
        "NCERT states mitochondria are sausage-shaped or cylindrical having a diameter of 0.2-1.0 µm (average 0.5 µm) and length 1.0-4.1 µm.",
        2
    ),
    (
        "BIO_11_CELL_004",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "According to Singer and Nicolson's Fluid Mosaic Model (1972), what provides fluidity to the plasma membrane?",
        "Peripheral proteins",
        "Quasi-fluid nature of lipid bilayer",
        "Cholesterol anchored tightly",
        "Rigid carbohydrate chains",
        1,
        "The quasi-fluid nature of lipids enables lateral movement of proteins within the overall bilayer, which defines membrane fluidity.",
        2
    ),
    (
        "BIO_11_CELL_005",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "assertion_reason",
        "Statement I: The endomembrane system includes ER, Golgi complex, lysosomes, and vacuoles.\nStatement II: Mitochondria, chloroplasts, and peroxisomes are coordinated with the endomembrane system.",
        "Both Statement I and Statement II are correct",
        "Both Statement I and Statement II are incorrect",
        "Statement I is correct, but Statement II is incorrect",
        "Statement I is incorrect, but Statement II is correct",
        2,
        "Statement I is correct. Statement II is incorrect because functions of mitochondria, chloroplasts, and peroxisomes are not coordinated with ER/Golgi, so they are excluded from the endomembrane system.",
        3
    ),
    (
        "BIO_11_CELL_006",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "Which face of the Golgi apparatus is the 'forming face' that receives transition vesicles from the endoplasmic reticulum?",
        "Trans or maturing face",
        "Cis or convex forming face",
        "Medial cisternae",
        "Secretory vesicle face",
        1,
        "Cis (convex) face is the forming face oriented toward the nucleus/ER, while trans (concave) face is the maturing/shipping face.",
        2
    ),
    (
        "BIO_11_CELL_007",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "Hydrolytic enzymes of lysosomes (hydrolases) are maximally active at which environmental pH?",
        "Neutral pH (7.0)",
        "Alkaline pH (8.5)",
        "Acidic pH (~4.5 - 5.0)",
        "Extremely basic pH (12.0)",
        2,
        "Lysosomal enzymes (lipases, proteases, carbohydrases) are optimized to function under acidic conditions maintained by proton pumps.",
        2
    ),
    (
        "BIO_11_CELL_008",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "In plant cells, what percentage of cell volume can be occupied by the central vacuole?",
        "Up to 30%",
        "Up to 50%",
        "Up to 70%",
        "Up to 90%",
        3,
        "In plant cells, the central vacuole bound by the semi-permeable tonoplast can occupy up to 90 percent of the total cellular volume.",
        1
    ),
    (
        "BIO_11_CELL_009",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "What is the sedimentation coefficient (S) known as, and what does it indirectly measure?",
        "Stahl unit; measures DNA density",
        "Svedberg unit; indirectly measures density and size",
        "Singer coefficient; measures lipid fluid velocity",
        "Schleiden unit; measures cell wall thickness",
        1,
        "'S' stands for Svedberg unit, representing the sedimentation coefficient, which is an indirect measurement of density and size.",
        2
    ),
    (
        "BIO_11_CELL_010",
        "bio_11_cell_unit_of_life",
        "Biology",
        11,
        "mcq_fact",
        "What is the arrangement of peripheral doublet microtubules and central microtubules in a eukaryotic cilium or flagellum axoneme?",
        "9 + 0 array",
        "9 + 2 array",
        "8 + 2 array",
        "9 + 3 triplets",
        1,
        "The eukaryotic axoneme possesses 9 pairs of radially arranged peripheral doublets and one central pair of singlet microtubules (9 + 2 array). Centrioles have 9 + 0 triplets.",
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
    cur.execute("SELECT COUNT(*) FROM questions WHERE chapter_key = 'bio_11_cell_unit_of_life';")
    count = cur.fetchone()[0]
    conn.close()
    print(f"Ingested {len(QUESTIONS)} questions. Total in bio_11_cell_unit_of_life: {count}")

if __name__ == "__main__":
    ingest()