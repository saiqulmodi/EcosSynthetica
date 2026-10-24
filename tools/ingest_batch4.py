import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic_master.db")

BATCH4_QUESTIONS = [
    # Human Reproduction (Class 12)
    ("BIO_12_REP_001", "bio_12_human_reproduction", "Biology", 12, "mcq_fact",
     "Which cells in the testes secrete testosterone under LH regulation?",
     "Sertoli cells", "Leydig cells (Interstitial cells)", "Spermatogonia", "Secondary spermatocytes",
     1, "Leydig cells located in interstitial spaces produce androgens (principally testosterone) stimulated by LH.", 1),
    ("BIO_12_REP_002", "bio_12_human_reproduction", "Biology", 12, "mcq_fact",
     "Sertoli cells inside seminiferous tubules provide:",
     "Motility to mature sperms", "Nutrition and mechanical support to developing germ cells", "Direct secretion of estrogen", "Acrosome enzymes",
     1, "Sertoli cells act as nurse cells providing structural and nutritional support to developing spermatogenic cells.", 1),
    ("BIO_12_REP_003", "bio_12_human_reproduction", "Biology", 12, "mcq_fact",
     "The acrosome of a mature spermatozoon is derived embryologically from which organelle?",
     "Centriole", "Mitochondria", "Golgi apparatus", "Endoplasmic reticulum",
     2, "The acrosome filled with hydrolytic enzymes is formed from the Golgi apparatus.", 2),
    ("BIO_12_REP_004", "bio_12_human_reproduction", "Biology", 12, "mcq_fact",
     "At which stage is human oogenesis arrested from embryonic development until puberty?",
     "Metaphase II", "Diakinesis", "Prophase I (Diplotene stage)", "Anaphase I",
     2, "Primary oocytes begin meiosis during fetal life and remain suspended at Prophase I (diplotene stage) until puberty.", 2),
    ("BIO_12_REP_005", "bio_12_human_reproduction", "Biology", 12, "mcq_fact",
     "What triggers the secondary oocyte to complete Meiosis II?",
     "LH surge", "Entry of sperm into the vitelline membrane", "Implantation into endometrium", "Progesterone decline",
     1, "Sperm entry into the secondary oocyte triggers the completion of Meiosis II, releasing the second polar body and an ootid.", 2),
    ("BIO_12_REP_006", "bio_12_human_reproduction", "Biology", 12, "mcq_fact",
     "Corpus luteum formed after ovulation primarily secretes high quantities of:",
     "Estrogen", "Progesterone", "FSH", "hCG",
     1, "The ruptured Graafian follicle transforms into the corpus luteum, which secretes large amounts of progesterone to maintain the endometrium.", 1),
    ("BIO_12_REP_007", "bio_12_human_reproduction", "Biology", 12, "mcq_fact",
     "The primary site of human fertilization under physiological conditions is:",
     "Uterus", "Cervix", "Ampullary region of the Fallopian tube", "Infundibulum",
     2, "Fertilization typically occurs in the ampulla (ampullary-isthmic junction region) of the Fallopian tube.", 1),

    # Body Fluids and Circulation (Class 11)
    ("BIO_11_CIRC_001", "bio_11_body_fluids_circulation", "Biology", 11, "mcq_fact",
     "What is the average lifespan of human red blood cells (erythrocytes) before destruction in the spleen?",
     "30 days", "60 days", "120 days", "365 days",
     2, "RBCs have an average lifespan of 120 days, after which they are destroyed in the spleen.", 1),
    ("BIO_11_CIRC_002", "bio_11_body_fluids_circulation", "Biology", 11, "mcq_fact",
     "Which plasma protein is primarily responsible for maintaining intravascular colloid osmotic pressure?",
     "Fibrinogen", "Albumin", "Globulin", "Heparin",
     1, "Albumins make up ~60% of plasma proteins and generate oncotic pressure to retain fluid inside capillary beds.", 2),
    ("BIO_11_CIRC_003", "bio_11_body_fluids_circulation", "Biology", 11, "mcq_fact",
     "The second heart sound ('dub') during a cardiac cycle is caused by:",
     "Closure of atrioventricular (bicuspid/tricuspid) valves",
     "Closure of semilunar valves at the beginning of ventricular diastole",
     "Rapid opening of semilunar valves",
     "Rush of blood into atria",
     1, "The first heart sound ('lub') is closure of AV valves; the second sound ('dub') is closure of aortic and pulmonary semilunar valves.", 2),
    ("BIO_11_CIRC_004", "bio_11_body_fluids_circulation", "Biology", 11, "mcq_fact",
     "In a standard ECG, the QRS complex represents:",
     "Atrial depolarization", "Ventricular depolarization", "Ventricular repolarization", "Atrial repolarization",
     1, "P-wave = atrial depolarization, QRS complex = ventricular depolarization, T-wave = ventricular repolarization.", 2),
    ("BIO_11_CIRC_005", "bio_11_body_fluids_circulation", "Biology", 11, "mcq_fact",
     "Erythroblastosis fetalis occurs when:",
     "Rh negative mother carries Rh positive fetus",
     "Rh positive mother carries Rh negative fetus",
     "Both mother and fetus are Rh negative",
     "Both mother and fetus are Rh positive",
     0, "An Rh⁻ mother carrying an Rh⁺ fetus can produce anti-Rh antibodies that attack erythrocytes of subsequent Rh⁺ fetuses.", 2),

    # Excretory Products and Their Elimination (Class 11)
    ("BIO_11_EXCR_001", "bio_11_excretory_products", "Biology", 11, "mcq_fact",
     "What is the average daily glomerular filtration rate (GFR) in a healthy human adult?",
     "1.5 liters/day", "18 liters/day", "180 liters/day", "1200 liters/day",
     2, "GFR is ~125 mL/min (~180 L/day). Around 99% is reabsorbed, yielding ~1.5 L of urine per day.", 2),
    ("BIO_11_EXCR_002", "bio_11_excretory_products", "Biology", 11, "mcq_fact",
     "The ascending limb of the loop of Henle is:",
     "Permeable to water but impermeable to electrolytes",
     "Impermeable to water but allows transport of electrolytes (NaCl)",
     "Freely permeable to both water and urea",
     "Completely impermeable to all ions and water",
     1, "The descending limb is permeable to water and impermeable to salts; the ascending limb is impermeable to water and reabsorbs NaCl.", 2),
    ("BIO_11_EXCR_003", "bio_11_excretory_products", "Biology", 11, "mcq_fact",
     "Juxtaglomerular cells release renin in response to:",
     "High arterial blood pressure",
     "Fall in glomerular filtration rate (GFR) or blood volume",
     "Increased sodium delivery to macula densa",
     "Release of Atrial Natriuretic Factor (ANF)",
     1, "A drop in glomerular blood flow/pressure/GFR activates juxtaglomerular cells to release renin, initiating RAAS.", 2),
    ("BIO_11_EXCR_004", "bio_11_excretory_products", "Biology", 11, "mcq_fact",
     "Podocytes with filtration slits are specialized epithelial cells lining:",
     "Parietal layer of Bowman's capsule",
     "Visceral layer of Bowman's capsule wrapping around glomerular capillaries",
     "Proximal Convoluted Tubule (PCT)",
     "Collecting duct",
     1, "Podocytes form the visceral layer of Bowman's capsule, providing filtration slits for ultrafiltration.", 2),

    # Neural Control and Coordination (Class 11)
    ("BIO_11_NEUR_001", "bio_11_neural_coordination", "Biology", 11, "mcq_fact",
     "During resting membrane potential (-70 mV), the axonal membrane is relatively more permeable to:",
     "Sodium ions (Na⁺)", "Potassium ions (K⁺)", "Calcium ions (Ca²⁺)", "Chloride ions (Cl⁻)",
     1, "At rest, the axolemma is substantially more permeable to K⁺ than to Na⁺, allowing K⁺ efflux.", 2),
    ("BIO_11_NEUR_002", "bio_11_neural_coordination", "Biology", 11, "mcq_fact",
     "Depolarization of an axonal membrane during action potential generation is driven by rapid influx of:",
     "K⁺ ions", "Na⁺ ions", "Ca²⁺ ions", "Mg²⁺ ions",
     1, "Voltage-gated Na⁺ channel opening allows inward rush of Na⁺, reversing membrane polarity from -70 mV toward +30 mV.", 1),
    ("BIO_11_NEUR_003", "bio_11_neural_coordination", "Biology", 11, "mcq_fact",
     "The sodium-potassium pump (Na⁺/K⁺ ATPase) transports ions across the resting membrane in which ratio?",
     "2 Na⁺ out for 3 K⁺ in", "3 Na⁺ out for 2 K⁺ in", "3 Na⁺ in for 2 K⁺ out", "1 Na⁺ out for 1 K⁺ in",
     1, "The electrogenic pump consumes 1 ATP to export 3 Na⁺ ions and import 2 K⁺ ions.", 2),
    ("BIO_11_NEUR_004", "bio_11_neural_coordination", "Biology", 11, "mcq_fact",
     "Which part of the human brain contains vital centers controlling cardiovascular reflexes and respiration?",
     "Cerebrum", "Cerebellum", "Medulla oblongata", "Corpus callosum",
     2, "The medulla oblongata contains autonomous centers controlling cardiac rate, breathing, and vasomotor tone.", 2)
]

def ingest_batch4():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executemany("""
    INSERT OR REPLACE INTO questions
    (id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, BATCH4_QUESTIONS)
    conn.commit()
    print(f"Ingested {len(BATCH4_QUESTIONS)} Batch 4 questions.")
    conn.close()

if __name__ == "__main__":
    ingest_batch4()