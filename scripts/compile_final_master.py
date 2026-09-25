import json, re, sys
sys.path.append('scripts')
from equalize_engine import ENHANCEMENTS

# Load all overrides
with open('scripts/master_tricky_overrides.json', 'r', encoding='utf-8') as f:
    master_overrides = json.load(f)

# Load base clean questions from 9786b8f + vpa_60
import subprocess
proc = subprocess.run(['git', 'show', '9786b8f:src/data/questionPacks/high_yield_master_clean.json'], capture_output=True, text=True, encoding='utf-8')
data_1665 = json.loads(proc.stdout)
clean_map = {q['id']: q for q in data_1665}

with open('src/data/questionPacks/vpa_60_new.json', 'r', encoding='utf-8') as f:
    vpa_60 = json.load(f)
for q in vpa_60:
    clean_map[q['id']] = q

from pyq_van import get_van_pyqs
from pyq_vpp import get_vpp_pyqs
from pyq_vmc import get_vmc_pyqs
from pyq_vbc import get_vbc_pyqs
core_pyqs = {q['id']: q for q in (get_van_pyqs() + get_vpp_pyqs() + get_vmc_pyqs() + get_vbc_pyqs())}

# Extra domain dictionary for the remaining high-yield concepts
EXTRA_ENHANCEMENTS = {
    # VPY / VBC
    "Acetate": "Acetate (oxidized in peripheral tissues and used for fatty acid synthesis)",
    "Propionate": "Propionate (transported via portal vein for hepatic gluconeogenesis)",
    "Formate": "Formate (metabolized via folate one-carbon tetrahydrofolate pathway)",
    "Isobutyrate": "Isobutyrate (branched-chain volatile fatty acid from valine catabolism)",
    "Alveolar macrophages": "Alveolar macrophages (Pulmonary dust cells phagocytosing inhaled particles)",
    "Type I pneumocytes": "Type I pneumocytes (Squamous alveolar cells providing thin gas barrier)",
    "Clara cells": "Club / Clara cells (Non-ciliated bronchiolar cells secreting protective proteins)",
    "Duodenum": "Duodenum (Receiving pancreatic enzymes and common bile duct secretions)",
    "Stomach": "Stomach (True gastric chamber secreting hydrochloric acid and pepsinogen)",
    "Ileum": "Ileum (Distal small intestine with prominent aggregated Peyer's patches)",
    "Vagus nerve trauma": "Traumatic injury to the dorsal vagal nerve trunk along the esophagus",
    "Rumen flukes": "Paramphistomum cervi infection of ruminal papillae and reticulum",
    "Esophageal foreign body": "Complete physical obstruction of the thoracic esophagus (Choke in cattle)",
    "Acid digestion": "Enzymatic mucosal digestion and acidic chyme emulsification",
    "Methane production": "Methanogenesis by Archaea consuming metabolic hydrogen gas",
    "Fat emulsification": "Biliary micellar solubilization and enterocyte lymphatic transport",
    "Synthesizing vitamin C": "De novo enzymatic biosynthesis of L-ascorbic acid in hepatocytes",
    "Producing lactic acid": "Rapid homofermentative conversion of soluble sugars to D-lactate",
    "Degrading toxic oxalates": "Microbial breakdown of soluble pasture oxalates by Oxalobacter formigenes",
    "Oxygen and Nitrogen": "Atmospheric air (78% Nitrogen and 21% Oxygen swallowed during grazing)",
    "Ammonia and Argon": "Metabolic ammonia (50-60%) and inert Argon gas (20-30%)",
    "Hydrogen sulfide and Helium": "Hydrogen sulfide (40-50%) and trace Helium gas (20-30%)",
    "Hyperflexion of hock": "Hyperflexion of the hock joint, knuckling of fetlock, dropped metatarsus (Peroneal nerve)",
    "Paralysis of tongue": "Flaccid paralysis and hemiatrophy of the lingual musculature (Hypoglossal nerve)",
    "Splay leg posture": "Extreme lateral abduction and splaying of the pelvic limbs (Obturator nerve)",
    "Venous sinusoids and Billroth cords": "Splenic red pulp sinusoids and cellular Billroth cords",
    "Trabeculae exclusively": "Connective tissue fibromuscular trabeculae and capsular bands",
    "Red blood cell reservoirs": "Sinusoidal reservoirs storing circulating erythrocytes for splenic contraction"
}

