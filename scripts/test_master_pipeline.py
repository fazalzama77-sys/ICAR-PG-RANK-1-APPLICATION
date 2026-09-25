import json, random, re

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

print(f"Total base questions loaded: {len(clean_map)}")

# Core PYQ source files
import sys
sys.path.append('scripts')
from pyq_van import get_van_pyqs
from pyq_vpp import get_vpp_pyqs
from pyq_vmc import get_vmc_pyqs
from pyq_vbc import get_vbc_pyqs

core_pyqs = {q['id']: q for q in (get_van_pyqs() + get_vpp_pyqs() + get_vmc_pyqs() + get_vbc_pyqs())}
print(f"Total core authentic PYQs: {len(core_pyqs)}")

generic_phrases = [
    'producing marked histopathological lesions',
    'characterized by distinctive cellular morphologic alterations',
    'providing collateral arterial distribution',
    'forming key topographical anatomical landmarks',
    'characterized by distinctive structural configurations',
    'facilitating standard physiological neurovascular transport',
    'characterized by classical diagnostic histopathological alterations',
    'characterized by prominent diagnostic manifestations',
    'associated with severe microvascular thrombosis'
]

# Apply updates
processed = []
for qid, q in clean_map.items():
    q_copy = dict(q)
    
    # CASE 1: Core authentic PYQ -> DO NOT CHANGE OPTION TEXT
    if qid in core_pyqs:
        orig = core_pyqs[qid]
        # Use authentic text from official paper
        c_text = orig['options'][orig['correctOptionIndex']]
        d_texts = [orig['options'][i] for i in range(len(orig['options'])) if i != orig['correctOptionIndex']]
    
    # CASE 2: Question in master_overrides
    elif qid in master_overrides:
        # Correct option is unchanged from clean_map
        c_text = q['options'][q['correctOptionIndex']]
        d_texts = master_overrides[qid]
        assert len(d_texts) == 3, f"Expected 3 distractors for {qid}, got {len(d_texts)}"
    
    # CASE 3: Clean questions without overrides -> ensure no generic suffixes
    else:
        c_text = q['options'][q['correctOptionIndex']]
        d_texts = []
        for i, opt in enumerate(q['options']):
            if i != q['correctOptionIndex']:
                clean_opt = opt
                for gp in generic_phrases:
                    clean_opt = clean_opt.replace(f" ({gp})", "").replace(f"({gp})", "").replace(gp, "")
                d_texts.append(clean_opt.strip())

    # Deterministic balanced shuffling across A, B, C, D
    # Use hash of question ID so placement is permanent and deterministic
    h = sum(ord(ch) for ch in qid)
    target_idx = h % 4
    
    # Construct 4 options
    all_4 = list(d_texts)
    all_4.insert(target_idx, c_text)
    
    q_copy['options'] = all_4
    q_copy['correctOptionIndex'] = target_idx
    processed.append(q_copy)

print(f"Processed total questions: {len(processed)}")

# Analyze balanced option distribution
from collections import Counter
opt_dist = Counter(q['correctOptionIndex'] for q in processed)
print(f"Correct option distribution: A={opt_dist[0]} ({opt_dist[0]/len(processed)*100:.1f}%), B={opt_dist[1]} ({opt_dist[1]/len(processed)*100:.1f}%), C={opt_dist[2]} ({opt_dist[2]/len(processed)*100:.1f}%), D={opt_dist[3]} ({opt_dist[3]/len(processed)*100:.1f}%)")

# Check for length bias in our questions
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

print(f"Remaining our own questions with notable length bias: {len(biased_remaining)}")
if biased_remaining:
    print("Sample remaining biased:")
    for b in biased_remaining[:5]:
        print(f"[{b[0]}] C ({b[2]}): {b[4]}")
        print(f"      D (max {b[3]}): {b[5]}")
