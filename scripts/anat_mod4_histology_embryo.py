# scripts/anat_mod4_histology_embryo.py
# Module 4: Histology & Embryology (25 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit I (Sub-subject 13.1)

def get_module4_questions():
    qs = [
        # 1-10: General Histology (Epithelium, Connective tissue, Cartilage, Bone, Muscle, Nerve)
        ("Which of the following cartilages is completely devoid of a perichondrium, relying solely on surrounding synovial fluid or adjacent tissues for its nutrition?",
         ["Fibrocartilage (e.g., intervertebral discs and pelvic symphysis)", "Hyaline cartilage (e.g., tracheal rings)", "Elastic cartilage (e.g., external pinna)", "Costal cartilage"],
         0, "Fibrocartilage lacks an outer perichondrium (unlike hyaline and elastic cartilages); it blends gradually into adjacent dense fibrous connective tissue and receives nutrition by diffusion from adjacent structures or synovial fluid.",
         True, "General Histology (ICAR PG PYQ)"),

        ("In compact bone histology, the transverse or oblique vascular channels that penetrate the bone matrix to connect adjacent Haversian canals and periosteal vessels are known as:",
         ["Volkmann's canals (Perforating canals)", "Canaliculi", "Haversian canals (Central canals)", "Lacunae"],
         0, "Volkmann's canals run perpendicularly or obliquely to the long axis of osteons, carrying blood vessels and nerves from the periosteal and endosteal surfaces to communicate with Haversian (central) canals.",
         True, "General Histology (ICAR PG PYQ)"),

        ("In mammalian skeletal muscle fibers, a 'Triad' observed at the junction of the A and I bands is anatomically composed of:",
         ["One central transverse tubule (T-tubule) flanked by two terminal cisternae of the sarcoplasmic reticulum", "Two T-tubules and one terminal cisterna", "One T-tubule and one sarcoplasmic reticulum cisterna (Dyad)", "Three adjacent myofibrils"],
         0, "In mammalian skeletal muscle, a triad consists of a central invagination of the sarcolemma (T-tubule) flanked on either side by two dilated terminal cisternae of the sarcoplasmic reticulum at each A-I band junction (two triads per sarcomere).",
         True, "General Histology (ICAR PG PYQ)"),

        ("In cardiac muscle histology, the 'Intercalated Discs' that bind cardiomyocytes end-to-end contain which specialized intercellular junctions for low-resistance electrical coupling?",
         ["Gap junctions (Nexus)", "Zonula occludens (Tight junctions)", "Desmosomes (Macula adherens) only", "Hemidesmosomes"],
         0, "While fascia adherens and desmosomes provide mechanical anchoring across the transverse portions of intercalated discs, the longitudinal lateral portions are packed with Gap Junctions (nexuses) that allow rapid ionic and action potential transmission.",
         True, "General Histology (ICAR PG PYQ)"),

        ("In neuronal cytology, the basophilic clumps known as 'Nissl bodies' (Nissl substance) correspond ultrastructurally to:",
         ["Rough Endoplasmic Reticulum (RER) and polyribosomes (absent in the axon and axon hillock)", "Golgi apparatus complexes", "Mitochondrial aggregations", "Neurofilaments and microtubules"],
         0, "Nissl granules represent prominent stacks of rough endoplasmic reticulum and free ribosomes actively synthesizing structural and neurotransmitter proteins; they are characteristically absent from the axon and axon hillock.",
         True, "General Histology (ICAR PG PYQ)"),

        ("Which resident connective tissue cell is characterized by metachromatic cytoplasmic granules containing histamine, heparin, and serotonin, playing a central role in Type I hypersensitivity?",
         ["Mast cell (Mastocyte)", "Plasma cell", "Macrophage (Histiocyte)", "Fibroblast"],
         0, "Mast cells originate from bone marrow CD34+ precursors, reside in connective tissues along microvessels, and display intense metachromatic granules (staining purple-red with toluidine blue) rich in heparin and histamine.",
         True, "General Histology (ICAR PG PYQ)"),

        ("The predominant collagen type found in hyaline cartilage matrix and the vitreous body of the eye is:",
         ["Type II Collagen", "Type I Collagen", "Type III Collagen (Reticular fibers)", "Type IV Collagen (Basement membrane)"],
         0, "Type II collagen forms thin fibrils embedded in proteoglycan ground substance in hyaline and elastic cartilage; Type I is the chief structural collagen of bone, tendon, and skin; Type III forms reticular meshworks; Type IV forms basal laminae.",
         True, "General Histology (ICAR PG PYQ)"),

        ("Which neuroglial cell of the Central Nervous System (CNS) is derived from embryonic mesoderm / monocytes rather than neuroectoderm, functioning as the resident phagocyte?",
         ["Microglia", "Astrocyte (Protoplasmic and Fibrous)", "Oligodendrocyte", "Ependymal cell"],
         0, "Microglia are mononuclear phagocyte lineage cells originating from embryonic yolk sac mesenchyme that invade the developing CNS; all other glial cells (astrocytes, oligodendrocytes, ependymal cells) derive from neuroectoderm.",
         False, "General Histology"),

        ("The epithelial lining of the urinary bladder and ureter that exhibits specialized umbrella (facet) cells and the ability to accommodate severe distension without rupture is:",
         ["Transitional epithelium (Urothelium)", "Simple cuboidal epithelium", "Pseudostratified ciliated columnar epithelium", "Stratified squamous non-keratinized epithelium"],
         0, "Transitional epithelium (urothelium) lines the renal calyces, pelvis, ureters, and urinary bladder; its superficial layer has specialized polyhedral umbrella cells with thickened apical asymmetric plaques that resist osmotic and mechanical stress.",
         False, "General Histology"),

        ("The specialized sensory mechanoreceptors in deep skin, tendons, and joint capsules characterized by concentric lamellae of Schwann cells surrounding a central unmyelinated axon like an onion bulb are:",
         ["Pacinian corpuscles (Lamellar corpuscles)", "Meissner's corpuscles", "Merkel nerve endings", "Ruffini corpuscles"],
         0, "Pacinian corpuscles are large onion-like lamellated mechanoreceptors in the deep dermis, hypodermis, mesentery, and periosteum responsive to high-frequency vibration and deep pressure.",
         True, "General Histology (ICAR PG PYQ)"),

        # 11-18: Organ Histology (Liver, Kidney, Lymphoid, Respiratory, Endocrine)
        ("In liver histology, the microvascular perisinusoidal space where blood plasma filters through fenestrated endothelial cells to bathe hepatocyte microvilli is the:",
         ["Space of Disse (Perisinusoidal space)", "Space of Mall", "Canal of Hering", "Bile canaliculus"],
         0, "The space of Disse lies between the sinusoidal fenestrated endothelial lining and the hepatocyte basolateral microvillar surface, permitting rapid macromolecular exchange and housing hepatic stellate (Ito) cells.",
         True, "Organ Histology (ICAR PG PYQ)"),

        ("Hepatic stellate cells (Ito cells / Lipocytes) located within the Space of Disse are the primary physiological storage site for which lipid-soluble vitamin, and transform into myofibroblasts during liver fibrosis?",
         ["Vitamin A (Retinoids)", "Vitamin D", "Vitamin E", "Vitamin K"],
         0, "Hepatic stellate cells (Ito cells) store approximately 80% of total body Vitamin A in cytoplasmic lipid droplets; upon chronic liver injury, they activate into alpha-smooth muscle actin-positive myofibroblasts, secreting collagen.",
         True, "Organ Histology (ICAR PG PYQ)"),

        ("In the mammalian spleen, the 'Periarteriolar Lymphoid Sheath' (PALS) surrounding the central arterioles is predominantly composed of which immune cell population?",
         ["T lymphocytes", "B lymphocytes", "Plasma cells", "Erythrocytes and platelets"],
         0, "PALS is the thymus-dependent periarterial lymphoid sheath of the splenic white pulp populated selectively by T lymphocytes, whereas splenic follicles (Malpighian bodies) are populated by B lymphocytes.",
         True, "Organ Histology (ICAR PG PYQ)"),

        ("The diagnostic histological hallmark of the Thymus gland medulla, consisting of concentric whorls of keratinizing and degenerated eosinophilic epithelial reticular cells, is the:",
         ["Hassall's corpuscle (Thymic corpuscle)", "Malpighian corpuscle", "Herring body", "Peyer's patch"],
         0, "Hassall's corpuscles (thymic corpuscles) are unique eosinophilic concentric laminated epithelial structures found exclusively in the thymic medulla, producing thymic stromal lymphopoietin (TSLP) and increasing with age.",
         True, "Organ Histology (ICAR PG PYQ)"),

        ("In the mammalian kidney, the 'Juxtaglomerular Apparatus' includes a specialized plaque of densely packed, tall, narrow epithelial cells sensing sodium chloride concentration in which nephron segment?",
         ["Distal Convoluted Tubule (Macula densa)", "Proximal Convoluted Tubule", "Descending thin limb of Henle", "Cortical collecting duct"],
         0, "The macula densa consists of specialized tubular epithelial cells in the initial segment of the distal convoluted tubule located directly adjacent to the afferent and efferent arterioles of its parent glomerulus, monitoring luminal NaCl.",
         True, "Organ Histology (ICAR PG PYQ)"),

        ("In the domestic Ox and Sheep, the outer adrenal cortex (zona subcapsularis) exhibits cellular cords arranged in arched or loop-like clusters, earning it the histological designation:",
         ["Zona arcuata (characteristic of carnivores and equines, whereas ruminants display rounded clusters as classic Zona glomerulosa)", "Zona fasciculata", "Zona reticularis", "Chromaffin zone"],
         0, "In dogs, cats, and horses, the subcapsular mineralocorticoid-producing zone has looping arches termed 'Zona arcuata'; in ruminants and humans, the cells are in rounded clumps designated 'Zona glomerulosa'.",
         True, "Organ Histology (ICAR PG PYQ)"),

        ("In lung alveoli, which specialized epithelial cell type is responsible for the synthesis, storage in lamellar bodies, and secretion of pulmonary surfactant (dipalmitoylphosphatidylcholine)?",
         ["Type II Pneumocyte (Great alveolar cell)", "Type I Pneumocyte (Squamous alveolar cell)", "Alveolar macrophage (Dust cell)", "Club cell (Clara cell)"],
         0, "Type II pneumocytes are cuboidal cells with apical microvilli and lamellar bodies that secrete pulmonary surfactant to lower alveolar surface tension and prevent end-expiratory atelectasis; they also divide to regenerate Type I cells.",
         True, "Organ Histology (ICAR PG PYQ)"),

        ("The specialized venous vessels in the paracortex of lymph nodes lined by plump cuboidal endothelial cells that facilitate lymphocyte homing from the bloodstream are designated:",
         ["High Endothelial Venules (HEVs)", "Sinusoids", "Trabecular veins", "Subcapsular sinuses"],
         0, "High Endothelial Venules (HEVs) in the paracortex have tall, plump, cuboidal endothelial cells expressing specific selectins and addressins that enable naive T and B lymphocytes in circulation to tether, roll, and extravasate into lymph node parenchyma.",
         True, "Organ Histology (ICAR PG PYQ)"),

        # 19-25: Embryology (Germ layers, Somites, Fetal circulation, Derivatives)
        ("In the developing mammalian embryo, the somites (derived from paraxial mesoderm) differentiate into three distinct cellular components: Sclerotome, Myotome, and Dermatome. The Sclerotome gives rise to:",
         ["The axial skeleton (vertebrae and ribs)", "All skeletal musculature of the trunk and limbs", "Dermis of the dorsal trunk skin", "Urogenital system"],
         0, "Paraxial mesoderm divides into somites; the ventromedial sclerotome cells migrate around the notochord and neural tube to form vertebrae, intervertebral discs, and ribs; myotome forms striated skeletal muscle; dermatome forms dorsal dermis.",
         True, "Veterinary Embryology (ICAR PG PYQ)"),

        ("Which extraordinary population of pluripotent embryonic cells arises from the neural fold margins during neurulation, migrating throughout the body to form melanocytes, Schwann cells, spinal and autonomic ganglia, and the adrenal medulla?",
         ["Neural Crest cells", "Notochordal cells", "Endodermal epithelial cells", "Lateral plate mesoderm"],
         0, "Neural crest cells (often called the 'fourth germ layer') delaminate from neural folds, giving rise to peripheral sensory and autonomic ganglia, Schwann cells, melanocytes, craniofacial skeletal tissues, and adrenal medullary chromaffin cells.",
         True, "Veterinary Embryology (ICAR PG PYQ)"),

        ("In fetal circulation, the physiological vascular shunt that diverts oxygen-rich blood directly from the umbilical vein into the caudal vena cava, largely bypassing the fetal hepatic sinusoids, is the:",
         ["Ductus venosus", "Ductus arteriosus", "Foramen ovale", "Urachus"],
         0, "The ductus venosus shunts approximately 50% of umbilical venous blood directly into the inferior (caudal) vena cava, bypassing the liver; postnatally, its fibrous remnant persists as the Ligamentum Venosum.",
         True, "Veterinary Embryology (ICAR PG PYQ)"),

        ("The adult anatomical remnant of the fetal 'Ductus Arteriosus' (which diverted pulmonary artery blood into the descending aorta) is the:",
         ["Ligamentum arteriosum", "Ligamentum teres hepatis", "Ligamentum venosum", "Fossa ovalis"],
         0, "The ductus arteriosus connects the pulmonary artery to the descending aorta in the fetus; functional closure occurs at birth upon initiation of respiration, fibrosing into the adult Ligamentum Arteriosum (failure of closure results in Patent Ductus Arteriosus / PDA).",
         True, "Veterinary Embryology (ICAR PG PYQ)"),

        ("The adult anatomical remnant of the embryonic Left Umbilical Vein, running in the free margin of the falciform ligament to the visceral surface of the liver, is the:",
         ["Ligamentum teres hepatis (Round ligament of the liver)", "Median umbilical ligament", "Ligamentum arteriosum", "Coronary ligament"],
         0, "The round ligament of the liver (Ligamentum teres hepatis) is the fibrous obliterated remnant of the embryonic left umbilical vein, transporting oxygenated blood from placenta to fetus during gestation.",
         True, "Veterinary Embryology (ICAR PG PYQ)"),

        ("During embryonic gastrulation, the epithelial lining of the gastrointestinal tract, liver parenchyma, gall bladder, pancreas, and respiratory tree develops from which primary germ layer?",
         ["Endoderm", "Ectoderm", "Mesoderm", "Neural crest"],
         0, "The endoderm forms the epithelial lining of the entire digestive canal (except stomodeum and proctodeum), the parenchyma of liver and pancreas, and the epithelial lining of the respiratory tract, urinary bladder, and urethra.",
         False, "Veterinary Embryology"),

        ("In male mammalian embryology, the primordial embryonic duct system that regresses under the influence of Anti-Müllerian Hormone (AMH / MIS) secreted by fetal Sertoli cells is the:",
         ["Paramesonephric duct (Müllerian duct)", "Mesonephric duct (Wolffian duct)", "Pronephric duct", "Metanephric duct"],
         0, "In male embryos, Sertoli cells produce AMH, causing regression of the paramesonephric (Müllerian) ducts (which would otherwise form uterine tubes, uterus, and cranial vagina), while testosterone supports Wolffian ducts to form epididymis and deferent ducts.",
         True, "Veterinary Embryology (ICAR PG PYQ)")
    ]
    return qs
