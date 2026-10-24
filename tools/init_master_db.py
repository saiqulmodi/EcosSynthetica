import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic_master.db")

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Chapters & Syllabus Catalog Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS syllabus_catalog (
        batch_id INTEGER,
        batch_name TEXT,
        sub_batch_id INTEGER,
        chapter_key TEXT PRIMARY KEY,
        chapter_title TEXT,
        subject TEXT,
        grade INTEGER,
        target_volume INTEGER
    );
    """)

    # 2. Master Questions Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY,
        chapter_key TEXT NOT NULL,
        subject TEXT NOT NULL,
        grade INTEGER NOT NULL,
        q_type TEXT NOT NULL, -- 'mcq_fact', 'assertion_reason', 'match_list', 'numerical'
        question TEXT NOT NULL,
        opt_a TEXT NOT NULL,
        opt_b TEXT NOT NULL,
        opt_c TEXT NOT NULL,
        opt_d TEXT NOT NULL,
        answer_idx INTEGER NOT NULL CHECK(answer_idx BETWEEN 0 AND 3),
        explanation TEXT NOT NULL,
        difficulty INTEGER DEFAULT 2, -- 1 (Easy) to 5 (Hard)
        FOREIGN KEY (chapter_key) REFERENCES syllabus_catalog(chapter_key)
    );
    """)

    # 3. High Performance Indexes for Quick Fetching and Filtering
    cur.execute("CREATE INDEX IF NOT EXISTS idx_q_chapter ON questions(chapter_key);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_q_subject_grade ON questions(subject, grade);")

    # 4. Insert Batch 1, Batch 2, and Batch 3 Mapping
    batches = [
        # Batch 1: High-Weightage Biology (Target: 750 Qs each)
        (1, "Batch 1: High-Weightage Biology", 1, "bio_11_cell_unit_of_life", "Cell: The Unit of Life", "Biology", 11, 750),
        (1, "Batch 1: High-Weightage Biology", 2, "bio_11_cell_cycle_division", "Cell Cycle and Cell Division", "Biology", 11, 750),
        (1, "Batch 1: High-Weightage Biology", 3, "bio_12_principles_of_inheritance", "Principles of Inheritance and Variation", "Biology", 12, 750),
        (1, "Batch 1: High-Weightage Biology", 4, "bio_12_molecular_basis_inheritance", "Molecular Basis of Inheritance", "Biology", 12, 750),
        (1, "Batch 1: High-Weightage Biology", 5, "bio_12_biotechnology_principles", "Biotechnology: Principles and Processes", "Biology", 12, 750),

        # Batch 2: Core Physical & Organic Chemistry (Target: 700 Qs each)
        (2, "Batch 2: Core Chemistry", 1, "chem_11_chemical_bonding", "Chemical Bonding and Molecular Structure", "Chemistry", 11, 700),
        (2, "Batch 2: Core Chemistry", 2, "chem_11_thermodynamics", "Thermodynamics", "Chemistry", 11, 700),
        (2, "Batch 2: Core Chemistry", 3, "chem_11_equilibrium", "Equilibrium (Physical & Chemical)", "Chemistry", 11, 700),
        (2, "Batch 2: Core Chemistry", 4, "chem_12_aldehydes_ketones_acids", "Aldehydes, Ketones and Carboxylic Acids", "Chemistry", 12, 700),

        # Batch 3: Core Physics (Target: 500 Qs each)
        (3, "Batch 3: Core Physics", 1, "phy_11_laws_of_motion", "Laws of Motion", "Physics", 11, 500),
        (3, "Batch 3: Core Physics", 2, "phy_11_work_energy_power", "Work, Energy and Power", "Physics", 11, 500),
        (3, "Batch 3: Core Physics", 3, "phy_12_current_electricity", "Current Electricity", "Physics", 12, 500),
        (3, "Batch 3: Core Physics", 4, "phy_12_ray_optics", "Ray Optics and Optical Instruments", "Physics", 12, 500)
       # Batch 4: Human Physiology & Zoology (Target: 750 Qs each)
        (4, "Batch 4: Human Physiology & Zoology", 1, "bio_12_human_reproduction", "Human Reproduction", "Biology", 12, 750),
        (4, "Batch 4: Human Physiology & Zoology", 2, "bio_11_body_fluids_circulation", "Body Fluids and Circulation", "Biology", 11, 750),
        (4, "Batch 4: Human Physiology & Zoology", 3, "bio_11_excretory_products", "Excretory Products and Their Elimination", "Biology", 11, 750),
        (4, "Batch 4: Human Physiology & Zoology", 4, "bio_11_neural_coordination", "Neural Control and Coordination", "Biology", 11, 750)
    ]

    cur.executemany("""
    INSERT OR REPLACE INTO syllabus_catalog 
    (batch_id, batch_name, sub_batch_id, chapter_key, chapter_title, subject, grade, target_volume)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, batches)

    conn.commit()
    conn.close()
    print("Academic Master SQLite initialized with all 3 batches and 13 sub-batches.")

if __name__ == "__main__":
    setup_database()