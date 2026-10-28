"""Chemistry chapters (NCERT rationalised 2023-24) that had no questions.
Each item: (question, right answer, [three wrong answers], why).
PACKS rows: (topic, class, scientist form pack, items)."""

BASIC_CONCEPTS = [
    ("One mole of any substance contains:", "6.022 × 10^23 particles", ["6.022 × 10^22 particles", "1,000 particles", "3.011 × 10^23 particles"], "This is Avogadro's number."),
    ("The molar mass of water (H2O) is:", "18 g/mol", ["16 g/mol", "10 g/mol", "20 g/mol"], "2 × 1 + 16 = 18."),
    ("Molarity is defined as:", "moles of solute per litre of solution", ["moles of solute per kg of solvent", "grams of solute per litre", "moles of solvent per litre"], "Molality uses kg of solvent."),
    ("Molality of a solution is:", "moles of solute per kilogram of solvent", ["moles of solute per litre of solution", "grams of solute per 100 g", "moles of solvent per kg of solute"], "Molality does not change with temperature."),
    ("The law stating that a compound always contains the same elements in the same proportion by mass is the law of:", "definite proportions", ["multiple proportions", "conservation of mass", "gaseous volumes"], "Given by Joseph Proust."),
    ("The law of conservation of mass was given by:", "Antoine Lavoisier", ["John Dalton", "Gay Lussac", "Avogadro"], "Mass is neither created nor destroyed in a chemical reaction."),
    ("The number of significant figures in 0.00250 is:", "3", ["2", "5", "6"], "Leading zeros are not significant; the trailing zero after 5 is."),
    ("The reactant that is used up first and limits the amount of product is the:", "limiting reagent", ["excess reagent", "catalyst", "solvent"], "It decides how much product forms."),
    ("At STP, one mole of an ideal gas occupies about:", "22.7 L (at 1 bar, 273.15 K)", ["1 L", "100 L", "2.27 L"], "Earlier books used 22.4 L at 1 atm."),
    ("The empirical formula of glucose (C6H12O6) is:", "CH2O", ["C6H12O6", "C2H4O2", "CHO"], "The simplest whole-number ratio of atoms."),
    ("1 atomic mass unit (amu or u) is defined as:", "one-twelfth of the mass of one carbon-12 atom", ["the mass of one hydrogen atom exactly", "the mass of one proton exactly", "1 gram"], "1 u = 1.66056 × 10^-24 g."),
    ("Mole fraction of a component in a solution is:", "moles of that component divided by total moles", ["grams of solute per litre", "moles per kg of solvent", "volume of solute per volume of solution"], "The mole fractions add up to 1."),
]

PERIODICITY = [
    ("The modern periodic law states that properties of elements are periodic functions of their:", "atomic numbers", ["atomic masses", "number of neutrons", "densities"], "Given by Moseley."),
    ("Mendeleev arranged elements in order of increasing:", "atomic mass", ["atomic number", "electronegativity", "valency only"], "He left gaps for undiscovered elements like eka-aluminium (gallium)."),
    ("Across a period from left to right, atomic radius generally:", "decreases", ["increases", "stays the same", "first doubles then halves"], "Nuclear charge increases while electrons enter the same shell."),
    ("Down a group, ionisation enthalpy generally:", "decreases", ["increases", "stays constant", "becomes zero"], "Outer electrons are farther from the nucleus."),
    ("The most electronegative element is:", "fluorine", ["oxygen", "chlorine", "caesium"], "Its Pauling electronegativity is 4.0."),
    ("Elements of Group 18 are called:", "noble gases", ["alkali metals", "halogens", "chalcogens"], "Their outer shells are completely filled."),
    ("Elements of Group 17 are called:", "halogens", ["noble gases", "alkaline earth metals", "transition metals"], "Fluorine, chlorine, bromine, iodine, astatine."),
    ("The first ionisation enthalpy of nitrogen is higher than that of oxygen because nitrogen has:", "a stable half-filled 2p subshell", ["fewer protons", "a full 2p subshell", "a larger atom"], "Removing an electron from 2p3 needs more energy."),
    ("Isoelectronic species have the same:", "number of electrons", ["number of protons", "mass number", "number of neutrons"], "Example: Na+, Mg2+, F-, O2- all have 10 electrons."),
    ("Among Na+, Mg2+ and Al3+, the smallest ion is:", "Al3+", ["Na+", "Mg2+", "all are equal"], "Greater nuclear charge pulls the same 10 electrons closer."),
    ("Elements of the f-block are called:", "inner transition elements", ["representative elements", "noble gases", "metalloids"], "Lanthanoids and actinoids."),
    ("The element with atomic number 120 would be placed in Group:", "2 (alkaline earth metals)", ["1", "18", "17"], "It would follow element 119 in period 8."),
]

