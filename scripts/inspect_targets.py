import json

with open('src/data/questionPacks/high_yield_master_clean.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

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

def is_target(q):
    if q['id'].startswith('pyq_'):
        return False
    opts = q['options']
    c_idx = q['correctOptionIndex']
    c_opt = opts[c_idx]
    d_opts = [opts[i] for i in range(len(opts)) if i != c_idx]
    c_len = len(c_opt)
    max_d = max(len(d) for d in d_opts)
    is_gen = any(any(gp in opt for gp in generic_phrases) for opt in opts)
    is_disp = (c_len - max_d > 18) or (c_len > 40 and c_len > 1.35 * max_d)
    return is_gen or is_disp

targets = [q for q in master if is_target(q)]
print(f"Total targets: {len(targets)}")

for sub in ['vpp', 'van', 'vmc']:
    sub_targets = [q for q in targets if q['subjectId'] == sub]
    print(f"\n=== SAMPLE FOR {sub} (Total: {len(sub_targets)}) ===")
    for q in sub_targets[:4]:
        c_opt = q['options'][q['correctOptionIndex']]
        print(f"ID: {q['id']} | Q: {q['questionText'][:75]}")
        print(f"  [Correct]: {c_opt}")
        for i, opt in enumerate(q['options']):
            if i != q['correctOptionIndex']:
                print(f"  [Distractor]: {opt}")
