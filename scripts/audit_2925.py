# scripts/audit_2925.py
import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from canonical_topics import CANONICAL_UNITS


def main():
    packs_dir = os.path.join(scripts_dir, "..", "src", "data", "questionPacks")
    master_path = os.path.join(packs_dir, "high_yield_master_clean.json")
    with open(master_path, "r", encoding="utf-8") as f:
        qs = json.load(f)

    print("=========================================================================")
    print(f"4-PASS AUDIT OF MASTER QUESTION BANK ({len(qs)} QUESTIONS)")
    print("=========================================================================")
    assert len(qs) == 2925, f"Expected 2925, got {len(qs)}"

    # Pass 1: Subject counts & Index distribution
    subj_counts = Counter(q["subjectId"] for q in qs)
    expected = {
        "van": 320, "vpy": 120, "vbc": 163, "lpm": 52,
        "vpp": 792, "vmc": 797, "vpa": 107, "agb": 284, "ann": 290
    }
    print("\n--- PASS 1: SUBJECT TOTALS & A/B/C/D INDEX BALANCE ---")
    for s, exp_n in expected.items():
        actual_n = subj_counts[s]
        assert actual_n == exp_n, f"Subject {s}: expected {exp_n}, got {actual_n}"
        idx_dist = Counter(q["correctOptionIndex"] for q in qs if q["subjectId"] == s)
        print(f"  [{s.upper()}] {actual_n:3d} Qs | A:{idx_dist[0]:3d} B:{idx_dist[1]:3d} C:{idx_dist[2]:3d} D:{idx_dist[3]:3d}")

    # Pass 2: 54 Canonical Syllabus Units coverage
    print("\n--- PASS 2: 54 CANONICAL SYLLABUS UNITS / CHAPTERS COVERAGE ---")
    total_units = 0
    for s in ["van", "vpy", "vbc", "lpm", "vpp", "vmc", "vpa", "agb", "ann"]:
        units = CANONICAL_UNITS[s]
        print(f"\n  [{s.upper()}] ({len(units)} Canonical Units):")
        for u_idx, u in enumerate(units, 1):
            c = sum(1 for q in qs if q["subjectId"] == s and q["topic"] == u)
            assert c > 0, f"Unit has 0 questions: {s} -> {u}"
            total_units += 1
            print(f"    Unit {u_idx}: {c:3d} Qs | {u}")
    print(f"\n  Verified all {total_units}/54 Canonical Syllabus Units have active question banks!")

    # Pass 3: Option-Length Parity Audit
    print("\n--- PASS 3: OPTION-LENGTH PARITY AUDIT (STRICTLY LONGEST CORRECT OPTION) ---")
    for s in sorted(expected.keys()):
        sqs = [q for q in qs if q["subjectId"] == s]
        lc = sum(
            1 for q in sqs
            if len(q["options"][q["correctOptionIndex"]]) == max(len(o) for o in q["options"])
            and sum(1 for o in q["options"] if len(o) == max(len(x) for x in q["options"])) == 1
        )
        lw = sum(
            1 for q in sqs
            if len(q["options"][q["correctOptionIndex"]].split()) == max(len(o.split()) for o in q["options"])
            and sum(1 for o in q["options"] if len(o.split()) == max(len(x.split()) for x in q["options"])) == 1
        )
        print(f"  [{s.upper()}] Char-longest correct: {lc:3d}/{len(sqs):3d} ({lc/len(sqs)*100:4.1f}%) | Word-longest correct: {lw:3d}/{len(sqs):3d} ({lw/len(sqs)*100:4.1f}%)")

    tot_lc = sum(
        1 for q in qs
        if len(q["options"][q["correctOptionIndex"]]) == max(len(o) for o in q["options"])
        and sum(1 for o in q["options"] if len(o) == max(len(x) for x in q["options"])) == 1
    )
    tot_lw = sum(
        1 for q in qs
        if len(q["options"][q["correctOptionIndex"]].split()) == max(len(o.split()) for o in q["options"])
        and sum(1 for o in q["options"] if len(o.split()) == max(len(x.split()) for x in q["options"])) == 1
    )
    print(f"\n  OVERALL MASTER BANK (2,925 Qs):")
    print(f"    Char-longest correct: {tot_lc}/2925 ({tot_lc/2925*100:.1f}%) [Random baseline = 25.0%]")
    print(f"    Word-longest correct: {tot_lw}/2925 ({tot_lw/2925*100:.1f}%) [Random baseline = 25.0%]")

    # Pass 4: Deduplication & Integrity
    ids = set(q["id"] for q in qs)
    stems = set(" ".join(q["questionText"].lower().split()) for q in qs)
    print("\n--- PASS 4: DEDUPLICATION & INTEGRITY ---")
    print(f"  Unique IDs:   {len(ids)}/2925 (0 duplicates)")
    print(f"  Unique Stems: {len(stems)}/2925 ({2925 - len(stems)} duplicates)")
    assert len(ids) == 2925
    assert len(stems) == 2925
    print("  ALL 4 AUDIT PASSES SUCCEEDED 100%!")


if __name__ == "__main__":
    main()
