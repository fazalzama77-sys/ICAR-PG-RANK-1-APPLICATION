import json
import os

with open('src/data/questionPacks/high_yield_1080.json', 'r', encoding='utf-8') as f:
    q1080 = json.load(f)

with open('src/data/questionPacks/pyqs_300.json', 'r', encoding='utf-8') as f:
    q300 = json.load(f)

print(f"Loaded {len(q1080)} high-yield questions and {len(q300)} PYQ questions.")

# Group by subjectId
subjects_1080 = {}
for q in q1080:
    s = q['subjectId']
    if s not in subjects_1080:
        subjects_1080[s] = []
    subjects_1080[s].append(q)

subjects_300 = {}
for q in q300:
    s = q['subjectId']
    if s not in subjects_300:
        subjects_300[s] = []
    subjects_300[s].append(q)

print("\n--- High Yield 1080 Subjects ---")
for s, qs in subjects_1080.items():
    print(f"Subject {s.upper()}: {len(qs)} questions")

print("\n--- PYQ 300 Subjects ---")
for s, qs in subjects_300.items():
    print(f"Subject {s.upper()}: {len(qs)} questions")

# Detailed check of each subject's topics
with open('audit_report_raw.txt', 'w', encoding='utf-8') as out:
    out.write("=== AUDIT REPORT: HIGH YIELD 1080 & PYQ 300 ===\n\n")
    for s, qs in subjects_1080.items():
        out.write(f"\n========================================\n")
        out.write(f"SUBJECT: {s.upper()} ({len(qs)} questions)\n")
        out.write(f"========================================\n")
        topics = set(q.get('topic', 'N/A') for q in qs)
        out.write(f"Topics: {topics}\n\n")
        for i, q in enumerate(qs):
            out.write(f"{i+1:03d}. [{q['id']}] ({q.get('topic', '')}) {q['questionText']}\n")
            out.write(f"     Ans: {q['options'][q['correctOptionIndex']]}\n")
            out.write(f"     Exp: {q['explanation'][:120]}...\n")

    for s, qs in subjects_300.items():
        out.write(f"\n========================================\n")
        out.write(f"PYQ SUBJECT: {s.upper()} ({len(qs)} questions)\n")
        out.write(f"========================================\n")
        for i, q in enumerate(qs):
            out.write(f"{i+1:03d}. [{q['id']}] {q['questionText']}\n")
            out.write(f"     Ans: {q['options'][q['correctOptionIndex']]}\n")

print("Wrote audit_report_raw.txt successfully.")
