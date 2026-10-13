# scripts/option_parity_engine.py
"""
Intra-Question Option-Length Parity & Distractor Refinement Engine.
Strictly operates WITHIN each individual question (NEVER swaps distractors between questions).
"""
import re
import random

STRICT_PAIR_STEM = (
    'which two', 'which 2', 'both ', 'union of', 'between which',
    'ratio of', 'pair of', 'triad'
)

CONCISE_REPLACEMENTS = [
    ("Central Nervous System", "CNS"),
    ("central nervous system", "CNS"),
    ("Autonomous Nervous System", "ANS"),
    ("autonomic nervous system", "ANS"),
    ("Gastrointestinal tract", "GI tract"),
    ("gastrointestinal tract", "GI tract"),
    ("Rough endoplasmic reticulum", "Rough ER"),
    ("rough endoplasmic reticulum", "rough ER"),
    ("Smooth endoplasmic reticulum", "Smooth ER"),
    ("smooth endoplasmic reticulum", "smooth ER"),
    ("endoplasmic reticulum", "ER"),
    ("reticuloendothelial system", "RES"),
    ("polymorphonuclear leukocytes", "neutrophils"),
    ("Polymorphonuclear leukocytes", "Neutrophils"),
    ("red blood cells", "erythrocytes"),
    ("Red blood cells", "Erythrocytes"),
    ("white blood cells", "leukocytes"),
    ("White blood cells", "Leukocytes"),
    ("cerebrospinal fluid", "CSF"),
    ("Cerebrospinal fluid", "CSF"),
    ("immunoglobulin ", "Ig "),
    ("Immunoglobulin ", "Ig "),
    ("immunoglobulins", "Igs"),
    ("Immunoglobulins", "Igs"),
    ("adenosine triphosphate", "ATP"),
    ("molecular weight", "MW"),
    ("degrees Fahrenheit", "degrees F"),
    ("degrees Celsius", "degrees C"),
    ("is characterized by ", ""),
    ("characterized by ", ""),
    ("which is responsible for ", "for "),
    ("that is responsible for ", "for "),
    ("in the presence of ", "with "),
    ("as a result of ", "from "),
    ("at the level of the ", "at the "),
    ("in the region of the ", "in the "),
    ("on the surface of the ", "on the "),
    ("within the cytoplasm of ", "in "),
    ("within the nucleus of ", "in "),
]


