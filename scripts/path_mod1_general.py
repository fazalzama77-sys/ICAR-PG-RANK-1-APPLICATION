# scripts/path_mod1_general.py
# Module 1: General Pathology & Cell Injury (80 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module1_questions():
    qs = [
        # 1-10: Cellular injury, swelling, degeneration, lipid accumulation
        ("The earliest morphologically detectable manifestation of almost all forms of cell injury is:",
         ["Cellular swelling (cloudy swelling)", "Pyknosis", "Karyolysis", "Fatty change"],
         0, "Cellular swelling (hydropic change/cloudy swelling) results from failure of the ATP-dependent Na+/K+ pump in the plasma membrane, causing intracellular sodium and water accumulation. It is completely reversible upon removal of the injurious stimulus.",
         True, "Cell Injury & Degeneration"),

        ("Ballooning degeneration is a specific form of cellular swelling characterized by marked cytoplasmic vacuolation and cell lysis, classically seen in the stratum spinosum during infection with:",
         ["Poxviruses and Aphthoviruses (FMD)", "Pestiviruses (BVD)", "Parvoviruses", "Rhabdoviruses (Rabies)"],
         0, "Ballooning degeneration is typical of epitheliotropic viral infections such as Poxviruses (e.g. Swinepox, Sheeppox) and Aphthovirus (FMD), causing severe hydropic swelling of keratinocytes leading to vesicle formation.",
         True, "Cell Injury & Degeneration"),

        ("In feline hepatic lipidosis, the primary intracellular accumulated substance within hepatocytes is:",
         ["Triglycerides", "Cholesterol esters", "Glycogen", "Lipofuscin"],
         0, "Hepatic lipidosis (fatty liver) in anorectic obese cats results from excessive mobilization of free fatty acids from adipose tissue, which are re-esterified into neutral triglycerides exceeding the liver's capacity for VLDL synthesis.",
         True, "Cell Injury & Degeneration"),

        ("To demonstrate neutral lipids in histological sections without dissolving them during routine paraffin embedding, the recommended tissue preparation and staining method is:",
         ["Frozen section stained with Oil Red O or Sudan Black B", "Formalin-fixed paraffin section stained with Periodic Acid-Schiff (PAS)", "Carnoy's fixed section stained with Hematoxylin & Eosin", "Bouin's fixed section stained with Masson's Trichrome"],
         0, "Routine clearing agents (xylene) dissolve neutral lipids from tissue sections. Demonstration of triglycerides requires frozen sections (cryostat) stained with lysochrome dyes like Oil Red O or Sudan Black B.",
         True, "Histopathological Techniques"),

        ("Steroid-induced hepatopathy in dogs receiving exogenous corticosteroids or suffering from Cushing's disease is histologically characterized by excessive hepatocellular accumulation of:",
         ["Glycogen", "Amyloid", "Hemosiderin", "Ceroid"],
         0, "Glucocorticoids induce hepatic glycogen synthetase, leading to massive cytoplasmic storage of glycogen. This produces pale, swollen hepatocytes with reticulated cytoplasm, stainable with PAS and digested by diastase.",
         True, "Cell Injury & Degeneration"),

        ("Which of the following biochemical defects is the primary cause of 'Fat Cow Syndrome' (severe bovine ketosis / fatty liver)?",
         ["Imbalance between fat mobilization from adipose reserves and hepatic VLDL secretion", "Excessive production of ketone bodies by the rumen wall", "Congenital deficiency of apolipoprotein B-100", "Dietary deficiency of methionine alone"],
         0, "In high-yielding dairy cows during early lactation, negative energy balance triggers massive lipolysis. Non-esterified fatty acids (NEFAs) flood hepatocytes, where triglyceride synthesis surpasses the secretion rate of very low-density lipoproteins (VLDL).",
         True, "Metabolic Pathology"),

        ("Amyloid deposits in tissues exhibit a characteristic optical property under polarized light microscopy when stained with Congo Red, which is:",
         ["Apple-green birefringence", "Golden-yellow dichroism", "Metachromatic purple fluorescence", "Red-orange autofluorescence"],
         0, "Congo Red intercalates between the parallel beta-pleated sheet fibrillar structure of amyloid. When viewed under cross-polarized light, this unique alignment produces pathognomonic apple-green birefringence.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("The predominant biochemical precursor of reactive systemic amyloidosis (AA amyloid) associated with chronic inflammatory and suppurative diseases in domestic animals is:",
         ["Serum Amyloid A (SAA) synthesized by hepatocytes", "Immunoglobulin light chains synthesized by plasma cells", "Transthyretin synthesized by the choroid plexus", "Apolipoprotein A-I"],
         0, "Amyloid A (AA) protein is derived from Serum Amyloid A (SAA), an acute-phase apolipoprotein synthesized by hepatocytes under the stimulus of pro-inflammatory cytokines (IL-1, IL-6, TNF-alpha) during chronic infections like tuberculosis or chronic mastitis.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("In 'sago spleen' (follicular amyloidosis), amyloid deposits are anatomically restricted to:",
         ["Splenic Malpighian corpuscles (lymphoid follicles)", "Red pulp sinuses and cords of Billroth", "Trabeculae and central splenic arterioles only", "Splenic capsule and subcapsular sinus"],
         0, "In the sago spleen pattern of amyloidosis, amyloid fibrils are selectively deposited in the walls of the follicular central arterioles and within the germinal centers of Malpighian corpuscles, resembling boiled sago grains.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Primary (AL) amyloidosis in dogs and horses is most commonly associated with which underlying neoplasm?",
         ["Multiple myeloma (plasma cell myeloma)", "Lymphoma", "Hemangiosarcoma", "Squamous cell carcinoma"],
         0, "AL amyloid (Amyloid Light chain) is formed from monoclonal immunoglobulin light chains (Bence-Jones proteins) secreted by neoplastic plasma cell proliferations, particularly in multiple myeloma.",
         False, "General Pathology"),

        # 11-20: Hyaline change, Zenker's, Necrosis types
        ("Russell bodies observed inside plasma cells during chronic antigenic stimulation represent intra-cytoplasmic accumulations of:",
         ["Synthesized immunoglobulins in distended rough endoplasmic reticulum cisternae", "Degenerated mitochondrial remnants", "Aggregated actin filaments", "Phagocytosed bacterial fragments"],
         0, "Russell bodies are round, glassy, eosinophilic inclusions within plasma cells (Mott cells) caused by the accumulation of newly synthesized immunoglobulins within dilated cisternae of the rough endoplasmic reticulum.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Zenker's necrosis (waxy hyaline degeneration) is a specific type of coagulative necrosis selectively affecting:",
         ["Striated skeletal muscle fibers", "Hepatocytes of centrilobular zones", "Proximal convoluted renal tubular epithelium", "Cardiac Purkinje fibers"],
         0, "Zenker's degeneration/necrosis specifically affects striated skeletal muscles (e.g. in nutritional muscular dystrophy / White Muscle Disease due to Vitamin E and Selenium deficiency, and in equine azoturia / exertional rhabdomyolysis).",
         True, "General Pathology (ICAR PG PYQ)"),

        ("The definitive microscopic hallmark distinguishing coagulative necrosis from liquefactive necrosis is:",
         ["Preservation of basic cellular outline and tissue architectural ghost shadows", "Complete enzymatic dissolution of all cell margins", "Presence of abundant caseous debris", "Infiltration by Langhans giant cells"],
         0, "Coagulative necrosis involves rapid denaturation of both structural proteins and lysosomal enzymes, which blocks proteolysis and preserves the tombstones/ghost outlines of cells for several days.",
         True, "General Pathology"),

        ("Ischemic infarction in solid parenchymal organs with end-arterial circulation, such as the renal cortex, heart, or spleen, results primarily in:",
         ["Coagulative necrosis", "Liquefactive necrosis", "Fibrinoid necrosis", "Caseous necrosis"],
         0, "Sudden arterial occlusion in organs with end-arteries produces ischemic coagulative necrosis, manifesting grossly as pale, wedge-shaped infarcts with their base along the organ capsule.",
         True, "Hemodynamic Pathology"),

        ("Focal infarction or ischemic injury within the Central Nervous System (brain and spinal cord) classically manifests as which type of necrosis?",
         ["Liquefactive necrosis (malacia)", "Coagulative necrosis", "Caseous necrosis", "Fat necrosis"],
         0, "The mammalian CNS has high lipid content and negligible connective tissue stroma; upon ischemia, lysosomal hydrolases from microglial cells and astrocytes rapidly digest necrotic tissue, causing encephalomalacia / myelomalacia (liquefactive necrosis).",
         True, "General Pathology (ICAR PG PYQ)"),

        ("The phagocytic scavenger cells responsible for clearing necrotic lipid-rich debris in brain liquefactive necrosis (malacia) are termed:",
         ["Gitter cells (lipophages / foamy microglia)", "Langhans cells", "Kupffer cells", "Ito cells"],
         0, "Gitter cells are transformed, activated microglial macrophages packed with engulfed lipid droplets and myelin breakdown products, imparting a foamy, vacuolated appearance.",
         True, "Neuropathology"),

        ("Caseous necrosis is pathognomonic for which of the following chronic veterinary infections?",
         ["Mycobacterium bovis (Bovine Tuberculosis)", "Bacillus anthracis (Anthrax)", "Clostridium chauvoei (Blackleg)", "Streptococcus equi (Strangles)"],
         0, "Caseous necrosis (dry, friable, cheese-like) is characteristic of granulomatous infections, particularly tuberculosis (M. bovis) and caseous lymphadenitis (C. pseudotuberculosis), where lipid-rich bacterial cell walls resist complete enzymatic liquefaction.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Enzymatic fat necrosis around the pancreas and in the omentum during acute pancreatitis results from the hydrolytic release of:",
         ["Pancreatic lipase and colipase", "Amylase", "Pepsin", "Enterokinase"],
         0, "Premature activation of pancreatic lipase inside the parenchyma causes hydrolysis of neutral triglycerides into free fatty acids, which combine with extracellular calcium to form chalky white calcium soaps (saponification).",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Fibrinoid necrosis is classically seen in blood vessel walls during which pathological condition?",
         ["Type III hypersensitivity reactions and immune complex vasculitis", "Severe Vitamin C deficiency (Scurvy)", "Primary amyloidosis", "Chronic venous congestion"],
         0, "Fibrinoid necrosis occurs when antigen-antibody complexes are deposited in arterial walls together with extravasated fibrinogen, forming a bright pink, amorphous, smudgy band in vascular tunica media.",
         True, "General Pathology"),

        ("Apoptosis differs fundamentally from necrosis in domestic animals because apoptosis:",
         ["Involves single cells without eliciting an acute inflammatory reaction", "Causes widespread plasma membrane rupture and cellular leakage", "Always causes marked neutrophilic infiltration", "Is exclusively a pathological event"],
         0, "Apoptosis is programmed single-cell death characterized by cell shrinkage, chromatin condensation, membrane blebbing, and formation of apoptotic bodies phagocytosed by macrophages without inciting inflammation.",
         True, "General Pathology (ICAR PG PYQ)"),

        # 21-30: Apoptosis, post-mortem, calcification
        ("The key executioner (effector) caspase responsible for cleaving vital cellular substrates during the final execution phase of apoptosis is:",
         ["Caspase-3", "Caspase-8", "Caspase-9", "Caspase-1"],
         0, "Caspases-3, -6, and -7 are executioner caspases. Caspase-3 is the central executioner activated by both the intrinsic (mitochondrial/caspase-9) and extrinsic (death receptor/caspase-8) pathways.",
         True, "Cellular Pathology"),

        ("Which of the following proteins serves as a critical anti-apoptotic guardian residing in the outer mitochondrial membrane?",
         ["Bcl-2", "Bax", "Bak", "Bid"],
         0, "Bcl-2 and Bcl-xL are anti-apoptotic proteins that prevent mitochondrial permeability transition and cytochrome c release, whereas Bax and Bak are pro-apoptotic pore formers.",
         False, "Cellular Pathology"),

        ("The biochemical basis of rigor mortis after somatic death is the progressive post-mortem depletion of:",
         ["Adenosine triphosphate (ATP)", "Intracellular calcium", "Lactic acid", "Creatine phosphate"],
         0, "Rigor mortis occurs because actin-myosin cross-bridge dissociation in skeletal and cardiac muscle requires binding of ATP. When ATP is depleted, actin and myosin remain permanently locked together.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Rigor mortis in domestic animals classically commences first in:",
         ["Myocardium of the heart", "Diaphragm", "Quadriceps femoris", "Gastrocnemius"],
         0, "Rigor mortis begins approximately 1-2 hours post-mortem in the cardiac muscle, followed by the masseters and cervical muscles, before progressing caudally to trunk and limb muscles.",
         True, "General Pathology"),

        ("Post-mortem rigor mortis is characteristically incomplete or entirely absent in carcasses of cattle dying from:",
         ["Anthrax", "Blackleg", "Tetanus", "Strychnine poisoning"],
         0, "In Anthrax, severe terminal bacteremia and toxin-mediated vascular collapse cause profound anoxia and rapid post-mortem blood liquefaction, resulting in complete absence or rapid disappearance of rigor mortis.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("The greenish-black discoloration of abdominal viscera (liver, intestines) observed during post-mortem autolysis is termed:",
         ["Pseudomelanosis", "Anthracosis", "Melanosis maculosa", "Ceroidosis"],
         0, "Pseudomelanosis is a post-mortem change caused by hydrogen sulfide (H2S) produced by putrefactive intestinal bacteria reacting with iron from lysed erythrocytes, forming black iron sulfide (FeS).",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Which diagnostic feature allows a veterinary pathologist to distinguish ante-mortem bloat (ruminal tympany) from post-mortem tympany?",
         ["Presence of a sharp 'bloat line' in the thoracic esophagus", "Presence of froth in the rumen", "Dark red color of the rumen wall", "Distension of the left paralumbar fossa"],
         0, "The 'bloat line' is characterized by sharp pallor and ischemia of the caudal thoracic esophagus due to increased intrathoracic pressure, contrasting sharply with congestion and hemorrhage in the cervical esophagus. It is absent in post-mortem bloat.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Dystrophic calcification occurs under which of the following metabolic states?",
         ["Normal serum calcium and phosphate levels in dead or degenerating tissues", "Elevated serum calcium and normal phosphate levels", "Severe hyperparathyroidism with normal tissues", "Excessive dietary intake of Vitamin D3"],
         0, "Dystrophic calcification occurs locally in necrotic, dying, or degenerate tissues (e.g. caseous TB granulomas, dead parasites) despite completely normal circulating levels of serum calcium and phosphate.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Metastatic calcification in cattle and horses typically affects which specific group of tissues?",
         ["Alveolar septa of lungs, gastric mucosa, and renal tubular basement membranes", "Liver parenchyma and spleen red pulp", "Skeletal muscle fibers and articular cartilage", "Skin epidermis and hooves"],
         0, "Metastatic calcification occurs in viable tissues during hypercalcemia. It preferentially affects tissues that secrete acid (stomach acid, renal tubular acid) or lose CO2 (lungs), leaving an internal alkaline milieu favored by calcium phosphate precipitation.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Enzootic calcinosis in grazing cattle (Manchester wasting disease) is caused by chronic ingestion of plants containing Vitamin D-like glycosides, such as:",
         ["Solanum malacoxylon (Solanum glaucophyllum) and Cestrum diurnum", "Lantana camara", "Pteridium aquilinum", "Senecio jacobaea"],
         0, "Solanum malacoxylon and Cestrum diurnum contain 1,25-dihydroxycholecalciferol glycosides that cause hypercalcemia, hyperphosphatemia, and widespread metastatic mineralization of the aorta, heart, and lungs.",
         True, "Toxicologic Pathology"),

        # 31-40: Special staining, calcification, pigmentations
        ("The classical histological histochemical stain used to identify calcium deposits by silver reduction, producing a dense black precipitate, is:",
         ["Von Kossa stain", "Masson's trichrome", "Prussian blue stain", "Alcian blue stain"],
         0, "Von Kossa's method uses silver nitrate, which reacts with phosphate and carbonate ions in calcium salts; exposure to UV light or chemical reduction produces opaque black metallic silver deposits.",
         True, "Histopathological Techniques"),

        ("Dry gangrene in domestic animals is characterized pathologically by:",
         ["Arterial occlusion in extremities leading to ischemic mummification with a clear line of demarcation", "Rapid liquefactive necrosis with saprophytic putrefaction and foul odor", "Extensive gas bubble formation inside crepitating muscle", "Abundant purulent exudate dripping from the lesion"],
         0, "Dry gangrene occurs when arterial supply to an extremity (ear tips, tail, digits) is blocked while venous drainage is relatively intact, leading to dessication, shrinkage, black discoloration, and a sharp boundary of demarcation.",
         True, "General Pathology"),

        ("Ergot poisoning (Claviceps purpurea) in grazing cattle produces dry gangrene of the tail tip, ears, and hooves through which mechanism?",
         ["Direct vasoconstriction of peripheral arterioles and endothelial injury caused by ergot alkaloids", "Suppression of bone marrow megakaryocytes", "Hypersecretion of parathyroid hormone", "Bacterial invasion of digital corium"],
         0, "Ergotamine and related ergot alkaloids cause potent alpha-adrenergic peripheral vasoconstriction and direct vascular endothelial damage, leading to ischemia, stasis, thrombosis, and dry gangrene of extremities.",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("Congenital melanosis (Melanosis maculosa) in calves is characterized by flat, dark melanin patches on organs such as the lungs, aorta, and meninges, and its clinical significance is:",
         ["Completely benign incidental finding with normal organ architecture and function", "Highly aggressive premalignant condition requiring euthanasia", "Always accompanied by severe cardiac insufficiency", "Associated with lethal albinism"],
         0, "Congenital melanosis is a harmless, benign embryonic heterotopia where aberrant melanocytes deposit pigment in connective tissues (meninges, aorta, pleura, liver) without disrupting organ histology or function.",
         True, "General Pathology"),

        ("The histochemical technique of choice for distinguishing melanin pigment from other dark pigments (such as formalin pigment or lipofuscin) is:",
         ["Fontana-Masson silver reduction stain and bleachability with hydrogen peroxide", "Pearl's Prussian blue stain", "Von Kossa silver nitrate stain", "Oil Red O stain"],
         0, "Melanin reduces ammoniacal silver nitrate to metallic silver (argentaffin reaction) in the Fontana-Masson method and is decolorized (bleached) by prolonged exposure to hydrogen peroxide or potassium permanganate.",
         False, "Histopathological Techniques"),

        ("Hemosiderin, the intracellular storage complex of ferric iron, is demonstrated histochemically as a brilliant Prussian blue precipitate using:",
         ["Perls' Prussian blue reaction (potassium ferrocyanide + dilute HCl)", "Periodic Acid-Schiff (PAS) reaction", "Alizarin Red S", "Sudan IV"],
         0, "Perls' reaction uses dilute hydrochloric acid to liberate ferric (Fe3+) ions from protein complexes, which then react with potassium ferrocyanide to form insoluble ferric ferrocyanide (Prussian blue).",
         True, "General Pathology (ICAR PG PYQ)"),

        ("'Heart failure cells' found in the pulmonary alveolar spaces during chronic passive congestion of the lungs are:",
         ["Alveolar macrophages packed with phagocytosed hemosiderin", "Degenerated Type II pneumocytes", "Extravasated cardiac Purkinje fibers", "Hypertrophied bronchial myofibroblasts"],
         0, "In left-sided heart failure, chronic venous hypertension causes diapedesis of erythrocytes into pulmonary alveoli; alveolar macrophages phagocytose lysed RBCs and accumulate brown hemosiderin granules, becoming 'heart failure cells'.",
         True, "Cardiopulmonary Pathology (ICAR PG PYQ)"),

        ("In pre-hepatic (hemolytic) jaundice in dogs with immune-mediated hemolytic anemia (IMHA), the circulating bilirubin is predominantly:",
         ["Unconjugated (indirect-reacting) and bound to serum albumin", "Conjugated (direct-reacting) with glucuronic acid", "Water-soluble and readily excreted in urine as bilirubinuria", "Bound to haptoglobin"],
         0, "Massive intravascular or extravascular hemolysis produces large amounts of unconjugated (indirect) bilirubin, which is lipid-soluble, bound to albumin, cannot pass the renal glomerulus, and gives an indirect van den Bergh reaction.",
         True, "Clinical Pathology"),

        ("Lipofuscin ('wear-and-tear' or brown atrophy pigment) accumulates primarily in tertiary lysosomes of post-mitotic cells and represents:",
         ["Incompletely digested, oxidized polyunsaturated fatty acid-protein complexes", "Unused glycogen polymers", "Excessive breakdown of hemoglobin", "Phagocytosed melanin particles"],
         0, "Lipofuscin is an insoluble, yellowish-brown granular pigment derived from free-radical-induced peroxidation of membrane polyunsaturated lipids in aged or chronically cachectic animals, especially in cardiac myocytes and neurons.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Congenital erythropoietic porphyria ('Pink tooth') in cattle and pigs is caused by an inherited deficiency of which heme biosynthetic enzyme?",
         ["Uroporphyrinogen III synthase", "Ferrochelatase", "ALA dehydratase", "Porphobilinogen deaminase"],
         0, "Deficiency of uroporphyrinogen III synthase leads to accumulation of photoactive uroporphyrin I and coproporphyrin I, causing reddish-brown discoloration of teeth and bones (fluorescing pink under UV light) and severe cutaneous photosensitization.",
         True, "Metabolic Pathology (ICAR PG PYQ)"),

        # 41-50: Pigments, hemodynamics, edema, hyperemia, congestion
        ("The distinctive dark brown to black crystalline pigment formed artifacts in tissues when blood-rich organs are fixed in non-buffered acidic formalin (pH < 5.6) is:",
         ["Formalin pigment (acid hematin)", "Malarial pigment (hemozoin)", "Hemosiderin", "Lipofuscin"],
         0, "Acid formalin reacts with hemoglobin to form acid hematin (formalin pigment), an amorphous brown-black birefringence-negative artifact that can be removed prior to staining by treatment with alcoholic ammonium hydroxide.",
         False, "Histopathological Techniques"),

        ("The fundamental hemodynamic difference between active hyperemia and passive congestion is that hyperemia:",
         ["Is an active process mediated by arteriolar dilation with increased oxygenated arterial inflow", "Results from impaired venous outflow with accumulation of deoxygenated blood", "Always causes severe centrilobular hepatic necrosis", "Is invariably associated with thrombosis"],
         0, "Hyperemia is an active physiological or pathological process resulting from arteriolar vasodilation (e.g. during exercise, digestion, or acute inflammation), whereas congestion is a passive impairment of venous drainage.",
         True, "Hemodynamic Pathology"),

        ("The classical gross pathological appearance of 'nutmeg liver' is produced by:",
         ["Chronic passive congestion of the liver resulting from right-sided congestive heart failure", "Diffuse hepatocellular amyloidosis", "Acute infectious canine hepatitis", "Severe biliary cirrhosis"],
         0, "In right-sided heart failure, backward venous pressure causes stasis and coagulative necrosis in centrilobular hepatocytes (dark red areas) contrasted against periportal viable hepatocytes with fatty degeneration (yellow-tan areas), resembling a cut nutmeg.",
         True, "Cardiovascular Pathology (ICAR PG PYQ)"),

        ("Which alteration in Starling's capillary forces is the primary mechanism causing 'bottle jaw' (submandibular edema) in sheep with severe Haemonchosis?",
         ["Decreased plasma colloid oncotic pressure due to hypoalbuminemia", "Increased capillary hydrostatic pressure from right heart failure", "Lymphatic vessel obstruction by adult nematodes", "Increased vascular permeability from histamine release"],
         0, "Haemonchus contortus is an active blood-feeder in the abomasum causing severe blood loss. The resulting hypoalbuminemia drastically lowers plasma colloid oncotic pressure, leading to fluid extravasation into loose dependent intermandibular tissues ('bottle jaw').",
         True, "Hemodynamic Pathology (ICAR PG PYQ)"),

        ("Minute, pinpoint hemorrhages measuring 1 to 2 mm in diameter on skin, mucous membranes, or serosal surfaces are classified as:",
         ["Petechiae", "Purpura", "Ecchymoses", "Hematomas"],
         0, "Petechiae are pinpoint hemorrhages (1-2 mm) usually associated with thrombocytopenia, platelet function defects, or acute endothelial damage. Purpura measures 3-5 mm, and ecchymoses measure >1 cm.",
         True, "Hemodynamic Pathology"),

        ("The three primary components of Virchow's Triad governing the pathogenesis of intravascular thrombosis are:",
         ["Endothelial injury, stasis or turbulent blood flow, and blood hypercoagulability", "Hypercalcemia, hyperkalemia, and acidosis", "Hypertension, hypothermia, and hypoglycemia", "Leukopenia, thrombocytopenia, and anemia"],
         0, "Virchow's Triad comprises: (1) Endothelial injury (most critical), (2) Alterations in normal laminar blood flow (stasis or turbulence), and (3) Hypercoagulability of the blood.",
         True, "Hemodynamic Pathology (ICAR PG PYQ)"),

        ("Microscopically, true ante-mortem arterial thrombi are distinguished by alternating pale laminations of platelets/fibrin and dark layers of erythrocytes, known as:",
         ["Lines of Zahn", "Aschoff bodies", "Lines of Russell", "Zenker's bands"],
         0, "Lines of Zahn represent alternating laminar deposits of pale platelets mixed with fibrin and darker layers of trapped erythrocytes, confirming that the thrombus formed in a flowing blood stream before death.",
         True, "Hemodynamic Pathology (ICAR PG PYQ)"),

        ("A post-mortem blood clot is accurately distinguished from an ante-mortem intravascular thrombus by being:",
         ["Elastic, moist, easily removable from the vessel lumen, and exhibiting a 'chicken-fat' layer", "Dry, friable, granular, and firmly adherent to the damaged endothelial wall", "Layered with distinct Lines of Zahn", "Composed entirely of cross-linked collagen fibrils"],
         0, "Post-mortem clots are gelatinous, shiny, elastic, take the shape of the vessel, and do not adhere to the vascular wall. In slow death, sedimentation produces a dependent red-currant jelly layer and a superficial yellow 'chicken-fat' plasma clot.",
         True, "Hemodynamic Pathology (ICAR PG PYQ)"),

        ("Fibrocartilaginous embolic myelopathy (FCEM) in dogs originates from the embolization of which tissue into spinal cord vasculature?",
         ["Nucleus pulposus of degenerate intervertebral discs", "Bone marrow fat after femoral fracture", "Bacterial vegetative valvular endocarditis", "Metastatic osteosarcoma"],
         0, "In FCEM, fragments of the proteoglycan-rich gelatinous nucleus pulposus of an intervertebral disc herniate into adjacent vertebral venules or spinal arterioles, causing acute ischemic spinal cord infarction.",
         False, "Neuropathology"),

        ("In domestic animals, septic shock triggered by Gram-negative septicemia (such as E. coli or Salmonella) is fundamentally driven by the interaction of which bacterial molecule with host macrophages?",
         ["Lipopolysaccharide (LPS, specifically Lipid A)", "Peptidoglycan monomer", "Bacterial flagellin", "Dipicolinic acid"],
         0, "Lipid A of Gram-negative bacterial lipopolysaccharide (LPS/endotoxin) binds TLR-4 on monocytes and macrophages, triggering massive systemic outpouring of pro-inflammatory cytokines (TNF-alpha, IL-1, IL-6, NO) leading to widespread vasodilation and shock.",
         True, "Hemodynamic Pathology (ICAR PG PYQ)"),

        # 51-60: Shock, vascular events of inflammation, leukocyte extravasation
        ("Disseminated Intravascular Coagulation (DIC) represents a severe consumptive coagulopathy characterized paradoxical combination of:",
         ["Widespread microvascular thrombosis alongside spontaneous systemic hemorrhages", "Isolated venous thrombosis without any bleeding tendency", "Massive neutrophilia with decreased clotting times", "Excessive production of albumin by the liver"],
         0, "In DIC, uncontrolled systemic activation of thrombin generates microthrombi throughout the microcirculation, which exhausts platelets, fibrinogen, and clotting factors (consumptive coagulopathy), provoking uncontrollable multi-organ hemorrhage.",
         True, "Hemodynamic Pathology (ICAR PG PYQ)"),

        ("The classic 'triple response of Lewis' observed in acute inflammatory vascular responses consists of:",
         ["Red line (local vasodilation), Flare (surrounding arteriolar dilation), and Wheal (local edema)", "Vasoconstriction, thrombosis, and necrosis", "Pallor, cyanosis, and gangrene", "Ulceration, scarring, and fibrosis"],
         0, "Lewis described the triple response: (1) Flush/red line from local capillary dilation, (2) Flare from axon reflex-mediated arteriolar dilation, and (3) Wheal from increased vascular permeability causing focal edema.",
         False, "Inflammation & Repair"),

        ("The immediate, transient increase in vascular permeability in acute inflammation (lasting 15 to 30 minutes) is primarily mediated by the action of histamine on:",
         ["Endothelial cells of post-capillary venules causing cell contraction and intercellular gaps", "Arteriolar smooth muscle cells causing constriction", "Capillary pericytes causing proliferation", "Large muscular arteries causing dissection"],
         0, "Histamine acts selectively on H1 receptors of post-capillary venular endothelial cells, causing rapid phosphorylation of cytoskeletal proteins, endothelial contraction, and separation of intercellular junctions.",
         True, "Inflammation & Repair"),

        ("During the leukocyte extravasation cascade in acute inflammation, the initial low-affinity rolling of leukocytes along activated endothelium is mediated by which family of adhesion molecules?",
         ["Selectins (L-selectin, E-selectin, P-selectin)", "Integrins (LFA-1, Mac-1)", "Immunoglobulin superfamily (ICAM-1, VCAM-1)", "Cadherins (E-cadherin)"],
         0, "The fast, reversible rolling interaction of neutrophils along the vessel wall is mediated by selectins (P-selectin from Weibel-Palade bodies, E-selectin induced by TNF/IL-1, and L-selectin on leukocytes) binding sialylated oligosaccharide ligands.",
         True, "Inflammation & Repair (ICAR PG PYQ)"),

        ("Bovine Leukocyte Adhesion Deficiency (BLAD) in Holstein calves is an inherited autosomal recessive disorder caused by a mutation in the gene encoding:",
         ["CD18 (the common beta-2 integrin subunit)", "CD4", "P-selectin glycoprotein ligand-1 (PSGL-1)", "ICAM-1"],
         0, "BLAD is caused by a point mutation in the CD18 gene, preventing the formation of functional heterodimeric beta-2 integrins (LFA-1, Mac-1). Neutrophils cannot firmly adhere to or transmigrate across the endothelium, resulting in extreme leukocytosis and fatal recurrent bacterial infections.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Transmigration (diapedesis) of leukocytes through endothelial intercellular junctions into perivascular tissue is facilitated by which homophilic adhesion molecule?",
         ["PECAM-1 (CD31)", "L-selectin", "Fibronectin", "Vimentin"],
         0, "Platelet Endothelial Cell Adhesion Molecule-1 (PECAM-1 / CD31) is expressed on both the transmigrating leukocyte and endothelial cell intercellular junctions, mediating the mechanical squeezing across the vessel wall.",
         False, "Inflammation & Repair"),

        ("Which of the following endogenous chemical mediators serves as the most potent chemoattractant for neutrophils in acute inflammation?",
         ["Complement component C5a and Leukotriene B4 (LTB4)", "Prostaglandin E2 (PGE2)", "Histamine", "Bradykinin"],
         0, "C5a (cleavage product of complement activation) and LTB4 (lipoxygenase metabolite of arachidonic acid) are the most potent endogenous chemotactic factors directing neutrophil migration along a concentration gradient.",
         True, "Inflammation & Repair (ICAR PG PYQ)"),

        ("The primary antimicrobial killing mechanism utilized by neutrophils during the 'respiratory burst' involves the rapid generation of hypochlorous acid (HOCl) catalyzed by which enzyme?",
         ["Myeloperoxidase (MPO)", "Superoxide dismutase (SOD)", "Catalase", "Glutathione peroxidase"],
         0, "During phagocytosis, NADPH oxidase produces superoxide (O2-), which dismutates to hydrogen peroxide (H2O2). In azurophilic granules, Myeloperoxidase (MPO) uses H2O2 to oxidize chloride (Cl-) into highly bactericidal hypochlorous acid (HOCl).",
         True, "Inflammation & Repair (ICAR PG PYQ)"),

        ("Chronic Granulomatous Disease (CGD) is a congenital immunodeficiency characterized by recurrent suppurative infections due to a genetic defect in:",
         ["NADPH oxidase complex subunits (phagocyte oxidase)", "Myeloperoxidase", "Lysozyme", "Lactoferrin"],
         0, "Defects in NADPH oxidase prevent generation of reactive oxygen species (superoxide, H2O2) during the respiratory burst. Neutrophils can phagocytose catalase-positive bacteria (e.g. Staph aureus) but cannot kill them, resulting in chronic granuloma formation.",
         False, "General Pathology"),

        ("The Chédiak-Higashi syndrome occurring in Hereford cattle, Persian cats, and Aleutian mink is pathologically characterized by:",
         ["Abnormally giant lysosomal granules in neutrophils and partial oculocutaneous albinism", "Total absence of neutrophils in peripheral blood", "Hypersegmentation of neutrophil nuclei", "Excessive production of collagen in tissues"],
         0, "Chédiak-Higashi syndrome is an autosomal recessive disorder caused by a mutation in the LYST gene regulating lysosomal trafficking, resulting in giant, dysfunctional lysosomal granules in leukocytes, platelet storage defects (bleeding diathesis), and hypopigmentation.",
         True, "General Pathology (ICAR PG PYQ)"),

        # 61-70: Chemical mediators, exudate types, granulomatous inflammation
        ("The pyrogenic effect (fever induction) of cytokines IL-1 and TNF-alpha during acute systemic inflammation is mediated by stimulating the synthesis of which local lipid mediator in the preoptic area of the hypothalamus?",
         ["Prostaglandin E2 (PGE2)", "Prostacyclin (PGI2)", "Thromboxane A2 (TXA2)", "Leukotriene C4 (LTC4)"],
         0, "IL-1 and TNF-alpha act on the endothelial cells of the hypothalamic perivascular organum vasculosum laminae terminalis (OVLT) to induce Cyclooxygenase-2 (COX-2) and PGE2 synthesis, which resets the thermoregulatory set-point upward.",
         True, "Inflammation & Repair (ICAR PG PYQ)"),

        ("Aspirin and traditional Non-Steroidal Anti-Inflammatory Drugs (NSAIDs) reduce inflammatory swelling and pain primarily by inhibiting:",
         ["Cyclooxygenase (COX-1 and COX-2) enzymes", "5-Lipoxygenase (5-LOX)", "Phospholipase A2", "Histaminase"],
         0, "NSAIDs inhibit cyclooxygenase (COX) enzymes, preventing the conversion of arachidonic acid into prostaglandins (PGE2, PGF2-alpha) and thromboxanes.",
         True, "Inflammation & Repair"),

        ("In acute fibrinous pericarditis ('bread-and-butter pericardium') in cattle suffering from Traumatic Reticulopericarditis (TRP), the exudate consists primarily of:",
         ["A thick, tangled meshwork of fibrin strands coating the epicardium and parietal pericardium", "Clear, protein-poor transudate with low specific gravity", "Abundant mucinous fluid rich in hyaluronic acid", "Pure collections of eosinophils"],
         0, "Severe vascular permeability lets large fibrinogen molecules escape into the pericardial sac. Coagulation converts fibrinogen to fibrin, which forms shaggy, yellow-gray deposits between the visceral and parietal layers ('bread and butter').",
         True, "Systemic Pathology (ICAR PG PYQ)"),

        ("Diphtheritic (pseudomembranous) inflammation is characterized by a necrotic surface membrane composed of fibrin and necrotic epithelial cells that:",
         ["Adheres firmly to underlying eroded tissue, so that forced peeling leaves a bleeding ulcerated raw surface", "Sloughs off effortlessly without damaging the basement membrane", "Is composed exclusively of intact keratinized squamous scales", "Is readily digested by salivary amylase"],
         0, "In diphtheritic/pseudomembranous inflammation (e.g. Calf Diphtheria / necrotic laryngitis caused by Fusobacterium necrophorum), coagulation necrosis penetrates deep into the submucosa; mechanical removal tears capillaries, creating deep bleeding ulcers.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Epithelioid cells, the diagnostic cellular hallmark of chronic granulomatous inflammation, are transformed and activated derivatives of:",
         ["Monocyte-derived tissue macrophages (histiocytes)", "Endothelial cells", "Basal epidermal keratinocytes", "Fibroblasts"],
         0, "Under prolonged exposure to IFN-gamma secreted by Th1 lymphocytes, tissue macrophages transform into epithelioid cells, acquiring abundant pale eosinophilic cytoplasm, indistinct borders, and an elongated 'slipper-shaped' vesicular nucleus.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Langhans-type multinucleated giant cells characteristic of tuberculous granulomas possess nuclei arranged in a:",
         ["Horseshoe or peripheral wreath-like pattern along the cytoplasmic margins", "Haphazard, disorganized clump in the center of the cell", "Perfect single central circle surrounded by lipids", "Linear array resembling a train track"],
         0, "Langhans giant cells form by the fusion of epithelioid macrophages; their nuclei are symmetrically arranged in a peripheral crescent or horseshoe pattern along the outer edge of the cell, contrasting with foreign-body giant cells (central haphazard nuclei).",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Touton giant cells, characterized by a central ring of nuclei surrounded by a wide zone of foamy, lipid-rich cytoplasm, are classically associated with:",
         ["Xanthomas and xanthogranulomatous lesions", "Foreign body granulomas", "Tuberculosis", "Mycotic infections"],
         0, "Touton giant cells are lipid-laden multinucleated histiocytes with a wreath of nuclei encircling a non-foamy central cytoplasm, with vacuolated, lipid-rich cytoplasm outside the wreath, typical of xanthomas.",
         False, "General Pathology"),

        ("The Splendore-Hoeppli phenomenon (asteroid bodies) observed histologically around bacterial colonies in Actinomycosis, Actinobacillosis, and Botryomycosis represents:",
         ["Deposition of radiant, eosinophilic antigen-antibody complexes and host proteinaceous material", "Enlarged bacterial capsules composed of hyaluronic acid", "Calcified necrotic cellular debris", "Colonies of intracellular microsporidia"],
         0, "The Splendore-Hoeppli phenomenon is the formation of radiating, intensely eosinophilic, club-shaped or star-shaped proteinaceous precipitates (immunoglobulins and host proteins) surrounding foreign organisms or dense bacterial aggregates.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("The major cytokine responsible for stimulating hepatic synthesis of acute-phase proteins (such as C-reactive protein, serum amyloid A, and fibrinogen) during systemic inflammation is:",
         ["Interleukin-6 (IL-6)", "Interleukin-4 (IL-4)", "Interleukin-10 (IL-10)", "Interleukin-13 (IL-13)"],
         0, "IL-6 is the principal endocrine cytokine acting on hepatocytes to stimulate the transcription of acute-phase protein genes while simultaneously downregulating albumin synthesis.",
         True, "General Pathology"),

        ("Granulation tissue, the specialized tissue of wound repair, is histologically composed of which two primary elements?",
         ["Proliferating newly formed capillaries (angiogenesis) and proliferating fibroblasts in an edematous ECM", "Dense bundles of mature cross-linked type I collagen and fat cells", "Abundant multinucleated giant cells and mineral deposits", "Stratified squamous epithelium and nerve endings"],
         0, "Granulation tissue is soft, pink, granular tissue formed during healing, characterized microscopically by newly formed capillary loops proliferating perpendicular to the wound surface alongside activated fibroblasts (myofibroblasts).",
         True, "Inflammation & Repair (ICAR PG PYQ)"),

        # 71-80: Wound repair, proud flesh, cellular adaptations, metaplasia, dysplasia
        ("The pathological phenomenon known as 'proud flesh' occurring commonly on the distal limbs of horses represents:",
         ["Exuberant, excessive granulation tissue protruding above the margin of the wound, preventing re-epithelialization", "Malignant transformation into an equine sarcoid", "Severe purulent osteomyelitis of the third phalanx", "Spontaneous keloid formation composed solely of mast cells"],
         0, "'Proud flesh' is exuberant granulation tissue in equine distal limb wounds, resulting from persistent low-grade inflammation, hypoxia, and prolonged fibroblastic/vascular proliferation exceeding epidermal advancement.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Wound contraction during healing by second intention is actively driven by which specialized cell type?",
         ["Myofibroblasts", "Mast cells", "Endothelial cells", "Skeletal myocytes"],
         0, "Myofibroblasts possess features of both fibroblasts and smooth muscle cells, containing alpha-smooth muscle actin filaments that anchor to the surrounding extracellular matrix, generating mechanical tension to contract wound margins.",
         True, "Inflammation & Repair"),

        ("Which category of cells in domestic animals possesses no regenerative capacity and cannot re-enter the cell cycle after terminally differentiating?",
         ["Permanent cells (neurons and cardiac myocytes)", "Stable cells (hepatocytes and renal tubular epithelium)", "Labile cells (epidermal keratinocytes)", "Stem cells of the intestinal crypts"],
         0, "Permanent cells (e.g. neurons in the CNS and adult cardiac myocytes) are considered terminally differentiated and cannot divide; injury to these tissues inevitably heals by replacement fibrosis (scar formation) rather than regeneration.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Goiter in domestic animals (diffuse non-toxic enlargement of the thyroid gland) is a classic pathological example of:",
         ["Hyperplasia driven by elevated Thyroid-Stimulating Hormone (TSH)", "Pure cellular hypertrophy without cell division", "Squamous metaplasia", "Atrophy of follicular lining"],
         0, "Dietary iodine deficiency impairs thyroxine (T4/T3) synthesis, removing negative feedback on the pituitary; high TSH levels drive intense follicular epithelial cell proliferation (hyperplasia), producing enlarged goitrous thyroid glands.",
         True, "General Pathology"),

        ("Cystic Endometrial Hyperplasia (CEH) in bitches predisposes them directly to pyometra and is triggered by prolonged uterine exposure to which hormone?",
         ["Progesterone", "Estrogen", "Oxytocin", "Prolactin"],
         0, "Under prolonged influence of luteal progesterone during diestrus (frequently preceded by estrogen priming), endometrial glands undergo hyperplastic proliferation and cystic dilation with fluid secretion, creating an ideal medium for E. coli colonization.",
         True, "Systemic Pathology (ICAR PG PYQ)"),

        ("Squamous metaplasia of the esophageal mucous glands in poultry and the tracheal pseudostratified ciliated epithelium in calves is pathognomonic for deficiency of:",
         ["Vitamin A (Retinol)", "Vitamin D3 (Cholecalciferol)", "Vitamin E (Tocopherol)", "Vitamin C (Ascorbic acid)"],
         0, "Vitamin A is essential for differentiation of mucous-secreting and ciliated epithelia. In its deficiency, columnar and cuboidal epithelia undergo squamous metaplasia into stratified squamous keratinized epithelium (nutritional roup in poultry).",
         True, "Metabolic Pathology (ICAR PG PYQ)"),

        ("Which of the following definitions precisely describes cellular 'dysplasia'?",
         ["Disordered cellular growth and maturation with loss of architectural orientation and nuclear pleomorphism", "Reversible transformation of one adult cell type into another adult cell type", "Increase in the size of an organ due to increased individual cell size", "Premature programmed cell death without membrane dissolution"],
         0, "Dysplasia is disordered cell proliferation characterized by loss of uniformity, cellular and nuclear pleomorphism, hyperchromasia, and disturbed architectural layering, representing a pre-neoplastic change.",
         True, "General Pathology"),

        ("The complete congenital absence of an organ along with the complete absence of its developmental embryonic primordium is termed:",
         ["Agenesia (agenesis)", "Aplasia", "Hypoplasia", "Atrophy"],
         0, "Agenesia is the total developmental failure of an organ to appear, including its embryonic primordium. In aplasia, the primordium forms but fails to develop, and in hypoplasia, the organ develops but fails to reach full mature size.",
         True, "General Pathology (ICAR PG PYQ)"),

        ("Cerebellar hypoplasia in feline kittens is caused by in utero or perinatal infection with Feline Panleukopenia Virus (FPV) because the virus selectively destroys:",
         ["Mitotically active external germinal layer neurons of the developing cerebellum", "Myelin-producing oligodendrocytes", "Mature Purkinje neurons exclusively", "Microvascular endothelial cells"],
         0, "Parvoviruses depend on host DNA polymerases and selectively destroy rapidly dividing cells. In the neonatal kitten, FPV targets dividing neurons in the external germinal layer of the cerebellum, preventing normal migration and folial development.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("Brown atrophy of the heart and liver in severely cachectic and senile domestic animals is characterized by reduction in organ weight accompanied by intracellular accumulation of:",
         ["Lipofuscin", "Hemosiderin", "Melanin", "Copper complexes"],
         0, "Brown atrophy occurs when cell shrinkage and organ atrophy are accompanied by massive accumulation of lipofuscin (wear-and-tear pigment) within autophagolysosomes of atrophied parenchymal cells.",
         True, "General Pathology")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module1_questions()
    print(f"Pathology Module 1 loaded: {len(qs)} questions")
