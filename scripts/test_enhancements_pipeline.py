import json, sys
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

# Core PYQ source files
from pyq_van import get_van_pyqs
from pyq_vpp import get_vpp_pyqs
from pyq_vmc import get_vmc_pyqs
from pyq_vbc import get_vbc_pyqs

core_pyqs = {q['id']: q for q in (get_van_pyqs() + get_vpp_pyqs() + get_vmc_pyqs() + get_vbc_pyqs())}

processed = []
for qid, q in clean_map.items():
    q_copy = dict(q)
    
    # CASE 1: Core authentic PYQ -> DO NOT CHANGE OPTION TEXT
    if qid in core_pyqs:
        orig = core_pyqs[qid]
        c_text = orig['options'][orig['correctOptionIndex']]
        d_texts = [orig['options'][i] for i in range(len(orig['options'])) if i != orig['correctOptionIndex']]
    
    # CASE 2: Question in master_overrides
    elif qid in master_overrides:
        c_text = q['options'][q['correctOptionIndex']]
        d_texts = master_overrides[qid]
    
    # CASE 3: Apply ENHANCEMENTS dictionary
    else:
        c_text = q['options'][q['correctOptionIndex']]
        d_texts = []
        for i, opt in enumerate(q['options']):
            if i != q['correctOptionIndex']:
                clean_opt = opt.strip()
                # Check ENHANCEMENTS dictionary
                if clean_opt in ENHANCEMENTS:
                    d_texts.append(ENHANCEMENTS[clean_opt])
                else:
                    # check case insensitive
                    matched = False
                    for ek, ev in ENHANCEMENTS.items():
                        if clean_opt.lower() == ek.lower():
                            d_texts.append(ev)
                            matched = True
                            break
                    if not matched:
                        d_texts.append(clean_opt)

    # Deterministic balanced shuffling across A, B, C, D
    h = sum(ord(ch) for ch in qid)
    target_idx = h % 4
    
    all_4 = list(d_texts)
    all_4.insert(target_idx, c_text)
    
    q_copy['options'] = all_4
    q_copy['correctOptionIndex'] = target_idx
    processed.append(q_copy)

# Check length bias in our questions
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
        biased_remaining.append((q['id'], q['subjectId'], c_len, max_d, c_opt, d_opts, q['questionText'][:60]))

print(f"Total our own questions: {len(our_processed)}")
print(f"Remaining our own questions with length disparity > 25 chars: {len(biased_remaining)}")