def clean_correct_option(q_text: str, c_opt: str, d_opts: list[str], aggressive: bool = False) -> str:
    max_d = max(len(d) for d in d_opts)
    cur = c_opt.strip()
    d_lower = {d.strip().lower() for d in d_opts}
    ql = q_text.lower()

    # 1. Remove parenthetical (...) whenever cur > max_d
    if len(cur) > max_d and "(" in cur:
        no_paren = re.sub(r"\s*\([^)]*\)", "", cur).strip(" ,;-")
        if len(no_paren) >= 1 and no_paren.lower() not in d_lower:
            cur = no_paren

    # 2. Remove slash alternative (' / ' or '/')
    if len(cur) > max_d and "/" in cur and not any("/" in d for d in d_opts):
        if " / " in cur:
            parts = [p.strip() for p in cur.split(" / ") if len(p.strip()) >= 2 and p.strip().lower() not in d_lower]
            if parts:
                cur = min(parts, key=len)
        else:
            p0 = cur.split("/")[0].strip()
            if len(p0) >= 3 and p0.lower() not in d_lower:
                cur = p0

    # 3. Remove ' or ' alternative if distractors don't have ' or '
    if len(cur) > max_d and " or " in cur and not any(" or " in d for d in d_opts):
        p0 = cur.split(" or ")[0].strip()
        if len(p0) >= 2 and p0.lower() not in d_lower:
            cur = p0

    # 4. Strip trailing explanatory clauses & participial phrases (with or without comma)
    if len(cur) > max_d:
        for sep in [
            " — ", " - ", ", which ", " which ", ", that ", " that ",
            ", causing ", " causing ", ", resulting in ", " resulting in ",
            ", characterized by ", " characterized by ", ", leading to ", " leading to ",
            ", producing ", " producing ", ", forming ", " forming ",
            ", reducing ", " reducing ", ", regulating ", " regulating ",
            ", releasing ", " releasing ", ", trapping ", " trapping ",
            ", contacting ", " contacting ", ", preventing ", " preventing ",
            ", allowing ", " allowing ", ", making ", ", giving ",
            ", especially ", ", particularly ", ", with ", " with obligatory ",
            ", where ", " instead of ", " rather than ", " due to ",
            " to form ", " to produce ", " to prevent ", " in order to ",
            " for continued ", " in the presence of ", " buffered at ",
            " by inhibiting ", " by activating ", " by blocking ", " by binding ",
            " located ", " situated ", " found in ", " present in ",
            " secreted by ", " produced by ", " synthesized in ", " synthesized by ",
            " derived from ", " originating from ", " mediated by ", "; "
        ]:
            if sep in cur and not any(sep in d for d in d_opts):
                cand = cur.split(sep)[0].strip(" ,;-")
                if len(cand) >= 3 and cand.lower() not in d_lower:
                    cur = cand
                    break

    # 5. Strip redundant leading filler phrases
    if len(cur) > max_d:
        for prefix in [
            "The presence of a ", "The presence of ", "Presence of a ", "Presence of ",
            "Complete absence of ", "The absence of ", "A marked increase in ",
            "An increased level of ", "Predominantly ", "Specifically ",
            "Characteristic ", "Classic ", "Definitive ", "Seasonally polyestrous "
        ]:
            if cur.startswith(prefix) and not any(d.startswith(prefix) for d in d_opts):
                cand = cur[len(prefix):].strip()
                if len(cand) >= 4:
                    cand = cand[0].upper() + cand[1:]
                    if cand.lower() not in d_lower:
                        cur = cand
                        break

    # 6. Apply concise standard veterinary abbreviations/replacements
    if len(cur) > max_d:
        for old_s, new_s in CONCISE_REPLACEMENTS:
            if old_s in cur and len(cur) > max_d:
                cand = cur.replace(old_s, new_s).strip(" ,")
                if len(cand) >= 3 and cand.lower() not in d_lower:
                    cur = cand

    # 7. Strip trailing prepositional modifier when distractors don't have it
    if len(cur) > max_d + 5:
        for prep in [
            " of the ", " in the ", " on the ", " at the ", " from the ",
            " into the ", " into ", " across the ", " through the ", " via ",
            " of ", " in "
        ]:
            if prep in cur and not any(prep in d for d in d_opts):
                cand = cur.split(prep)[0].strip(" ,")
                if len(cand) >= 8 and cand.lower() not in d_lower and not cand.lower().endswith((
                    'lack', 'absence', 'presence', 'increase', 'decrease', 'loss', 'fusion',
                    'union', 'branch', 'branches', 'site', 'form', 'type', 'types', 'stage',
                    'phase', 'rate', 'ratio', 'number', 'concentration', 'level', 'levels',
                    'activity', 'deficiency', 'excess', 'inhibition', 'activation', 'stimulation',
                    'degeneration', 'necrosis', 'inflammation', 'hypoplasia', 'atrophy',
                    'hypertrophy', 'hyperplasia', 'metaplasia', 'carcinoma', 'sarcoma',
                    'entrapment', 'migration', 'penetration', 'deposition', 'secretion',
                    'excretion', 'absorption', 'digestion', 'fermentation', 'oxidation',
                    'reduction', 'synthesis', 'hydrolysis', 'cleavage', 'binding',
                    'attachment', 'detachment', 'mobility', 'inability', 'failure', 'removal'
                )):
                    cur = cand
                    break

    # 8. Comma-separated list of 3+ items
    if len(cur) > max_d and cur.count(",") >= 2 and not any(d.count(",") >= 2 for d in d_opts) and "triad" not in ql and "three" not in ql and "four" not in ql:
        parts = [p.strip() for p in cur.replace(", and ", ", ").replace(" and ", ", ").split(",") if p.strip()]
        if len(parts) >= 3:
            cand = f"{parts[0]} and {parts[1]}"
            if len(cand) >= 6 and cand.lower() not in d_lower:
                cur = cand

    # 9. Compound ' and '
    if len(cur) > max_d + 5 and (" and " in cur or " AND " in cur):
        if not any(kw in ql for kw in STRICT_PAIR_STEM):
            parts = re.split(r"\s+and\s+", cur, flags=re.IGNORECASE)
            p0 = parts[0].strip(" ,")
            if len(p0) >= 10 and p0.lower() not in d_lower and not p0.lower().endswith((
                'cranial', 'caudal', 'dorsal', 'ventral', 'medial', 'lateral',
                'internal', 'external', 'upper', 'lower', 'acute', 'chronic',
                'primary', 'secondary', 'left', 'right', 'both', 'terminal',
                'proximal', 'distal', 'intracytoplasmic', 'intranuclear'
            )):
                cur = p0
            elif len(parts) == 2 and len(parts[1].split()) >= 2:
                cand2 = parts[1].strip(" ,")
                if len(cand2) >= 10 and cand2.lower() not in d_lower:
                    cur = cand2[0].upper() + cand2[1:]

    if aggressive and len(cur) > max_d:
        cand = re.sub(r"\b(the|a|an)\s+", "", cur, flags=re.IGNORECASE).strip()
        if cand:
            cand = cand[0].upper() + cand[1:]
            if len(cand) >= 4 and cand.lower() not in d_lower:
                cur = cand

    return cur