def full_enhance(d_str, correct_str, subject_id, topic):
    clean_d = d_str.strip()
    if len(clean_d) >= len(correct_str) * 0.75:
        return clean_d
    
    # 1. Extra domain dictionary
    if clean_d in EXTRA_ENHANCEMENTS:
        return EXTRA_ENHANCEMENTS[clean_d]
    for k, v in EXTRA_ENHANCEMENTS.items():
        if clean_d.lower() == k.lower():
            return v
    
    # 2. Base ENHANCEMENTS
    if clean_d in ENHANCEMENTS:
        return ENHANCEMENTS[clean_d]
    for k, v in ENHANCEMENTS.items():
        if clean_d.lower() == k.lower():
            return v
    for k, v in ENHANCEMENTS.items():
        if clean_d.lower().startswith(k.lower()) and len(clean_d) <= len(k) + 5:
            return v

    # 3. Ratios
    ratio_m = re.match(r'^(\d+)\s*:\s*(\d+)$', clean_d)
    if ratio_m and ':' in correct_str and '%' in correct_str:
        p1, p2 = ratio_m.group(1), ratio_m.group(2)
        return f"{p1}:{p2} ({p1}% active operational phase : {p2}% rest relaxation phase)"

    # 4. Decimals
    dec_m = re.match(r'^(0\.\d+)$', clean_d)
    if dec_m and ('%' in correct_str or 'in ' in correct_str):
        val = float(dec_m.group(1))
        pct = val * 100
        inv = int(round(1.0 / val)) if val > 0 else 0
        return f"Approximately {clean_d} ({pct:.2f}% or 1 in {inv} animals in population)"

    # 5. Units
    num_unit_m = re.match(r'^([\d\.]+)\s*(kPa|per minute|per hour|square feet|square meters|days|months|mg/dL|g/dL|mm|cm|m)?$', clean_d, re.I)
    if num_unit_m:
        val_str = num_unit_m.group(1)
        unit = num_unit_m.group(2) or ''
        if 'kPa' in correct_str:
            v = float(val_str)
            return f"{val_str} kPa (approx {int(v*7.5)} mmHg / {int(v*0.3)} inches of Hg)"
        elif 'per minute' in correct_str or 'contractions' in correct_str:
            return f"{val_str} contractions per minute (or elevated frequency in 2 minutes)"
        elif 'square' in correct_str or 'sq' in correct_str:
            return f"{val_str} {unit} (standard covered floor allowance per animal)"
        elif 'due to' in correct_str or 'ph' in topic.lower() or 'acidosis' in correct_str.lower():
            return f"{val_str} (subacute ruminal fluid fermentation threshold pH)"

    # 6. Ranges
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
            return f"{clean_d} (average ~{lower}-{upper} {unit})"
        elif 'approx' in paren_tmpl:
            return f"{clean_d} (approx {int(val*10)} standard units)"
            
    return clean_d

# Build full clean bank
final_master = []
for qid, q in clean_map.items():
    q_copy = dict(q)
    
    # CASE 1: Core authentic PYQ -> DO NOT CHANGE OPTION TEXT
    if qid in core_pyqs:
        orig = core_pyqs[qid]
        c_text = orig['options'][orig['correctOptionIndex']]
        d_texts = [orig['options'][i] for i in range(len(orig['options'])) if i != orig['correctOptionIndex']]
    
    # CASE 2: Master overrides
    elif qid in master_overrides:
        c_text = q['options'][q['correctOptionIndex']]
        d_texts = master_overrides[qid]
        assert len(d_texts) == 3, f"Expected 3 distractors for {qid}, got {len(d_texts)}"
    
    # CASE 3: Clean enhance
    else:
        c_text = q['options'][q['correctOptionIndex']]
        d_texts = [full_enhance(opt, c_text, q.get('subjectId', ''), q.get('topic', '')) for i, opt in enumerate(q['options']) if i != q['correctOptionIndex']]

    # Deterministic balanced shuffling
    h = sum(ord(ch) for ch in qid)
    target_idx = h % 4
    all_4 = list(d_texts)
    all_4.insert(target_idx, c_text)
    
    q_copy['options'] = all_4
    q_copy['correctOptionIndex'] = target_idx
    final_master.append(q_copy)

print(f"Compiled {len(final_master)} master questions successfully.")

# Save final_master.json
with open('scripts/compiled_final_master.json', 'w', encoding='utf-8') as f:
    json.dump(final_master, f, indent=2)

print("Saved to scripts/compiled_final_master.json")
