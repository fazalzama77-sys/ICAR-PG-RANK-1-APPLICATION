import json, re, sys
sys.path.append('scripts')
from equalize_engine import QUESTION_OVERRIDES

with open('scripts/need_tricky_293.json', 'r', encoding='utf-8') as f:
    need_tricky = json.load(f)

missing = [q for q in need_tricky if q['id'] not in QUESTION_OVERRIDES]
print(f"Total missing across all: {len(missing)}")

with open('scripts/missing_253.json', 'w', encoding='utf-8') as f:
    json.dump([{'id': q['id'], 'sub': q['subjectId'], 'q': q['questionText'], 'c': q['options'][q['correctOptionIndex']], 'd': [q['options'][i] for i in range(len(q['options'])) if i != q['correctOptionIndex']]} for q in missing], f, indent=2)

print("Saved missing to scripts/missing_253.json")
