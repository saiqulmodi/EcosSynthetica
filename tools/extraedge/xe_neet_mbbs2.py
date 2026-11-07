"""Extra-Edge Q/A, NEET/MBBS batch 2: physiology numbers, embryology, genetics, clinical basics."""
CLS = 12
LEVEL = "NEET/MBBS"

SETS = [
    ("Biology", "MBBS physiology: normal values", [
        ("Normal adult blood pressure is about:", "120/80 mm Hg", ["90/40 mm Hg", "160/110 mm Hg", "200/120 mm Hg"], "Systolic/diastolic."),
        ("Normal fasting blood glucose is about:", "70–100 mg/dL", ["20–40 mg/dL", "200–300 mg/dL", "500 mg/dL"], "126 mg/dL or more fasting suggests diabetes."),
        ("Normal haemoglobin in adult men is about:", "13–17 g/dL", ["5–7 g/dL", "25–30 g/dL", "1–2 g/dL"], "Women about 12–15 g/dL."),
        ("Normal platelet count is about:", "1.5–4.5 lakh per mm³", ["5,000 per mm³", "50 lakh per mm³", "500 per mm³"], "Low count raises bleeding risk (dengue)."),
        ("Normal total white cell count is about:", "4,000–11,000 per mm³", ["100–500 per mm³", "1–2 lakh per mm³", "50 lakh per mm³"], "Neutrophils are the largest share."),
        ("The most numerous white blood cells are:", "neutrophils", ["lymphocytes", "monocytes", "basophils"], "About 60–65%."),
        ("Normal core body temperature is about:", "37 °C (98.6 °F)", ["35 °C", "40 °C", "33 °C"], "Controlled by the hypothalamus."),
        ("Daily urine output of a healthy adult is about:", "1–1.5 L", ["5–6 L", "100 mL", "10 L"], "Below 400 mL/day is oliguria."),
    ]),
    ("Biology", "MBBS embryology and genetics basics", [
        ("The placenta forms from the:", "chorionic villi of the embryo and the uterine tissue", ["yolk sac alone", "amnion alone", "ovary"], "It also makes hormones like hCG."),
        ("The heart of the human embryo starts beating at about:", "the end of the first month", ["the ninth month", "the second week only", "birth"], "First signs of a beating heart."),
        ("Gastrulation forms the:", "three germ layers", ["morula", "zygote", "placenta"], "Ectoderm, mesoderm and endoderm."),
        ("Neural tube defects can be reduced by taking before and in early pregnancy:", "folic acid", ["vitamin C", "iron alone", "calcium"], "Spina bifida is an example."),
        ("A Barr body is an inactive:", "X chromosome", ["Y chromosome", "autosome", "mitochondrion"], "Normal females have one Barr body."),
        ("Thalassaemia is a:", "quantitative defect in globin chain synthesis", ["qualitative amino acid change like sickle cell", "clotting factor deficiency", "white cell cancer"], "Autosomal recessive."),
        ("Huntington's disease is inherited as:", "autosomal dominant", ["autosomal recessive", "X-linked recessive", "Y-linked"], "One copy is enough to cause it."),
        ("Turner syndrome (45, XO) individuals are:", "females with underdeveloped ovaries", ["males with extra X", "normal fertile males", "always triploid"], "Short stature is common."),
    ]),
    ("Biology", "MBBS clinical basics", [
        ("Jaundice is a yellow colour of skin due to excess:", "bilirubin", ["haemoglobin", "urea", "cholesterol"], "From breakdown of haem."),
        ("Goitre with bulging eyes (exophthalmos) is typical of:", "Graves' disease (hyperthyroidism)", ["cretinism", "Addison's disease", "diabetes insipidus"], "An autoimmune disease."),
        ("Addison's disease is due to too little:", "cortisol and aldosterone (adrenal cortex)", ["insulin", "thyroxine", "growth hormone"], "Skin may darken."),
        ("Acromegaly in adults is caused by too much:", "growth hormone", ["thyroxine", "insulin", "melatonin"], "Hands, feet and jaw enlarge."),
        ("Atherosclerosis is narrowing of arteries by:", "fatty plaques of cholesterol", ["calcium in veins", "blood clots in capillaries only", "bacteria"], "Leads to heart attacks and strokes."),
        ("Angina pectoris is chest pain caused by:", "too little oxygen reaching the heart muscle", ["a broken rib", "lung infection", "stomach acid only"], "Coronary arteries are narrowed."),
        ("Dialysis is used when the:", "kidneys fail", ["lungs fail", "liver is enlarged", "heart rate is slow"], "An artificial kidney filters blood."),
        ("Oral rehydration solution contains:", "sodium, glucose and water in set amounts", ["only sugar", "only salt", "antibiotics"], "Glucose helps sodium and water absorption."),
    ]),
    ("Chemistry", "MBBS-relevant chemistry", [
        ("Antacids such as Mg(OH)₂ work by:", "neutralising excess stomach acid", ["killing bacteria", "making more acid", "blocking nerves"], "Ranitidine-type drugs cut acid production instead."),
        ("Paracetamol is chemically an:", "amide (acetaminophen)", ["ester", "alkane", "ketone"], "N-acetyl-p-aminophenol."),
        ("Tincture of iodine is used as an:", "antiseptic", ["antacid", "antibiotic tablet", "analgesic"], "Iodine in alcohol–water."),
        ("Saccharin is an artificial sweetener about:", "550 times sweeter than sugar", ["2 times sweeter", "as sweet as sugar", "less sweet"], "Excreted unchanged in urine."),
        ("Sulpha drugs (sulphonamides) act as:", "antibacterial agents", ["antacids", "tranquillisers", "antihistamines"], "They block folic acid synthesis in bacteria."),
    ]),
    ("Physics", "MBBS-relevant physics", [
        ("MRI scanners image the body using:", "strong magnetic fields and radio waves", ["X-rays", "gamma rays", "ultrasound"], "No ionising radiation."),
        ("Ultrasound scans of the foetus use frequencies of about:", "2–15 MHz", ["20 Hz", "50 Hz", "1 THz"], "Above human hearing."),
        ("A CT scan uses:", "X-rays from many angles", ["sound waves", "magnetism only", "visible light"], "A computer builds cross-sections."),
        ("Lead aprons protect X-ray staff because lead:", "has a high density and atomic number that absorbs X-rays", ["reflects all light", "is magnetic", "is a good conductor"], "Absorption rises steeply with Z."),
    ]),
]
