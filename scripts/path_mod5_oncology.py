# scripts/path_mod5_oncology.py
# Module 5: Veterinary Oncology & Neoplasia (40 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module5_questions():
    qs = [
        # 1-10: Classical veterinary tumors & cytogenetics
        ("Canine Transmissible Venereal Tumor (CTVT / Sticker's sarcoma) is cytogenetically unique among animal neoplasms because it possesses a stable somatic chromosome number of:",
         ["59 chromosomes (normal canine 2n = 78)", "78 chromosomes", "38 chromosomes", "64 chromosomes"],
         0, "CTVT is a naturally transmissible allograft clone where neoplastic cells are transferred via coitus. Karyotypic analysis shows a consistent, unique chromosome count of 59 (with numerous metacentric and submetacentric chromosomes) compared to normal canine 2n = 78.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("The specific molecular diagnostic fingerprint confirming CTVT by PCR analysis is the detection of a:",
         ["LINE-1 (Long Interspersed Nuclear Element-1) retrotransposon inserted upstream of the c-myc oncogene", "Point mutation in the p53 tumor suppressor gene", "Translocation between chromosomes 9 and 22", "Deletion of the Rb gene"],
         0, "A pathognomonic diagnostic feature of CTVT is the insertion of a specific 1.4-kb LINE-1 retrotransposon element immediately upstream of the c-myc oncogene promoter, found in all CTVT tumors worldwide.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("The histological appearance of CTVT cells on cytological smears or biopsies is characterized as:",
         ["Round cells arranged in sheets with central round nuclei, coarse chromatin, prominent nucleoli, and clear vacuolated cytoplasm", "Spindle-shaped cells forming interlacing bundles", "Polygonal epithelial cells forming distinct acini", "Pleomorphic multinucleated cells with striations"],
         0, "CTVT belongs to the round cell tumor group. Neoplastic cells are round to polyhedral with centrally placed nuclei, single prominent nucleoli, and distinct punctate, clear cytoplasmic lipid vacuoles.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("The chemotherapy agent of choice for treating Canine Transmissible Venereal Tumor, achieving >90% complete remission, is:",
         ["Vincristine sulfate administered intravenously weekly", "Doxorubicin", "Cyclophosphamide", "Methotrexate"],
         0, "Vincristine is a vinca alkaloid that binds tubulin, disrupting mitotic spindle microtubules during metaphase; CTVT cells are exceptionally sensitive to it, achieving complete cure within 3-6 weekly treatments.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Canine Cutaneous Mast Cell Tumors (MCTs) contain intracytoplasmic granules that display metachromatic staining (turning purple/magenta) when stained with:",
         ["Toluidine Blue or Giemsa stain", "Hematoxylin and Eosin", "Masson's Trichrome", "Von Kossa stain"],
         0, "Mast cell granules are packed with polyanionic sulfated glycosaminoglycans (heparin and chondroitin sulfate); they shift the absorption spectrum of cationic dyes like Toluidine Blue from blue to reddish-purple (metachromasia).",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("The two-tier histological grading system for Canine Cutaneous Mast Cell Tumors proposed by Kiupel et al. classifies tumors into:",
         ["Low-grade and High-grade", "Grade I, Grade II, and Grade III", "Stage 1 to Stage 4", "Benign and Malignant only"],
         0, "Kiupel's system simplifies mast cell tumor grading into a two-tier scheme: Low-grade vs High-grade, based on mitotic count (>=7/10 HPF), multinucleation (>=3 nuclei in >=3 cells/10 HPF), bizarre nuclei, and karyomegaly.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("In dogs with mast cell tumors, the systemic paraneoplastic development of gastrointestinal ulceration is directly caused by neoplastic release of:",
         ["Histamine acting on H2 receptors of gastric parietal cells, stimulating massive hydrochloric acid secretion", "Heparin inhibiting prothrombin conversion", "Serotonin causing severe vasoconstriction", "Platelet Activating Factor"],
         0, "Degranulating neoplastic mast cells release large quantities of histamine into circulation; histamine stimulates H2 receptors on gastric parietal cells, causing severe hyperchlorhydria, mucosal ischemia, and gastric/duodenal ulcers.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Canine Osteosarcoma classically exhibits a radiographic and anatomical distribution rule known as:",
         ["'Away from the elbow, towards the knee' (proximal humerus, distal radius, distal femur, proximal tibia)", "'Towards the elbow, away from the knee'", "'Confined exclusively to the axial skeleton'", "'Symmetrically involving all four distal digits'"],
         0, "Canine osteosarcoma has a strong predilection for the metaphysis of long bones: distal radius and proximal humerus in the forelimb ('away from the elbow'), and distal femur and proximal tibia in the hindlimb ('towards the knee').",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("The classic radiographic signs of primary canine appendicular osteosarcoma on plain radiographs are:",
         ["Cortical bone lysis, 'sunburst' periosteal reaction, and Codman's triangle", "Pure osteosclerosis with no cortical disruption", "Punched-out radiolucent osteolytic lesions in the calvarium only", "Diffuse subchondral bone cysts"],
         0, "Rapid tumor expansion causes cortical destruction and stimulates the periosteum to deposit reactive spicules perpendicular to the cortex ('sunburst' pattern) and elevate the periosteum at the margins ('Codman's triangle').",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("In dogs with canine appendicular osteosarcoma, the most common route and anatomical site of early hematogenous metastasis is the:",
         ["Lungs (pulmonary metastasis)", "Liver parenchyma", "Spleen red pulp", "Kidney cortex"],
         0, "Over 90% of dogs with osteosarcoma already have microscopic hematogenous micrometastases in the pulmonary capillary beds at the time of initial clinical presentation.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        # 11-20: Mammary tumors, Hemangiosarcoma, Lymphoma
        ("Canine Mammary Tumors show a marked reduction in incidence if ovariohysterectomy (spaying) is performed before the first estrus, reducing the risk to approximately:",
         ["0.5% (compared to 8% after 1st estrus and 26% after 2nd estrus)", "15%", "50%", "75%"],
         0, "Ovarian steroid hormones (estrogen and progesterone) drive the proliferation of canine mammary epithelium; spaying before the 1st cycle reduces risk to 0.5%, demonstrating profound hormone-dependency during initiation.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("In female dogs, the approximate biological distribution between benign and malignant mammary neoplasms is:",
         ["50% benign and 50% malignant (of which 50% metastasize)", "90% malignant and 10% benign", "95% benign and 5% malignant", "100% malignant"],
         0, "In bitches, approximately 50% of mammary tumors are histologically benign (adenomas, fibroadenomas, complex/mixed tumors) and 50% are malignant carcinomas; this contrasts sharply with cats, where >85-90% are highly malignant adenocarcinomas.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("A 'Canine Mixed Mammary Tumor' (Pleomorphic Adenoma / Benign Mixed Tumor) is histologically characterized by the presence of:",
         ["Both epithelial/myoepithelial cells and heterologous mesenchymal elements (such as cartilage and bone)", "Both neoplastic lymphocytes and squamous cells", "Both mast cells and histiocytes", "Metastatic cells from an osteosarcoma"],
         0, "Mixed mammary tumors contain benign neoplastic secretory epithelium along with proliferating myoepithelial cells that undergo metaplastic transformation into mesenchymal tissues, notably myxoid matrix, hyaline cartilage, and woven bone.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Canine Hemangiosarcoma is a malignant neoplasm arising from vascular endothelial cells, with the most common primary anatomical site of origin being the:",
         ["Spleen (followed by the right atrium of the heart and liver)", "Kidney cortex", "Adrenal medulla", "Pancreas"],
         0, "The spleen is the primary organ of origin in over 50% of canine hemangiosarcoma cases, followed by the right auricle/atrium of the heart (frequently causing hemopericardium and cardiac tamponade) and the liver.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Canine Cutaneous Histiocytoma, a common benign dermal tumor in dogs under 3 years of age ('button tumor'), is derived from which epidermal immune cell?",
         ["Langerhans cells (epidermal dendritic cells)", "Melanocytes", "Merkel cells", "Basal keratinocytes"],
         0, "Cutaneous histiocytomas are benign self-limiting round cell tumors originating from epidermal Langerhans cells (expressing CD1a, CD11c, and E-cadherin); they spontaneously regress within 1-2 months via CD8+ T-cell infiltration.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Equine Sarcoid, the most common skin tumor of horses, donkeys, and mules, is fundamentally induced by infection with:",
         ["Bovine Papillomavirus Type 1 and Type 2 (BPV-1 and BPV-2)", "Equine Herpesvirus 1", "Equine Arteritis Virus", "Equine Papillomavirus Type 1"],
         0, "Equine sarcoids are non-metastatic, locally invasive fibroblastic skin neoplasms induced by cross-species infection with Bovine Papillomaviruses 1 and 2, which express E5 and E6 oncoproteins that stimulate dermal fibroblasts.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Histologically, an Equine Sarcoid is characterized by the diagnostic combination of:",
         ["Hyperplastic epidermis with elongated, hyperkeratotic rete pegs ('picket-fence' pattern) and a dermal proliferation of fibroblasts in whorls and interlacing bundles", "Pure squamous cell carcinoma with epithelial pearls", "Sheets of round cells with metachromatic granules", "Caseous granulomas with Langhans giant cells"],
         0, "The diagnostic hallmark of equine sarcoids is epidermal hyperplasia with deep rete pegs interdigitating with dense, perpendicular bundles of proliferating dermal fibroblasts oriented perpendicular to the basement membrane ('picket-fence' pattern).",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("In cattle, Squamous Cell Carcinoma of the eye and orbit ('Cancer Eye') has the highest incidence in which breed, primarily due to lack of circumocular pigmentation?",
         ["Hereford", "Jersey", "Holstein-Friesian", "Angus"],
         0, "Hereford cattle lack protective melanin pigmentation on the eyelids and corneoscleral limbus, predisposing them to solar UV-induced DNA damage, actinic keratosis, plaque formation, and invasive squamous cell carcinoma.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("The pathognomonic microscopic feature confirming a diagnosis of well-differentiated Squamous Cell Carcinoma (SCC) is the presence of:",
         ["'Keratin pearls' (concentric lamellae of keratinized squames) and intercellular bridges (desmosomes)", "Intracellular mucin droplets staining with Mucicarmine", "Osteoid matrix trabeculae surrounded by osteoblasts", "Melanin granules within spindle cells"],
         0, "SCC is characterized by cords and nests of malignant squamous epithelial cells that undergo central individual-cell keratinization, forming concentric whorls of keratin called 'keratin pearls' or 'epithelial pearls', linked by intercellular bridges.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("In horses, melanomas and melanocytomas have an exceptionally high incidence in which specific coat color and anatomical region?",
         ["Gray horses, located in the perineal region, ventral tail base, and parotid gland area", "Chestnut horses, on the distal limbs", "Bay horses, on the cornea", "Black horses, on the ventral abdomen"],
         0, "Over 80% of gray horses older than 15 years develop melanocytic neoplasms, particularly around the perineum, ventral tail base, commissures of the lips, and parotid salivary glands, due to abnormal dermal melanocyte proliferation during graying.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        # 21-30: Paraneoplastic syndromes, endocrine tumors, sarcomas
        ("The most frequent paraneoplastic syndrome in veterinary medicine is 'Humoral Hypercalcemia of Malignancy' (HHM), most commonly associated with canine lymphoma and apocrine gland adenocarcinoma of the anal sac, mediated by:",
         ["Parathyroid Hormone-related Protein (PTHrP)", "Excessive calcitriol secretion", "Direct osteolytic osteoclast destruction", "Interleukin-10"],
         0, "PTHrP is synthesized by neoplastic cells (e.g. T-cell lymphoma, anal sac adenocarcinoma); it binds PTH-1 receptors on osteoclasts and renal tubules, stimulating bone resorption and renal calcium retention, driving severe hypercalcemia.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Canine Apocrine Gland Adenocarcinoma of the Anal Sac (AGASACA) is a malignant perineal tumor that is characterized clinically by:",
         ["Severe paraneoplastic hypercalcemia (PTHrP-induced) and early metastasis to the sublumbar (medial iliac) lymph nodes", "Severe hypoglycemia", "Bilateral alopecia without lymph node enlargement", "Benign behavior in 99% of cases"],
         0, "AGASACA is highly malignant; ~25-50% of cases present with severe hypercalcemia of malignancy due to PTHrP secretion, and tumors metastasize early to internal iliac and sacral lymph nodes.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("In ferrets and dogs, an 'Insulinoma' is a functional neuroendocrine tumor originating from which cell type in the islets of Langerhans?",
         ["Pancreatic Beta cells, causing paraneoplastic hypoglycemia through autonomous insulin secretion", "Alpha cells, causing persistent hyperglycemia", "Delta cells, secreting somatostatin", "PP cells, secreting pancreatic polypeptide"],
         0, "Insulinomas are malignant (in dogs) or benign/malignant (in ferrets) neoplasms of beta cells that autonomously oversecrete insulin independent of blood glucose, producing severe neuroglycopenia, weakness, tremors, and seizures.",
         True, "Endocrine Pathology (ICAR PG PYQ)"),

        ("A 'Pheochromocytoma' in dogs and cattle is a neoplasm of the adrenal medulla arising from which cell type?",
         ["Chromaffin cells, secreting excessive catecholamines (epinephrine and norepinephrine)", "Zona glomerulosa cells", "Zona fasciculata cells", "Cortical stromal cells"],
         0, "Pheochromocytomas arise from chromaffin cells of the adrenal medulla; excessive catecholamine release causes paraneoplastic systemic hypertension, tachycardia, cardiac hypertrophy, and frequent local invasion into the caudal vena cava.",
         True, "Endocrine Pathology (ICAR PG PYQ)"),

        ("The definitive microscopic distinction between an 'Adenoma' and an 'Adenocarcinoma' is that the adenocarcinoma exhibits:",
         ["Invasion through the basement membrane into surrounding stroma, lymphatic/vascular permeation, and cellular anaplasia", "Glandular architectural organization", "A thin, fibrous capsule", "Uniform round nuclei without mitoses"],
         0, "Adenomas are benign, well-circumscribed, encapsulated epithelial neoplasms that do not invade basement membranes; adenocarcinomas display stromal invasion, nuclear pleomorphism, high mitotic rate, and metastatic competence.",
         False, "Veterinary Oncology"),

        ("In veterinary histopathology, malignant mesenchymal neoplasms derived from connective tissues (fibroblasts, endothelial cells, smooth muscle) are collectively classified as:",
         ["Sarcomas", "Carcinomas", "Teratomas", "Blastomas"],
         0, "Malignant tumors of mesenchymal origin (bone, cartilage, fibrous tissue, muscle, blood vessels) are termed sarcomas, whereas malignant tumors of epithelial origin (ectoderm, endoderm) are termed carcinomas.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Feline Injection-Site Sarcoma (FISS / Vaccine-Associated Sarcoma) is an aggressive mesenchymal malignancy, predominantly a Fibrosarcoma, strongly linked to chronic inflammation induced by:",
         ["Adjuvanted vaccines (such as Rabies and Feline Leukemia Virus vaccines) containing aluminum adjuvants", "Subcutaneous insulin injections", "Intramuscular antibiotic therapy", "Intravenous catheterization"],
         0, "FISS in cats arises from malignant transformation of reactive fibroblasts and myofibroblasts at injection sites, associated with chronic inflammation triggered by adjuvanted vaccines (aluminum hydroxide), characterized by blue aluminum granules in macrophages.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("A 'Teratoma' is a germ cell neoplasm characterized histologically by the presence of tissues derived from:",
         ["All three embryonic germ layers: ectoderm, mesoderm, and endoderm", "Ectoderm exclusively", "Mesoderm and neuroectoderm only", "Endoderm only"],
         0, "Teratomas arise from totipotent primordial germ cells (predominantly in the ovary or cryptorchid testis) and contain disorganized elements of all three germ cell layers: skin, hair, teeth (ectoderm), bone, cartilage, muscle (mesoderm), and gut epithelium (endoderm).",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("In male dogs, Cryptorchidism (retained undescended testicle) increases the relative risk of developing testicular neoplasia by 10 to 14 times, especially for which two tumors?",
         ["Sertoli Cell Tumor and Seminoma", "Leydig cell tumor only", "Hemangiosarcoma and Melanoma", "Fibrosarcoma and Osteosarcoma"],
         0, "Higher intra-abdominal temperatures in cryptorchid testes disrupt normal spermatogenesis and predispose germ cells and supporting cells to malignant transformation, predominantly Sertoli cell tumors and Seminomas.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Canine Oral Melanoma is considered biologically one of the most aggressive tumors in veterinary medicine because:",
         ["Over 80-90% of cases exhibit rapid bone invasion and early metastasis to regional lymph nodes and lungs, regardless of histological pigmentation", "It is always responsive to surgical debulking alone", "It rarely recurs after excision", "It never invades the mandible or maxilla"],
         0, "Unlike cutaneous melanocytomas, oral melanomas in dogs (amelanotic or melanotic) are highly invasive, osteolytic, and early to metastasize via lymphatic and hematogenous routes, carrying a guarded prognosis.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        # 31-40: Diagnostic oncology, IHC, cytopathology
        ("Immunohistochemistry (IHC) utilizes specific intermediate filament antibodies to determine tumor histogenesis. Which marker confirms the epithelial origin of a carcinoma?",
         ["Cytokeratin (CK)", "Vimentin", "Desmin", "Glial Fibrillary Acidic Protein (GFAP)"],
         0, "Cytokeratins are intermediate filaments unique to epithelial cells; positivity confirms carcinoma. Vimentin marks mesenchymal cells (sarcoma), Desmin marks myogenic tumors, and GFAP marks astrocytic glial tumors.",
         True, "Diagnostic Oncology (ICAR PG PYQ)"),

        ("Which immunohistochemical marker is specific for demonstrating smooth and skeletal muscle differentiation in veterinary neoplasms (such as rhabdomyosarcomas and leiomyosarcomas)?",
         ["Desmin (and muscle-specific actin)", "Cytokeratin 19", "Chromogranin A", "S100 protein"],
         0, "Desmin is the 52-kDa intermediate filament characteristic of skeletal, smooth, and cardiac muscle cells, serving as the gold standard diagnostic IHC marker for myogenic neoplasms.",
         True, "Diagnostic Oncology"),

        ("In diagnostic veterinary oncology, CD3 and CD79a (or CD20) immunohistochemical markers are universally employed to differentiate:",
         ["T-cell Lymphoma (CD3 positive) from B-cell Lymphoma (CD79a/CD20 positive)", "Carcinoma from Sarcoma", "Melanoma from Mast cell tumor", "Adenoma from Papilloma"],
         0, "CD3 is a specific surface marker for T-lymphocytes, whereas CD79a and CD20 are pan-B-cell markers; this distinction is essential for subtyping canine and feline lymphomas for prognostic and therapeutic protocols.",
         True, "Diagnostic Oncology (ICAR PG PYQ)"),

        ("The primary tumor marker used to identify neuroendocrine differentiation (e.g. in thyroid C-cell tumors, pheochromocytomas, carcinoids) is:",
         ["Chromogranin A and Synaptophysin", "Neuron-specific enolase only", "Vimentin", "Von Willebrand factor"],
         0, "Chromogranin A (dense-core neurosecretory granule protein) and Synaptophysin (small synaptic vesicle protein) are the two definitive immunohistochemical markers establishing neuroendocrine differentiation.",
         False, "Diagnostic Oncology"),

        ("Von Willebrand Factor (Factor VIII-related antigen) and CD31 (PECAM-1) are specific immunohistochemical markers for:",
         ["Vascular endothelial cells (confirming Hemangioma and Hemangiosarcoma)", "Epithelial keratinocytes", "Skeletal myocytes", "Adipocytes"],
         0, "Endothelial cells synthesize Factor VIII-related antigen (stored in Weibel-Palade bodies) and express CD31 on their surface, serving as specific diagnostic markers for benign and malignant vascular neoplasms.",
         True, "Diagnostic Oncology (ICAR PG PYQ)"),

        ("In cytological evaluation of a fine-needle aspirate (FNA), which triad of cytological criteria provides the most definitive evidence of malignancy?",
         ["Marked anisokaryosis (variation in nuclear size), prominent and multiple nucleoli, and atypical mitotic figures", "Uniform cell size, round nuclei, and low N:C ratio", "Abundant mature cytoplasm with absence of mitoses", "Presence of normal inflammatory cells only"],
         0, "Nuclear criteria are the most reliable indicators of malignancy, including anisokaryosis, macronucleoli, variable numbers and shapes of nucleoli, high nuclear-to-cytoplasmic (N:C) ratio, and abnormal/atypical tripolar or quadripolar mitoses.",
         True, "Diagnostic Oncology (ICAR PG PYQ)"),

        ("Canine Plasmacytoma (extramedullary plasmacytoma) is cytologically recognized by which distinctive cellular features?",
         ["Eccentric round nuclei, coarse 'clock-face' or 'cartwheel' chromatin, deeply basophilic cytoplasm, and a prominent perinuclear clear halo (Golgi zone)", "Central spindle-shaped nuclei with bipolar tails", "Clear vacuolated cytoplasm with signet-ring morphology", "Multinucleated osteoclasts"],
         0, "Plasma cells have an eccentrically placed nucleus with radially arranged heterochromatin ('cartwheel' or 'spoke-wheel' pattern), rich basophilic cytoplasm (abundant rough ER), and a clear pale perinuclear zone corresponding to the Golgi apparatus.",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("Bovine Papillomatosis (cutaneous warts in cattle) is caused by Bovine Papillomaviruses (BPV-1, BPV-2, BPV-6) that produce benign neoplasms characterized histologically by:",
         ["Marked epidermal hyperkeratosis, acanthosis, and proliferating rete pegs over a fibrovascular core, containing koilocytes with clear halos", "Invasive nests of squamous cells with keratin pearls", "Pure liquefactive necrosis of the dermis", "Diffuse granulomatous panniculitis"],
         0, "Papillomas are benign exophytic fibroepithelial tumors featuring severe acanthosis (thickened stratum spinosum), hyperkeratosis, and pathognomonic 'koilocytes' (keratinocytes with pyknotic nuclei and clear cytoplasmic halos).",
         True, "Veterinary Oncology (ICAR PG PYQ)"),

        ("In dogs with Zollinger-Ellison Syndrome, a rare paraneoplastic disorder, recurrent severe gastroduodenal ulceration is driven by an islet cell tumor secreting:",
         ["Gastrin (Gastrinoma)", "Glucagon (Glucagonoma)", "Vasoactive Intestinal Peptide (VIPoma)", "Secretin"],
         0, "Gastrinomas secrete autonomous gastrin, which overstimulates gastric parietal cells to produce continuous hydrochloric acid secretion, overcoming mucosal defense barriers and causing intractable peptic ulcers.",
         False, "Endocrine Pathology"),

        ("The 'Warburg Effect' observed in veterinary oncology describes the metabolic preference of neoplastic cells to:",
         ["Ferment glucose into lactate via aerobic glycolysis even in the abundant presence of oxygen", "Oxidize fatty acids exclusively in the mitochondrial matrix", "Produce all ATP via the urea cycle", "Depend exclusively on glutamine transamination"],
         0, "Otto Warburg demonstrated that cancer cells reprogram their energy metabolism to undergo glycolysis and lactate production despite adequate oxygen (aerobic glycolysis), providing glycolytic intermediates for rapid macromolecular synthesis.",
         False, "Veterinary Oncology")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module5_questions()
    print(f"Pathology Module 5 loaded: {len(qs)} questions")
