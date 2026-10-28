"""Physics chapters (NCERT rationalised 2023-24) that had no questions.
Each item: (question, right answer, [three wrong answers], why).
PACKS rows: (topic, class, scientist form pack, items)."""

UNITS = [
    ("The SI unit of luminous intensity is the:", "candela", ["lumen", "lux", "watt"], "The seven SI base units include the candela."),
    ("The SI unit of amount of substance is the:", "mole", ["kilogram", "gram", "litre"], "1 mol contains 6.022 × 10^23 entities."),
    ("The dimensional formula of force is:", "[M L T^-2]", ["[M L^2 T^-2]", "[M L T^-1]", "[M^0 L T^-2]"], "Force = mass × acceleration."),
    ("The dimensional formula of energy (work) is:", "[M L^2 T^-2]", ["[M L T^-2]", "[M L^2 T^-3]", "[M L^-1 T^-2]"], "Work = force × distance."),
    ("Two quantities with the same dimensions are:", "work and torque", ["force and power", "momentum and energy", "velocity and acceleration"], "Both are [M L^2 T^-2]."),
    ("One light year is a unit of:", "distance", ["time", "speed", "intensity of light"], "The distance light travels in one year, about 9.46 × 10^15 m."),
    ("The number of significant figures in 2.308 is:", "4", ["3", "2", "5"], "Zeros between non-zero digits are significant."),
    ("The principle of homogeneity of dimensions states that in a correct equation:", "each term must have the same dimensions", ["all numbers must be equal", "dimensions must be zero", "only SI units can be used"], "Used to check equations."),
    ("A dimensionless quantity among these is:", "strain", ["force", "velocity", "pressure"], "Strain is a ratio of two lengths."),
    ("If length is measured as 2.0 cm and breadth 1.5 cm, the area with correct significant figures is:", "3.0 cm²", ["3 cm²", "3.00 cm²", "3.000 cm²"], "The result keeps the least number of significant figures (2)."),
    ("The SI unit of plane angle is the:", "radian", ["degree", "steradian", "revolution"], "Solid angle is measured in steradian."),
    ("1 astronomical unit (AU) is the:", "mean distance of the Earth from the Sun", ["distance light travels in one second", "radius of the Earth", "distance to the Moon"], "About 1.496 × 10^11 m."),
]

SOLIDS = [
    ("Stress is defined as:", "restoring force per unit area", ["change in length per unit length", "force × area", "work per unit volume only"], "Its SI unit is N m-2 or pascal."),
    ("Hooke's law states that within the elastic limit:", "stress is directly proportional to strain", ["stress is inversely proportional to strain", "strain is always zero", "stress is constant"], "The constant is the modulus of elasticity."),
    ("Young's modulus is the ratio of:", "tensile (or compressive) stress to longitudinal strain", ["shear stress to shear strain", "volume stress to volume strain", "strain to stress"], "Steel has a high Young's modulus."),
    ("The ratio of lateral strain to longitudinal strain is:", "Poisson's ratio", ["Young's modulus", "bulk modulus", "shear modulus"], "It has no units."),
    ("Bulk modulus relates to change in:", "volume under hydraulic stress", ["shape at constant volume", "length only", "temperature"], "B = -p/(ΔV/V)."),
    ("Steel is more elastic than rubber because:", "it needs a much larger stress for the same strain", ["it stretches more easily", "it is lighter", "it is a liquid"], "Elasticity means resistance to deformation."),
    ("The shear modulus (modulus of rigidity) is the ratio of:", "shearing stress to shearing strain", ["tensile stress to strain", "volume stress to strain", "pressure to density"], "It applies to change of shape."),
    ("Beyond the elastic limit, a wire:", "does not return to its original length when the load is removed", ["always breaks at once", "returns exactly to its length", "becomes shorter"], "It shows plastic deformation."),
    ("Bridges use I-shaped beams because they:", "give strength against bending with less material", ["are easy to paint", "are lighter than air", "conduct heat better"], "The large faces resist bending stress."),
    ("The maximum height of a mountain on Earth is limited by:", "the elastic limit of rocks at its base", ["the speed of wind", "the colour of rocks", "the number of trees"], "Rocks at the base would flow under too much stress."),
    ("The unit of Young's modulus is:", "N m-2 (pascal)", ["N m", "N", "m-2"], "Strain has no units."),
    ("Materials that break soon after the elastic limit, like glass, are:", "brittle", ["ductile", "elastomers", "malleable"], "Ductile materials like copper can be drawn into wires."),
]