EQUILIBRIUM = [
    ("For the reaction aA + bB ⇌ cC + dD, the equilibrium constant Kc is:", "[C]^c[D]^d / [A]^a[B]^b", ["[A]^a[B]^b / [C]^c[D]^d", "[C][D] - [A][B]", "c + d - a - b"], "Law of chemical equilibrium (law of mass action)."),
    ("Kp and Kc are related by:", "Kp = Kc(RT)^Δn", ["Kp = Kc + RT", "Kp = Kc/Δn", "Kp = Kc only always"], "Δn = moles of gaseous products minus reactants."),
    ("Le Chatelier's principle states that a system at equilibrium, when disturbed:", "shifts to counteract the change", ["stops reacting", "always moves forward", "always moves backward"], "Applies to changes in concentration, pressure and temperature."),
    ("Adding a catalyst to a reaction at equilibrium:", "does not change the equilibrium position", ["shifts it forward", "shifts it backward", "changes Kc"], "It only helps reach equilibrium faster."),
    ("For N2 + 3H2 ⇌ 2NH3 (exothermic), increasing pressure:", "favours formation of ammonia", ["favours decomposition of ammonia", "has no effect", "stops the reaction"], "Fewer gaseous moles on the product side (Haber process)."),
    ("The ionic product of water Kw at 298 K is:", "1.0 × 10^-14", ["1.0 × 10^-7", "1.0 × 10^14", "7"], "Kw = [H+][OH-]."),
    ("pH of a neutral solution at 298 K is:", "7", ["0", "14", "1"], "pH = -log[H+] = -log(10^-7)."),
    ("According to Brønsted-Lowry, an acid is a:", "proton donor", ["proton acceptor", "electron pair donor", "hydroxide donor"], "A base is a proton acceptor."),
    ("A Lewis acid is an:", "electron pair acceptor", ["electron pair donor", "proton donor only", "OH- donor"], "Example: BF3, AlCl3."),
    ("A solution that resists change in pH on adding a small amount of acid or base is a:", "buffer solution", ["saturated solution", "supersaturated solution", "colloid"], "Example: acetic acid and sodium acetate."),
    ("The solubility product (Ksp) of AgCl is written as:", "[Ag+][Cl-]", ["[AgCl]", "[Ag+] + [Cl-]", "[Ag+]/[Cl-]"], "Solid AgCl is not included."),
    ("The common ion effect means that adding NaCl to a saturated solution of AgCl:", "decreases the solubility of AgCl", ["increases the solubility of AgCl", "has no effect", "dissolves silver"], "Extra Cl- shifts the equilibrium to the solid."),
]

ELECTROCHEMISTRY = [
    ("In a galvanic (Daniell) cell, oxidation takes place at the:", "anode", ["cathode", "salt bridge", "both electrodes"], "Zn → Zn2+ + 2e- at the anode."),
    ("The standard electrode potential of the standard hydrogen electrode is taken as:", "0.00 V", ["1.00 V", "-0.76 V", "0.34 V"], "It is the reference electrode."),
    ("The Nernst equation relates the electrode potential to:", "the concentrations of the species involved", ["only temperature", "only pressure", "mass of the electrode"], "E = E° - (RT/nF) ln Q."),
    ("The relation between standard Gibbs energy and EMF is:", "ΔG° = -nFE°cell", ["ΔG° = nFE°", "ΔG° = E°/nF", "ΔG° = -RT/E°"], "A positive EMF means a spontaneous reaction."),
    ("One Faraday of electricity is about:", "96,487 coulombs (charge on one mole of electrons)", ["1 coulomb", "6.022 × 10^23 coulombs", "1,000 coulombs"], "Usually rounded to 96,500 C/mol."),
    ("Faraday's first law of electrolysis states that the mass deposited is proportional to the:", "quantity of electricity passed", ["volume of the cell", "size of the electrodes", "temperature only"], "m = ZIt."),
    ("Molar conductivity of a solution generally:", "increases on dilution", ["decreases on dilution", "does not depend on dilution", "becomes zero on dilution"], "Ions move more freely in dilute solution."),
    ("Kohlrausch's law states that limiting molar conductivity of an electrolyte is the sum of:", "contributions of its individual cations and anions", ["the masses of its ions", "the charges only", "the volumes of the ions"], "Λ°m = ν+λ°+ + ν-λ°-."),
    ("The lead storage battery used in cars is a:", "secondary (rechargeable) cell", ["primary cell", "fuel cell", "dry cell"], "It can be recharged by passing current the opposite way."),
    ("The fuel cell used in the Apollo space programme combined:", "hydrogen and oxygen to give water and electricity", ["carbon and oxygen", "zinc and copper", "lead and acid"], "Fuel cells are highly efficient and pollution free."),
    ("Rusting of iron is an example of:", "electrochemical corrosion", ["a nuclear reaction", "sublimation", "dehydration"], "Iron is oxidised in the presence of water and oxygen."),
    ("Galvanisation protects iron from rusting by coating it with:", "zinc", ["copper", "silver", "lead"], "Zinc is more reactive and is oxidised first."),
]

