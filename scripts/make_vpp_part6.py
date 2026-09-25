import json

part6 = {
    "vpp_exp_232": [
        "SINE (Short Interspersed Nuclear Element) insertion upstream of p53 tumor suppressor",
        "LTR (Long Terminal Repeat) retroviral promoter insertion into the feline c-kit gene",
        "Reciprocal balanced chromosomal translocation fusing BCR and ABL kinase genes"
    ],
    "vpp_exp_234": [
        "Doxorubicin hydrochloride administered as a slow intravenous infusion",
        "Cyclophosphamide administered orally in alternating pulse doses",
        "L-asparaginase administered intramuscularly alongside corticosteroids"
    ],
    "vpp_exp_237": [
        "Serotonin acting on 5-HT3 receptors stimulating intense vagal emetic pathways",
        "Heparin acting on clotting factors causing widespread diffuse mucosal bleeding",
        "Leukotrienes stimulating mucosal goblet cells to hypersecrete viscous mucus"
    ],
    "vpp_exp_238": [
        "'Towards the elbow, away from the knee' (distal humerus and proximal femur)",
        "Axial skeleton exclusively (scapula, ribs, pelvic wing, and mandible)",
        "Vertebral bodies and sternum (diaphyseal cortices of cancellous bone)"
    ],
    "vpp_exp_242": [
        "80% malignant and 20% benign (of which 90% metastasize early to lungs)",
        "90% benign and 10% malignant (of which less than 1% ever metastasize)",
        "100% malignant with rapid lymphatic invasion and carcinomatosis"
    ],
    "vpp_exp_243": [
        "Homogeneous monomorphic proliferation of neoplastic secretory ductal epithelial cells",
        "Anaplastic spindle-shaped mesenchymal cells without any epithelial differentiation",
        "Metastatic squamous cell carcinoma with prominent extracellular keratin pearls"
    ],
    "vpp_exp_244": [
        "Kidney (followed by the urinary bladder trigone and prostate gland)",
        "Lungs (followed by bronchial lymph nodes and pericardial cavity)",
        "Skin (followed by deep subcutaneous adipose tissue of limbs)"
    ],
    "vpp_exp_245": [
        "Tissue mast cells containing histamine and heparin metachromatic granules",
        "Plasma cells actively producing monoclonal immunoglobulin paraproteins",
        "Vascular endothelial cells forming disorganized irregular vascular slits"
    ],
    "vpp_exp_246": [
        "Equine Herpesvirus 1 and Equine Herpesvirus 4 (EHV-1 / EHV-4)",
        "Equine Arteritis Virus and Equine Infectious Anemia Virus (EVA / EIA)",
        "Equine Papillomavirus Type 1 and Type 2 (EcPV-1 / EcPV-2)"
    ],
    "vpp_exp_249": [
        "Homer-Wright rosettes and perivascular pseudorosettes of neuroblasts",
        "Signet-ring cells containing abundant intracytoplasmic mucin droplets",
        "Stellate cells embedded in abundant loose Alcian blue-positive myxoid stroma"
    ],
    "vpp_exp_250": [
        "Chestnut horses, located on the dorsal withers, ventral abdomen, and flank",
        "Bay horses, located strictly on the lower extremities and coronary band",
        "Black horses, located along the jugular furrow and ventral cervical region"
    ],
    "vpp_exp_252": [
        "Severe paraneoplastic hypoglycemia (Insulin-like growth factor II secretion)",
        "Paraneoplastic polycythemia caused by autonomous erythropoietin secretion",
        "Severe hypergammaglobulinemia with monoclonal spike and hyperviscosity"
    ],
    "vpp_exp_253": [
        "Pancreatic Alpha cells, causing paraneoplastic hyperglycemia through glucagon",
        "Pancreatic Delta cells, causing somatostatinoma and systemic malabsorption",
        "Adrenal chromaffin cells, causing hypertensive crises through epinephrine"
    ],
    "vpp_exp_254": [
        "Adrenal cortex zona glomerulosa cells, secreting excess aldosterone (Conn's)",
        "Adrenal cortex zona fasciculata cells, secreting excess cortisol (Cushing's)",
        "Thyroid parafollicular C-cells, secreting excess calcitonin and causing tetany"
    ],
    "vpp_exp_255": [
        "Presence of an intact fibrous pseudocapsule and regular uniform cell cords",
        "Low mitotic count without prominent nucleoli or nuclear pleomorphism",
        "Secretory differentiation with retention of normal organellar microarchitecture"
    ],
    "vpp_exp_257": [
        "Modified live viral vaccines administered subcutaneously without adjuvants",
        "Intramuscular penicillin and oxytetracycline antimicrobial injections",
        "Subcutaneous microchip transponder implantation in interscapular tissue"
    ],
    "vpp_exp_263": [
        "Epithelial tumors (Cytokeratin positive) from Mesenchymal tumors (Vimentin positive)",
        "Histiocytic tumors (Iba-1 positive) from Mast cell tumors (c-kit positive)",
        "Melanocytic tumors (Melan-A positive) from Neural tumors (S100 positive)"
    ],
    "vpp_exp_265": [
        "Smooth muscle and skeletal muscle cells (confirming Leiomyoma and Rhabdomyoma)",
        "Pericytes and vascular mural cells (confirming Hemangiopericytoma)",
        "Fibroblasts and myofibroblasts (confirming Fibrosarcoma and Myofibroma)"
    ],
    "vpp_exp_266": [
        "Uniform cell size and shape, small round nuclei, and absence of mitotic figures",
        "Abundant clear lipid-filled cytoplasm with eccentric pyknotic small nuclei",
        "Regular honeycomb arrangement of cohesive cells with low nuclear:cytoplasm ratio"
    ],
    "vpp_exp_268": [
        "Deep necrotic ulceration extending into subcutaneous adipose tissue with suppuration",
        "Diffuse proliferation of uniform round cells arranged in sheets without stroma",
        "Expansile encapsulated proliferation of mature adipocytes separated by thin septa"
    ],
    "vpp_exp_270": [
        "Utilize fatty acid beta-oxidation exclusively while completely halting glycolysis",
        "Shut down all metabolic glucose utilization to preserve extracellular energy",
        "Rely strictly on oxidative phosphorylation generating maximum 36 ATP molecules"
    ],
    "vpp_exp_271": [
        "Right lateral recumbency (right side down, left side up exposing rumen)",
        "Dorsal recumbency (lying flat on back with all four limbs splayed outward)",
        "Sternal recumbency (resting upright on brisket with head fully extended)"
    ],
    "vpp_exp_272": [
        "Left lateral recumbency (left side down to expose right-side organs)",
        "Dorsal recumbency (lying flat on spine with limbs secured symmetrically)",
        "Sternal recumbency (resting on sternum to allow bilateral rib removal)"
    ],
    "vpp_exp_274": [
        "1:1 to 2:1 (tissue specimen volume equal to fixative volume)",
        "50:1 to 100:1 (large industrial reservoir immersion fixative volume)",
        "5:1 to 7:1 (minimal practical fixative allowance in field biopsies)"
    ],
    "vpp_exp_275": [
        "15 to 20 mm (approximately the width of two adult thumbs)",
        "1 to 2 mm (ultra-thin biopsy specimen requiring rapid processing)",
        "30 to 40 mm (large intact organ slices ensuring deep architecture)"
    ],
    "vpp_exp_278": [
        "Routine light microscopic examination of paraffin-embedded tissue sections",
        "Rapid intraoperative frozen section diagnosis using a cryostat",
        "Immunohistochemical staining of delicate cell surface antigens"
    ],
    "vpp_exp_279": [
        "Clearing (xylene) -> Dehydration (alcohols) -> Fixation -> Infiltration / Embedding",
        "Fixation -> Infiltration / Embedding -> Dehydration (alcohols) -> Clearing (xylene)",
        "Dehydration (alcohols) -> Fixation -> Clearing (xylene) -> Embedding in paraffin"
    ],
    "vpp_exp_281": [
        "Pink to red (eosinophilic), while Eosin stains nuclear chromatin blue to purple (basophilic)",
        "Bright green, while Eosin is a counterstain that stains cytoplasm yellow to orange",
        "Dark black, while Eosin stains collagen fibers and muscle bundles bright azure blue"
    ],
    "vpp_exp_285": [
        "Bright crimson red against an intense blue counterstained tissue background",
        "Deep violet purple against a light yellow counterstained background",
        "Brilliant magenta pink against a dark brown counterstained background"
    ],
    "vpp_exp_287": [
        "Trypsin enzyme digestion prior to Masson's trichrome staining (collagen vanishes)",
        "Hyaluronidase enzyme digestion prior to Alcian blue staining (mucin vanishes)",
        "Lipase digestion prior to Oil Red O staining (lipid droplets vanish)"
    ],
    "vpp_exp_288": [
        "Concentrated hydrochloric acid (10% aqueous HCl providing rapid decalcification)",
        "Nitric acid solution (5% aqueous HNO3 providing rapid tissue softening)",
        "Formic acid solution (buffered 10% formic acid providing gentle decalcification)"
    ],
    "vpp_exp_290": [
        "Delayed immersion in fixative allowing post-mortem autolysis to proceed",
        "Inadequate dehydration during tissue processing leaving water in tissues",
        "Use of dull microtome knives producing chattering and thick-and-thin sections"
    ],
    "vpp_exp_291": [
        "Total protein > 3.0 g/dL, TNCC > 7,000/uL, and high specific gravity (>1.025)",
        "Total protein 2.5-3.0 g/dL, TNCC 1,500-5,000/uL, and intermediate specific gravity",
        "Total protein > 5.0 g/dL, TNCC > 50,000/uL with degenerate neutrophils and bacteria"
    ],
    "vpp_exp_293": [
        "Low viscosity (watery drop), total protein > 4.5 g/dL, and TNCC > 20,000 cells/uL",
        "Zero viscosity, turbid serosanguinous fluid, and TNCC > 100,000 degenerate neutrophils",
        "Moderate viscosity, total protein < 0.5 g/dL, and absence of all cellular elements"
    ],
    "vpp_exp_299": [
        "Dogs (and to a lesser degree ruminants)",
        "Cattle and sheep (ruminant domestic species)",
        "Birds and reptiles (avian/reptilian species)"
    ],
    "vpp_exp_300": [
        "The Coombs Test: direct antiglobulin test detecting red cell bound antibodies",
        "The Osmotic Fragility Test: evaluating erythrocyte lysis in hypotonic saline solutions",
        "The Crossmatch Test: incubating donor red cells with recipient serum for hemolysis"
    ]
}

with open('scripts/vpp_part6.json', 'w', encoding='utf-8') as f:
    json.dump(part6, f, indent=2)

print(f"Wrote {len(part6)} overrides in part 6")