FLUIDS = [
    ("Pascal's law states that pressure applied to an enclosed fluid is:", "transmitted undiminished to every part of the fluid", ["lost at the walls", "doubled at the bottom", "only felt at the top"], "Used in hydraulic lifts and brakes."),
    ("Pressure at a depth h in a liquid of density ρ is:", "P = Pa + ρgh", ["P = ρ/gh", "P = Pa - ρgh", "P = ρgh/Pa"], "Pressure increases with depth."),
    ("Archimedes' principle: a body immersed in a fluid experiences an upward force equal to the:", "weight of the fluid displaced", ["weight of the body", "volume of the body", "density of the body"], "This is the buoyant force."),
    ("Bernoulli's principle for a streamlined flow is a statement of conservation of:", "energy", ["mass only", "momentum only", "charge"], "P + ½ρv² + ρgh is constant along a streamline."),
    ("The equation of continuity Av = constant follows from conservation of:", "mass", ["energy", "momentum", "angular momentum"], "Water flows faster where a pipe is narrow."),
    ("An aeroplane wing gets lift because air above it moves:", "faster, so pressure above is lower", ["slower, so pressure above is lower", "at the same speed as below", "upward only"], "An application of Bernoulli's principle."),
    ("Viscosity is the property of a fluid that:", "opposes relative motion between its layers", ["makes it boil", "makes it transparent", "increases its density"], "Honey is more viscous than water."),
    ("A small sphere falling through a viscous liquid soon moves with a constant velocity called:", "terminal velocity", ["escape velocity", "orbital velocity", "critical velocity of light"], "Given by Stokes' law."),
    ("Stokes' law gives the viscous force on a sphere as:", "F = 6πηrv", ["F = ηrv", "F = 6πr²v", "F = ma"], "η is the coefficient of viscosity."),
    ("Flow changes from streamline to turbulent when the Reynolds number exceeds about:", "2,000", ["2", "20", "2,000,000 only"], "Re = ρvd/η."),
    ("Surface tension makes small drops of liquid take the shape of a:", "sphere", ["cube", "cone", "flat sheet"], "A sphere has the least surface area for a given volume."),
    ("Water rises in a thin glass tube because of:", "capillarity due to surface tension and adhesion", ["air pressure only", "gravity pulling up", "viscosity only"], "Mercury falls in a glass capillary."),
]

THERMAL = [
    ("The temperature at which the Celsius and Fahrenheit scales read the same is:", "-40°", ["0°", "100°", "32°"], "F = (9/5)C + 32."),
    ("0 °C on the Kelvin scale is:", "273.15 K", ["0 K", "100 K", "-273.15 K"], "Absolute zero is 0 K."),
    ("When a solid is heated, its increase in length per unit length per degree rise in temperature is the:", "coefficient of linear expansion", ["specific heat", "latent heat", "thermal conductivity"], "Railway tracks have gaps for expansion."),
    ("Water has its maximum density at:", "4 °C", ["0 °C", "100 °C", "-4 °C"], "Lakes freeze from the top, so fish survive below."),
    ("The heat required to change the state of unit mass of a substance without change in temperature is:", "latent heat", ["specific heat", "heat capacity", "thermal expansion"], "Latent heat of fusion of ice is 3.33 × 10^5 J kg-1."),
    ("The amount of heat needed to raise the temperature of 1 kg of a substance by 1 K is its:", "specific heat capacity", ["latent heat", "thermal conductivity", "coefficient of expansion"], "Water's is about 4,186 J kg-1 K-1."),
    ("Heat travels from the Sun to the Earth by:", "radiation", ["conduction", "convection", "evaporation"], "Radiation needs no medium."),
    ("Sea breezes during the day are caused by:", "convection, as land heats faster than water", ["conduction through sand", "radiation from the Moon", "evaporation only"], "Warm air over land rises and cool sea air moves in."),
    ("Newton's law of cooling states that the rate of loss of heat is proportional to the:", "temperature difference between the body and its surroundings", ["mass of the body only", "square of time", "colour of the body only"], "Valid for small temperature differences."),
    ("Wien's displacement law: λm T = constant. A hotter body emits maximum energy at a:", "shorter wavelength", ["longer wavelength", "same wavelength", "zero wavelength"], "Hot stars look bluish."),
    ("The Stefan-Boltzmann law states that energy radiated per second by a black body is proportional to:", "the fourth power of its absolute temperature", ["its absolute temperature", "the square of temperature", "the cube root of temperature"], "H = σAT^4."),
    ("Metals feel colder than wood at the same temperature because metals:", "are good conductors and draw heat from the hand faster", ["are actually colder", "have more mass", "do not conduct heat"], "Wood is a poor conductor."),
]

