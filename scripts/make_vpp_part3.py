import json

part3 = {
    "vpp_exp_068": [
        "Marked swelling and enlargement of the thyroid and parathyroid glands",
        "Acute catarrhal enteritis with copious watery luminal diarrhea",
        "Multiple discrete caseous granulomas within mesenteric lymph nodes"
    ],
    "vpp_exp_069": [
        "Equine Purpura Hemorrhagica (aseptic necrotizing vasculitis post-strangles)",
        "Equine Infectious Anemia (retroviral chronic immune-mediated hemolysis)",
        "African Horse Sickness (orbiviral severe pulmonary edema and cardiac effusion)"
    ],
    "vpp_exp_070": [
        "Type III Hypersensitivity (Arthus reaction with immune complex deposition)",
        "Type I Hypersensitivity (Immediate IgE-mediated mast cell anaphylaxis)",
        "Type IV Hypersensitivity (Delayed-type cell-mediated T-cell cytotoxicity)"
    ],
    "vpp_exp_071": [
        "Fibrinoid necrosis of small muscular arteries with intense neutrophil infiltration",
        "Extensive amyloid deposition within renal glomerular capillary loops",
        "Severe caseous necrosis with multinucleated Langhans giant cells"
    ],
    "vpp_exp_073": [
        "Equine Viral Arteritis (EVA, arterivirus causing panvasculitis and edema)",
        "Equine Herpesvirus-1 (EHV-1, herpesvirus causing myeloencephalopathy)",
        "African Horse Sickness (AHSV, orbivirus causing high-protein pulmonary effusion)"
    ],
    "vpp_exp_074": [
        "Bovine Malignant Catarrhal Fever (Ovine herpesvirus-2 causing lymphoproliferation)",
        "Bovine Viral Diarrhea (Pestivirus causing mucosal disease and ulcers)",
        "Infectious Bovine Rhinotracheitis (Bovine herpesvirus-1 causing tracheitis)"
    ],
    "vpp_exp_075": [
        "Generalized necrotizing vasculitis with marked perivascular lymphoid cuffing",
        "Severe chronic granulomatous lymphadenitis with caseous necrosis",
        "Extensive microvesicular fatty degeneration of hepatic parenchyma"
    ],
    "vpp_exp_076": [
        "Bluetongue Virus (Orbivirus transmitted by Culicoides midges)",
        "Peste des Petits Ruminants Virus (Morbillivirus transmitted by aerosols)",
        "Sheeppox Virus (Capripoxvirus transmitted by direct contact and fomites)"
    ],
    "vpp_exp_077": [
        "Cyanosis of tongue, coronitis, pulmonary artery base hemorrhage, and muscle necrosis",
        "Severe erosive stomatitis, button ulcers in colon, and splenomegaly",
        "Generalized cutaneous papules, pocks, and proliferative lung nodules"
    ],
    "vpp_exp_078": [
        "Peste des Petits Ruminants (PPR / Goat Plague caused by a Morbillivirus)",
        "Contagious Caprine Pleuropneumonia (CCPP caused by Mycoplasma)",
        "Contagious Ecthyma (Orf caused by a Parapoxvirus producing scabs)"
    ],
    "vpp_exp_079": [
        "Zebra-stripe hemorrhages on the mucosal folds of the large intestine and rectum",
        "Pale chalky dry streaks of Zenker's degeneration in pectoral muscles",
        "Concentric 'onion-peel' caseous lymphadenitis of superficial lymph nodes"
    ],
    "vpp_exp_080": [
        "Erosive stomatitis, catarrhal conjunctivitis, severe enteritis, and pneumonia",
        "Severe acute laminitis with hooves sloughing and dorsal decubitus ulcers",
        "Extensive generalized cutaneous nodular plaques healing with star-shaped scars"
    ],
    "vpp_exp_081": [
        "Swine Erysipelas (Diamond skin disease caused by Erysipelothrix rhusiopathiae)",
        "Porcine Dermatitis and Nephropathy Syndrome (PDNS caused by PCV-2)",
        "Greasy Pig Disease (Exudative epidermitis caused by Staphylococcus hyicus)"
    ],
    "vpp_exp_082": [
        "Microvascular thrombosis, endothelial necrosis, and cutaneous rhomboid infarcts",
        "Superficial bacterial colonization producing excessive exfoliative sebaceous crusts",
        "Type III immune-complex glomerulonephritis with widespread purpuric vasculitis"
    ],
    "vpp_exp_083": [
        "Vegetative endocarditis of the mitral and aortic valves resembling cauliflower",
        "Chronic caseous lymphadenitis of mesenteric and bronchial lymph nodes",
        "Extensive button ulcers encircling the mucosal folds of the cecum"
    ],
    "vpp_exp_084": [
        "Glanders (Farcy caused by Burkholderia mallei in equids)",
        "Strangles (Suppurative lymphadenitis caused by Streptococcus equi)",
        "Epizootic Lymphangitis (Granulomatous lymphangitis caused by Histoplasma)"
    ],
    "vpp_exp_085": [
        "Stellate (star-shaped) scars following ulceration of nasal mucosal nodules",
        "Extensive button ulcers on the mucosal surface of the ileocecal valve",
        "Concentric calcified laminar rings within mediastinal lymph node capsules"
    ],
    "vpp_exp_086": [
        "Nasal, pulmonary, and cutaneous forms (Farcy with beaded lymphatics)",
        "Visceral, ocular, and cutaneous forms with severe internal lymphosarcoma",
        "Neural, visceral, and ocular forms with bilateral sciatic enlargement"
    ],
    "vpp_exp_087": [
        "Contagious Bovine Pleuropneumonia (CBPP caused by Mycoplasma mycoides)",
        "Hemorrhagic Septicemia (HS caused by Pasteurella multocida B:2 / E:2)",
        "Bovine Tuberculosis (BTB caused by Mycobacterium bovis)"
    ],
    "vpp_exp_088": [
        "Marbled appearance of lungs due to wide interlobular septa distended with lymph and fibrin",
        "Consolidation of cranial ventral lung lobes with suppurative bronchopneumonia",
        "Disseminated fibrocaseous calcified granulomas throughout the dorsal lung lobes"
    ],
    "vpp_exp_089": [
        "Sequestrum formation (necrotic lung parenchyma encapsulated by dense fibrous tissue)",
        "Cavitation with bronchopleural fistula draining into thoracic cavity",
        "Complete resolution without any residual fibrosis or pleural adhesions"
    ],
    "vpp_exp_090": [
        "Hemorrhagic Septicemia (Pasteurella multocida serotypes B:2 and E:2)",
        "Blackleg (Clostridium chauvoei emphysematous necrotizing myositis)",
        "Anthrax (Bacillus anthracis peracute septicemic splenomegaly)"
    ],
    "vpp_exp_091": [
        "Severe submandibular, pharyngeal, and brisket edema with marked petechiae",
        "Emphysematous crackling crepitant swelling of thigh and shoulder muscles",
        "Marked uncoagulated tarry dark blood oozing from all natural body orifices"
    ],
    "vpp_exp_092": [
        "Blackleg (Black Quarter / Emphysematous Gangrene caused by Clostridium chauvoei)",
        "Malignant Edema (False blackleg caused by Clostridium septicum)",
        "Bacillary Hemoglobinuria (Redwater disease caused by Clostridium novyi type D)"
    ],
    "vpp_exp_093": [
        "Dark red/black crepitant swelling in heavy muscle masses smelling of rancid butter",
        "Diffuse soft, non-crepitant, cold gelatinous subcutaneous edema without gas",
        "Massive focal ischemic infarction of the liver with pale necrotic borders"
    ],
    "vpp_exp_094": [
        "Malignant Edema (Gas Gangrene following wound contamination by Clostridium septicum)",
        "Tetanus (Spastic neurotoxic paralysis following Clostridium tetani puncture)",
        "Botulism (Flaccid neurotoxic paralysis following Clostridium botulinum ingestion)"
    ],
    "vpp_exp_095": [
        "Bacillary Hemoglobinuria (Redwater Disease caused by Clostridium haemolyticum / novyi type D)",
        "Black Disease (Infectious Necrotic Hepatitis caused by Clostridium novyi type B)",
        "Pulpy Kidney Disease (Enterotoxemia caused by Clostridium perfringens type D)"
    ],
    "vpp_exp_096": [
        "Large ischemic infarct in liver initiated by migrating immature Fasciola hepatica flukes",
        "Diffuse hepatic lipidosis accompanied by severe ketonuria and hypoglycemia",
        "Severe caseous abscessation of mesenteric lymph nodes causing portal hypertension"
    ],
    "vpp_exp_097": [
        "Black Disease (Infectious Necrotic Hepatitis caused by Clostridium novyi type B)",
        "Braxy (Acute abomasitis in sheep caused by Clostridium septicum)",
        "Lamb Dysentery (Hemorrhagic enterotoxemia caused by Clostridium perfringens type B)"
    ],
    "vpp_exp_098": [
        "Pulpy Kidney Disease (Enterotoxemia / Overeating disease caused by Clostridium perfringens type D)",
        "Struck (Acute enterotoxemia in adult sheep caused by Clostridium perfringens type C)",
        "Lamb Dysentery (Severe ulcerating enteritis caused by Clostridium perfringens type B)"
    ],
    "vpp_exp_099": [
        "Epsilon toxin (activated by trypsin in the intestinal lumen into a lethal neurotoxin)",
        "Alpha toxin (phospholipase C causing rapid membrane destruction and hemolysis)",
        "Beta toxin (necrotizing toxin inducing acute severe hemorrhagic enteritis)"
    ],
    "vpp_exp_100": [
        "Rapid post-mortem autolysis of renal parenchyma (pulpy kidneys) and glucosuria",
        "Extensive button ulcers in the colon mucosa and severe splenic infarction",
        "Chronic caseous lymphadenitis with concentric onion-ring laminations"
    ]
}

with open('scripts/vpp_part3.json', 'w', encoding='utf-8') as f:
    json.dump(part3, f, indent=2)

print(f"Wrote {len(part3)} overrides in part 3")