KINETICS = [
    ("The rate of a reaction is the change in concentration of a reactant or product per unit:", "time", ["volume", "mass", "temperature"], "Units: mol L-1 s-1."),
    ("The order of a reaction is:", "the sum of the powers of concentration terms in the rate law", ["always equal to the stoichiometric coefficients", "always a whole number", "the number of products"], "It is found by experiment and can be fractional or zero."),
    ("The half-life of a first-order reaction is:", "0.693/k, independent of initial concentration", ["proportional to the initial concentration", "1/k[A]0", "always 1 second"], "t1/2 = ln 2 / k."),
    ("The unit of the rate constant for a first-order reaction is:", "s^-1", ["mol L-1 s-1", "L mol-1 s-1", "mol2 L-2 s-1"], "For zero order it is mol L-1 s-1."),
    ("The Arrhenius equation is:", "k = A e^(-Ea/RT)", ["k = A + Ea/RT", "k = Ea × RT", "k = A/RT"], "Ea is the activation energy."),
    ("For many reactions, a 10 K rise in temperature makes the rate constant nearly:", "double", ["halve", "ten times", "unchanged"], "This is the temperature coefficient."),
    ("A catalyst increases the rate of a reaction by:", "providing a path with lower activation energy", ["increasing the activation energy", "changing ΔG of the reaction", "shifting the equilibrium"], "It is not consumed in the reaction."),
    ("Hydrolysis of an ester in large excess of water behaves as a:", "pseudo first-order reaction", ["zero-order reaction", "third-order reaction", "reaction with no rate"], "Water's concentration stays almost constant."),
    ("Molecularity of a reaction:", "applies only to elementary reactions and cannot be zero", ["can be fractional", "is always found experimentally", "can be zero"], "It is the number of species colliding in one step."),
    ("Radioactive decay follows:", "first-order kinetics", ["zero-order kinetics", "second-order kinetics", "no fixed order"], "It has a constant half-life."),
    ("According to collision theory, a reaction occurs when molecules collide with:", "sufficient energy and proper orientation", ["any energy at all", "no energy", "only at absolute zero"], "These are effective collisions."),
    ("For a zero-order reaction, the rate:", "does not depend on concentration of the reactant", ["doubles when concentration doubles", "depends on the square of concentration", "is always zero"], "Example: decomposition of NH3 on hot platinum."),
]

D_F_BLOCK = [
    ("Transition elements show variable oxidation states because:", "electrons from both (n-1)d and ns orbitals take part in bonding", ["they have no d electrons", "they are gases", "they have full shells"], "Manganese shows oxidation states from +2 to +7."),
    ("Most transition metal ions are coloured because of:", "d-d transitions of electrons", ["their large size", "the presence of s electrons only", "nuclear reactions"], "Ions like Sc3+ and Zn2+ with d0 or d10 are colourless."),
    ("Zinc, cadmium and mercury are not regarded as typical transition elements because:", "they have completely filled d orbitals in the ground state and common oxidation states", ["they are non-metals", "they have no electrons", "they are radioactive"], "Their configuration is (n-1)d10 ns2."),
    ("The steady decrease in atomic and ionic size across the lanthanoid series is called:", "lanthanoid contraction", ["actinoid expansion", "inert pair effect", "shielding increase"], "Due to poor shielding by 4f electrons."),
    ("Because of lanthanoid contraction, Zr and Hf have:", "almost identical radii", ["very different radii", "different numbers of protons only", "no chemical similarity"], "They occur together and are hard to separate."),
    ("Potassium permanganate (KMnO4) is used as a strong:", "oxidising agent", ["reducing agent", "drying agent", "fertiliser"], "Mn is in the +7 state."),
    ("Potassium dichromate (K2Cr2O7) has chromium in the oxidation state:", "+6", ["+3", "+2", "+7"], "It is orange and is used as an oxidant."),
    ("Transition metals and their compounds are good catalysts because they:", "show variable oxidation states and form complexes", ["are always inert", "are gases", "have no free orbitals"], "Example: V2O5 in the Contact process, iron in the Haber process."),
    ("Interstitial compounds form when small atoms like H, C or N are trapped in the:", "crystal lattices of transition metals", ["nucleus of the metal", "noble gases", "ionic salts only"], "Example: TiC, Fe3H."),
    ("Most lanthanoids show the common oxidation state:", "+3", ["+1", "+7", "-2"], "Some show +2 and +4 as well."),
    ("The actinoids are:", "all radioactive", ["all stable", "all gases", "non-metals"], "Elements from thorium to lawrencium."),
    ("Paramagnetism of transition metal ions is due to:", "unpaired electrons", ["paired electrons only", "neutrons", "full shells"], "Magnetic moment μ = √(n(n+2)) BM."),
]