THERMODYNAMICS = [
    ("The zeroth law of thermodynamics is the basis of the concept of:", "temperature", ["entropy", "work", "pressure only"], "Two systems in equilibrium with a third are in equilibrium with each other."),
    ("The first law of thermodynamics is a statement of conservation of:", "energy (ΔQ = ΔU + ΔW)", ["mass", "momentum", "charge"], "Heat supplied = change in internal energy + work done."),
    ("In an isothermal process, the quantity that stays constant is:", "temperature", ["pressure", "volume", "heat"], "For an ideal gas, internal energy also stays constant."),
    ("In an adiabatic process:", "no heat enters or leaves the system", ["temperature stays constant", "volume stays constant", "pressure stays constant"], "PV^γ = constant."),
    ("A process at constant volume is called:", "isochoric", ["isobaric", "isothermal", "adiabatic"], "No work is done by the gas."),
    ("A process at constant pressure is called:", "isobaric", ["isochoric", "isothermal", "adiabatic"], "Work done = PΔV."),
    ("The efficiency of a Carnot engine working between T1 (hot) and T2 (cold) is:", "1 - T2/T1", ["T2/T1", "T1 - T2", "1 + T2/T1"], "No engine between the same temperatures can do better."),
    ("The second law of thermodynamics (Kelvin-Planck) says that no engine can:", "convert all the heat absorbed into work", ["do any work", "use heat at all", "run in cycles"], "Some heat must be rejected to a cold reservoir."),
    ("A refrigerator works by:", "transferring heat from a cold body to a hot body using work", ["creating cold", "destroying heat", "working without energy"], "Clausius statement of the second law."),
    ("The ratio of specific heats γ = Cp/Cv for a monatomic ideal gas is about:", "1.67", ["1.40", "1.00", "2.50"], "For diatomic gases it is about 1.40."),
    ("For an ideal gas, Cp - Cv equals:", "R (gas constant), per mole", ["zero", "γ", "2R always"], "Mayer's relation."),
    ("Work done by a gas in a cyclic process equals:", "the area enclosed by the cycle on the P-V diagram", ["zero always", "the pressure only", "the volume only"], "Net heat absorbed equals net work done."),
]

KINETIC_THEORY = [
    ("According to the kinetic theory, the pressure of a gas is due to:", "collisions of molecules with the walls of the container", ["attraction between molecules", "the weight of the gas", "light falling on the gas"], "P = (1/3)nm v²(rms)."),
    ("The average kinetic energy of a gas molecule is proportional to its:", "absolute temperature", ["volume", "pressure only", "mass only"], "Average KE = (3/2)k_B T."),
    ("The ideal gas equation is:", "PV = nRT", ["PV = n/RT", "P = VRT", "PV = R/T"], "n is the number of moles."),
    ("Avogadro's hypothesis states that equal volumes of all gases at the same temperature and pressure contain:", "the same number of molecules", ["the same mass", "different numbers of molecules", "no molecules"], "Avogadro's number is 6.022 × 10^23 per mole."),
    ("The law of equipartition of energy says that each degree of freedom has an average energy of:", "½ k_B T", ["k_B T", "3/2 k_B T", "2 k_B T"], "A monatomic gas has 3 translational degrees of freedom."),
    ("The root mean square speed of gas molecules is:", "√(3RT/M)", ["√(RT/M)", "3RT/M", "RT/3M"], "Lighter gases move faster at the same temperature."),
    ("The average distance a molecule travels between two successive collisions is its:", "mean free path", ["displacement", "wavelength", "amplitude"], "It is larger at lower pressure."),
    ("Real gases behave most like ideal gases at:", "low pressure and high temperature", ["high pressure and low temperature", "absolute zero", "any condition"], "Then intermolecular forces are negligible."),
    ("The number of degrees of freedom of a diatomic molecule at moderate temperature is:", "5", ["3", "6", "7"], "3 translational and 2 rotational."),
    ("Boyle's law states that at constant temperature:", "PV = constant", ["V/T = constant", "P/T = constant", "PT = constant"], "Pressure is inversely proportional to volume."),
    ("Charles' law states that at constant pressure:", "V is proportional to T", ["V is proportional to 1/T", "P is proportional to V", "V is constant"], "Gases expand when heated."),
    ("Dalton's law of partial pressures states that the total pressure of a gas mixture is:", "the sum of the partial pressures of its components", ["the average of partial pressures", "the largest partial pressure", "always 1 atm"], "Each gas behaves as if alone."),
]

