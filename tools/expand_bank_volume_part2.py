import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic_master.db")

EXPANSION_QUESTIONS_PART2 = [
    # chem_11_equilibrium (Add 6 more)
    ("CHEM_11_EQ_005", "chem_11_equilibrium", "Chemistry", 11, "mcq_fact", 
     "For the equilibrium 2SO2(g) + O2(g) ⇌ 2SO3(g) (exothermic), which condition maximizes SO3 yield?", 
     ["Low temperature and high pressure", "High temperature and low pressure", "High temperature and high pressure", "Low temperature and low pressure"], 
     0, "Exothermic reactions are favored by low temperature; forward reaction decreases gas moles (3 to 2), so high pressure shifts equilibrium right."),

    ("CHEM_11_EQ_006", "chem_11_equilibrium", "Chemistry", 11, "mcq_fact", 
     "What is the solubility product (Ksp) expression for a sparingly soluble salt of type A2B3 with molar solubility 's'?", 
     ["6s⁵", "108s⁵", "27s⁴", "108s⁴"], 
     1, "A2B3 ⇌ 2A³⁺ + 3B²⁻. Ksp = [A³⁺]²[B²⁻]³ = (2s)² * (3s)³ = 4s² * 27s³ = 108s⁵."),

    ("CHEM_11_EQ_007", "chem_11_equilibrium", "Chemistry", 11, "mcq_fact", 
     "Which of the following mixtures behaves as an acidic buffer solution?", 
     ["CH3COOH + CH3COONa", "NH4OH + NH4Cl", "HCl + NaCl", "NaOH + CH3COONa"], 
     0, "An acidic buffer consists of an equimolar mixture of a weak acid (CH3COOH) and its conjugate salt with a strong base (CH3COONa)."),

    ("CHEM_11_EQ_008", "chem_11_equilibrium", "Chemistry", 11, "mcq_fact", 
     "Addition of an inert gas at constant volume to a gaseous equilibrium system causes:", 
     ["Shift toward products", "Shift toward reactants", "No change in equilibrium position", "Change in equilibrium constant Kp"], 
     2, "At constant volume, addition of inert gas increases total pressure, but partial pressures of reacting gases remain unchanged, causing zero shift."),

    ("CHEM_11_EQ_009", "chem_11_equilibrium", "Chemistry", 11, "mcq_fact", 
     "The ionic product of water (Kw) at 25 °C is 1.0 x 10⁻¹⁴. If temperature is increased to 60 °C, Kw will:", 
     ["Decrease", "Increase", "Remain 1.0 x 10⁻¹⁴", "Become zero"], 
     1, "Auto-ionization of water (H2O ⇌ H⁺ + OH⁻) is endothermic (ΔH > 0). Increasing temperature shifts equilibrium right, increasing Kw."),

    ("CHEM_11_EQ_010", "chem_11_equilibrium", "Chemistry", 11, "mcq_fact", 
     "Ostwald's dilution law states that degree of dissociation (α) of a weak electrolyte is inversely proportional to:", 
     ["Square of concentration", "Square root of concentration", "Volume of dilution", "Temperature"], 
     1, "For a weak binary electrolyte, Ka = Cα² / (1 - α) ≈ Cα². Therefore, α = √(Ka / C), inversely proportional to √C."),

    # chem_12_aldehydes_ketones_acids (Add 6 more)
    ("CHEM_12_ALDKET_005", "chem_12_aldehydes_ketones_acids", "Chemistry", 12, "mcq_fact", 
     "The reaction of an aldehyde or ketone with zinc amalgam (Zn-Hg) and concentrated HCl to yield hydrocarbons is:", 
     ["Wolff-Kishner reduction", "Clemmensen reduction", "Stephen reduction", "Etard reaction"], 
     1, "Clemmensen reduction converts >C=O to >CH2 using Zn-Hg/conc. HCl (acidic medium)."),

    ("CHEM_12_ALDKET_006", "chem_12_aldehydes_ketones_acids", "Chemistry", 12, "mcq_fact", 
     "Wolff-Kishner reduction accomplishes >C=O to >CH2 conversion using which reagents?", 
     ["Hydrazine (NH2NH2) followed by KOH in ethylene glycol", "LiAlH4 in dry ether", "Sn/HCl", "H2 / Ni"], 
     0, "Wolff-Kishner operates under basic conditions by heating the hydrazone derivative with KOH in high-boiling ethylene glycol."),

    ("CHEM_12_ALDKET_007", "chem_12_aldehydes_ketones_acids", "Chemistry", 12, "mcq_fact", 
     "Tollens' reagent consists of:", 
     ["Ammoniacal silver nitrate solution", "Alkaline copper sulfate with sodium potassium tartrate", "Neutral ferric chloride", "Potassium permanganate"], 
     0, "Tollens' reagent is [Ag(NH3)2]⁺ OH⁻, which oxidizes aliphatic and aromatic aldehydes to form a characteristic silver mirror."),

    ("CHEM_12_ALDKET_008", "chem_12_aldehydes_ketones_acids", "Chemistry", 12, "mcq_fact", 
     "Which carboxylic acid halogenation reaction introduces chlorine or bromine specifically at the alpha-position?", 
     ["Hell-Volhard-Zelinsky (HVZ) reaction", "Kolbe's electrolysis", "Hunsdiecker reaction", "Decarboxylation"], 
     0, "Carboxylic acids having an alpha-hydrogen react with Cl2 or Br2 in presence of red phosphorus (HVZ reaction) to yield alpha-halocarboxylic acids."),

    ("CHEM_12_ALDKET_009", "chem_12_aldehydes_ketones_acids", "Chemistry", 12, "mcq_fact", 
     "What is the correct order of acid strength among chlorinated acetic acids?", 
     ["CH3COOH > CH2ClCOOH > CHCl2COOH > CCl3COOH", "CCl3COOH > CHCl2COOH > CH2ClCOOH > CH3COOH", "CHCl2COOH > CCl3COOH > CH2ClCOOH > CH3COOH", "CH2ClCOOH > CHCl2COOH > CCl3COOH > CH3COOH"], 
     1, "The strong -I (electron-withdrawing inductive effect) of chlorine stabilizes the carboxylate anion: trichloroacetic acid is the strongest."),

    ("CHEM_12_ALDKET_010", "chem_12_aldehydes_ketones_acids", "Chemistry", 12, "mcq_fact", 
     "Aldol condensation requires aldehydes or ketones to possess at least one:", 
     ["Aromatic ring", "Alpha-hydrogen atom", "Beta-hydrogen atom", "Terminal methyl group"], 
     1, "Aldol condensation is initiated by base-catalyzed deprotonation of an acidic alpha-hydrogen to generate an enolate nucleophile."),

    # phy_11_work_energy_power (Add 6 more)
    ("PHY_11_WEP_005", "phy_11_work_energy_power", "Physics", 11, "mcq_fact", 
     "A spring of spring constant 'k' is stretched from extension x1 to x2. Work done by the external stretching force is:", 
     ["(1/2) k (x2 - x1)²", "(1/2) k (x2² - x1²)", "k (x2 - x1)", "k (x2² - x1²)"], 
     1, "Work done = ∫ (k x) dx from x1 to x2 = (1/2) k (x2² - x1²)."),

    ("PHY_11_WEP_006", "phy_11_work_energy_power", "Physics", 11, "mcq_fact", 
     "Work-Energy theorem states that the change in kinetic energy of a particle equals:", 
     ["Work done by conservative forces only", "Work done by non-conservative forces only", "Net work done by all forces (conservative + non-conservative + external)", "Work done against friction only"], 
     2, "The Work-Energy theorem is universal: ΔK = W_total, accounting for all forces acting on the system."),

    ("PHY_11_WEP_007", "phy_11_work_energy_power", "Physics", 11, "mcq_fact", 
     "What is the coefficient of restitution (e) for a completely elastic collision?", 
     ["e = 0", "e = 1", "0 < e < 1", "e = infinity"], 
     1, "In perfectly elastic collisions, relative velocity of separation equals relative velocity of approach (e = 1). In perfectly inelastic, e = 0."),

    ("PHY_11_WEP_008", "phy_11_work_energy_power", "Physics", 11, "mcq_fact", 
     "Potential energy function U(x) = ax² - bx. The position of stable equilibrium is given by:", 
     ["x = b / (2a)", "x = a / (2b)", "x = 2b / a", "x = 0"], 
     0, "At equilibrium, dU/dx = 0 -> 2ax - b = 0 -> x = b/(2a). Since d²U/dx² = 2a > 0 (assuming a > 0), it is stable equilibrium."),

    ("PHY_11_WEP_009", "phy_11_work_energy_power", "Physics", 11, "mcq_fact", 
     "One kilowatt-hour (1 kWh) of commercial electrical energy equals how many Joules?", 
     ["3.6 x 10⁵ J", "3.6 x 10⁶ J", "1.0 x 10³ J", "3.6 x 10⁷ J"], 
     1, "1 kWh = 1000 W * 3600 s = 3.6 x 10⁶ J (or 3.6 MJ)."),

    ("PHY_11_WEP_010", "phy_11_work_energy_power", "Physics", 11, "mcq_fact", 
     "A body of mass m is released from the top of a smooth hemisphere of radius R. At what vertical distance below the apex does it leave contact?", 
     ["R / 2", "R / 3", "2R / 3", "R / 4"], 
     1, "Centrifugal balance gives mg cos θ = mv²/R, and energy conservation gives v² = 2gh. Solving yields h = R/3 below the top."),

    # phy_12_ray_optics (Add 6 more)
    ("PHY_12_OPT_005", "phy_12_ray_optics", "Physics", 12, "mcq_fact", 
     "For an equilateral triangular prism with minimum deviation angle Dm = 30°, what is the refractive index (n)?", 
     ["1.414 (√2)", "1.732 (√3)", "1.500", "1.333"], 
     0, "A = 60°, Dm = 30°. n = sin((A + Dm)/2) / sin(A/2) = sin(45°) / sin(30°) = (1/√2) / (1/2) = √2 ≈ 1.414."),

    ("PHY_12_OPT_006", "phy_12_ray_optics", "Physics", 12, "mcq_fact", 
     "Two thin lenses of optical powers +5 D and -3 D are kept in close contact. The focal length of the combination is:", 
     ["+50 cm", "-50 cm", "+20 cm", "+10 cm"], 
     0, "Net power P = P1 + P2 = +5 - 3 = +2 D. Focal length f = 1/P = 1/2 m = +50 cm."),

    ("PHY_12_OPT_007", "phy_12_ray_optics", "Physics", 12, "mcq_fact", 
     "An astronomical telescope has an objective of focal length 100 cm and an eyepiece of focal length 5 cm. Normal magnification is:", 
     ["20", "500", "95", "105"], 
     0, "In normal adjustment (final image at infinity), magnifying power m = f_obj / f_eye = 100 / 5 = 20."),

    ("PHY_12_OPT_008", "phy_12_ray_optics", "Physics", 12, "mcq_fact", 
     "Chromatic aberration in optical lenses is caused by:", 
     ["Reflection from lens surfaces", "Variation of refractive index with wavelength (dispersion)", "Non-spherical lens curvatures", "Total internal reflection"], 
     1, "Different colors have different refractive indices in glass (n_violet > n_red), focusing light at different points along the principal axis."),

    ("PHY_12_OPT_009", "phy_12_ray_optics", "Physics", 12, "mcq_fact", 
     "The power of a convex lens in air is +4 D. What is its focal length?", 
     ["4 cm", "25 cm", "40 cm", "2.5 cm"], 
     1, "f = 1 / P = 1 / 4 m = 0.25 m = 25 cm."),

    ("PHY_12_OPT_010", "phy_12_ray_optics", "Physics", 12, "mcq_fact", 
     "In an optical fiber, light propagates along the central core via repeated:", 
     ["Refraction", "Diffraction", "Total Internal Reflection", "Polarization"], 
     2, "The core has a higher refractive index than the cladding; light incident beyond the critical angle suffers lossless total internal reflection.")
]

def expand_part2():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for item in EXPANSION_QUESTIONS_PART2:
        qid, chkey, subj, grd, qtype, qtext, opts, ans, expl = item
        cur.execute("""
        INSERT OR REPLACE INTO questions
        (id, chapter_key, subject, grade, q_type, question, opt_a, opt_b, opt_c, opt_d, answer_idx, explanation, difficulty)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (qid, chkey, subj, grd, qtype, qtext, opts[0], opts[1], opts[2], opts[3], ans, expl, 2))

    conn.commit()
    print(f"Added {len(EXPANSION_QUESTIONS_PART2)} expansion questions to master SQLite.")
    conn.close()

if __name__ == "__main__":
    expand_part2()