if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from data_van import get_van_questions
    from data_vpy import get_vpy_questions
    from data_vbc import get_vbc_questions
    from data_lpm import get_lpm_questions
    from data_vpp import get_vpp_questions
    from data_vmc import get_vmc_questions
    from data_vpa import get_vpa_questions
    from data_agb import get_agb_questions
    from data_ann import get_ann_questions
    from enrich_to_120 import SUPPLEMENTARY_POOLS
    from pyq_van import get_van_pyqs
    from pyq_vpp import get_vpp_pyqs
    from pyq_vmc import get_vmc_pyqs
    from pyq_vbc import get_vbc_pyqs
    from build_pathology_300 import get_all_300_vpp_questions
    from build_microbiology_300 import get_all_300_vmc_questions
    from build_anatomy_150 import get_all_150_van_questions
    from build_parasitology_60 import get_all_60_vpa_questions

    def is_dummy(q):
        q_text = q.get('questionText', '')
        topic = q.get('topic', '')
        opts = q.get('options', [])
        return ('Clinical Landmark MCQ #' in q_text or 'Core Diagnostic' in topic or any('Standard validated laboratory' in opt for opt in opts))

    vpy_init = get_vpy_questions()
    vpy_supp = []
    for q_text, opts, ans, exp in SUPPLEMENTARY_POOLS.get('vpy', []):
        idx = len(vpy_init) + len(vpy_supp) + 1
        vpy_supp.append({'id': f'vpy_q_{idx:03d}', 'domain': 'animal_science', 'year': '1st_year', 'subjectId': 'vpy', 'topic': 'Veterinary Physiology High-Yield Core', 'questionText': q_text, 'options': list(opts), 'correctOptionIndex': ans, 'explanation': exp, 'difficulty': 'Medium', 'tags': ['Veterinary Physiology', 'ICAR PG Core'], 'createdAt': 1773000000000 + idx})

    base = [q for qs in [get_van_questions(), vpy_init + vpy_supp, get_vbc_questions(), get_lpm_questions(), get_vpp_questions(), get_vmc_questions(), get_vpa_questions(), get_agb_questions(), get_ann_questions()] for q in qs if not is_dummy(q)]
    pyqs = get_van_pyqs() + get_vpp_pyqs() + get_vmc_pyqs() + get_vbc_pyqs()
    exp1 = get_all_300_vpp_questions() + get_all_300_vmc_questions() + get_all_150_van_questions() + get_all_60_vpa_questions()
    all_1725 = base + pyqs + exp1

    gt12 = []
    for q in all_1725:
        c = q['options'][q['correctOptionIndex']]
        ds = [o for i, o in enumerate(q['options']) if i != q['correctOptionIndex']]
        nc = clean_correct_option(q['questionText'], c, ds, aggressive=True)
        diff = len(nc) - max(len(d) for d in ds)
        if diff > 12:
            gt12.append((diff, q, nc, ds))

    print(f"Total questions with diff > 12 after clean_correct_option: {len(gt12)}")
    for diff, q, nc, ds in gt12[:40]:
        print(f"[{q['id']}] diff={diff} | *C({len(nc)}): {nc} | D: {ds}")
