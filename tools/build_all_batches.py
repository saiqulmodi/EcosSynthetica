import sqlite3
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "tools", "academic_master.db")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "chapters")
MANIFEST_PATH = os.path.join(BASE_DIR, "data", "manifest.json")

# Master Syllabus Bank Definition (Batch 1, 2, 3)
CHAPTER_DATA = {
    # BATCH 1: BIOLOGY
    "bio_11_cell_unit_of_life": [
        ("Who proposed 'Omnis cellula-e cellula'?", ["Matthias Schleiden", "Theodore Schwann", "Rudolf Virchow", "Robert Brown"], 2, "Rudolf Virchow in 1855 clarified that cells arise from pre-existing cells."),
        ("Which organelle lacks a membrane and is found in prokaryotes and eukaryotes?", ["Lysosome", "Ribosome", "Peroxisome", "Endoplasmic Reticulum"], 1, "Ribosomes are universal non-membrane-bound ribonucleoprotein particles."),
        ("What is the typical diameter of a mitochondrion?", ["0.2 - 1.0 µm", "1.0 - 4.1 µm", "0.02 - 0.2 µm", "5.0 - 10.0 µm"], 0, "NCERT gives mitochondrial diameter as 0.2-1.0 µm (average 0.5 µm)."),
        ("The 9+2 microtubule axoneme arrangement is found in:", ["Centriole", "Cilia and flagella", "Spindle fibers", "Basal body"], 1, "Eukaryotic cilia and flagella have a 9 doublet + 2 singlet microtubule arrangement.")
    ],
    "bio_11_cell_cycle_division": [
        ("DNA replication and centriole duplication occur in which phase?", ["G1 Phase", "S Phase", "G2 Phase", "M Phase"], 1, "S phase (synthesis) is dedicated to nuclear DNA replication and cytoplasmic centriole duplication."),
        ("Synapsis and synaptonemal complex formation occur during:", ["Leptotene", "Zygotene", "Pachytene", "Diplotene"], 1, "Homologous chromosome pairing (synapsis) takes place during Zygotene."),
        ("Crossing over mediated by recombinase occurs during:", ["Zygotene", "Pachytene", "Diplotene", "Diakinesis"], 1, "Recombination nodules and crossing over occur in Pachytene."),
        ("Centromere splitting and sister chromatid separation happen in:", ["Prophase", "Metaphase", "Anaphase", "Telophase"], 2, "Anaphase marks the simultaneous division of centromeres.")
    ],
    "bio_12_principles_of_inheritance": [
        ("Mendel's monohybrid genotypic ratio is:", ["3:1", "1:2:1", "9:3:3:1", "1:1:1:1"], 1, "Genotypic ratio of Tt x Tt is 1 TT : 2 Tt : 1 tt."),
        ("Which disorder is caused by Trisomy of chromosome 21?", ["Turner's syndrome", "Klinefelter's syndrome", "Down's syndrome", "Cri-du-chat syndrome"], 2, "Down's syndrome is an autosomal aneuploidy (trisomy 21)."),
        ("A test cross involves crossing an unknown dominant phenotype with:", ["Homozygous dominant parent", "Heterozygous parent", "Homozygous recessive parent", "Any F1 progeny"], 2, "Test crosses cross with homozygous recessive to reveal zygosity."),
        ("In snapdragon (Antirrhinum), pink flowers in F1 illustrate:", ["Codominance", "Incomplete dominance", "Polygenic inheritance", "Pleiotropy"], 1, "Heterozygous condition yields an intermediate pink hue (incomplete dominance).")
    ],
    "bio_12_molecular_basis_inheritance": [
        ("In the lac operon, the repressor protein binds to the:", ["Promoter", "Operator", "Structural gene z", "Cap site"], 1, "The repressor binds the operator sequence to prevent RNA polymerase from transcribing."),
        ("Which enzyme is primarily responsible for unwinding the DNA double helix?", ["DNA Ligase", "DNA Polymerase III", "Helicase", "Topoisomerase"], 2, "Helicase unwinds the double helix at replication forks by breaking hydrogen bonds."),
        ("What is the start codon that also codes for Methionine?", ["UAA", "UAG", "AUG", "UGA"], 2, "AUG acts as the universal initiation codon for protein translation."),
        ("In eukaryotic transcription, RNA Polymerase II synthesizes:", ["rRNA (28S, 18S, 5.8S)", "hnRNA (precursor of mRNA)", "tRNA and 5S rRNA", "Small nuclear RNA"], 1, "RNA Pol II transcribes heterogeneous nuclear RNA (hnRNA), which matures into mRNA.")
    ],
    "bio_12_biotechnology_principles": [
        ("Taq polymerase used in PCR is isolated from which thermophilic bacterium?", ["Thermus aquaticus", "Bacillus thuringiensis", "Escherichia coli", "Agrobacterium tumefaciens"], 0, "Taq polymerase withstands high-temperature denaturation cycles."),
        ("Which enzyme acts as 'molecular glue' by joining DNA fragments?", ["Restriction endonuclease", "DNA Ligase", "Exonuclease", "Alkaline phosphatase"], 1, "DNA ligase seals nicks in the phosphodiester backbone."),
        ("The natural genetic engineer utilized for plant transformation is:", ["E. coli", "Agrobacterium tumefaciens", "Rhizobium", "Salmonella"], 1, "Agrobacterium tumefaciens delivers the T-DNA portion of its Ti-plasmid into plant genomes."),
        ("EcoRI restriction enzyme recognizes which palindromic sequence?", ["5'-GAATTC-3'", "5'-GGATCC-3'", "5'-AAGCTT-3'", "5'-CTCGAG-3'"], 0, "EcoRI cuts specifically at 5'-G|AATTC-3'.")
    ],

    # BATCH 2: CHEMISTRY
    "chem_11_chemical_bonding": [
        ("According to VSEPR theory, the molecular shape of SF4 is:", ["Tetrahedral", "Square planar", "See-saw", "Trigonal bipyramidal"], 2, "SF4 has 4 bond pairs and 1 equatorial lone pair on sulfur, adopting a see-saw geometry."),
        ("Which of the following molecules has a dipole moment of zero?", ["NH3", "NF3", "BF3", "H2O"], 2, "BF3 is symmetrical trigonal planar (sp2), so bond dipole vectors cancel to zero."),
        ("The hybridization of the central xenon atom in XeF4 is:", ["sp3d", "sp3d2", "sp3", "dsp2"], 1, "XeF4 has 4 bond pairs and 2 lone pairs (steric number 6), giving sp3d2 hybridization."),
        ("Which chemical bond has the highest bond dissociation enthalpy?", ["C-C single bond", "C=C double bond", "C≡C triple bond", "C-H single bond"], 2, "Bond dissociation energy increases with bond order: triple > double > single.")
    ],
    "chem_11_thermodynamics": [
        ("For an isolated system undergoing a spontaneous process, the change in entropy (ΔS) is:", ["Zero", "Negative", "Positive", "Undefined"], 2, "Second Law states entropy of an isolated system always increases for spontaneous processes."),
        ("The criteria for spontaneity at constant temperature and pressure is:", ["ΔH < 0", "ΔS < 0", "ΔG < 0", "ΔG > 0"], 2, "A process is thermodynamically spontaneous when Gibbs free energy change ΔG is negative."),
        ("For an adiabatic process, which parameter is strictly zero?", ["Work done (w)", "Heat exchange (q)", "Internal energy (ΔU)", "Temperature change (ΔT)"], 1, "Adiabatic processes prevent any heat flow across the system boundary (q = 0)."),
        ("The standard enthalpy of formation (ΔfH°) of pure elements in their standard state is:", ["Positive", "Negative", "Assigned as zero", "Infinity"], 2, "By convention, elements in their most stable reference state have ΔfH° = 0.")
    ],
    "chem_11_equilibrium": [
        ("According to Le Chatelier's principle, increasing pressure favors the direction that:", ["Increases moles of gas", "Decreases moles of gas", "Absorbs heat", "Releases heat"], 1, "High pressure shifts equilibrium toward the side with fewer moles of gas."),
        ("What is the conjugate base of HCO3⁻ (bicarbonate ion)?", ["H2CO3", "CO3²⁻", "OH⁻", "H3O⁺"], 1, "Removing one proton (H⁺) from HCO3⁻ yields carbonate (CO3²⁻)."),
        ("For the reaction N2(g) + 3H2(g) ⇌ 2NH3(g), the relation between Kp and Kc is:", ["Kp = Kc(RT)", "Kp = Kc(RT)⁻²", "Kp = Kc(RT)²", "Kp = Kc"], 1, "Δng = 2 - (1 + 3) = -2, so Kp = Kc(RT)⁻²."),
        ("The pH of a 10⁻⁸ M aqueous HCl solution at 25 °C is:", ["8.0", "Exactly 7.0", "Between 6.7 and 6.99", "1.0"], 2, "Water autodissociation ([H⁺] = 10⁻⁷ M) must be accounted for, keeping pH slightly below 7.")
    ],
    "chem_12_aldehydes_ketones_acids": [
        ("Which aldehyde undergoes the Cannizzaro reaction when treated with concentrated NaOH?", ["Acetaldehyde", "Benzaldehyde", "Propionaldehyde", "Acetone"], 1, "Benzaldehyde has no alpha-hydrogens, undergoing self oxidation-reduction (Cannizzaro reaction)."),
        ("The reagent used in the Rosenmund reduction to form aldehydes from acyl chlorides is:", ["LiAlH4", "Pd/BaSO4 poisoned with sulfur/quinoline", "NaBH4", "Zn/HCl"], 1, "Pd/BaSO4 partially poisons the catalyst to halt reduction at the aldehyde stage."),
        ("Which compound gives a positive yellow precipitate in the iodoform test?", ["Methanol", "Pentan-3-one", "Acetophenone", "Benzaldehyde"], 2, "Acetophenone possesses the requisite -COCH3 terminal methyl ketone group."),
        ("Carboxylic acids have higher boiling points than alcohols of comparable mass due to:", ["Intermolecular dipole forces", "Extensive cyclic dimer hydrogen bonding", "Covalent resonance", "Steric hindrance"], 1, "Carboxylic acids form strong cyclic dimers held by two intermolecular hydrogen bonds.")
    ],

    # BATCH 3: PHYSICS
    "phy_11_laws_of_motion": [
        ("A rocket operates on the fundamental conservation principle of:", ["Angular momentum", "Linear momentum", "Mechanical energy", "Mass-energy equivalence"], 1, "Rocket propulsion is based on Newton's third law and conservation of linear momentum."),
        ("The maximum static friction force is directly proportional to:", ["Contact surface area", "Normal reaction force", "Object velocity", "Applied pulling force"], 1, "f_max = μ_s * N; static friction depends on coefficient and normal force, not surface area."),
        ("Apparent weight of a person in a lift accelerating downward with acceleration 'a' is:", ["m(g + a)", "m(g - a)", "mg", "Zero"], 1, "Downwards acceleration reduces contact reaction: N = m(g - a)."),
        ("What is the angle between centrifugal force and centripetal force?", ["0 degrees", "90 degrees", "180 degrees", "45 degrees"], 2, "Centrifugal force acts radially outward as an inertial reaction to the inward centripetal force.")
    ],
    "phy_11_work_energy_power": [
        ("The work done by a conservative force along a closed loop path is:", ["Always positive", "Always negative", "Zero", "Path-dependent"], 2, "Conservative forces (like gravity and electrostatics) do net zero work over any closed loop."),
        ("If momentum of a body increases by 100%, its kinetic energy increases by:", ["100%", "200%", "300%", "400%"], 2, "KE = p² / 2m. If p doubles (2p), KE becomes 4x original, representing a 300% increase."),
        ("In a perfectly inelastic collision, which quantity is conserved?", ["Kinetic energy only", "Linear momentum only", "Both momentum and kinetic energy", "Neither"], 1, "Linear momentum is always conserved in isolated collisions, but maximum kinetic energy is lost in inelastic impacts."),
        ("A crane lifts 2000 kg by 10 m in 20 seconds. What is the power output (g = 10 m/s²)?", ["5 kW", "10 kW", "20 kW", "100 kW"], 1, "Work = mgh = 2000 * 10 * 10 = 200,000 J. Power = Work / t = 200,000 / 20 = 10,000 W = 10 kW.")
    ],
    "phy_12_current_electricity": [
        ("Kirchhoff's First Rule (Junction Rule) is based on the conservation of:", ["Energy", "Linear momentum", "Electric charge", "Angular momentum"], 2, "Junction rule (Σ I = 0) states charge cannot accumulate at a conductor node."),
        ("Kirchhoff's Second Rule (Loop Rule) is based on the conservation of:", ["Electric charge", "Energy", "Magnetic flux", "Potential difference"], 1, "Loop rule (Σ ΔV = 0) is a direct consequence of energy conservation in closed circuits."),
        ("When temperature of a metallic conductor increases, its electrical resistance:", ["Decreases", "Increases", "Remains constant", "First decreases then increases"], 1, "Thermal agitation increases lattice ion vibrations, shortening electron relaxation time (τ)."),
        ("In a balanced Wheatstone bridge with resistors P, Q, R, S, the condition is:", ["P * Q = R * S", "P / Q = R / S", "P + Q = R + S", "P - Q = R - S"], 1, "Bridge balance occurs when potential difference across detector is zero: P/Q = R/S.")
    ],
    "phy_12_ray_optics": [
        ("The focal length of a plane glass mirror is:", ["Zero", "1 meter", "Infinity", "Depends on thickness"], 2, "A flat mirror has an infinite radius of curvature, so f = R/2 = infinity."),
        ("A convex lens of focal length 20 cm in air is submerged in water (n = 1.33). Its focal length will:", ["Decrease", "Increase", "Remain 20 cm", "Become negative"], 1, "Lens maker's formula shows reducing relative refractive index ratio increases focal length."),
        ("The phenomenon that explains the brilliant sparkle of diamonds is:", ["Refraction", "Diffraction", "Total Internal Reflection", "Polarization"], 2, "Diamond's high refractive index (2.42) produces a very low critical angle (~24.4°)."),
        ("For a compound microscope, the final image formed by the eyepiece is:", ["Real and inverted", "Virtual, inverted, and magnified", "Virtual and erect", "Real and erect"], 1, "The eyepiece magnifies the real inverted image formed by objective, producing a virtual inverted image.")
    ]
}

