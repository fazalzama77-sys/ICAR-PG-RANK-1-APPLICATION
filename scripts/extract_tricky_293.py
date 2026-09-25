import json

with open('scripts/active_targets.json', 'r', encoding='utf-8') as f:
    targets = json.load(f)

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

need_tricky = []
for q in targets:
    c_opt = q['options'][q['correctOptionIndex']]
    c_len = len(c_opt)
    has_gen = any(any(gp in opt for gp in generic_phrases) for opt in q['options'])
    
    if (has_gen and c_len >= 35) or (not has_gen):
        need_tricky.append(q)

print(f"Total questions needing tricky authentic distractors: {len(need_tricky)}")
from collections import Counter
print("By subject:", Counter(q['subjectId'] for q in need_tricky))

with open('scripts/need_tricky_293.json', 'w', encoding='utf-8') as f:
    json.dump(need_tricky, f, indent=2)
print("Saved to scripts/need_tricky_293.json")
