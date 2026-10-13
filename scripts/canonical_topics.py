# scripts/canonical_topics.py
# Maps any question across all 9 subjects to its exact canonical Syllabus Unit / Chapter (Subsection)
# matching src/data/subjects.ts

CANONICAL_UNITS = {
    "van": [
        "Osteology & Arthrology",
        "Myology & Angiology",
        "Neurology & Special Senses",
        "Digestive, Respiratory & Urogenital Splanchnology",
        "General & Systemic Histology",
        "General & Applied Embryology & Avian Anatomy",
    ],
    "vpy": [
        "Blood, Hematology & Body Fluids",
        "Cardiovascular & Respiratory Physiology",
        "Digestive & Ruminant Physiology",
        "Renal & Environmental Physiology",
        "Neurophysiology, Muscle & Sense Organs",
        "Endocrinology, Reproduction & Lactation Physiology",
    ],
    "vbc": [
        "Biomolecules: Carbohydrates, Lipids & Proteins",
        "Enzymology, Coenzymes & Bioenergetics",
        "Intermediary Metabolism (Carbs, Lipid, Amino Acid)",
        "Molecular Biology & Acid-Base / Electrolyte Balance",
        "Clinical & Diagnostic Biochemistry (Liver/Kidney Function)",
        "Biochemistry of Hormones, Vitamins & Minerals",
    ],
    "lpm": [
        "General Livestock Management, Housing & Behavior",
        "Dairy Cattle & Buffalo Production Management",
        "Sheep & Goat Production Management",
        "Swine, Equine & Camel Management",
        "Poultry Production, Broiler & Layer Management",
        "Hatchery Management, Biosecurity & Animal Welfare",
    ],
    "vpp": [
        "General Pathology: Cell Injury, Degenerations & Necrosis",
        "Inflammation, Tissue Repair & Hemodynamic Disorders",
        "Systemic Pathology (Digestive, Respiratory, Cardiovascular, Urinary, Nervous & Reproductive)",
        "Pathology of Infectious Diseases (Bacterial, Viral, Fungal & Parasitic)",
        "Veterinary Oncology & Neoplasia",
        "Avian, Clinical & Necropsy Pathology",
    ],
    "vmc": [
        "General Bacteriology & Bacterial Genetics",
        "Systematic Bacteriology (Gram +ve, Gram -ve, Acid-Fast, Spirochetes & Mycoplasma)",
        "Veterinary Mycology & Mycotoxicoses",
        "General & Systematic Virology (DNA & RNA Animal/Poultry Viruses & Prions)",
        "Veterinary Immunology & Vaccinology",
        "Diagnostic Serology & Molecular Microbiology",
    ],
    "vpa": [
        "General Parasitology & Helminthology: Trematodes (Flukes)",
        "Helminthology: Cestodes (Tapeworms & Metacestodes)",
        "Helminthology: Nematodes (Gastrointestinal, Bursate & Filarial)",
        "Veterinary Entomology (Flies, Myiasis, Lice & Fleas)",
        "Veterinary Acarology (Hard/Soft Ticks & Mange Mites)",
        "Veterinary Protozoology (Hemoprotozoa, Coccidia & Flagellates)",
    ],
    "agb": [
        "Mendelian, Chromosomal & Cytogenetics",
        "Molecular Genetics, Genomics & Markers",
        "Population Genetics (Hardy-Weinberg Equilibrium & Gene Frequency)",
        "Quantitative Genetics (Variance, Heritability, Repeatability & Correlations)",
        "Selection Methods, Sire Evaluation & Breeding Values (BLUP)",
        "Mating Systems, Heterosis, Breeds & Conservation",
    ],
    "ann": [
        "Principles of Nutrition, Proximate Analysis & Nutrient Metabolism",
        "Feed Evaluation & Energy/Protein Partitioning (TDN, ME, NE, RUP/RDP)",
        "Forage Conservation (Silage, Hay), Feed Processing & Anti-Nutritional Factors",
        "Minerals, Vitamins, Feed Additives & Metabolic Deficiency Diseases",
        "Applied Ruminant Nutrition (Dairy Cattle, Buffalo, Sheep & Goat)",
        "Applied Monogastric, Poultry & Pet/Equine Nutrition",
    ],
}


