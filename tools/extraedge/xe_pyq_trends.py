"""Extra-Edge Q/A, NEET/MBBS level: concepts asked again and again in the medical entrance
tests (CBSE-PMT / AIPMT 1988-2016, NEET-UG 2013 onwards). Questions are freshly written on
those repeated concepts; they are not copies of any paper and carry no exact year."""
CLS = 12
LEVEL = "NEET/MBBS"

SETS = [
    ("Physics", "Often asked in AIPMT/NEET: mechanics", [
        ("A particle moves with x = 3t² + 2t (SI). Its acceleration is:", "6 m/s²", ["3 m/s²", "2 m/s²", "8 m/s²"], "a = d²x/dt²."),
        ("A body dropped from height h reaches the ground with speed:", "√(2gh)", ["2gh", "√(gh)", "gh/2"], "v² = u² + 2gh."),
        ("If the kinetic energy of a body increases by 300%, its momentum increases by:", "100%", ["300%", "200%", "50%"], "KE ×4 → p ×2."),
        ("A shell at rest explodes into two equal pieces. They move:", "in opposite directions with equal speeds", ["in the same direction", "at right angles", "with different speeds"], "Total momentum stays zero."),
        ("The work done by a centripetal force in uniform circular motion is:", "zero", ["mv²", "mv²/r × 2πr", "negative"], "Force is perpendicular to displacement."),
        ("A body slides down a smooth incline of height h. Its speed at the bottom depends on:", "h only", ["the angle only", "its mass", "the length of the incline only"], "v = √(2gh)."),
        ("The ratio of rotational to total kinetic energy of a rolling solid sphere is:", "2 : 7", ["2 : 5", "1 : 2", "5 : 7"], "Rotational ⅕mv², total 7⁄10 mv²."),
    ]),
    ("Physics", "Often asked in AIPMT/NEET: electricity and modern physics", [
        ("Two resistors 4 Ω and 12 Ω in parallel across 6 V draw a total current of:", "2 A", ["0.375 A", "1.5 A", "8 A"], "R = 3 Ω; I = 6/3."),
        ("A cell of emf E and internal resistance r gives maximum power to an external resistance R when:", "R = r", ["R = 0", "R = 2r", "R is infinite"], "Maximum power transfer theorem."),
        ("The magnetic field at the centre of a circular loop of radius R carrying current I is:", "μ₀I/(2R)", ["μ₀I/(2πR)", "μ₀IR/2", "zero"], "For a long straight wire it is μ₀I/(2πr)."),
        ("The energy of a photon of wavelength 1240 nm is about:", "1 eV", ["12.4 eV", "0.1 eV", "124 eV"], "E (eV) ≈ 1240/λ(nm)."),
        ("In a common-emitter transistor, current gain β relates to α by:", "β = α/(1 − α)", ["β = 1 − α", "β = α(1 − α)", "β = 1/α"], "α = Ic/Ie, β = Ic/Ib."),
        ("An electron and a proton have the same de Broglie wavelength. They have the same:", "momentum", ["speed", "kinetic energy", "mass"], "λ = h/p."),
        ("In the hydrogen spectrum, the shortest wavelength of the Lyman series corresponds to the transition:", "n = ∞ to n = 1", ["n = 2 to n = 1", "n = 3 to n = 2", "n = ∞ to n = 2"], "Largest energy gap."),
    ]),
    ("Chemistry", "Often asked in AIPMT/NEET: physical chemistry", [
        ("The number of atoms in 0.1 mol of a triatomic gas is:", "1.806 × 10²³", ["6.022 × 10²³", "6.022 × 10²²", "3.01 × 10²³"], "0.1 × 3 × 6.022 × 10²³."),
        ("For an ideal gas, a plot of PV against P at constant temperature is:", "a straight line parallel to the P-axis", ["a hyperbola", "a straight line through the origin", "a parabola"], "PV is constant (Boyle's law)."),
        ("The rate of a reaction doubles when concentration of A doubles. The order with respect to A is:", "1", ["0", "2", "½"], "Rate ∝ [A]¹."),
        ("For a reaction with ΔH < 0 and ΔS > 0, the reaction is:", "spontaneous at all temperatures", ["non-spontaneous at all temperatures", "spontaneous only at high T", "spontaneous only at low T"], "ΔG is always negative."),
        ("The pH of a solution obtained by mixing equal volumes of pH 2 and pH 4 HCl solutions is about:", "2.3", ["3", "6", "1.7"], "[H⁺] = (10⁻² + 10⁻⁴)/2 ≈ 5 × 10⁻³."),
        ("The solubility product of AgCl is 1.8 × 10⁻¹⁰. Its solubility in water is about:", "1.34 × 10⁻⁵ mol/L", ["1.8 × 10⁻¹⁰ mol/L", "1.8 × 10⁻⁵ mol/L", "3.6 × 10⁻¹⁰ mol/L"], "s = √Ksp."),
        ("Which aqueous solution has the highest boiling point?", "0.1 M Al₂(SO₄)₃", ["0.1 M NaCl", "0.1 M glucose", "0.1 M MgSO₄"], "i = 5 gives the largest elevation."),
    ]),
    ("Chemistry", "Often asked in AIPMT/NEET: inorganic and organic", [
        ("The correct order of ionic radii is:", "N³⁻ > O²⁻ > F⁻ > Na⁺", ["Na⁺ > F⁻ > O²⁻ > N³⁻", "F⁻ > O²⁻ > N³⁻ > Na⁺", "O²⁻ > N³⁻ > Na⁺ > F⁻"], "Isoelectronic: more protons, smaller ion."),
        ("Which species is paramagnetic?", "O₂", ["N₂", "CO", "F₂"], "O₂ has two unpaired π* electrons."),
        ("The hybridisation of the central atom in PCl₅ is:", "sp³d", ["sp³", "sp³d²", "dsp²"], "Trigonal bipyramidal."),
        ("The number of geometrical isomers of [Pt(NH₃)₂Cl₂] is:", "2", ["1", "3", "4"], "cis and trans."),
        ("Which reagent converts an alcohol into an aldehyde without further oxidation?", "PCC (pyridinium chlorochromate)", ["acidified KMnO₄", "K₂Cr₂O₇ with excess acid and heat", "HNO₃"], "Mild oxidant stops at the aldehyde."),
        ("Cannizzaro reaction is given by:", "benzaldehyde", ["acetaldehyde", "acetone", "propanal"], "Aldehydes without α-hydrogen."),
        ("The major product of nitration of toluene is:", "o- and p-nitrotoluene", ["m-nitrotoluene", "nitrobenzene", "benzoic acid"], "–CH₃ is ortho/para-directing."),
        ("Which is a natural polymer?", "cellulose", ["nylon-6", "PVC", "Teflon"], "Made of β-glucose units."),
    ]),
    ("Biology", "Often asked in AIPMT/NEET: zoology", [
        ("The 'kissing disease' (infectious mononucleosis) is caused by:", "Epstein–Barr virus", ["HIV", "influenza virus", "rabies virus"], "Spread through saliva."),
        ("The causal organism of filariasis (elephantiasis) is:", "Wuchereria bancrofti", ["Ascaris", "Plasmodium", "Entamoeba"], "Spread by Culex mosquitoes."),
        ("Oxytocin is stored in and released from the:", "posterior pituitary", ["anterior pituitary", "hypothalamus directly into blood only", "ovary"], "It is made in the hypothalamus."),
        ("Which cells of the gastric glands secrete HCl?", "parietal (oxyntic) cells", ["chief (peptic) cells", "goblet cells", "Kupffer cells"], "They also secrete intrinsic factor."),
        ("Which is a gene-related disorder of red cells that is X-linked?", "G6PD deficiency", ["sickle-cell anaemia", "thalassaemia", "phenylketonuria"], "Haemophilia and colour blindness are also X-linked."),
        ("Mammalian ear ossicles in order from the eardrum are:", "malleus, incus, stapes", ["stapes, incus, malleus", "incus, malleus, stapes", "malleus, stapes, incus"], "The stapes touches the oval window."),
        ("The organ of Corti is found in the:", "cochlea", ["semicircular canals", "utricle", "middle ear"], "It holds the hair cells for hearing."),
        ("Birds and mammals are:", "homeothermic (warm-blooded)", ["poikilothermic", "both cold-blooded", "only birds are warm-blooded"], "They keep a steady body temperature."),
        ("The embryonic layer that forms the nervous system is the:", "ectoderm", ["mesoderm", "endoderm", "trophoblast"], "Mesoderm forms muscles, blood and kidneys."),
        ("The process by which a blastocyst attaches to the uterine wall is:", "implantation", ["gastrulation", "parturition", "cleavage"], "Happens about 7 days after fertilisation."),
    ]),
    ("Botany", "Often asked in AIPMT/NEET: botany", [
        ("Which plant hormone is a gas?", "ethylene", ["auxin", "gibberellin", "cytokinin"], "C₂H₄."),
        ("The tapetum in the anther:", "nourishes the developing pollen", ["forms the pollen wall alone", "releases the pollen", "becomes the seed coat"], "Innermost wall layer."),
        ("Dicot roots differ from dicot stems in having:", "radial vascular bundles", ["conjoint vascular bundles", "a ring of open bundles", "scattered bundles"], "Xylem and phloem are on separate radii."),
        ("The cell wall of fungi is mostly made of:", "chitin", ["cellulose", "peptidoglycan", "pectin"], "Same polymer as in insect exoskeletons."),
        ("Red rust of tea is caused by:", "an alga (Cephaleuros)", ["a fungus", "a bacterium", "a virus"], "A parasitic green alga."),
        ("Which is a C₄ plant?", "maize", ["wheat", "rice", "potato"], "Sugarcane and sorghum also are C₄."),
        ("Phyllotaxy of Calotropis (two leaves at each node, opposite) is:", "opposite", ["alternate", "whorled", "spiral"], "Guava also has opposite leaves."),
        ("The ploidy of the endosperm in angiosperms is:", "3n (triploid)", ["2n", "n", "4n"], "Formed by triple fusion; gymnosperm endosperm is n."),
        ("Which is the haploid stage in a fern's life cycle?", "prothallus", ["the fern plant", "the rhizome", "the sporangium wall"], "The prothallus is the gametophyte."),
    ]),
]