OSCILLATIONS = [
    ("In simple harmonic motion, the restoring force is:", "proportional to displacement and directed towards the mean position", ["constant", "proportional to velocity", "directed away from the mean position"], "F = -kx."),
    ("The time period of a simple pendulum is:", "T = 2π√(L/g)", ["T = 2π√(g/L)", "T = 2πLg", "T = √(L/g)"], "It does not depend on the mass of the bob for small swings."),
    ("The time period of a mass m on a spring of constant k is:", "T = 2π√(m/k)", ["T = 2π√(k/m)", "T = 2πmk", "T = m/k"], "A stiffer spring gives faster oscillations."),
    ("In SHM, the speed of the particle is maximum at the:", "mean (equilibrium) position", ["extreme positions", "halfway point only", "it is always the same"], "There, kinetic energy is maximum and potential energy is minimum."),
    ("In SHM, acceleration is maximum at the:", "extreme positions", ["mean position", "it is always zero", "halfway point"], "a = -ω²x."),
    ("If the length of a simple pendulum is made four times, its time period becomes:", "twice", ["four times", "half", "unchanged"], "T is proportional to √L."),
    ("A pendulum clock on the Moon would:", "run slower because g is smaller", ["run faster", "keep the same time", "stop working at once"], "T = 2π√(L/g) increases when g decreases."),
    ("The total energy of a particle in SHM is:", "constant and proportional to the square of the amplitude", ["zero", "maximum only at the mean position", "proportional to time"], "E = ½kA²."),
    ("The number of oscillations per second is called:", "frequency", ["time period", "amplitude", "phase"], "Its unit is hertz (Hz)."),
    ("Oscillations whose amplitude gradually decreases because of friction are called:", "damped oscillations", ["forced oscillations", "free oscillations without loss", "resonance"], "Energy is lost to the surroundings."),
    ("When the frequency of a driving force equals the natural frequency of a system, the amplitude becomes large. This is:", "resonance", ["damping", "beats", "diffraction"], "Soldiers break step while crossing a bridge to avoid it."),
    ("Angular frequency ω is related to time period T by:", "ω = 2π/T", ["ω = T/2π", "ω = 2πT", "ω = 1/T"], "Its unit is rad s-1."),
]

MAGNETISM_MOVING = [
    ("The force on a charge q moving with velocity v in a magnetic field B is:", "F = q(v × B)", ["F = qvB always along v", "F = qE", "F = q/vB"], "This Lorentz magnetic force is perpendicular to both v and B."),
    ("A charged particle moving perpendicular to a uniform magnetic field follows a:", "circular path", ["straight line", "parabola", "zig-zag path"], "The magnetic force acts as the centripetal force."),
    ("The magnetic force on a charged particle does no work because it is:", "always perpendicular to the velocity", ["always zero", "parallel to the velocity", "too small"], "Speed stays constant."),
    ("The Biot-Savart law gives the magnetic field due to:", "a small current element", ["a stationary charge", "a permanent magnet only", "gravity"], "dB = (μ0/4π) I dl × r / r³."),
    ("The magnetic field at the centre of a circular loop of radius R carrying current I is:", "μ0 I / 2R", ["μ0 I / 2πR", "μ0 I R", "zero"], "It is along the axis of the loop."),
    ("The magnetic field inside a long solenoid with n turns per unit length is:", "μ0 n I, nearly uniform", ["zero", "μ0 I / 2R", "decreasing to zero at the centre"], "Field outside is nearly zero."),
    ("Ampere's circuital law relates the line integral of B around a closed loop to:", "μ0 times the current enclosed", ["the charge enclosed", "the voltage", "the resistance"], "∮B·dl = μ0 I."),
    ("Two parallel wires carrying currents in the same direction:", "attract each other", ["repel each other", "do not interact", "rotate"], "Opposite currents repel."),
    ("A moving coil galvanometer is converted into an ammeter by connecting:", "a low resistance (shunt) in parallel", ["a high resistance in series", "a battery in series", "a capacitor in parallel"], "Most current bypasses the coil."),
    ("A galvanometer is converted into a voltmeter by connecting:", "a high resistance in series", ["a low resistance in parallel", "a shunt in parallel", "nothing"], "It then draws very little current."),
    ("The SI unit of magnetic field is the:", "tesla (T)", ["weber", "henry", "gauss"], "1 gauss = 10^-4 T."),
    ("A current loop in a magnetic field experiences a:", "torque that tends to turn it", ["straight-line force only", "no effect", "change of charge"], "τ = m × B; this is how motors work."),
]

