"""Extra-Edge Q/A, Class 8 (NCERT + IGCSE Lower Secondary / Cambridge Checkpoint).
Each item: (question, right answer, [three wrong answers], why).
SETS rows: (subject, topic, items)."""
CLS = 8

SETS = [
    ("Physics", "Force and pressure", [
        ("A brick exerts the greatest pressure on the ground when it rests on its:", "smallest face", ["largest face", "medium face", "pressure is the same on every face"], "Pressure = force ÷ area; the weight is fixed, so the smallest area gives the largest pressure."),
        ("Liquid pressure at a point in a vessel depends on:", "the depth of the point below the surface", ["the shape of the vessel", "the width of the vessel", "the total amount of liquid in the vessel"], "p = hρg, so only depth, density and g matter, not the shape."),
        ("A rubber suction cup sticks to a smooth wall because:", "air pressure outside the cup is greater than the pressure inside it", ["the wall is magnetic", "rubber is sticky like glue", "gravity pulls the cup to the wall"], "Pressing the cup pushes air out; the outside atmosphere pushes it in place."),
        ("Dams are made thicker at the bottom than at the top because:", "water pressure increases with depth", ["water is lighter at the bottom", "the top must be thick to stop waves", "concrete is cheaper at the bottom"], "The deepest water pushes hardest on the wall."),
    ]),
    ("Physics", "Friction", [
        ("A ball rolled on grass stops sooner than one rolled on a cemented floor because:", "grass offers more friction", ["gravity is stronger over grass", "the cement floor pushes the ball forward", "air is thicker over grass"], "Rougher surfaces give more friction, which opposes motion."),
        ("Rolling friction compared with sliding friction is:", "smaller", ["larger", "always equal", "zero"], "That is why wheels and ball bearings make moving easier."),
        ("Ball bearings are used in the hubs of cycle wheels to:", "replace sliding friction with smaller rolling friction", ["increase friction for better grip", "make the wheel heavier", "stop the wheel from rusting"], "Less friction means less wear and less effort."),
        ("Fluid friction (drag) on a moving object can be reduced by giving it:", "a streamlined shape", ["a flat front face", "a rough surface", "a larger front area"], "Fish, birds and aeroplanes are streamlined."),
    ]),
    ("Physics", "Sound", [
        ("Astronauts on a spacewalk talk to each other by radio because:", "sound needs a medium and space is nearly a vacuum", ["sound travels too fast in space", "their helmets block light", "radio waves are louder than voices"], "Radio waves are electromagnetic and travel through vacuum; sound cannot."),
        ("A body completes 40 oscillations in 2 seconds. Its frequency is:", "20 Hz", ["80 Hz", "40 Hz", "0.05 Hz"], "Frequency = oscillations per second = 40 ÷ 2."),
        ("The loudness of a sound depends on its:", "amplitude", ["frequency", "time period only", "speed"], "Loudness is proportional to the square of the amplitude."),
        ("Sounds of frequency above 20,000 Hz are called:", "ultrasonic", ["infrasonic", "audible", "subsonic"], "Bats and dolphins use ultrasound; humans cannot hear it."),
    ]),
    ("Physics", "Light", [
        ("A ray strikes a plane mirror at 30° to the mirror surface. The angle of reflection is:", "60°", ["30°", "90°", "120°"], "Angles are measured from the normal: 90° − 30° = 60°, and angle of incidence = angle of reflection."),
        ("Two plane mirrors kept at 60° to each other form how many images of an object between them?", "5", ["6", "3", "4"], "n = 360° ÷ 60° − 1 = 5."),
        ("Splitting of white light into seven colours by a prism is called:", "dispersion", ["reflection", "diffraction", "scattering"], "Each colour bends by a different amount."),
        ("The part of the eye that controls how much light enters is the:", "iris (with the pupil)", ["retina", "cornea", "optic nerve"], "The iris widens or narrows the pupil."),
    ]),
    ("Physics", "Electricity and natural phenomena", [
        ("In electroplating copper on an iron spoon, the spoon is joined to the:", "negative terminal (cathode)", ["positive terminal (anode)", "neither terminal", "both terminals"], "Positive Cu²⁺ ions move to the cathode and deposit there."),
        ("Lightning conductors protect tall buildings by:", "leading the charge safely into the earth", ["stopping clouds from forming", "repelling lightning back to the clouds", "storing the charge in the building"], "A metal rod from the top to the ground gives an easy path."),
        ("The Richter scale is used to measure:", "the magnitude of an earthquake", ["wind speed of a cyclone", "loudness of sound", "height of sea waves"], "Each step up means about 32 times more energy released."),
        ("Tap water conducts electricity but distilled water hardly does because:", "tap water contains dissolved salts", ["distilled water is colder", "tap water has more oxygen", "distilled water is heavier"], "Dissolved ions carry the current."),
    ]),
    ("Chemistry", "Metals and non-metals", [
        ("Which metal is stored under kerosene because it reacts violently with air and water?", "sodium", ["copper", "aluminium", "iron"], "Kerosene keeps air and moisture away."),
        ("White phosphorus is stored under water because it:", "catches fire in air", ["dissolves in kerosene", "reacts with water", "is a liquid metal"], "Water keeps air away but does not react with phosphorus."),
        ("A non-metal that conducts electricity well is:", "graphite (a form of carbon)", ["sulphur", "diamond", "iodine"], "Graphite has free electrons between its layers."),
        ("An iron nail dipped in blue copper sulphate solution turns brownish and the solution turns green because:", "iron displaces copper and forms iron sulphate", ["copper displaces iron", "the nail dissolves completely", "water reacts with the nail"], "Iron is more reactive than copper."),
        ("Oxides of non-metals such as sulphur dioxide, when dissolved in water, are:", "acidic", ["basic", "neutral", "always salts"], "SO₂ + H₂O → H₂SO₃ (sulphurous acid)."),
    ]),
    ("Chemistry", "Combustion and flame", [
        ("The hottest zone of a candle flame is the:", "outer non-luminous zone", ["inner dark zone", "middle luminous zone", "wick"], "Complete combustion happens in the outer zone."),
        ("The calorific value of a fuel is expressed in:", "kilojoule per kilogram (kJ/kg)", ["joule per second", "kilogram per litre", "degree Celsius"], "It is the heat given by burning 1 kg of the fuel completely."),
        ("Water is not used to put out an oil fire because:", "oil floats on water and keeps burning", ["water turns into oil", "water is itself a fuel", "oil soaks up all the water"], "Sand or a CO₂ extinguisher is used instead."),
        ("A poisonous gas produced by incomplete burning of fuel is:", "carbon monoxide", ["carbon dioxide", "oxygen", "nitrogen"], "CO binds to haemoglobin and stops oxygen transport."),
    ]),
    ("Chemistry", "Synthetic materials, coal and petroleum", [
        ("A plastic that softens on heating and can be re-shaped is:", "polythene (a thermoplastic)", ["bakelite", "melamine", "both bakelite and melamine"], "Thermosetting plastics like bakelite cannot be softened again."),
        ("Bakelite is used to make electric switches because it:", "is a poor conductor of heat and electricity", ["is a good conductor", "softens when warm", "is magnetic"], "It is a thermosetting plastic and an insulator."),
        ("Coke is obtained by:", "heating coal in the absence of air", ["burning coal in plenty of air", "mixing coal with water", "cooling petroleum gas"], "Coke is almost pure carbon, used to extract metals."),
        ("The slow change of buried dead vegetation into coal is called:", "carbonisation", ["fermentation", "vulcanisation", "distillation"], "It took millions of years under heat and pressure."),
        ("Which petroleum fraction is used to surface roads?", "bitumen", ["paraffin wax", "diesel", "LPG"], "Bitumen is the thick residue of refining."),
    ]),
    ("Biology", "Microorganisms", [
        ("Viruses differ from bacteria because viruses:", "multiply only inside a living host cell", ["have a peptidoglycan cell wall", "are killed by antibiotics", "are larger than bacteria"], "Outside a host a virus behaves like a non-living particle."),
        ("Yeast makes bread dough rise because it:", "releases carbon dioxide during respiration", ["adds water to the dough", "produces oxygen", "makes the flour heavier"], "The CO₂ bubbles make the dough spongy."),
        ("Pasteurised milk is heated to about:", "70 °C for 15–30 seconds and then chilled quickly", ["100 °C for one hour", "below 0 °C for a day", "40 °C for a week"], "This kills most harmful microbes without boiling."),
        ("The first vaccine (for smallpox) was developed by:", "Edward Jenner", ["Louis Pasteur", "Alexander Fleming", "Robert Koch"], "Jenner used cowpox material in 1796."),
        ("The female Anopheles mosquito spreads:", "malaria", ["dengue", "typhoid", "cholera"], "It carries the protozoan Plasmodium."),
    ]),
    ("Biology", "Cell, reproduction and adolescence", [
        ("An organelle found in plant cells but not in animal cells is the:", "plastid (chloroplast)", ["mitochondrion", "ribosome", "nucleus"], "Plastids carry pigments such as chlorophyll."),
        ("Hydra reproduces asexually mainly by:", "budding", ["binary fission", "spore formation", "seed formation"], "A bud grows on the body and detaches as a new hydra."),
        ("The hormone that changes a tadpole into a frog is:", "thyroxine", ["insulin", "adrenaline", "oestrogen"], "Iodine is needed to make thyroxine."),
        ("Lack of iodine in the diet can cause:", "goitre", ["diabetes", "night blindness", "scurvy"], "The thyroid gland swells when it cannot make enough thyroxine."),
        ("The sex of a human baby is decided by the chromosome in the:", "father's sperm (X or Y)", ["mother's egg", "placenta", "umbilical cord"], "Egg always carries X; a Y sperm gives a boy."),
    ]),
    ("Botany", "Crop production and plant conservation", [
        ("Which pair are both rabi (winter) crops?", "wheat and mustard", ["paddy and maize", "cotton and groundnut", "soyabean and paddy"], "Rabi crops are sown in October–November."),
        ("Growing a legume between two cereal crops helps because legumes:", "add nitrogen to the soil", ["remove all the weeds", "make the soil salty", "add phosphorus from the air"], "Rhizobium in their root nodules fixes nitrogen."),
        ("2,4-D is sprayed in fields as a:", "weedicide", ["fertiliser", "insecticide", "fungicide"], "It kills broad-leaf weeds, not the cereal crop."),
        ("A species found only in one particular area is called:", "endemic", ["exotic", "extinct", "migratory"], "The Indian giant squirrel is endemic to some forests."),
        ("The Red Data Book keeps a record of:", "endangered plants and animals", ["all crops grown in India", "rainfall data", "rocks and minerals"], "It is kept by the IUCN."),
        ("The antibiotic penicillin is obtained from a:", "fungus", ["bacterium", "virus", "green alga"], "Fleming found it in the mould Penicillium in 1928."),
    ]),
    ("Maths", "Numbers and algebra", [
        ("The value of (−3)³ is:", "−27", ["27", "−9", "9"], "(−3) × (−3) × (−3) = −27."),
        ("If 3x + 5 = 20, then x =", "5", ["15", "25/3", "3"], "3x = 15, so x = 5."),
        ("√1764 =", "42", ["44", "38", "41"], "42 × 42 = 1764."),
        ("The sum of the interior angles of a hexagon is:", "720°", ["540°", "360°", "900°"], "(n − 2) × 180° = 4 × 180°."),
    ]),
]