HALOALKANES = [
    ("Haloalkanes undergo nucleophilic substitution because the carbon attached to the halogen is:", "partially positive (electron deficient)", ["partially negative", "neutral", "a free radical"], "The C-X bond is polar."),
    ("An SN2 reaction proceeds with:", "inversion of configuration in one step", ["retention of configuration", "formation of a carbocation first", "two steps always"], "The nucleophile attacks from the back side."),
    ("SN1 reactions are fastest for:", "tertiary alkyl halides", ["primary alkyl halides", "methyl halides", "vinyl halides"], "Tertiary carbocations are the most stable."),
    ("Which reaction converts an alkyl halide into an alkane with double the carbon atoms using sodium in dry ether?", "Wurtz reaction", ["Sandmeyer reaction", "Finkelstein reaction", "Kolbe reaction"], "2RX + 2Na → R-R + 2NaX."),
    ("Aryl halides are much less reactive towards nucleophilic substitution than alkyl halides because of:", "resonance giving partial double-bond character to C-X", ["their large size", "the absence of halogen", "their gaseous state"], "Electron-withdrawing groups at ortho/para positions increase reactivity."),
    ("Chloroform slowly reacts with air and light to form the poisonous gas:", "phosgene (carbonyl chloride)", ["methane", "carbon dioxide", "chlorine"], "So it is stored in closed, dark bottles."),
    ("DDT, an insecticide, was banned in many countries because it:", "is not biodegradable and accumulates in food chains", ["is too expensive", "dissolves quickly in water", "kills only mosquitoes harmlessly"], "It harms birds by thinning eggshells."),
    ("Freons (CFCs) used in refrigeration are harmful because they:", "release chlorine radicals that destroy ozone", ["are poisonous to eat", "explode easily", "cause acid rain only"], "They reach the stratosphere."),
    ("Dehydrohalogenation of an alkyl halide with alcoholic KOH gives an:", "alkene", ["alcohol", "alkane", "ether"], "This is a β-elimination reaction."),
    ("Saytzeff's rule states that in dehydrohalogenation the preferred alkene is the one:", "with more alkyl groups on the double-bonded carbons", ["with fewer alkyl groups", "that is a gas", "with a triple bond"], "The more substituted alkene is more stable."),
    ("A carbon atom attached to four different groups is called:", "chiral (asymmetric)", ["achiral", "planar", "symmetric"], "Such molecules can show optical activity."),
    ("A mixture of equal amounts of two enantiomers that shows zero optical rotation is a:", "racemic mixture", ["meso compound only", "pure enantiomer", "polymer"], "The rotations cancel each other."),
]