MAGNETISM_MATTER = [
    ("The Earth's magnetic field at the surface is about:", "10^-5 T (a few tenths of a gauss)", ["1 T", "10 T", "10^-12 T"], "It is similar to that of a giant bar magnet."),
    ("Materials weakly repelled by a magnet are:", "diamagnetic", ["paramagnetic", "ferromagnetic", "magnetised permanently"], "Examples: bismuth, copper, water."),
    ("Materials weakly attracted by a magnet are:", "paramagnetic", ["diamagnetic", "superconductors only", "non-metals only"], "Examples: aluminium, sodium, oxygen."),
    ("Iron, cobalt and nickel are strongly attracted by magnets. They are:", "ferromagnetic", ["diamagnetic", "paramagnetic", "non-magnetic"], "They have domains that align."),
    ("Above the Curie temperature, a ferromagnet becomes:", "paramagnetic", ["diamagnetic", "a superconductor", "a stronger magnet"], "Thermal motion destroys domain alignment."),
    ("A superconductor expels magnetic field lines completely. It is a perfect:", "diamagnet", ["paramagnet", "ferromagnet", "conductor of magnetism"], "This is the Meissner effect."),
    ("Magnetic field lines of a bar magnet outside the magnet go from:", "north pole to south pole", ["south pole to north pole", "nowhere", "centre outward only"], "Inside the magnet they go from south to north."),
    ("Isolated magnetic poles (monopoles):", "are not known to exist", ["are found in every magnet", "exist in iron only", "are made in laboratories easily"], "Cutting a magnet gives two smaller magnets."),
    ("Material for permanent magnets should have:", "high retentivity and high coercivity", ["low retentivity and low coercivity", "zero coercivity", "high permeability only"], "Steel is suitable; soft iron is used for electromagnets."),
    ("Soft iron is used for the core of electromagnets because it has:", "high permeability and low retentivity", ["high retentivity", "very high coercivity", "no magnetic properties"], "It loses magnetism quickly when current stops."),
    ("The magnetic moment of a bar magnet is directed from:", "its south pole to its north pole", ["its north pole to its south pole", "the centre outward", "nowhere"], "Like a current loop."),
    ("A freely suspended bar magnet points roughly in the:", "north-south direction", ["east-west direction", "vertical direction", "any random direction"], "It aligns with the Earth's magnetic field."),
]

AC = [
    ("The rms value of an alternating current with peak value I0 is:", "I0/√2", ["I0√2", "I0/2", "2I0"], "About 0.707 I0."),
    ("Household supply in India is 220 V at a frequency of:", "50 Hz", ["60 Hz", "100 Hz", "5 Hz"], "220 V is the rms value."),
    ("The reactance of an inductor is:", "XL = ωL, increasing with frequency", ["XL = 1/ωL", "XL = ωC", "independent of frequency"], "Inductors block high frequency AC."),
    ("The reactance of a capacitor is:", "XC = 1/ωC, decreasing with frequency", ["XC = ωC", "XC = ωL", "always zero"], "A capacitor blocks DC."),
    ("In a purely inductive AC circuit, current:", "lags the voltage by π/2", ["leads the voltage by π/2", "is in phase with voltage", "is always zero"], "In a capacitor, current leads by π/2."),
    ("The impedance of a series LCR circuit is:", "√(R² + (XL - XC)²)", ["R + XL + XC", "R - XL", "XL × XC"], "At resonance XL = XC and Z = R."),
    ("The resonant frequency of a series LCR circuit is:", "1/(2π√(LC))", ["2π√(LC)", "√(L/C)", "LC/2π"], "At this frequency current is maximum."),
    ("Average power in an AC circuit is P = Vrms Irms cos φ. Here cos φ is the:", "power factor", ["resistance", "frequency", "reactance"], "It is 1 for a purely resistive circuit."),
    ("Power consumed in a pure inductor or pure capacitor over a cycle is:", "zero", ["maximum", "Vrms × Irms", "infinite"], "The current is wattless."),
    ("A transformer works on the principle of:", "mutual induction", ["self induction only", "electrostatic induction", "the photoelectric effect"], "It works only with AC."),
    ("In a step-up transformer:", "secondary turns are more than primary turns", ["secondary turns are fewer", "the voltage decreases", "the frequency increases"], "Vs/Vp = Ns/Np."),
    ("Power is transmitted over long distances at high voltage to:", "reduce I²R losses in the lines", ["increase losses", "make electricity faster", "change its frequency"], "Higher voltage means lower current for the same power."),
]

