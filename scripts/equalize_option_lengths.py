# scripts/equalize_option_lengths.py
import json
import re
import os
import sys

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

# Domain term dictionaries for veterinary sciences
ANAT_SYNONYMS = {
    'Cephalic vein': 'Lateral cephalic vein (Antebrachial cephalic vein)',
    'Saphenous vein': 'Medial saphenous vein (Medial tarsal vein)',
    'Femoral vein': 'Deep femoral vein (Femoral triangle vein)',
    'Jugular vein': 'External jugular vein (Jugular furrow vein)',
    'Olfactory bulb': 'Olfactory bulb (Bulbus olfactorius)',
    'Cerebellum': 'Cerebellar vermis (Corpus cerebelli)',
    'Pineal body': 'Pineal body (Epiphysis cerebri)',
    'Roaring': 'Roaring (equine laryngeal hemiplegia)',
    'Stringhalt': 'Stringhalt (equine reflex hypertonia)',
    'Shivering': 'Shivering (caudal muscle myoclonus)',
    'Pericardial cavity': 'Pericardial cavity (parietal pericardial sac)',
    'Pleural space': 'Mediastinal pleural space (pleural cavity)',
    'Pelvic cavity': 'Ischiorectal fossa (pararectal pelvic cavity)',
    'Comb': 'Comb (cranial fleshy caruncle)',
    'Wing tip': 'Wing tip (carpometacarpus)',
    'Sternum': 'Sternum (ventral keel / carina)',
    'Zona fasciculata': 'Zona fasciculata (or Zona spongiosa)',
    'Zona reticularis': 'Zona reticularis (or Zona juxtamedullaris)',
    'Adrenal medulla': 'Adrenal medulla (or Chromaffin center)',
    'Hemoendothelial': 'Hemoendothelial (or Hemomaternal endothelial)',
    'Hemochorial': 'Hemochorial (or Hemomaternal trophotesticular)',
    'Endotheliochorial': 'Endotheliochorial (or Endothelio-trophoblastic)',
    'Skin precursor': 'Cutaneous skin and epidermal precursor',
    'Yolk accumulator': 'Nutrient yolk accumulator and storage sac',
    'Bony framework': 'Rigid cartilaginous and bony framework',
    'Cryptorchidism': 'Undescended intra-abdominal retention of testes',
    'Spina bifida': 'Dorsal non-union of vertebral arches and neural tube',
    'Cleft palate': 'Congenital palatoschisis defect of the secondary palate',
    'Secretin': 'Secretin (duodenal mucosal peptide)',
    'Hydrochloric acid': 'Hydrochloric acid (gastric parietal secretion)',
    'Gastrin': 'Gastrin (antral G-cell peptide)',
    'Alveoli': 'Alveoli (terminal gas exchange saccules)',
    'Nasal septum': 'Nasal septum (cartilaginous midline septum)',
    'Trachea': 'Trachea (cartilaginous tracheobronchial conduit)',
    'Kidney': 'Kidney (Renal cortical and medullary parenchyma)',
    'Spleen': 'Spleen (Splenic red pulp and white pulp lymphoid follicles)',
    'Myocardium': 'Myocardium (Left ventricular muscular wall)',
    'Liver': 'Liver (Hepatic lobules and portal triads)',
    'Brain': 'Brain (Cerebral cortex and cerebellar hemispheres)',
    'Reticulum': 'Reticulum (cranial honey-comb reticulum chamber)',
    'Abomasum': 'Abomasum (true acid-secreting glandular abomasum)',
    'Omasum': 'Omasum (manyplies water-absorbing laminae chamber)',
}

