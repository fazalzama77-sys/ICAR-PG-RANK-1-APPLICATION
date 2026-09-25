import json, re, sys
sys.path.append('scripts')
from equalize_engine import ENHANCEMENTS

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

def clean_enhance(d_str, correct_str, subject_id, topic):
    clean_d = d_str.strip()
    if len(clean_d) >= len(correct_str) * 0.75:
        return clean_d
    
    # 1. Exact or case-insensitive match in ENHANCEMENTS
    if clean_d in ENHANCEMENTS:
        return ENHANCEMENTS[clean_d]
    for k, v in ENHANCEMENTS.items():
        if clean_d.lower() == k.lower():
            return v
    for k, v in ENHANCEMENTS.items():
        if clean_d.lower().startswith(k.lower()) and len(clean_d) <= len(k) + 5:
            return v

    # 2. Ratios, e.g. "30:70"
    ratio_m = re.match(r'^(\d+)\s*:\s*(\d+)$', clean_d)
    if ratio_m and ':' in correct_str and '%' in correct_str:
        p1, p2 = ratio_m.group(1), ratio_m.group(2)
        return f"{p1}:{p2} ({p1}% active operational phase : {p2}% rest relaxation phase)"

    # 3. Decimal values, e.g. "0.0002"
    dec_m = re.match(r'^(0\.\d+)$', clean_d)
    if dec_m and ('%' in correct_str or 'in ' in correct_str):
        val = float(dec_m.group(1))
        pct = val * 100
        inv = int(round(1.0 / val)) if val > 0 else 0
        return f"Approximately {clean_d} ({pct:.2f}% or 1 in {inv} animals in population)"

    # 4. Units with numbers
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

    # 5. Numerical range matching
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

processed = []
for qid, q in clean_map.items():
    q_copy = dict(q)
    if qid in core_pyqs:
        orig = core_pyqs[qid]
        c_text = orig['options'][orig['correctOptionIndex']]
        d_texts = [orig['options'][i] for i in range(len(orig['options'])) if i != orig['correctOptionIndex']]
    elif qid in master_overrides:
        c_text = q['options'][q['correctOptionIndex']]
        d_texts = master_overrides[qid]
    else:
        c_text = q['options'][q['correctOptionIndex']]
        d_texts = [clean_enhance(opt, c_text, q.get('subjectId', ''), q.get('topic', '')) for i, opt in enumerate(q['options']) if i != q['correctOptionIndex']]

    h = sum(ord(ch) for ch in qid)
    target_idx = h % 4
    all_4 = list(d_texts)
    all_4.insert(target_idx, c_text)
    q_copy['options'] = all_4
    q_copy['correctOptionIndex'] = target_idx
    processed.append(q_copy)

our_processed = [q for q in processed if not q['id'].startswith('pyq_')]
biased_remaining = []
for q in our_processed:
    opts = q['options']
    c_idx = q['correctOptionIndex']
    c_opt = opts[c_idx]
    d_opts = [opts[i] for i in range(len(opts)) if i != c_idx]
    c_len = len(c_opt)
    max_d = max(len(d) for d in d_opts)
    if (c_len - max_d > 25) or (c_len > 40 and c_len > 1.5 * max_d):
        biased_remaining.append(q)

print(f"Remaining our own questions with length disparity > 25 chars: {len(biased_remaining)}")
