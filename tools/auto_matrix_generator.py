import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic_master.db")

def generate_all_matrix():
    qs = []

    # 1. OPTICS: Lens Powers and Focal Lengths (Class 12 Physics)
    for p in range(1, 11):
        f = 100 // p
        qs.append((
            f"MAT_PHY_OPT_{p}", "phy_12_ray_optics", "Physics", 12, "numerical",
            f"A thin convex lens has an optical power of +{p} Diopters. What is its focal length?",
            f"{f} cm", f"{f * 2} cm", f"{f // 2} cm", f"{f + 15} cm", 0,
            f"Power P = 100 / f(cm). Hence, f = 100 / {p} = {f} cm.", 2
        ))

    # 2. CIRCUITS: Parallel Equivalent Resistances (Class 12 Physics)
    pairs = [(2, 2), (3, 6), (4, 4), (6, 12), (10, 10), (12, 24), (20, 20), (30, 60), (5, 20), (8, 8)]
    for idx, (r1, r2) in enumerate(pairs):
        r_par = (r1 * r2) // (r1 + r2)
        qs.append((
            f"MAT_PHY_CURR_{idx+1}", "phy_12_current_electricity", "Physics", 12, "numerical",
            f"Two resistors of {r1} Ω and {r2} Ω are connected in parallel. What is the equivalent resistance?",
            f"{r_par} Ω", f"{r1 + r2} Ω", f"{r1 * 2} Ω", f"{r2 // 2} Ω", 0,
            f"1/R = 1/{r1} + 1/{r2} = ({r1}+{r2})/({r1}*{r2}) => R = {r_par} Ω.", 2
        ))

    # 3. LAWS OF MOTION: Newton's Second Law F = m * a (Class 11 Physics)
    f_pairs = [(2, 5), (3, 4), (4, 10), (5, 8), (10, 2), (6, 7), (8, 3), (12, 4)]
    for idx, (m, a) in enumerate(f_pairs):
        f = m * a
        qs.append((
            f"MAT_PHY_LOM_{idx+1}", "phy_11_laws_of_motion", "Physics", 11, "numerical",
            f"A constant net force acts on an object of mass {m} kg, producing an acceleration of {a} m/s². What is the applied force?",
            f"{f} N", f"{f * 2} N", f"{f // 2} N", f"{m + a} N", 0,
            f"Newton's second law: Force F = m * a = {m} kg * {a} m/s² = {f} N.", 1
        ))

    # 4. THERMODYNAMICS: Spontaneity Conditions (Class 11 Chemistry)
    thermo_cases = [
        ("Negative (ΔH < 0)", "Positive (ΔS > 0)", "Spontaneous at all temperatures", "ΔG = ΔH - TΔS is always negative when ΔH < 0 and ΔS > 0."),
        ("Positive (ΔH > 0)", "Negative (ΔS < 0)", "Non-spontaneous at all temperatures", "ΔG = ΔH - TΔS is always positive when ΔH > 0 and ΔS < 0."),
        ("Negative (ΔH < 0)", "Negative (ΔS < 0)", "Spontaneous only at low temperatures", "Enthalpy favors spontaneity, but entropy opposes it. Low T keeps |TΔS| smaller than |ΔH|."),
        ("Positive (ΔH > 0)", "Positive (ΔS > 0)", "Spontaneous only at high temperatures", "Entropy favors spontaneity, while enthalpy opposes it. High T makes TΔS overcome ΔH.")
    ]
    for idx, (dh, ds, outcome, expl) in enumerate(thermo_cases):
        qs.append((
            f"MAT_CHEM_THERMO_{idx+1}", "chem_11_thermodynamics", "Chemistry", 11, "mcq_fact",
            f"For a reaction where ΔH is {dh} and ΔS is {ds}, the reaction will be:",
            outcome, "Equilibrium at all temperatures", "Spontaneous only at absolute zero", "Rate-independent", 0,
            expl, 2
        ))

    # 5. EQUILIBRIUM: pH Calculations for Strong Acids (Class 11 Chemistry)
    for pwr in range(1, 6):
        ph = pwr
        qs.append((
            f"MAT_CHEM_PH_{pwr}", "chem_11_equilibrium", "Chemistry", 11, "numerical",
            f"What is the pH of a 1.0 x 10⁻{pwr} M aqueous solution of strong monoprotic HCl?",
            f"{ph}.0", f"{14 - ph}.0", f"{ph + 1}.0", f"{ph / 2:.1f}", 0,
            f"pH = -log10[H+] = -log10(10⁻{pwr}) = {ph}.0.", 1
        ))

    # 6. CHEMICAL BONDING: Hybridization Matrix (Class 11 Chemistry)
    bonds = [
        ("BeCl2", "sp", "Linear", "2 bond pairs, 0 lone pairs on central Be atom."),
        ("BCl3", "sp2", "Trigonal planar", "3 bond pairs, 0 lone pairs on central B atom."),
        ("CH4", "sp3", "Tetrahedral", "4 bond pairs, 0 lone pairs on central C atom."),
        ("PCl5", "sp3d", "Trigonal bipyramidal", "5 bond pairs, 0 lone pairs on central P atom."),
        ("SF6", "sp3d2", "Octahedral", "6 bond pairs, 0 lone pairs on central S atom.")
    ]
    for idx, (mol, hyb, shape, expl) in enumerate(bonds):
        qs.append((
            f"MAT_CHEM_BOND_{idx+1}", "chem_11_chemical_bonding", "Chemistry", 11, "mcq_fact",
            f"What is the hybridization and molecular geometry of the central atom in {mol}?",
            f"{hyb} and {shape}", f"{hyb} and Bent", f"sp3 and {shape}", "dsp2 and Square planar", 0,
            expl, 2
        ))

    # 7. MOLECULAR BIOLOGY: Chargaff Rule Permutations (Class 12 Biology)
    for a_pct in [20, 24, 28, 32]:
        t_pct = a_pct
        g_pct = (100 - (a_pct * 2)) // 2
        qs.append((
            f"MAT_BIO_MOL_CHARGAFF_{a_pct}", "bio_12_molecular_basis_inheritance", "Biology", 12, "numerical",
            f"In double-stranded DNA, if Adenine constitutes {a_pct}% of the bases, what is the expected percentage of Cytosine?",
            f"{g_pct}%", f"{a_pct}%", f"{100 - a_pct}%", f"{a_pct // 2}%", 0,
            f"By Chargaff's rule: %A = %T = {a_pct}%. Remaining G + C = {100 - a_pct*2}%. Since %G = %C, Cytosine = {g_pct}%.", 2
        ))

    # 8. BIOTECHNOLOGY: Restriction Enzymes & Cleavage Sites (Class 12 Biology)
    enzymes = [
        ("EcoRI", "5'-GAATTC-3'", "Sticky ends (staggered cut between G and A)", "Escherichia coli RY 13"),
        ("HindIII", "5'-AAGCTT-3'", "Sticky ends (cut between A and A)", "Haemophilus influenzae Rd"),
        ("BamHI", "5'-GGATCC-3'", "Sticky ends (cut between G and G)", "Bacillus amyloliquefaciens H"),
        ("SmaI", "5'-CCCGGG-3'", "Blunt ends (cut between C and G)", "Serratia marcescens")
    ]
    for idx, (enz, site, cut_type, src) in enumerate(enzymes):
        qs.append((
            f"MAT_BIO_BIOTECH_{idx+1}", "bio_12_biotechnology_principles", "Biology", 12, "mcq_fact",
            f"Which recognition sequence and cleavage feature corresponds to the restriction enzyme {enz}?",
            f"{site} generating {cut_type}", f"{site} generating random cuts", "5'-TTAA-3' generating blunt ends", "3'-AAAA-5' non-specific cleavage", 0,
            f"{enz} isolated from {src} recognizes {site} and creates {cut_type}.", 2
        ))

    # 9. GENETICS: Mendelian Cross Outcomes (Class 12 Biology)
    crosses = [
        ("Monohybrid Cross (Tt x Tt)", "3:1 Phenotypic, 1:2:1 Genotypic", "3 Tall : 1 Dwarf; 1 TT : 2 Tt : 1 tt"),
        ("Monohybrid Test Cross (Tt x tt)", "1:1 Phenotypic, 1:1 Genotypic", "1 Tall : 1 Dwarf; 1 Tt : 1 tt"),
        ("Dihybrid F2 Cross (RrYy x RrYy)", "9:3:3:1 Phenotypic", "9 Round Yellow : 3 Round Green : 3 Wrinkled Yellow : 1 Wrinkled Green"),
        ("Dihybrid Test Cross (RrYy x rryy)", "1:1:1:1 Phenotypic", "1 RrYy : 1 Rryy : 1 rrYy : 1 rryy")
    ]
    for idx, (cross_name, ratio, expl) in enumerate(crosses):
        qs.append((
            f"MAT_BIO_CROSS_{idx+1}", "bio_12_principles_of_inheritance", "Biology", 12, "mcq_fact",
            f"What is the characteristic offspring ratio produced in a classical Mendelian {cross_name}?",
            ratio, "1:1:1:1 always", "9:7 complementary", "15:1 duplicate", 0,
            expl, 2
        ))

    return qs

def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    all_qs = generate_all_matrix()
    cur.executemany("""
    INSERT OR REPLACE INTO questions
    (id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, all_qs)

    conn.commit()
    conn.close()
    print(f"Matrix generator successfully created and ingested {len(all_qs)} questions across syllabus.")

if __name__ == "__main__":
    run()