MICRO_SYNONYMS = {
    'Teichoic acid': 'Lipoteichoic acid (polyol phosphate polymer)',
    'Lipopolysaccharide': 'Lipopolysaccharide endotoxin (Lipid A with O-antigen)',
    'Peptidoglycan': 'Cross-linked peptidoglycan (murein sacculus polymer)',
    'Crystal violet': 'Gram crystal violet-iodine (demonstrating purple peptidoglycan)',
    'Indian ink': 'Indian ink negative staining (demonstrating clear halos of capsules)',
    'Carbol fuchsin': 'Ziehl-Neelsen carbol fuchsin (demonstrating bright red acid-fast bacilli)',
    'Methylene blue': 'Loeffler alkaline methylene blue (demonstrating metachromatic granules)',
    'Safranin': 'Safranin O counterstain (demonstrating pink Gram-negative envelopes)',
    'Malachite green': 'Schaeffer-Fulton malachite green (demonstrating green endospores)',
    'Giemsa stain': 'Giemsa Romanowsky stain (demonstrating blue cytoplasm and red nuclei)',
    'Coronary thrombosis': 'Coronary thrombosis (acute myocardial infarction)',
    'Rabies': 'Rabies virus (Negri body encephalomyelitis)',
    'Acute pancreatitis': 'Acute necrotizing enzymatic pancreatitis',
    'Actinobacillus pleuropneumoniae': 'Actinobacillus pleuropneumoniae (Porcine Pleuropneumonia)',
    'Classical Swine Fever': 'Classical Swine Fever Virus (Hog Cholera Petechiation)',
    'Streptococcus suis': 'Streptococcus suis (Porcine Streptococcal Polyserositis)',
    'Salmonella Typhimurium': 'Salmonella Typhimurium (Acute enterocolitis and septicemia)',
    'Bacillus anthracis': 'Bacillus anthracis (Anthrax / Splenic fever agent)',
    'Escherichia coli': 'Escherichia coli (Colibacillosis / Enteric scours)',
    'Trichophyton equinum': 'Trichophyton equinum (Equine dermatophytosis / Ringworm)',
    'Trichophyton verrucosum': 'Trichophyton verrucosum (Bovine barn ringworm / Dermatophyte)',
    'Microsporum gypseum': 'Microsporum gypseum (Geophilic dermatophyte ringworm)',
}

PATH_SYNONYMS = {
    'Pyogenic abscesses': 'Chronic suppurative microabscesses encapsulated by granulation tissue',
    'Caseous necrosis': 'Caseous necrosis with cheesy amorphous coagulated debris',
    'Granulomas': 'Chronic granulomatous inflammation with epithelioid macrophages and giant cells',
    'Coagulative necrosis': 'Coagulative necrosis preserving ghost cellular outlines',
    'Liquefactive necrosis': 'Liquefactive necrosis with rapid enzymatic tissue dissolution',
    'Fat necrosis': 'Enzymatic fat necrosis with opaque chalky calcium saponification',
    'Fibrinoid necrosis': 'Fibrinoid necrosis of arterial walls with immune complex deposition',
    'Pyknosis': 'Nuclear pyknosis with irreversible chromatin shrinkage and condensation',
    'Karyolysis': 'Nuclear karyolysis with total enzymatic dissolution of chromatin',
    'Karyorrhexis': 'Nuclear karyorrhexis with chromatin fragmentation into basophilic dust',
    'Fatty change': 'Hepatocellular accumulation of neutral triglycerides (Hepatic lipidosis)',
    'Amyloidosis': 'Extracellular deposition of fibrillar beta-pleated sheet amyloid protein',
    'Hyaline change': 'Homogeneous glassy eosinophilic proteinaceous intracellular degeneration',
    'Astrocyte death': 'Proliferation of reactive fibrous astrocytes forming dense gemistocytic glial scars',
    'Erythrocyte extravasation': 'Extravasation of erythrocytes through necrotic blood vessel walls with cuffing',
    'Demyelination alone': 'Progressive primary autoimmune demyelination of central axons with soma preservation',
    'Skeletal muscle': 'Striated skeletal muscle fibers undergoing coagulative Zenker necrosis',
    'Adipose tissue': 'Subcutaneous adipose tissue undergoing enzymatic saponification',
    'Brain cortex': 'Cerebral cortical gray matter suffering laminar polioencephalomalacia',
}