DUAL_NATURE = [
    ("The photoelectric effect was explained by:", "Albert Einstein (1905)", ["Isaac Newton", "Thomas Young", "Max Born"], "He received the Nobel Prize for it in 1921."),
    ("In the photoelectric effect, the maximum kinetic energy of emitted electrons depends on the:", "frequency of the incident light", ["intensity of the light", "duration of illumination", "area of the plate"], "Kmax = hν - φ0."),
    ("The minimum energy needed to remove an electron from a metal surface is the:", "work function", ["threshold wavelength", "stopping potential", "ionisation energy of gas"], "It is different for different metals."),
    ("Below the threshold frequency:", "no photoelectrons are emitted, however intense the light", ["many electrons are emitted", "electrons are emitted slowly", "the metal melts"], "Photon energy hν is less than the work function."),
    ("Increasing the intensity of light above the threshold frequency increases the:", "number of photoelectrons (photocurrent)", ["maximum kinetic energy", "work function", "threshold frequency"], "More photons, more electrons."),
    ("The energy of a photon of frequency ν is:", "hν", ["h/ν", "ν/h", "hν²"], "h is Planck's constant, 6.63 × 10^-34 J s."),
    ("The de Broglie wavelength of a particle of momentum p is:", "λ = h/p", ["λ = p/h", "λ = hp", "λ = h/p²"], "All moving matter has wave nature."),
    ("The wave nature of electrons was confirmed by the experiment of:", "Davisson and Germer", ["Michelson and Morley", "Rutherford", "Millikan"], "Electrons were diffracted by a nickel crystal."),
    ("Photoelectric emission is:", "instantaneous (no time lag)", ["delayed by minutes", "delayed by hours", "only after heating"], "Even with very dim light above the threshold."),
    ("The stopping potential in a photoelectric experiment measures the:", "maximum kinetic energy of photoelectrons", ["work function only", "number of electrons", "intensity of light"], "e V0 = Kmax."),
    ("A proton and an electron have the same kinetic energy. The one with the longer de Broglie wavelength is the:", "electron", ["proton", "both are equal", "neither has a wavelength"], "It has less mass, so less momentum."),
    ("Photocells (photoelectric cells) are used in:", "automatic doors, light meters and burglar alarms", ["refrigerators only", "making magnets", "boiling water"], "They convert light into current."),
]

ATOMS = [
    ("In Rutherford's alpha-particle scattering experiment, most alpha particles passed straight through the gold foil, showing that:", "most of the atom is empty space", ["the atom is solid", "electrons are heavy", "the nucleus is negative"], "A few were deflected by a tiny, dense, positive nucleus."),
    ("In Bohr's model, an electron can revolve only in orbits where its angular momentum is:", "an integral multiple of h/2π", ["zero", "any value", "an integral multiple of h"], "These are stationary orbits."),
    ("The energy of an electron in the nth orbit of hydrogen is:", "-13.6/n² eV", ["13.6 n² eV", "-13.6 n eV", "-13.6/n eV"], "The ground state energy is -13.6 eV."),
    ("The ionisation energy of a hydrogen atom in its ground state is:", "13.6 eV", ["3.4 eV", "1.51 eV", "0 eV"], "Energy needed to remove the electron completely."),
    ("The radius of the first Bohr orbit of hydrogen is about:", "0.53 Å (5.3 × 10^-11 m)", ["5.3 Å", "53 Å", "0.053 Å"], "Called the Bohr radius."),
    ("Lines of the hydrogen spectrum in the visible region belong to the:", "Balmer series", ["Lyman series", "Paschen series", "Pfund series"], "Electrons jump down to n = 2."),
    ("The Lyman series of hydrogen lies in the:", "ultraviolet region", ["visible region", "infrared region", "radio region"], "Transitions end at n = 1."),
    ("When an electron jumps from a higher to a lower orbit, it:", "emits a photon of energy equal to the energy difference", ["absorbs a photon", "gains mass", "becomes a proton"], "hν = Ei - Ef."),
    ("The radius of the nth Bohr orbit is proportional to:", "n²", ["n", "1/n", "1/n²"], "rn = n² a0."),
    ("A limitation of Bohr's model is that it:", "applies only to hydrogen-like (one-electron) atoms", ["cannot explain any spectral line", "predicts the atom is solid", "has no orbits"], "It also cannot explain relative intensities of lines."),
    ("The distance of closest approach of an alpha particle to the nucleus gives an estimate of the:", "size of the nucleus", ["size of the atom", "mass of the electron", "charge of the alpha particle only"], "About 10^-14 m for gold."),
    ("Electrons in an atom do not fall into the nucleus in Bohr's model because:", "they are in stationary orbits that do not radiate energy", ["they have no charge", "the nucleus repels them", "gravity holds them out"], "Classical theory predicted they would spiral in."),
]