def map_question_to_canonical_unit(q: dict) -> str:
    subj = q.get("subjectId", "").lower()
    raw_topic = (q.get("topic") or "").strip()
    units = CANONICAL_UNITS.get(subj)
    if not units:
        return raw_topic

    # If already an exact match to one of the 6 canonical units, return it immediately
    if raw_topic in units:
        return raw_topic

    text = f"{q.get('questionText', '')} {' '.join(q.get('options', []))} {q.get('explanation', '')}".lower()
    rt = raw_topic.lower()

    if subj == "vpp":
        # Check explicit raw_topic hints first
        if any(k in rt for k in ["avian", "poultry", "clinical pathology", "histopath", "necropsy", "post-mortem", "cytology"]):
            return units[5]
        if any(k in rt for k in ["oncology", "neoplasia", "tumor", "neoplasm"]):
            return units[4]
        if any(k in rt for k in ["inflammation", "healing", "repair", "hemodynamic", "edema", "thrombo", "shock", "infarct", "hyperemia", "congestion"]):
            return units[1]
        if any(k in rt for k in ["general pathology", "cell injury", "degeneration", "necrosis", "apoptosis", "pigment", "calcification", "amyloid"]):
            return units[0]
        if any(k in rt for k in ["infectious", "bacterial", "viral", "fungal", "prion", "parasitic"]):
            return units[3]
        if any(k in rt for k in ["systemic", "digestive", "respiratory", "cardiovascular", "urinary", "renal", "nervous", "reproductive", "endocrine", "cutaneous", "musculoskeletal", "toxicologic", "nutritional"]):
            return units[2]

        # Content-based classification for generic 'Veterinary Pathology' or 'Veterinary Pathology (ICAR PG PYQ)'
        if any(k in text for k in ["marek", "gumboro", "bursal", "newcastle", "ranikhet", "fowl", "poultry", "chicks", "broiler", "layer", "bursa of fabricius", "pullorum", "histomonas", "blackhead", "angara", "anticoagulant", "edta", "wintrobe", "mcv", "mchc", "transudate", "fixative", "formalin", "bouin", "zenker's fluid", "necropsy", "rigor mortis"]):
            return units[5]
        if any(k in text for k in ["tumor", "tumour", "carcinoma", "sarcoma", "melanoma", "lymphoma", "adenoma", "papilloma", "oncogene", "p53", "sticker", "venereal", "sarcoid", "sertoli cell", "seminoma", "mast cell tumor", "ameloblastoma", "paraneoplastic", "metastasis", "teratoma"]):
            return units[4]
        if any(k in text for k in ["inflammation", "exudate", "selectin", "integrin", "chemotaxis", "opsonin", "prostaglandin", "leukotriene", "bradykinin", "granuloma", "giant cell", "healing", "granulation tissue", "edema", "hyperemia", "congestion", "nutmeg liver", "heart failure cell", "thrombus", "thrombosis", "virchow", "zahn", "embolism", "infarct", "shock", "dic "]):
            return units[1]
        if any(k in text for k in ["cloudy swelling", "hydropic", "fatty change", "steatosis", "hyaline", "zenker", "amyloid", "congo red", "coagulative necrosis", "liquefactive necrosis", "caseous necrosis", "fat necrosis", "gangrene", "apoptosis", "caspase", "necroptosis", "pyroptosis", "calcification", "von kossa", "hemosiderin", "prussian blue", "bilirubin", "lipofuscin", "melanin", "anthracosis", "atrophy", "hypertrophy", "hyperplasia", "metaplasia", "dysplasia", "free radical"]):
            return units[0]
        if any(k in text for k in ["negri", "bollinger", "borrel", "cowdry", "johne", "paratuberculosis", "tuberculosis", "pearl disease", "black quarter", "enterotoxemia", "pulpy kidney", "actinomycosis", "wooden tongue", "lumpy jaw", "glanders", "anthrax", "brucella", "listeria", "button ulcer", "turkey-egg", "diamond skin", "zebra marking", "rinderpest", "ppr", "bluetongue", "foot-and-mouth", "distemper", "parvovirus", "rabies", "scrapie", "prion", "aspergill"]):
            return units[3]
        return units[2]

    if subj == "vmc":
        if any(k in rt for k in ["mycology", "fungal", "fungi", "mycotoxin"]):
            return units[2]
        if any(k in rt for k in ["immunology", "vaccine", "hypersensitivity", "immunity"]):
            return units[4]
        if any(k in rt for k in ["serology", "molecular", "diagnostic micro", "biosafety", "pcr", "elisa"]):
            return units[5]
        if any(k in rt for k in ["virology", "virus", "prion"]):
            return units[3]
        if any(k in rt for k in ["general bacteriology", "bacterial genetics", "sterilization", "staining", "morphology"]):
            return units[0]
        if any(k in rt for k in ["systematic bacteriology", "bacteriology"]):
            return units[1]

        # Content-based classification for generic 'Veterinary Microbiology'
        if any(k in text for k in ["fungus", "fungi", "yeast", "mold", "dermatophyte", "microsporum", "trichophyton", "aspergillus", "candida", "cryptococcus", "histoplasma", "blastomyces", "coccidioides", "sporothrix", "rhinosporidium", "sabouraud", "aflatoxin", "ochratoxin", "zearalenone", "fumonisin", "ergot", "mycotoxin"]):
            return units[2]
        if any(k in text for k in ["immunoglobulin", "igg", "igm", "iga", "ige", "igy", "mhc ", "t-cell", "b-cell", "cytokine", "interleukin", "interferon", "complement", "hypersensitivity", "arthus", "tuberculin", "adjuvant", "vaccine", "colostrum", "toll-like", "tlr", "bursa of fabricius", "thymus"]):
            return units[4]
        if any(k in text for k in ["elisa", "agid", "coggins", "coombs", "rose bengal", "milk ring", "complement fixation", "pcr", "taqman", "western blot", "southern blot", "northern blot", "biosafety", "bsl-", "hepa filter", "prozone", "flocculation"]):
            return units[5]
        if any(k in text for k in ["virus", "viridae", "virion", "capsid", "baltimore", "poxvirus", "herpesvirus", "adenovirus", "parvovirus", "circovirus", "picornavirus", "aphthovirus", "flavivirus", "pestivirus", "coronavirus", "rhabdovirus", "rabies", "paramyxovirus", "morbillivirus", "orthomyxovirus", "influenza", "reovirus", "orbivirus", "bluetongue", "birnavirus", "retrovirus", "lentivirus", "prion", "bacteriophage"]):
            return units[3]
        if any(k in text for k in ["peptidoglycan", "teichoic", "lipopolysaccharide", "lipid a", "endospore", "dipicolinic", "flagella", "pili", "fimbria", "gram stain", "ziehl-neelsen", "autoclave", "tyndallization", "hot air oven", "growth curve", "lag phase", "log phase", "transformation", "conjugation", "transduction", "plasmid", "transposon", "operon"]):
            return units[0]
        return units[1]

    if subj == "van":
        if any(k in rt for k in ["embryology", "avian", "fowl", "bird"]):
            return units[5]
        if any(k in rt for k in ["histology", "epithelium", "connective"]):
            return units[4]
        if any(k in rt for k in ["splanchnology", "digestive", "respiratory", "urogenital", "reproductive", "urinary"]):
            return units[3]
        if any(k in rt for k in ["neurology", "nervous", "cranial nerve", "eye", "ear", "sense"]):
            return units[2]
        if any(k in rt for k in ["myology", "angiology", "muscle", "artery", "vein", "heart", "cardiovascular"]):
            return units[1]
        if any(k in rt for k in ["osteology", "arthrology", "bone", "skull", "vertebra", "joint"]):
            return units[0]

        if any(k in text for k in ["avian", "fowl", "chicken", "synsacrum", "notarium", "pygostyle", "pecten", "proventriculus", "gizzard", "cloaca", "embryo", "placenta", "blastocyst", "neural crest", "pronephros", "mesonephros", "metanephros", "somite", "ectoderm", "endoderm", "mesoderm"]):
            return units[5]
        if any(k in text for k in ["epithelium", "histolog", "purkinje", "kupffer", "sertoli", "leydig", "parietal cell", "chief cell", "podocyte", "hassall", "pulp", "collagen", "stain", "h&e"]):
            return units[4]
        if any(k in text for k in ["nerve", "plexus", "spinal cord", "brain", "cerebell", "meninges", "cauda equina", "eye", "cornea", "retina", "tapetum", "ear", "cochlea"]):
            return units[2]
        if any(k in text for k in ["tongue", "papilla", "tooth", "dental", "stomach", "rumen", "omasum", "abomasum", "intestine", "colon", "cecum", "liver", "pancreas", "lung", "trachea", "bronchus", "guttural", "kidney", "renal", "testis", "penis", "ovary", "uterus", "cervix"]):
            return units[3]
        if any(k in text for k in ["muscle", "tendon", "ligament", "stay apparatus", "lacertus", "linea alba", "diaphragm", "heart", "ventricle", "atrium", "aorta", "artery", "vein", "ductus", "foramen ovale", "rete mirabile", "thoracic duct"]):
            return units[1]
        return units[0]

    if subj == "vpy":
        if any(k in text for k in ["blood", "erythrocyte", "rbc", "hemoglobin", "leukocyte", "neutrophil", "platelet", "coagulation", "clotting", "plasma", "albumin", "esr", "anticoagulant", "extracellular fluid"]):
            return units[0]
        if any(k in text for k in ["heart", "cardiac", "ecg", "pacemaker", "sinoatrial", "frank-starling", "blood pressure", "baroreceptor", "respirat", "lung", "alveol", "surfactant", "bohr", "haldane", "chloride shift", "tidal volume", "oxygen", "parabronchi"]):
            return units[1]
        if any(k in text for k in ["saliva", "rumen", "ruminant", "reticul", "omas", "abomas", "volatile fatty", "vfa", "eructation", "cud", "gastric", "bile", "pancrea", "intestin", "digestion", "cholecystokinin", "secretin", "gastrin"]):
            return units[2]
        if any(k in text for k in ["kidney", "renal", "nephron", "glomerul", "gfr", "henle", "macula densa", "renin", "angiotensin", "aldosterone", "adh", "vasopressin", "urine", "thermoregulation", "sweat", "panting", "heat stress"]):
            return units[3]
        if any(k in text for k in ["neuron", "action potential", "synapse", "neurotransmitter", "acetylcholine", "muscle", "sarcomere", "actin", "myosin", "troponin", "rigor", "reflex", "hypothalamus", "eeg", "vision", "hearing"]):
            return units[4]
        return units[5]

    if subj == "vbc":
        if any(k in text for k in ["glycolysis", "gluconeogenesis", "glycogen", "hmp shunt", "pentose", "cori cycle", "propionate", "beta-oxidation", "carnitine", "ketogenesis", "fatty acid synthesis", "cholesterol", "hmg-coa", "transamination", "urea cycle", "ammonia"]):
            return units[2]
        if any(k in text for k in ["dna", "rna", "replication", "transcription", "translation", "codon", "pcr", "operon", "okazaki", "telomerase", "ph ", "buffer", "bicarbonate", "henderson-hasselbalch", "acidosis", "alkalosis", "anion gap"]):
            return units[3]
        if any(k in text for k in ["ast", "alt", "sdh", "gldh", "ggtp", "alkaline phosphatase", "ck ", "creatine kinase", "troponin", "bilirubin", "van den bergh", "jaundice", "bun", "creatinine", "clearance", "ketone", "rothera", "bence-jones", "glycosuria"]):
            return units[4]
        if any(k in text for k in ["vitamin", "thiamine", "riboflavin", "niacin", "pyridoxine", "biotin", "cobalamin", "folic", "ascorbic", "retinol", "calciferol", "tocopherol", "phylloquinone", "calcium", "phosphorus", "magnesium", "iron", "copper", "zinc", "selenium", "cobalt", "hormone", "camp", "second messenger", "steroid"]):
            return units[5]
        if any(k in text for k in ["enzyme", "michaelis", "km ", "vmax", "competitive inhibition", "allosteric", "isoenzyme", "coenzyme", "atp", "electron transport", "oxidative phosphorylation", "cytochrome", "rotenone", "oligomycin", "uncoupler", "tca cycle", "krebs"]):
            return units[1]
        return units[0]

    if subj == "lpm":
        if any(k in text for k in ["hatchery", "incubation", "fumigation", "candling", "egg storage", "quarantine", "biosecurity", "disinfection", "welfare", "transport"]):
            return units[5]
        if any(k in text for k in ["broiler", "layer", "poultry", "chick", "deep litter", "cage", "debeaking", "dubbing", "photoperiod", "lighting", "hen"]):
            return units[4]
        if any(k in text for k in ["pig", "swine", "sow", "boar", "piglet", "farrowing", "needle teeth", "ear notching", "horse", "equine", "mare", "stallion", "foal", "camel"]):
            return units[3]
        if any(k in text for k in ["sheep", "goat", "ewe", "doe", "ram", "buck", "lamb", "kid", "flushing", "shearing", "tagging", "crutching", "docking", "browse"]):
            return units[2]
        if any(k in text for k in ["loose housing", "floor space", "paddock", "orientation", "long axis", "eave", "ventilation", "dentition", "ageing", "branding", "tattooing", "ear tagging"]):
            return units[0]
        return units[1]

    if subj == "vpa":
        if any(k in text for k in ["protozo", "trypanosom", "babesia", "theileria", "eimeria", "coccidia", "isospora", "toxoplasma", "cryptosporidium", "histomonas", "trichomonas", "giardia", "leishmania", "sarcocystis", "anaplasma", "ehrlichia", "hepatozoon"]):
            return units[5]
        if any(k in text for k in ["tick", "mite", "acarolog", "boophilus", "rhipicephalus", "hyalomma", "haemaphysalis", "amblyomma", "ixodes", "dermacentor", "argus", "ornithodoros", "otobius", "sarcoptes", "psoroptes", "chorioptes", "demodex", "knemidocoptes", "notoedres", "otodectes", "haller"]):
            return units[4]
        if any(k in text for k in ["fly", "flies", "diptera", "tabanus", "stomoxys", "glossina", "musca", "culicoides", "simulium", "phlebotomus", "oestrus ovis", "hypoderma", "gasterophilus", "chrysomya", "lucilia", "myiasis", "melophagus", "hippobosca", "lice", "louse", "haematopinus", "linognathus", "damalinia", "menopon", "flea", "ctenocephalides", "xenopsylla"]):
            return units[3]
        if any(k in text for k in ["cestod", "tapeworm", "taenia", "echinococcus", "hydatid", "moniezia", "dipylidium", "anoplocephala", "davainea", "raillietina", "cotugnia", "cysticerc", "coenurus", "sparganum", "diphyllobothrium", "mesocestoides", "scolex", "proglottid", "oribatid"]):
            return units[1]
        if any(k in text for k in ["trematod", "fluke", "fasciola", "paramphistom", "cotylophoron", "gastrothylax", "gastrodiscoides", "dicrocoelium", "schistosoma", "prosthogonimus", "paragonimus", "opisthorchis", "nanophyetus", "miracidium", "sporocyst", "redia", "cercaria", "metacercaria", "snail", "lymnaea", "indoplanorbis"]):
            return units[0]
        return units[2]

    if subj == "agb":
        if any(k in text for k in ["dna", "rna", "pcr", "marker", "rflp", "microsatellite", "snp", "genomic selection", "qtl", "booroola", "fecb", "callipyge", "myostatin", "halothane", "blad", "dumps", "cvm", "operon", "codon", "transgenic"]):
            return units[1]
        if any(k in text for k in ["hardy-weinberg", "gene frequency", "allele frequency", "2pq", "random mating", "mutation", "migration", "genetic drift", "effective population"]):
            return units[2]
        if any(k in text for k in ["selection differential", "intensity of selection", "response to selection", "genetic gain", "tandem", "independent culling", "selection index", "progeny test", "blup", "henderson", "sire evaluation", "moet", "onbs"]):
            return units[4]
        if any(k in text for k in ["heritability", "repeatability", "mppa", "variance", "additive", "genetic correlation", "half-sib", "regression", "quantitative", "polygenic"]):
            return units[3]
        if any(k in text for k in ["inbreeding", "outbreeding", "crossbreeding", "grading up", "crisscross", "rotational", "heterosis", "hybrid vigor", "karan", "frieswal", "sunandini", "hissardale", "avikalin", "conservation", "nbagr"]):
            return units[5]
        return units[0]

    if subj == "ann":
        if any(k in text for k in ["weende", "proximate", "kjeldahl", "ether extract", "soxhlet", "crude fiber", "nitrogen-free", "van soest", "ndf", "adf", "adl", "hemicellulose", "metabolic water", "biohydrogenation"]):
            return units[0]
        if any(k in text for k in ["tdn", "gross energy", "digestible energy", "metabolizable energy", "net energy", "heat increment", "starch equivalent", "biological value", "npu", "respiratory quotient", "digestibility", "tilley", "in sacco", "rdp", "rup", "bypass"]):
            return units[1]
        if any(k in text for k in ["silage", "hay", "haylage", "flieg", "urea treatment", "ammoniation", "ummb", "pellet", "extrusion", "hcn", "dhurrin", "prussic", "nitrate", "oxalate", "gossypol", "mimosine", "trypsin inhibitor", "tannin", "saponin", "aflatoxin", "ricin", "anti-nutritional"]):
            return units[2]
        if any(k in text for k in ["mineral", "calcium", "phosphorus", "milk fever", "magnesium", "grass tetany", "copper", "swayback", "enzootic ataxia", "cobalt", "zinc", "parakeratosis", "manganese", "perosis", "selenium", "white muscle", "mulberry heart", "exudative diathesis", "alkali disease", "iodine", "goiter", "iron", "vitamin", "retinol", "tocopherol", "crazy chick", "thiamine", "star-gazing", "riboflavin", "curled-toe", "niacin", "pantothenic", "goose-stepping", "biotin", "choline", "ionophore", "monensin", "probiotic"]):
            return units[3]
        if any(k in text for k in ["poultry", "broiler", "layer", "chick", "swine", "pig", "sow", "limiting amino", "methionine", "lysine", "cat ", "feline", "taurine", "dog", "canine", "equine", "horse", "pearson"]):
            return units[5]
        return units[4]

    return raw_topic