def enrich_distractor(d_str, correct_str, subject_id, topic):
    # If already long enough or empty, return
    if len(d_str) >= len(correct_str) * 0.75:
        return d_str

    # Direct dictionary lookups
    clean_d = d_str.strip()
    if clean_d in ANAT_SYNONYMS:
        return ANAT_SYNONYMS[clean_d]
    if clean_d in MICRO_SYNONYMS:
        return MICRO_SYNONYMS[clean_d]
    if clean_d in PATH_SYNONYMS:
        return PATH_SYNONYMS[clean_d]

    # Pattern: correct has parenthetical numerical range, e.g. "21 days (range 18-24 days)"
    num_match = re.search(r'(\d+)\s*(days?|hours?|months?|weeks?|lobes?|%|mg/dL|g/dL|mm|cm|m)\s*\((.*?)\)', correct_str)
    d_num_match = re.search(r'(\d+)\s*(days?|hours?|months?|weeks?|lobes?|%|mg/dL|g/dL|mm|cm|m)', clean_d)
    if num_match and d_num_match and '(' not in clean_d:
        val = int(d_num_match.group(1))
        unit = d_num_match.group(2)
        paren_tmpl = num_match.group(3)
        if 'range' in paren_tmpl:
            lower = max(1, int(val * 0.85))
            upper = int(val * 1.15)
            return f"{clean_d} (range {lower}-{upper} {unit})"
        elif 'average' in paren_tmpl or '~' in paren_tmpl:
            lower = max(1, int(val * 0.95))
            upper = int(val * 1.05)
            return f"{clean_d} (average ~{lower}-{upper}{unit})"
        elif 'approx' in paren_tmpl:
            return f"{clean_d} (approx {int(val*10)} standard units)"
        else:
            return f"{clean_d} (reference interval value)"

    # Pattern: correct has abbreviation or Latin synonym in parens, e.g. "Name (Synonym)"
    paren_match = re.search(r'^(.*?)\s*\((.*?)\)$', correct_str)
    if paren_match and '(' not in clean_d:
        # Check if distractor looks like an anatomical vein/artery/nerve/muscle
        if any(w in clean_d.lower() for w in ['vein', 'artery', 'nerve', 'muscle', 'ligament', 'sinus', 'lymph node']):
            return f"{clean_d} (anatomical collateral branch)"
        elif any(w in clean_d.lower() for w in ['bacillus', 'virus', 'clostridium', 'bacterium', 'mycobacterium', 'streptococcus', 'staphylococcus']):
            return f"{clean_d} (associated clinical pathogen)"
        elif any(w in clean_d.lower() for w in ['staining', 'stain', 'reaction', 'agar', 'broth', 'medium']):
            return f"{clean_d} (differential diagnostic formulation)"
        elif any(w in clean_d.lower() for w in ['hormone', 'factor', 'protein', 'enzyme', 'acid', 'vitamin']):
            return f"{clean_d} (biochemical active derivative)"

    return d_str

def main():
    with open('scripts/biased_questions.json', 'r', encoding='utf-8') as f:
        biased = json.load(f)

    print(f"Testing enricher on {len(biased)} questions...")
    resolved = 0
    for q in biased:
        c = q['correct']
        orig_ds = q['distractors']
        new_ds = [enrich_distractor(d, c, q['subjectId'], q['topic']) for d in orig_ds]
        d_lens = [len(d) for d in new_ds]
        c_len = len(c)
        if not (c_len >= 1.35 * (sum(d_lens)/3) and (c_len - max(d_lens)) >= 12):
            resolved += 1

    print(f"Initial dictionary resolved: {resolved} / {len(biased)} questions")

if __name__ == '__main__':
    main()