ALCOHOLS = [
    ("Phenol is more acidic than ethanol because:", "the phenoxide ion is stabilised by resonance", ["ethanol has more oxygen", "phenol has no OH group", "ethanol is aromatic"], "Electron-withdrawing groups like NO2 increase phenol's acidity."),
    ("Lucas test distinguishes primary, secondary and tertiary alcohols. Tertiary alcohols give turbidity:", "immediately", ["after 5 minutes", "only on heating", "never"], "Lucas reagent is concentrated HCl and ZnCl2."),
    ("Oxidation of a primary alcohol with PCC gives an:", "aldehyde", ["ketone", "carboxylic acid always", "ether"], "Strong oxidants take it further to carboxylic acid."),
    ("Oxidation of a secondary alcohol gives a:", "ketone", ["aldehyde", "carboxylic acid", "alkene"], "Tertiary alcohols resist oxidation."),
    ("The Reimer-Tiemann reaction converts phenol with chloroform and NaOH into:", "salicylaldehyde", ["aspirin", "benzoic acid", "picric acid"], "A -CHO group is introduced at the ortho position."),
    ("Kolbe's reaction of sodium phenoxide with CO2 gives:", "salicylic acid", ["acetic acid", "benzaldehyde", "phenol only"], "Salicylic acid is used to make aspirin."),
    ("Phenol reacts with bromine water to give a white precipitate of:", "2,4,6-tribromophenol", ["bromobenzene", "benzoic acid", "phenyl bromide only"], "The -OH group strongly activates the ring."),
    ("Williamson synthesis is a method of preparing:", "ethers", ["alcohols", "aldehydes", "esters"], "An alkyl halide reacts with a sodium alkoxide."),
    ("Absolute ethanol made unfit for drinking by adding copper sulphate and pyridine is called:", "denatured alcohol", ["rectified spirit", "power alcohol", "wood spirit"], "This prevents misuse."),
    ("Methanol is poisonous; drinking it can cause:", "blindness and death", ["only mild cough", "better eyesight", "no effect"], "It is also called wood spirit."),
    ("Alcohols have higher boiling points than ethers of similar mass because of:", "hydrogen bonding", ["larger size", "ionic bonds", "metallic bonding"], "The -OH groups form hydrogen bonds."),
    ("Acid-catalysed dehydration of ethanol at 443 K gives:", "ethene", ["ethane", "diethyl ether", "ethanal"], "At 413 K, ethoxyethane (ether) forms instead."),
]

AMINES = [
    ("Amines are basic because the nitrogen atom has a:", "lone pair of electrons", ["positive charge", "double bond", "missing electron"], "They accept protons."),
    ("Aniline is a weaker base than ammonia because:", "its lone pair is delocalised into the benzene ring", ["it has no nitrogen", "it is a gas", "it has more hydrogen atoms"], "Resonance reduces electron availability."),
    ("The Hofmann bromamide reaction converts an amide into a primary amine with:", "one carbon atom less", ["one carbon atom more", "the same number of carbons", "two carbons more"], "Uses Br2 and NaOH."),
    ("Gabriel phthalimide synthesis is used to prepare:", "primary aliphatic amines", ["secondary amines", "tertiary amines", "aromatic amines"], "Aryl halides do not react in this method."),
    ("The carbylamine (isocyanide) test gives a foul smell with:", "primary amines", ["secondary amines", "tertiary amines", "all amides"], "Heated with chloroform and alcoholic KOH."),
    ("Hinsberg's reagent used to distinguish amines is:", "benzenesulphonyl chloride", ["benzoyl chloride", "nitrous acid", "acetic anhydride"], "The sulphonamide of a primary amine dissolves in alkali."),
    ("Benzenediazonium chloride is made by treating aniline with nitrous acid at:", "273-278 K (0-5 °C)", ["373 K", "500 K", "room temperature always"], "This is diazotisation; diazonium salts are unstable when warm."),
    ("Diazonium salts couple with phenol to give:", "brightly coloured azo dyes", ["colourless gases", "alcohols", "plastics"], "Example: p-hydroxyazobenzene (orange)."),
    ("In the Sandmeyer reaction, a diazonium group is replaced by Cl or Br using:", "cuprous chloride or cuprous bromide", ["sodium metal", "zinc dust", "water only"], "CuCN gives a nitrile."),
    ("Methylamine in water turns red litmus:", "blue", ["red", "colourless", "green"], "Amines are basic."),
    ("In the gas phase, the basic strength of methylamines follows:", "tertiary > secondary > primary > NH3", ["NH3 > primary > secondary > tertiary", "all equal", "primary > NH3 > tertiary > secondary"], "In water, solvation changes this order."),
    ("Direct nitration of aniline gives a large amount of meta product because:", "aniline is protonated to the anilinium ion in strong acid", ["the NH2 group is meta directing", "nitric acid is a base", "the ring is not reactive"], "The anilinium ion is meta directing."),
]

PACKS = [
    ("Some Basic Concepts of Chemistry", 11, 1, BASIC_CONCEPTS),
    ("Classification of Elements and Periodicity in Properties", 11, 1, PERIODICITY),
    ("Equilibrium", 11, 1, EQUILIBRIUM),
    ("Electrochemistry", 12, 2, ELECTROCHEMISTRY),
    ("Chemical Kinetics", 12, 2, KINETICS),
    ("The d- and f-Block Elements", 12, 2, D_F_BLOCK),
    ("Haloalkanes and Haloarenes", 12, 2, HALOALKANES),
    ("Alcohols, Phenols and Ethers", 12, 2, ALCOHOLS),
    ("Amines", 12, 2, AMINES),
]
