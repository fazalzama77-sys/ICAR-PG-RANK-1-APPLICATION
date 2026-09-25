# scripts/anat_mod5_avian.py
# Module 5: Avian Anatomy (15 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit I (Sub-subject 13.1)

def get_module5_questions():
    qs = [
        # 1-7: Avian Osteology and Myology
        ("In the domestic fowl (Gallus domesticus), the fusion of the second to fifth thoracic vertebrae into a rigid dorsal bony unit to stabilize the trunk during flight is called the:",
         ["Notarium (Os dorsale)", "Synsacrum", "Pygostyle", "Furcula"],
         0, "The notarium (os dorsale) is formed by the fusion of thoracic vertebrae T2 to T5 in the chicken, providing a rigid anchor for the thoracic cage and wing action, separated from the synsacrum by a single mobile thoracic vertebra (T6).",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("The 'Synsacrum' of birds is a rigid skeletal complex formed by the extensive fusion of which vertebral regions with the pelvic ilium?",
         ["The last thoracic (T7), all lumbar, all sacral, and the first few caudal vertebrae", "Sacral vertebrae alone", "Cervical and thoracic vertebrae", "Caudal coccygeal vertebrae only"],
         0, "The avian synsacrum is formed by the complete bony fusion of the last thoracic vertebra, all lumbar vertebrae, all primary sacral vertebrae, and the cranial caudal (coccygeal) vertebrae, fusing seamlessly with the ilium of the pelvis.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("The terminal fused caudal vertebrae in birds, shaped like a ploughshare and supporting the tail flight feathers (rectrices) and uropygial gland, is designated the:",
         ["Pygostyle", "Notarium", "Synsacrum", "Furcula"],
         0, "The pygostyle consists of the fusion of the last 4 to 6 caudal coccygeal vertebrae, supporting the tail retrices (flight steering feathers) and providing an anchor for tail musculature and the preen gland.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("The 'Triosseal Canal' (Foramen triosseum) of the avian pectoral girdle, through which the tendon of the Supracoracoideus muscle passes to act as a pulley for wing elevation, is formed by the junction of:",
         ["Scapula, Coracoid, and Clavicle", "Humerus, Radius, and Ulna", "Sternum, Ribs, and Coracoid", "Ilium, Ischium, and Pubis"],
         0, "The triosseal canal is bounded by the scapula, coracoid, and clavicle; the tendon of the deep supracoracoideus muscle traverses this canal over the shoulder joint to insert on the dorsal humerus, functioning as a pulley to raise the wing (upstroke).",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("The 'Furcula' (popularly known as the 'wishbone') in birds is formed by the ventral midline fusion of the:",
         ["Right and Left Clavicles (along with the interclavicle)", "Two Coracoid bones", "Two Scapulae", "Costal cartilages"],
         0, "The furcula is formed by the fusion of the left and right clavicles at their ventral ends, acting as an elastic spring during wing flapping to maintain spacing between shoulder joints.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("In domestic poultry, the massive breast muscle responsible for the powerful downstroke of the wing during flight is the:",
         ["Pectoralis muscle (Pectoralis major / Pectoralis superficialis)", "Supracoracoideus muscle", "Latissimus dorsi", "Biceps brachii"],
         0, "The Pectoralis (pectoralis major) originates from the ventral keel of the sternum and clavicle and inserts on the deltopectoral crest of the humerus, providing the main power for the downstroke; the Supracoracoideus elevates the wing.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        # 8-15: Avian Splanchnology (Respiratory, Digestive, Urogenital)
        ("In birds, the primary vocal organ responsible for sound production is situated at the bifurcation of the trachea into the primary bronchi and is termed the:",
         ["Syrinx", "Larynx (which lacks vocal cords)", "Pharynx", "Tracheal bulb"],
         0, "The syrinx is the avian voice organ located at the caudal end of the trachea at the bronchial bifurcation, containing vibrating tympanic membranes (membrana tympaniformis) and syringeal muscles; the cranial avian larynx lacks vocal cords.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("Avian lungs differ fundamentally from mammalian lungs because they are non-collapsible, constant-volume structures where gas exchange occurs in tubular:",
         ["Parabronchi (Air capillaries) with unidirectional airflow", "Terminal blind alveoli with tidal airflow", "Trabeculae carnae", "Pleural pouches"],
         0, "Avian lungs do not expand or collapse and lack dead-end alveoli; instead, inspired air flows unidirectionally through tertiary bronchi (parabronchi) and microscopic air capillaries that interlace with blood capillaries.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("How many total air sacs (sacci pneumatici) are typically present in the domestic fowl (Gallus domesticus)?",
         ["9 (1 single interclavicular, 2 cervical, 2 cranial thoracic, 2 caudal thoracic, and 2 abdominal)", "7", "8", "12"],
         0, "The domestic chicken has 9 air sacs: one unpaired Interclavicular air sac, and four paired air sacs (Cervical, Cranial Thoracic, Caudal Thoracic, and Abdominal); they act as bellows to drive unidirectional air through the lungs.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("The thick muscular grinding stomach (gizzard / ventriculus) of the domestic fowl is lined internally by a tough, wear-resistant, yellowish-green protective cuticle termed:",
         ["Koilin layer (composed of hardened protein secreted by mucosal tubular glands)", "Mucous gel layer", "Stratified squamous keratinized epithelium", "Enamel"],
         0, "The gizzard lumen is protected by a tough koilin layer, a keratin-like polysaccharide-protein complex secreted by deep mucosal tubular glands that hardens upon exposure to hydrochloric acid from the proventriculus.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("In the domestic fowl, the glandular stomach (Proventriculus) contains specialized mucosal cells that secrete both pepsinogen and hydrochloric acid, known as:",
         ["Oxynticopeptic cells", "Chief cells", "Parietal cells", "Enterochromaffin cells"],
         0, "Unlike mammals which have distinct parietal (HCl) and chief (pepsinogen) cells, avian proventricular glands possess a single composite cell type: the Oxynticopeptic cell, which performs both secretory functions.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("Prominent lymphoid aggregations located in the mucosal wall at the proximal origin (base) of each of the two ceca in the domestic fowl are designated:",
         ["Cecal tonsils", "Peyer's patches", "Bursa of Fabricius", "Harderian glands"],
         0, "The cecal tonsils are major gut-associated lymphoid tissue (GALT) structures located at the ileocecal junctions at the proximal neck of both ceca, mounting mucosal immune responses against enteric pathogens.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("The dorsal diverticulum of the cloacal proctodeum in young birds that serves as the primary site of B lymphocyte differentiation and lymphopoiesis is the:",
         ["Bursa of Fabricius (Cloacal bursa)", "Thymus", "Cecal tonsil", "Harderian gland"],
         0, "The Bursa of Fabricius is a dorsal diverticulum opening into the proctodeum of the cloaca; it is the unique primary lymphoid organ where B-cell maturation and immunoglobulin gene conversion occur in young birds, undergoing involution at sexual maturity.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("In the domestic hen, the segment of the functional left oviduct where the thick and thin albumen (egg white) is synthesized and secreted over approximately 3 hours is the:",
         ["Magnum", "Infundibulum", "Isthmus", "Uterus (Shell gland)"],
         0, "The magnum is the longest and most glandular segment of the avian oviduct (approx. 33 cm), densely lined with tubular glands secreting ovalbumin, conalbumin, ovomucoid, and lysozyme around the vitelline membrane of the descending yolk.",
         True, "Avian Anatomy (ICAR PG PYQ)"),

        ("In birds, the excretory system is characteristically devoid of which two anatomical structures that are otherwise universal in domestic mammals?",
         ["Renal pelvis and Urinary bladder", "Glomeruli and Proximal tubules", "Ureters and Collecting ducts", "Renal cortex and Medulla"],
         0, "Birds lack both a renal pelvis and a urinary bladder; ureters transport a semi-solid paste of uric acid directly from the three-lobed kidneys to empty into the urodeum of the cloaca, minimizing weight for flight and conserving water.",
         True, "Avian Anatomy (ICAR PG PYQ)")
    ]
    return qs
