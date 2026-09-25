import re
import json

with open('src/data/questionPacks/pyqQuestions.ts', 'r', encoding='utf-8') as f:
    pyq_text = f.read()

with open('src/data/questionPacks/allQuestions.ts', 'r', encoding='utf-8') as f:
    all_text = f.read()

# Extract IDs from both
pyq_ids = re.findall(r'"id":\s*"([^"]+)"', pyq_text)
all_ids = re.findall(r'"id":\s*"([^"]+)"', all_text)

print(f"pyqQuestions.ts IDs: {len(pyq_ids)} (unique: {len(set(pyq_ids))})")
print(f"allQuestions.ts IDs: {len(all_ids)} (unique: {len(set(all_ids))})")

# Let's also extract all questionText
pyq_questions = re.findall(r'"questionText":\s*"([^"]+)"', pyq_text)
all_questions = re.findall(r'"questionText":\s*"([^"]+)"', all_text)

print(f"pyqQuestions.ts question texts: {len(pyq_questions)}")
print(f"allQuestions.ts question texts: {len(all_questions)}")