NUCLEI = [
    ("The nucleus of an atom contains:", "protons and neutrons (nucleons)", ["electrons only", "protons and electrons", "photons"], "Nucleons are held by the strong nuclear force."),
    ("Isotopes are atoms with the same:", "atomic number but different mass numbers", ["mass number but different atomic numbers", "number of neutrons", "everything"], "Example: protium, deuterium, tritium."),
    ("Isobars are nuclides with the same:", "mass number but different atomic numbers", ["atomic number", "number of neutrons", "chemical properties"], "Example: tritium (H-3) and helium-3."),
    ("The radius of a nucleus is proportional to:", "A^(1/3), where A is the mass number", ["A", "A²", "1/A"], "R = R0 A^(1/3); nuclear density is nearly the same for all nuclei."),
    ("The difference between the mass of the separate nucleons and the mass of the nucleus is the:", "mass defect", ["binding fraction", "half-life", "atomic mass"], "It appears as binding energy, E = Δm c²."),
    ("Binding energy per nucleon is maximum for nuclei around mass number:", "56 (iron)", ["2 (deuterium)", "238 (uranium)", "4 only"], "Such nuclei are the most stable."),
    ("Splitting a heavy nucleus like U-235 into two lighter nuclei, releasing energy, is:", "nuclear fission", ["nuclear fusion", "radioactive decay only", "ionisation"], "Used in nuclear reactors."),
    ("Joining light nuclei like hydrogen to form helium, releasing energy, is:", "nuclear fusion", ["nuclear fission", "beta decay", "chemical combustion"], "It powers the Sun and stars."),
    ("The nuclear force is:", "strong, short-range and charge independent", ["weak and long-range", "the same as gravity", "the same as electrostatic force"], "It acts only up to a few femtometres."),
    ("1 atomic mass unit is equivalent to an energy of about:", "931.5 MeV", ["1 MeV", "13.6 eV", "1 J"], "From E = mc²."),
    ("A nuclear reactor controls the chain reaction using control rods made of:", "cadmium or boron", ["copper", "iron", "plastic"], "They absorb neutrons."),
    ("In a nuclear reactor, a moderator such as heavy water or graphite is used to:", "slow down fast neutrons", ["speed up neutrons", "absorb all heat", "stop the reactor permanently"], "Slow neutrons cause fission of U-235 more easily."),
]

PACKS = [
    ("Units and Measurements", 11, 2, UNITS),
    ("Mechanical Properties of Solids", 11, 2, SOLIDS),
    ("Mechanical Properties of Fluids", 11, 2, FLUIDS),
    ("Thermal Properties of Matter", 11, 2, THERMAL),
    ("Thermodynamics", 11, 2, THERMODYNAMICS),
    ("Kinetic Theory", 11, 2, KINETIC_THEORY),
    ("Oscillations", 11, 2, OSCILLATIONS),
    ("Moving Charges and Magnetism", 12, 3, MAGNETISM_MOVING),
    ("Magnetism and Matter", 12, 3, MAGNETISM_MATTER),
    ("Alternating Current", 12, 3, AC),
    ("Dual Nature of Radiation and Matter", 12, 3, DUAL_NATURE),
    ("Atoms", 12, 3, ATOMS),
    ("Nuclei", 12, 3, NUCLEI),
]
