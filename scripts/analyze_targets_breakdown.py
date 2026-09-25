import json, re

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

short_correct_with_generic = []
long_correct_with_generic = []
long_correct_without_generic = []

for q in targets:
    c_opt = q['options'][q['correctOptionIndex']]
    c_len = len(c_opt)
    has_gen = any(any(gp in opt for gp in generic_phrases) for opt in q['options'])
    
    if has_gen:
        if c_len < 35:
            short_correct_with_generic.append(q)
        else:
            long_correct_with_generic.append(q)
    else:
        long_correct_without_generic.append(q)

print(f"Short correct (<35 chars) with generic suffix on distractors: {len(short_correct_with_generic)}")
print(f"Long correct (>=35 chars) with generic suffix on distractors: {len(long_correct_with_generic)}")
print(f"Long correct without generic suffix (pure length disparity): {len(long_correct_without_generic)}")
