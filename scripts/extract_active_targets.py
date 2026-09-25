import json, re

with open('scripts/inspect_targets.py', 'r', encoding='utf-8') as f:
    code = f.read()

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

targets = []
for q in master:
    if q['id'].startswith('pyq_'):
        continue
    opts = q['options']
    c_idx = q['correctOptionIndex']
    c_opt = opts[c_idx]
    d_opts = [opts[i] for i in range(len(opts)) if i != c_idx]
    c_len = len(c_opt)
    max_d = max(len(d) for d in d_opts)
    is_gen = any(any(gp in opt for gp in generic_phrases) for opt in opts)
    is_disp = (c_len - max_d > 18) or (c_len > 40 and c_len > 1.35 * max_d)
    if is_gen or is_disp:
        targets.append(q)

print(f"Total target questions in high_yield_master_clean: {len(targets)}")

# Save these targets to a file so we can inspect and craft high quality options
with open('scripts/active_targets.json', 'w', encoding='utf-8') as f:
    json.dump(targets, f, indent=2)
print("Saved to scripts/active_targets.json")