def build_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    total_inserted = 0
    for chapter_key, q_list in CHAPTER_DATA.items():
        # Retrieve subject and grade from syllabus catalog
        cur.execute("SELECT subject, grade FROM syllabus_catalog WHERE chapter_key = ?", (chapter_key,))
        row = cur.fetchone()
        if not row:
            continue
        subj, grd = row

        for idx, item in enumerate(q_list):
            q_id = f"{chapter_key.upper()}_{idx+1:03d}"
            question, options, ans_idx, explanation = item
            cur.execute("""
            INSERT OR REPLACE INTO questions
            (id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (q_id, chapter_key, subj, grd, "mcq_fact", question, options[0], options[1], options[2], options[3], ans_idx, explanation, 2))
            total_inserted += 1

    conn.commit()
    print(f"Inserted/updated {total_inserted} questions into master SQLite.")

    # Export manifest
    cur.execute("""
    SELECT batch_id, batch_name, sub_batch_id, chapter_key, chapter_title, subject, grade, target_volume
    FROM syllabus_catalog ORDER BY batch_id, sub_batch_id;
    """)
    rows = cur.fetchall()

    manifest = []
    total_exported = 0
    for r in rows:
        cur.execute("SELECT COUNT(*) FROM questions WHERE chapter_key = ?", (r[3],))
        cnt = cur.fetchone()[0]

        manifest.append({
            "batch_id": r[0], "batch_name": r[1], "sub_batch_id": r[2],
            "chapter_key": r[3], "chapter_title": r[4], "subject": r[5],
            "grade": r[6], "target_volume": r[7], "current_volume": cnt,
            "file": f"data/chapters/{r[3]}.json"
        })

        cur.execute("""
        SELECT id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty
        FROM questions WHERE chapter_key = ?;
        """, (r[3],))
        q_rows = cur.fetchall()

        q_json = []
        for q in q_rows:
            q_json.append({
                "id": q[0], "chapter_key": q[1], "subject": q[2], "grade": q[3], "type": q[4],
                "question": q[5], "options": [q[6], q[7], q[8], q[9]], "answer": q[10],
                "explanation": q[11], "difficulty": q[12], "reward": {"energy": 25, "xp": 15}
            })

        out_file = os.path.join(OUTPUT_DIR, f"{r[3]}.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(q_json, f, indent=2)
        total_exported += len(q_json)

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    conn.close()
    print(f"Exported {total_exported} questions across all chapters to {OUTPUT_DIR}.")
    print(f"Manifest saved to {MANIFEST_PATH}.")

if __name__ == "__main__":
    build_all()