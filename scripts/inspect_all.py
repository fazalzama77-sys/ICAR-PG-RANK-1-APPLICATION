import re
import json

with open('src/data/questionPacks/pyqQuestions.ts', 'r', encoding='utf-8') as f:
    pyq_text = f.read()

with open('src/data/questionPacks/allQuestions.ts', 'r', encoding='utf-8') as f:
    all_text = f.read()

def parse_questions_from_ts(text):
    # Match JSON-like question objects
    # Find all { "id": ... }
    blocks = re.findall(r'\{\s*"id":\s*"[^"]+",[\s\S]*?\n\s*\}', text)
    qs = []
    for b in blocks:
        try:
            q = json.loads(b)
            qs.append(q)
        except Exception:
            pass
    return qs

pyq_qs = parse_questions_from_ts(pyq_text)
all_qs = parse_questions_from_ts(all_text)

print(f"Parsed PYQs: {len(pyq_qs)}")
print(f"Parsed Base: {len(all_qs)}")

pyq_subjs = {}
for q in pyq_qs:
    s = q.get('subjectId')
    pyq_subjs[s] = pyq_subjs.get(s, 0) + 1
print("PYQ by subject:", pyq_subjs)

base_subjs = {}
for q in all_qs:
    s = q.get('subjectId')
    base_subjs[s] = base_subjs.get(s, 0) + 1
print("Base by subject:", base_subjs)

combined = pyq_qs + all_qs
total_subjs = {}
for q in combined:
    s = q.get('subjectId')
    total_subjs[s] = total_subjs.get(s, 0) + 1
print("Total by subject:", total_subjs)

from collections import Counter
print("PYQ correctOptionIndex:", Counter(q.get('correctOptionIndex') for q in pyq_qs))
print("Base correctOptionIndex:", Counter(q.get('correctOptionIndex') for q in all_qs))

