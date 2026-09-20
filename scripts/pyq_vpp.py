# scripts/pyq_vpp.py
# 100 ICAR AIEEA PG (M.V.Sc.) Previous Year Question (PYQ) Style MCQs for Veterinary Pathology (VPP)

def get_vpp_pyqs():
    pyqs = [
        ("The pathognomonic diagnostic microscopic lesion of Rabies is the presence of Negri bodies, which are located predominantly in:",
         ["Pyramidal cells of hippocampus in carnivores and Purkinje cells of cerebellum in herbivores", "Neurons of dorsal horn of spinal cord", "Anterior pituitary cells", "Oligodendrocytes in corpus callosum"],
         0, "Negri bodies are round to oval, eosinophilic, intracytoplasmic viral inclusion bodies found in Ammon's horn (hippocampus) in dogs and cats, and cerebellar Purkinje cells in cattle and sheep."),

        ("In Anthrax, which of the following is considered a pathognomonic triad on post-mortem examination of a bovine carcass?",
         ["Failure of blood to clot (tarry black), absence of rigor mortis, and tremendous splenomegaly", "Petechiae on renal cortex, button ulcers, and splenic infarction", "Tiger heart, vesicular stomatitis, and coronitis", "Stellate scars on nasal septum, orchitis, and farcy pipes"],
         0, "Bacillus anthracis causes rapid bacteremia and toxin-mediated vascular endothelial damage. Post-mortem opening of carcasses is strictly prohibited to prevent environmental spore contamination."),

        ("The classic 'button ulcers' (concentric necrotic ulcerative plaques) seen in the mucosa of the cecum and colon near the ileocecal orifice are pathognomonic for:",
         ["Classical Swine Fever (Hog Cholera)", "African Swine Fever", "Swine Dysentery", "Transmissible Gastroenteritis"],
         0, "Button ulcers are formed by chronic ischemic necrosis and secondary bacterial infection (Salmonella cholerasuis) following Pestivirus-induced vascular damage in Classical Swine Fever."),

        ("The pathognomonic gross lesion described as 'turkey egg kidney' (subcapsular cortical petechial hemorrhages) is characteristic of:",
         ["Classical Swine Fever (Hog Cholera)", "Swine Erysipelas", "Porcine Parvovirus", "Glanders"],
         0, "In Classical Swine Fever, petechial hemorrhages spatter the pale subcapsular cortex of the kidney due to severe endothelial damage, resembling a speckled turkey egg."),

        ("The 'honeycomb' or 'cerebriform' corrugation of the ileal and cecal mucosa that CANNOT be smoothed out by stretching is pathognomonic for:",
         ["Johne’s Disease (Paratuberculosis / MAP)", "Bovine Viral Diarrhea (BVD)", "Bovine Tuberculosis", "Rinderpest"],
         0, "Mycobacterium avium subsp. paratuberculosis causes diffuse granulomatous enteritis; lamina propria and submucosa are packed with epithelioid macrophages, producing permanent mucosal folds."),

        ("The 'tiger heart' (cor tigrinum / myocarditis with pale grayish-yellow stripes or patches) is seen in young calves dying acutely of:",
         ["Foot and Mouth Disease (FMD)", "Bovine Malignant Catarrhal Fever", "Blackleg", "Anthrax"],
         0, "In young calves, the FMD aphthovirus exhibits high affinity for developing myocardium, producing acute non-suppurative multifocal necrotizing myocarditis without external vesicular lesions."),

        ("The 'rancid butter' (butyric acid) odor emitted upon incising dark, dry, spongy, crepitant muscle swellings is diagnostic of:",
         ["Blackleg (Clostridium chauvoei)", "Malignant Edema (Clostridium septicum)", "Anthrax", "Tetanus"],
         0, "C. chauvoei spores germinate in bruised muscle, releasing necrotizing and hemolytic toxins that ferment glycogen, producing gas bubbles (crepitation) and volatile butyric acid."),

        ("Under polarized light microscopy, amyloid deposits stained with Congo Red demonstrate which characteristic diagnostic optical property?",
         ["Apple-green birefringence", "Yellow fluorescence", "Metachromatic purple", "Golden-brown dichroism"],
         0, "Congo red intercalates between anti-parallel beta-pleated sheets of amyloid fibrils, exhibiting pathognomonic apple-green birefringence under cross-polarized light."),

        ("Zenker’s degeneration is a specific waxy / hyaline degeneration occurring classically in:",
         ["Skeletal muscle fibers", "Hepatocytes", "Renal tubular epithelium", "Cardiac Purkinje fibers"],
         0, "Zenker's degeneration affects striated skeletal muscle fibers (e.g. White Muscle Disease in calves/lambs and Azoturia in horses), causing swelling, loss of cross-striations, and hyalinization."),

        ("In tuberculosis, the multinucleated giant cells characterized by nuclei arranged in a horseshoe or peripheral wreath pattern are termed:",
         ["Langhans giant cells", "Foreign body giant cells", "Touton giant cells", "Reed-Sternberg cells"],
         0, "Langhans giant cells form by the fusion of epithelioid macrophages in chronic granulomatous inflammation (tuberculosis), with nuclei aligned along the cell periphery."),

        ("Touton giant cells, which have a central ring of nuclei surrounded by a foamy lipid-rich cytoplasm, are characteristically seen in:",
         ["Xanthomas and fat necrosis", "Tuberculosis", "Foreign body granulomas", "Asbestosis"],
         0, "Touton giant cells are lipid-laden multinucleated cells typical of xanthomatous lesions and conditions with heavy lipid breakdown."),

        ("Reed-Sternberg cells (owl-eye binucleated giant cells) are diagnostic markers of:",
         ["Hodgkin's lymphoma", "Bovine Lymphosarcoma", "Multiple Myeloma", "Canine Mastocytoma"],
         0, "Reed-Sternberg cells are giant transformed B-cells with prominent, mirror-image amphophilic nucleoli giving an 'owl-eye' appearance in Hodgkin's lymphoma."),

        ("The 'nutmeg liver' gross appearance is produced by:",
         ["Chronic passive venous congestion (congestive heart failure)", "Fatty liver dystrophy", "Diffuse hepatic cirrhosis", "Infectious canine hepatitis"],
         0, "Right-sided congestive heart failure causes venous stasis in hepatic central veins; centrilobular congestion (dark red) contrasted with periportal fatty degeneration (pale yellow) produces the nutmeg pattern."),

        ("The lines of Zahn are alternating pale and dark laminations found microscopically in:",
         ["Ante-mortem thrombi", "Post-mortem currant-jelly clots", "Post-mortem chicken-fat clots", "Hematomas"],
         0, "Lines of Zahn represent alternating layers of platelets/fibrin (pale) and trapped erythrocytes (dark), confirming that a thrombus formed in a flowing bloodstream ante-mortem."),

        ("The irreversible stage of cell injury characterized by nuclear shrinkage and increased basophilia (dark staining) is termed:",
         ["Pyknosis", "Karyorrhexis", "Karyolysis", "Chromatolysis"],
         0, "Nuclear changes in necrosis proceed through pyknosis (condensation/shrinkage), karyorrhexis (fragmentation), and karyolysis (dissolution by DNases)."),

        ("Liquefactive necrosis is the characteristic response to ischemia in which anatomical structure?",
         ["Brain and Spinal Cord (Central Nervous System)", "Heart", "Kidney", "Spleen"],
         0, "Due to high lipid and low fibrous tissue content and abundant hydrolytic lysosomal enzymes, infarcted brain tissue rapidly undergoes enzymatic liquefaction (malacia)."),

        ("The 'bread-and-butter' heart is the classical gross description for:",
         ["Fibrinous pericarditis (e.g. Traumatic Reticulopericarditis in cattle)", "Uremic pericarditis", "Purulent pericarditis", "Hydropericardium"],
         0, "In traumatic reticulopericarditis (hardware disease), fibrin deposits between visceral and parietal epicardium pull apart with cardiac contractions, resembling two slices of buttered bread."),

        ("The 'pipestem liver' appearance on necropsy of sheep or cattle is caused by chronic infection with:",
         ["Fasciola hepatica / Fasciola gigantica", "Echinococcus granulosus", "Dicrocoelium dendriticum", "Schistosoma bovis"],
         0, "Adult liver flukes residing in bile ducts induce chronic mechanical and proline-mediated irritation, causing massive periductal fibrosis and calcification that resemble white clay pipe stems."),

        ("The 'milk spot liver' in swine is caused by the larval migration of:",
         ["Ascaris suum", "Stephanurus dentatus", "Metastrongylus apri", "Trichuris suis"],
         0, "L3 larvae of Ascaris suum migrating through hepatic sinusoids cause focal eosinophilic necrotizing hepatitis that heals by fibrous replacement ('milk spots')."),

        ("The 'pimply gut' characterized by hard caseocalcareous nodules scattered throughout the small and large intestinal walls of sheep is caused by:",
         ["Oesophagostomum columbianum", "Haemonchus contortus", "Chabertia ovina", "Bunostomum trigonocephalum"],
         0, "Larvae of the nodular worm Oesophagostomum penetrate the intestinal submucosa; localized host hypersensitivity encapsulates them in calcified granulomatous nodules."),

        ("The 'hard pad disease' (marked hyperkeratosis of the footpads and nasal planum) in dogs is a classic manifestation of chronic:",
         ["Canine Distemper Virus (CDV)", "Canine Parvovirus (CPV)", "Infectious Canine Hepatitis (CAV-1)", "Rabies"],
         0, "Canine distemper virus targets epithelial basal cells, inducing excessive keratinocyte proliferation that leads to thick, cracked footpads ('hard pad')."),

        ("Canine Distemper is histologically unique among viral diseases because it forms:",
         ["Both intracytoplasmic AND intranuclear eosinophilic inclusion bodies", "Intranuclear inclusions only", "Intracytoplasmic inclusions only", "No inclusion bodies"],
         0, "Canine distemper virus (Morbillivirus) forms diagnostic eosinophilic inclusion bodies in both the cytoplasm and nucleus of epithelial, lymphoid, and neuroglial cells."),

        ("Infectious Canine Hepatitis (Rubarth's disease / CAV-1) characteristically produces which type of inclusion bodies?",
         ["Large basophilic intranuclear inclusion bodies (Cowdry Type A) in hepatocytes and vascular endothelium", "Intracytoplasmic eosinophilic inclusions", "Negri bodies", "Bollinger bodies"],
         0, "CAV-1 replicates in nuclei, producing diagnostic Cowdry A intranuclear inclusions in hepatocytes and Kupffer cells, accompanied by centrilobular necrosis."),

        ("'Blue eye' (transient or permanent corneal opacity / edema) in dogs convalescing from Infectious Canine Hepatitis is caused by:",
         ["Type III hypersensitivity (immune-complex deposition in corneal endothelial cells)", "Direct viral corneal ulceration", "Type I anaphylaxis", "Vitamin A deficiency"],
         0, "Circulating viral antigen-antibody complexes deposit in the anterior uvea and corneal endothelium, activating complement and causing severe corneal edema ('blue eye')."),

        ("Diamond-shaped skin lesions (urticaria / diamond skin disease) in swine are pathognomonic for:",
         ["Erysipelothrix rhusiopathiae (Swine Erysipelas)", "Actinobacillus pleuropneumoniae", "Streptococcus suis", "Classical Swine Fever"],
         0, "Erysipelothrix causes bacterial thrombosis of cutaneous arterioles, producing focal, sharply demarcated rhomboidal (diamond-shaped) ischemic red-purple skin infarcts."),

        ("Vegetative valvular endocarditis with cauliflower-like friable thrombi on the mitral valve of pigs is most frequently caused by chronic:",
         ["Erysipelothrix rhusiopathiae", "Pasteurella multocida", "Salmonella choleraesuis", "Bordetella bronchiseptica"],
         0, "Chronic swine erysipelas frequently manifests as vegetative endocarditis on the mitral and aortic valves, composed of fibrin, platelets, and bacterial colonies."),

        ("The pathognomonic lesion of 'Glanders' (Burkholderia mallei) in equids is the presence of nodules in the respiratory mucosa that ulcerate and heal leaving:",
         ["Stellate (star-shaped) scars on the nasal septum", "Button ulcers", "Pipestem lesions", "Tiger stripes"],
         0, "Glanders nodules rupture into crateriform ulcers on the nasal mucosa and septum; subsequent granulation and cicatrix formation produce diagnostic stellate (star-shaped) scars."),

        ("Farcy in horses represents the cutaneous form of Glanders, characterized by:",
         ["Nodules ('farcy buds') along subcutaneous lymphatics with thickening of vessels ('farcy pipes')", "Dry gangrene of tail", "Alopecia on mane", "Urticarial wheals"],
         0, "Burkholderia mallei travels via dermal lymph vessels; lymphangitis creates cord-like swollen vessels ('farcy pipes') with ulcerating cutaneous abscesses ('farcy buds')."),

        ("The 'zebra striping' (longitudinal congested stripes on the mucosa of the rectum and colon) is pathognomonic for:",
         ["Rinderpest (and Peste des Petits Ruminants - PPR)", "Foot and Mouth Disease", "Anthrax", "Bovine Spongiform Encephalopathy"],
         0, "Rinderpest and PPR induce marked capillary congestion and hemorrhage along the crests of the longitudinal rectal mucosal folds, appearing as zebra stripes."),

        ("The primary tumor marker / diagnostic chromosome abnormality in Canine Transmissible Venereal Tumor (CTVT) is a diploid chromosome number of:",
         ["59 chromosomes (compared to the normal canine 78)", "78 chromosomes", "60 chromosomes", "38 chromosomes"],
         0, "CTVT is a clonal transmissible allograft possessing a remarkably stable, aberrant karyotype of 57 to 59 chromosomes (normal canine 2n = 78)."),

        ("Which neoplasm is derived from tissue of all three embryonic germ layers (ectoderm, mesoderm, and endoderm)?",
         ["Teratoma", "Hamartoma", "Choristoma", "Carcinosarcoma"],
         0, "Teratomas arise from totipotent germ cells and contain bizarre mixtures of tissues: teeth, hair, bone, respiratory epithelium, and neural tissue."),

        ("A benign developmental mass composed of mature, disorganized tissues normal to that specific anatomical site is a:",
         ["Hamartoma", "Choristoma", "Teratoma", "Adenoma"],
         0, "Hamartomas (e.g. vascular hamartoma) are non-neoplastic developmental anomalies consisting of indigenous mature tissues arranged in a disorganized architecture."),

        ("A mass of histologically normal tissue present in an abnormal anatomical location is termed a:",
         ["Choristoma (heterotopia)", "Hamartoma", "Teratoma", "Chondroma"],
         0, "Choristomas (e.g. a dermoid choristoma on the cornea containing skin and hair follicles) consist of normal tissue misplaced during embryogenesis."),

        ("The most common primary malignant bone tumor in large-breed dogs, presenting with a 'sunburst' periosteal reaction on radiographs, is:",
         ["Osteosarcoma", "Chondrosarcoma", "Fibrosarcoma", "Hemangiosarcoma"],
         0, "Canine osteosarcoma characteristically affects the metaphyseal region of long bones ('away from the elbow, towards the knee') with cortical lysis and periosteal Codman's triangle."),

        ("Canine mast cell tumors (MCT) contain cytoplasmic granules that exhibit metachromasia (staining purple-red with blue dyes like Toluidine Blue) because of:",
         ["Heparin and sulfated glycosaminoglycans", "Melanin", "Hemosiderin", "Lipofuscin"],
         0, "Mast cell granules contain histamine, heparin, and proteases; polyanionic heparin complexes with basic dyes to shift absorption spectra (metachromasia)."),

        ("In avian pathology, 'Bollinger bodies' are diagnostic large intracytoplasmic inclusion bodies observed in epithelial cells in:",
         ["Fowl Pox", "Infectious Laryngotracheitis (ILT)", "Marek's Disease", "Infectious Bronchitis"],
         0, "Avian poxviruses produce giant lipid-rich, eosinophilic intracytoplasmic inclusion bodies (Bollinger bodies) which contain elementary viral particles (Borrel bodies)."),

        ("Infectious Laryngotracheitis (ILT) in domestic fowl produces which diagnostic inclusion bodies?",
         ["Intranuclear inclusion bodies in tracheal epithelial cells", "Intracytoplasmic Bollinger bodies", "Negri bodies", "Guarnieri bodies"],
         0, "ILT is caused by Gallid alphaherpesvirus 1; syncytia (multinucleated giant cells) with Cowdry Type A intranuclear inclusion bodies are formed in tracheal epithelium."),

        ("The 'water-belly' condition in feedlot steers and wethers is the pathological sequel of:",
         ["Rupture of the urinary bladder or urethra secondary to obstructive urolithiasis", "Ascites from portal hypertension", "Right heart failure", "Renal amyloidosis"],
         0, "Calculi (silica or struvite) lodge in the sigmoid flexure of the bovine urethra, causing urethral rupture, subcutaneous urine infiltration in the ventral abdomen ('water belly'), and uremia."),

        ("The 'pulpy kidney' lesion in sheep is pathognomonic for enterotoxemia caused by which clostridial organism?",
         ["Clostridium perfringens Type D", "Clostridium perfringens Type A", "Clostridium chauvoei", "Clostridium novyi"],
         0, "Epsilon toxin produced by C. perfringens Type D rapidly breaks down renal tubular architecture post-mortem, turning kidneys into a soft, pulpy mass within 1-2 hours of death."),

        ("'Black disease' (Infectious Necrotic Hepatitis) in sheep is triggered by migration of immature Fasciola flukes in liver tissue creating anaerobic niches for:",
         ["Clostridium novyi Type B", "Clostridium chauvoei", "Clostridium perfringens", "Clostridium tetani"],
         0, "Migrating liver flukes produce ischemic necrotic tracks that permit latent spores of Clostridium novyi Type B to germinate, releasing alpha-toxin that causes acute hepatic necrosis and toxemia."),

        ("'Braxy' in sheep is an acute abomasitis characterized by severe mucosal edema, necrosis, and gas production caused by:",
         ["Clostridium septicum", "Clostridium chauvoei", "Clostridium botulinum", "Clostridium tetani"],
         0, "Ingestion of frozen frosted roots/grass damages abomasal mucosa, allowing Clostridium septicum invasion, resulting in fatal hemorrhagic abomasitis ('Braxy')."),

        ("The classical pathological lesion in cattle with 'Bovine Spongiform Encephalopathy' (BSE) consists of:",
         ["Bilateral symmetrical vacuolation (spongiform change) of neuronal perikarya and neuropil in the obex", "Suppurative microabscesses in cerebellum", "Demyelination of peripheral nerves", "Diffuse lymphocytic cuffing"],
         0, "Prion protein (PrPSc) accumulation induces non-inflammatory vacuolation of neuronal cytoplasm and grey matter neuropil, especially in the solitary tract nucleus and spinal trigeminal nucleus in the obex."),

        ("Microabscesses in the brainstem (medulla oblongata) with marked mononuclear perivascular cuffing in ruminants with circling signs are diagnostic of:",
         ["Listeriosis (Listeria monocytogenes / Circling Disease)", "Rabies", "Polioencephalomalacia", "Scrapie"],
         0, "Listeria enters via abrasions in buccal mucosa and migrates up the trigeminal nerve (cranial nerve V), causing microabscesses and asymmetrical cranial nerve paralysis in the brainstem."),

        ("Autofluorescence of the cerebral cortex under long-wave ultraviolet light (Wood's lamp, 365 nm) is diagnostic of:",
         ["Polioencephalomalacia (Cerebrocortical necrosis) due to thiamine deficiency or sulfur excess", "Listeriosis", "Rabies", "Bovine Spongiform Encephalopathy"],
         0, "Laminar cortical necrosis in PEM results in lipid-breakdown products (lipofuscin/lipopigments) within necrotic macrophages that emit a brilliant bluish-white autofluorescence under UV light."),

        ("The primary lesion of 'Malignant Catarrhal Fever' (MCF) in cattle and bison is:",
         ["Generalized lymphocytic vasculitis and perivascular cuffing with fibrinoid vascular necrosis", "Vesicular stomatitis", "Severe fibrinous pleuropneumonia", "Acute hemorrhagic enteritis"],
         0, "Alcelaphine gammaherpesvirus-1 and Ovine gammaherpesvirus-2 induce cytotoxic T-cell proliferation and necrotizing pan-vasculitis across all organs, including keratoconjunctivitis and lymphadenopathy."),

        ("In 'Enzootic Bovine Hematuria' (EBH), chronic ingestion of bracken fern (Pteridium aquilinum) containing ptaquiloside induces:",
         ["Hemangiomas, hemangiosarcomas, and transitional cell carcinomas of the urinary bladder", "Renal amyloidosis", "Acute glomerulonephritis", "Interstitial nephritis"],
         0, "Ptaquiloside induces DNA adducts in urothelium, synergizing with Bovine Papillomavirus type 2/4 to produce multi-centric vascular and epithelial neoplasms in the bovine urinary bladder wall."),

        ("The gross lesion of 'Contagious Bovine Pleuropneumonia' (CBPP / Mycoplasma mycoides subsp. mycoides) is classically described as:",
         ["'Marbled lung' with massive widening of interlobular septa by serofibrinous exudate and sequestrum formation", "Miliary tubercles in pleura", "Diffuse catarrhal bronchitis", "Lobar atelectasis"],
         0, "Extensive interlobular edema, thrombosis, and alternating stages of red and grey hepatization give the bovine lung a dramatic 'marbled' pattern, often encapsulating necrotic lung as a sequestrum."),

        ("The presence of 'heart failure cells' in the pulmonary alveoli refers to:",
         ["Alveolar macrophages laden with golden-brown hemosiderin pigment from phagocytosed extravasated red blood cells", "Degenerated cardiac myocytes", "Infiltrating neutrophils", "Hypertrophied Type II pneumocytes"],
         0, "Chronic left-sided heart failure causes pulmonary venous congestion and micro-hemorrhages; alveolar macrophages ingest RBCs and accumulate hemosiderin, termed 'heart failure cells'."),

        ("The pathological lesion termed 'proud flesh' in horses represents excessive exuberant proliferation of:",
         ["Granulation tissue (fibroblasts and endothelial capillaries)", "Stratum corneum", "Subcutaneous adipose tissue", "Skeletal muscle fibers"],
         0, "Wounds on the distal limbs of horses frequently develop exuberant granulation tissue ('proud flesh') that protrudes above the skin margin, halting normal re-epithelialization."),

        ("A thrombus that forms in the caudal abdominal aorta at its bifurcation into external and internal iliac arteries in cats with hypertrophic cardiomyopathy is known as a:",
         ["'Saddle thrombus'", "Ball valve thrombus", "Septic embolus", "Paradoxical embolus"],
         0, "Left atrial dilation in feline HCM triggers thrombosis; thromboemboli dislodge and lodge at the aortic trifurcation ('saddle thrombus'), causing acute hindlimb paresis, cold footpads, and pulseless femoral arteries.")
    ]

    # Generate next 50 systematically covering all other classical PYQ items
    more_pyqs = [
        ("The 'Aschoff bodies' are pathognomonic granulomatous myocardial nodules seen in:",
         ["Rheumatic myocarditis", "FMD tiger heart", "White muscle disease", "Ionophore toxicity"],
         0, "Aschoff bodies consist of foci of fibrinoid necrosis surrounded by lymphocytes, plasma cells, and plump Anitschkow myocytes."),

        ("The 'Anitschkow myocytes' (caterpillar cells) found in cardiac lesions are characterized by:",
         ["An elongated wavy ribbon-like nucleus resembling a caterpillar", "Multiple peripherally arranged nuclei", "Owl-eye appearance", "Cross-striated cytoplasm"],
         0, "Anitschkow cells are specialized macrophages or modified myocytes with nuclear chromatin condensed in a central wavy serrated ribbon ('caterpillar appearance')."),

        ("The 'sago spleen' pattern of amyloidosis results from amyloid deposition selectively occurring in the:",
         ["Splenic follicles (Malpighian corpuscles / white pulp)", "Splenic red pulp sinusoids", "Splenic capsule", "Trabecular arteries"],
         0, "In the focal form (sago spleen), amyloid is restricted to lymphoid follicles, appearing as translucent granules resembling boiled sago grains."),

        ("The 'lardaceous spleen' pattern of amyloidosis involves diffuse deposition in the:",
         ["Walls of the red pulp venous sinusoids and splenic cords", "White pulp follicles only", "Germinal centers exclusively", "Lymphatic vessels"],
         0, "Lardaceous spleen represents diffuse amyloidosis where large glassy, waxy sheets infiltrate the venous sinuses of the red pulp."),

        ("The 'splinter hemorrhage' or 'flame-shaped hemorrhage' in tissues is typically located in:",
         ["Nerve fiber layer of the retina or along striated muscle fascicles", "Brain ventricles", "Pericardial sac", "Synovial space"],
         0, "Hemorrhages tracking linearly between longitudinal oriented fibers (retinal nerve fibers or muscle fascicles) assume a splinter or flame morphology."),

        ("The primary tumor suppressor gene frequently mutated or deleted in more than 50% of canine malignant tumors is:",
         ["p53 gene", "HER-2 / neu", "c-myc", "bcl-2"],
         0, "p53 encodes a nuclear transcription factor that senses DNA damage and arrests the cell cycle at G1/S or triggers apoptosis; its inactivation permits malignant clone survival."),

        ("Retinoblastoma gene (Rb) prevents excessive cell growth by inhibiting the cell cycle until a cell is ready to divide, acting at which checkpoint?",
         ["G1 to S phase transition", "G2 to M phase transition", "Metaphase to Anaphase", "S phase replication"],
         0, "Hypophosphorylated Rb holds the transcription factor E2F inactive; phosphorylation by cyclin D-CDK4/6 releases E2F, driving the cell past the restriction point into S phase."),

        ("The primary microscopic criterion for grading the malignancy of mast cell tumors according to the Patnaik system is:",
         ["Depth of invasion, cellular differentiation, and degree of cytoplasmic granulation", "Tumor volume", "Age of animal", "Presence of bacterial infection"],
         0, "The Patnaik system categorizes canine MCTs into Grade I (well-differentiated, confined to dermis), Grade II (intermediate), and Grade III (poorly differentiated, deep infiltration, high mitotic index)."),

        ("The 'strawberry gallbladder' in dogs and humans is caused by mucosal accumulation of:",
         ["Cholesterol inside macrophages (Cholesterolosis)", "Bilirubin calculi", "Amyloid fibrils", "Bile salts"],
         0, "Cholesterolosis produces yellow flecks of lipid-engorged lamina propria macrophages against a red congested mucosa, resembling a strawberry surface."),

        ("The primary cause of 'dry gangrene' of the extremities (ears, tail, hooves) in cattle is:",
         ["Ergotism (ingestion of Claviceps purpurea sclerotia) or Fescue foot", "Clostridial infection", "Hypovitaminosis A", "Traumatic rupture"],
         0, "Ergot alkaloids (ergotamine, ergocristine) cause chronic, intense peripheral arteriolar vasoconstriction and endothelial injury, resulting in ischemic necrosis and mummification (dry gangrene)."),

        ("The microscopic lesion characterized by 'onion-skin' concentric lamination in splenic arterioles is classic for:",
         ["Systemic Lupus Erythematosus (SLE)", "Polyarteritis nodosa", "Amyloidosis", "Anthrax"],
         0, "Onion-skin concentric periarteriolar fibrosis in the spleen is an immune-complex mediated vascular response characteristic of SLE."),

        ("In 'Canine Parvovirus Enteritis', the primary cellular target of viral destruction is the:",
         ["Actively dividing epithelial cells in the crypts of Lieberkühn and lymphoid tissues", "Surface absorptive enterocytes of villus tips", "Brunner's glands", "Gastric chief cells"],
         0, "CPV-2 requires host cellular DNA polymerases in S-phase, selectively destroying intestinal crypt cells, resulting in complete villous collapse, hemorrhage, and panleukopenia."),

        ("In contrast to Parvovirus, 'Rotavirus' and 'Coronavirus' in calves and piglets target and destroy:",
         ["Mature absorptive enterocytes on the upper two-thirds of the intestinal villi (sparing crypts)", "Crypt cells exclusively", "Lymph nodes exclusively", "Peyer's patches"],
         0, "Rotavirus and coronavirus infect differentiated enterocytes on villous tips, causing villous blunting and osmotic diarrhea; crypt cells remain intact to regenerate epithelium rapidly."),

        ("The 'blue-tongue' appearance (cyanosis of the tongue) in sheep with Bluetongue virus is caused by:",
         ["Orbivirus-induced endothelial cell necrosis resulting in microthrombi and severe venous stasis", "Direct muscle necrosis", "Hypothermia", "Methemoglobinemia"],
         0, "Bluetongue virus (an Orbivirus transmitted by Culicoides) has strict tropism for vascular endothelial cells, causing microvascular thrombosis, edema, and cyanosis of the tongue and coronet."),

        ("The 'button-like' or 'volcano-like' crateriform mucosal ulcers on the tongue and dental pad in Bovine Viral Diarrhea (Mucosal Disease) represent:",
         ["Acute erosive and ulcerative stomatitis with mucosal epithelial ballooning necrosis", "Caseous necrosis", "Pyogenic abscesses", "Granulomas"],
         0, "Cytopathic BVDV in mucosal disease causes severe epithelial necrosis and mucosal sloughing along the tongue, hard palate, esophagus, and Peyer's patches."),

        ("The 'lead line' on the gingival margins in animals with chronic lead poisoning is caused by the precipitation of:",
         ["Lead sulfide", "Lead carbonate", "Lead oxide", "Lead sulfate"],
         0, "Hydrogen sulfide produced by oral bacteria reacts with circulating lead ions in gingival capillaries to precipitate dark bluish-black insoluble lead sulfide granules."),

        ("The 'Satellitosis' and 'Neuronophagia' observed in viral encephalitis refer to:",
         ["Accumulation of oligodendrocytes/microglia around degenerating neurons followed by their phagocytosis", "Astrocyte death", "Erythrocyte extravasation", "Demyelination alone"],
         0, "When cortical neurons suffer lethal injury, perineuronal oligodendroglia multiply around them (satellitosis) and activated microglial macrophages engulf the dead soma (neuronophagia)."),

        ("The microscopic lesion known as 'fibrinoid necrosis' typically occurs in:",
         ["Blood vessel walls affected by immune-complex vasculitis (Type III) or malignant hypertension", "Skeletal muscle", "Adipose tissue", "Brain cortex"],
         0, "Antigen-antibody complexes and leaking fibrinogen deposit in arterial tunica media, polymerizing with necrotic smooth muscle into a smudgy, intensely eosinophilic 'fibrinoid' ring."),

        ("The primary chemical mediator of acute vascular permeability responsible for the immediate transient phase (first 15-30 minutes) is:",
         ["Histamine and Serotonin", "Bradykinin", "Leukotriene C4", "Interleukin-1"],
         0, "Preformed histamine released from mast cell granules binds H1 receptors on post-capillary venule endothelial cells, causing rapid endothelial contraction and inter-endothelial gaps."),

        ("The cytokine primarily responsible for inducing fever (pyrogenesis) by acting on the hypothalamic thermoregulatory center is:",
         ["Interleukin-1 (IL-1) and Tumor Necrosis Factor-alpha (TNF-alpha)", "Interleukin-10", "Interferon-gamma", "Interleukin-2"],
         0, "IL-1 and TNF-alpha cross the blood-brain barrier to stimulate local endothelial synthesis of Prostaglandin E2 (PGE2), which shifts the hypothalamic thermal set-point upward."),

        ("The principal chemokine responsible for directed chemotaxis of neutrophils toward bacterial infection sites is:",
         ["Interleukin-8 (CXCL8)", "Interleukin-4", "Interferon-alpha", "Transforming growth factor-beta"],
         0, "IL-8 is a powerful neutrophil-activating and chemoattractant peptide secreted by activated tissue macrophages and endothelial cells."),

        ("The 'opsonin' that most powerfully enhances macrophage phagocytosis of bacteria is:",
         ["Fc portion of IgG antibodies and complement fragment C3b", "Albumin", "Fibrinogen", "Transferrin"],
         0, "Phagocytes possess high-affinity surface receptors for the Fc region of IgG (Fc-gamma-R) and the cleaved complement fragment C3b (CR1), triggering engulfment."),

        ("The 'respiratory burst' in activated neutrophils that generates microbicidal reactive oxygen species (superoxide anion) is catalyzed by:",
         ["NADPH oxidase (phagocyte oxidase)", "Myeloperoxidase", "Superoxide dismutase", "Catalase"],
         0, "NADPH oxidase assembles on the phagolysosomal membrane, transferring electrons from NADPH to molecular oxygen to generate superoxide radical (O2.-)."),

        ("Chronic Granulomatous Disease (CGD) in dogs is an inherited genetic defect characterized by the deficiency of:",
         ["NADPH oxidase, preventing the generation of microbicidal reactive oxygen radicals", "Myeloperoxidase", "Lysozyme", "Integrin beta-2"],
         0, "Deficiency of NADPH oxidase subunits impairs the respiratory burst; neutrophils ingest bacteria normally but cannot kill catalase-positive organisms (Staphylococcus)."),

        ("Leukocyte Adhesion Deficiency (BLAD in Holstein cattle and CLAD in Irish Setters) is caused by a mutation in:",
         ["CD18 (Integrin beta-2 subunit), preventing neutrophil firm adhesion and extravasation", "Selectin", "ICAM-1", "Chemokine receptor"],
         0, "BLAD calves carry a point mutation in the CD18 gene; neutrophils cannot form CD11/CD18 beta-2 integrins to adhere to endothelial ICAM-1, causing persistent massive neutrophilia and death from infections."),

        ("The hallmark microscopic lesion of 'Canine Infectious Tracheobronchitis' (Kennel Cough) is:",
         ["Loss of ciliated tracheal epithelium with purulent or mucopurulent exudate and Bordetella adherence", "Granulomas in lungs", "Hyaline membrane disease", "Alveolar emphysema"],
         0, "Bordetella bronchiseptica produces tracheal cytotoxin and dermonecrotic toxin that paralyze and destroy ciliary clearance, facilitating secondary viral (CPIV, CAV-2) replication."),

        ("The 'hemosiderosis' seen in the spleen and liver of animals with autoimmune hemolytic anemia (AIHA) results from:",
         ["Massive extravascular erythrophagocytosis and breakdown of hemoglobin by macrophages", "Dietary iron overload", "Renal failure", "Biliary obstruction"],
         0, "Antibody-coated erythrocytes are sequestered and lysed by splenic red pulp macrophages, converting excess heme iron into insoluble ferritin micelle aggregates (hemosiderin)."),

        ("The microscopic appearance of 'Gout' in birds and reptiles consists of periarticular and visceral deposits of:",
         ["Needle-shaped radiating monosodium urate crystals surrounded by foreign-body giant cells (tophi)", "Calcium pyrophosphate", "Cholesterol crystals", "Calcium oxalate"],
         0, "Uricotelic species lacking uricase precipitate insoluble monosodium urate crystals in kidneys, heart, serosa (visceral gout), and joints (articular gout), inciting granulomatous tophi."),

        ("The pathognomonic renal lesion described as 'white spotted kidney' in young calves is caused by focal interstitial nephritis induced by:",
         ["Escherichia coli bacteremia", "Corynebacterium renale", "Leptospira interrogans", "Actinomyces bovis"],
         0, "Transient subclinical bacteremia with non-enterotoxigenic E. coli in young calves creates discrete, multifocal, whitish cortical lymphoplasmacytic nodules ('white-spotted kidney')."),

        ("Pulmonary 'emphysema' is anatomically defined as:",
         ["Permanent abnormal enlargement of air spaces distal to terminal bronchioles accompanied by destruction of alveolar walls", "Accumulation of fluid in alveoli", "Atelectasis", "Consolidation by neutrophils"],
         0, "Emphysema involves loss of alveolar septal elastic tissue without fibrosis, leading to trapped air, enlarged bullae, and decreased gas exchange surface area."),

        ("The 'bloat line' observed in the esophagus on necropsy of cattle dying from acute ruminal tympany is characterized by:",
         ["Sharp line of demarcation between the pale, ischemic cervical esophagus and congested thoracic/abdominal esophagus", "A tear in the esophagus", "Fibrinous pseudomembrane", "Periesophageal abscess"],
         0, "Enormous ruminal distension elevates intrathoracic pressure, impeding venous return; the cranial cervical esophagus remains congested while the intra-thoracic esophagus becomes compressed and pale/ischemic."),

        ("The characteristic microscopic brain lesion of 'Scrapie' in sheep is:",
         ["Neuronal vacuolation (intracytoplasmic clear vacuoles) in the dorsal motor nucleus of the vagus and reticular formation", "Extensive purulent microabscesses", "Inclusion bodies in astrocytes", "Demyelination of optic tracts"],
         0, "Scrapie (a transmissible spongiform encephalopathy of sheep) produces bilateral symmetrical neurodegenerative vacuoles in the somas of brainstem neurons, intense astrogliosis, and PrPSc deposits."),

        ("The 'sawhorse' stance in horses and cattle with Tetanus is a manifestation of:",
         ["Generalized persistent tonic contraction of extensor skeletal muscles due to disinhibition of motor neurons", "Flaccid paralysis", "Cerebellar hypoplasia", "Myasthenia gravis"],
         0, "Tetanospasmin prevents glycine release from inhibitory interneurons, causing continuous, unmitigated firing of alpha-motor neurons that rigidly extends all four limbs ('sawhorse posture')."),

        ("The diagnostic lesion termed 'hyaline membranes' in acute respiratory distress syndrome (ARDS / Shock Lung) is composed of:",
         ["Fibrin, cellular debris, and surfactant remnants lining the alveolar walls", "Amyloid fibrils", "Bacterial colonies", "Mucin"],
         0, "Diffuse alveolar damage (DAD) disrupts the alveolocapillary barrier, spilling proteinaceous fluid and fibrin that desiccates into dense, eosinophilic hyaline membranes along alveolar basements."),

        ("The 'cuffing' of blood vessels by lymphocytes and plasma cells in the brain (perivascular cuffing) is a classic histological hallmark of:",
         ["Non-suppurative viral encephalitis", "Acute suppurative bacterial meningitis", "Fungal granulomas", "Ischemic infarction"],
         0, "Neurotropic viral infections (Rabies, Canine Distemper, Borna, Pseudorabies) induce mononuclear leukocytes to extravasate and form concentric sleeves around Virchow-Robin spaces (perivascular cuffs)."),

        ("The 'syncytia' (multinucleated giant epithelial cells) observed in bovine lungs in Bovine Respiratory Syncytial Virus (BRSV) infection are produced by the action of:",
         ["Viral Fusion (F) protein causing adjacent host cell membranes to coalesce", "Bacterial toxins", "Complement lysis", "Interferon release"],
         0, "The viral F surface glycoprotein induces fusion of infected respiratory epithelial cells into large multinucleated syncytia with intracytoplasmic inclusion bodies."),

        ("The pathognomonic lesion of 'Canine Parvovirus Myocarditis' in young pups infected in utero or before 4 weeks of age is:",
         ["Non-suppurative necrotizing myocarditis with basophilic intranuclear inclusion bodies in cardiomyocytes", "Valvular vegetation", "Pericardial effusion", "Myocardial calcification"],
         0, "CPV-2 targets the rapidly dividing cardiomyocytes of neonatal puppies, producing acute cardiac failure with large intranuclear viral inclusions in myocardial nuclei."),

        ("The 'parrot mouth' (brachygnathia) in cattle and horses refers to:",
         ["Shortening of the mandible relative to the maxilla", "Elongation of the mandible (prognathism)", "Cleft palate", "Absence of teeth"],
         0, "Brachygnathia superior refers to a shortened maxilla, whereas brachygnathia inferior (commonly called parrot mouth) refers to a shortened mandible with protruding upper incisors."),

        ("The 'bull-dog calf' anomaly in Dexter cattle is a lethal genetic chondrodysplasia characterized by:",
         ["Extreme micromelia, compressed vertebral column, and protruding tongue due to aggrecan gene mutation", "Absence of skin", "Two heads", "Hydrocephalus alone"],
         0, "Dexter chondrodysplasia (an autosomal semi-dominant mutation in the aggrecan ACAN gene) impairs endochondral ossification, producing aborted fetuses with dwarfed limbs and a bulldog-like face."),

        ("The 'parakeratosis' in pigs is histopathologically recognized by:",
         ["Persistence of pyknotic nuclei in the stratum corneum with thickening of the epidermis", "Complete loss of stratum corneum", "Hypergranulosis", "Basal cell liquefaction"],
         0, "Parakeratosis results from incomplete keratinization (classically caused by Zinc deficiency or excess dietary Calcium), leaving retained nuclear fragments within keratin flakes."),

        ("The 'hyperkeratosis' seen in cattle with chronic Chlorinated Naphthalene poisoning (X-disease) is caused by interference with:",
         ["Vitamin A metabolism", "Vitamin D synthesis", "Calcium absorption", "Zinc utilization"],
         0, "Highly chlorinated naphthalenes destroy hepatic carotene and vitamin A, inducing systemic squamous metaplasia and profound hyperkeratosis of the skin and esophagus ('X-disease')."),

        ("The characteristic lesion of 'Black quarter' (Clostridium chauvoei) in cattle occurs primarily in which muscles?",
         ["Large heavy skeletal muscles (thigh, shoulder, rump, brisket)", "Intercostal muscles only", "Diaphragm exclusively", "Tongue only"],
         0, "Heavily muscled areas (gluteal, quadriceps, triceps) suffer micro-trauma during galloping, creating localized anoxia that triggers latent C. chauvoei spore germination."),

        ("The term 'sequestrum' in bone pathology refers to:",
         ["A detached piece of dead necrotic bone surrounded by ischemic exudate", "A newly formed collar of bone", "An opening through which pus drains", "A bone marrow tumor"],
         0, "In chronic osteomyelitis, devitalized necrotic bone separates from living bone as a sequestrum, enclosed within a reactive periosteal shell called an involucrum with draining cloacae."),

        ("The primary cause of 'osteodystrophia fibrosa' (big head disease / rubber jaw) in horses and goats is:",
         ["Secondary Hyperparathyroidism (nutritional Ca:P imbalance or chronic renal failure)", "Hypoparathyroidism", "Vitamin D toxicity", "Fluorosis"],
         0, "Excess dietary phosphorus (bran diet / 'miller's disease') or renal failure elevates PTH, stimulating massive osteoclastic bone resorption and replacement with fibrous connective tissue."),

        ("'Rickets' in growing young animals is characterized histologically by:",
         ["Failure of osteoid mineralization and persistence of hypertrophic chondrocyte columns at the growth plate (physis)", "Excessive brittle bone formation", "Atrophy of trabeculae", "Fibrous osteitis"],
         0, "Deficiency of Vitamin D or Phosphorus in young animals impairs calcification of cartilage at the epiphyseal growth plate, causing swollen, widened physes and bowed long bones."),

        ("In adult animals, the counterpart of rickets occurring AFTER growth plates have closed is:",
         ["Osteomalacia", "Osteopetrosis", "Osteoporosis", "Achondroplasia"],
         0, "Osteomalacia is failure of mineralization of newly formed bone matrix in mature adults with closed physes, predisposing to spontaneous fractures and bone softness."),

        ("'Osteoporosis' is distinct from osteomalacia because osteoporosis represents:",
         ["A reduction in total bone mass where the bone that remains is normally mineralized", "Defective mineralization with excess uncalcified osteoid", "Bacterial bone infection", "Cartilage tumor"],
         0, "Osteoporosis (osteopenia) is characterized by porous, thin cortical and trabecular bone; the mineral-to-collagen ratio remains normal, but total skeletal volume is reduced."),

        ("The 'goiter' (non-neoplastic, non-inflammatory enlargement of the thyroid gland) is histologically characterized by:",
         ["Follicular epithelial hyperplasia and hypertrophy in response to prolonged elevated TSH", "Lymphocytic infiltration", "Amyloidosis", "Follicular atrophy"],
         0, "Iodine deficiency or ingestion of goitrogens (brassica crops, thiocyanates) impairs T3/T4 synthesis; lack of negative feedback causes chronic TSH overstimulation and follicular hyperplasia."),

        ("The 'cataract' is clinically and pathologically defined as:",
         ["Any opacity or clouding of the crystalline lens of the eye or its capsule", "Corneal ulceration", "Glaucoma", "Retinal detachment"],
         0, "Cataracts involve denaturation and cross-linking of crystalline lens structural proteins, commonly secondary to diabetes mellitus (sorbitol accumulation) or uveitis."),

        ("The primary lesion in 'Canine Glaucoma' that causes retinal ganglion cell death and blindness is:",
         ["Sustained elevation of intraocular pressure (IOP) due to impaired aqueous humor outflow at the iridocorneal angle", "Low intraocular pressure", "Lens dislocation only", "Corneal perforation"],
         0, "Obstruction of the pectinate ligament or trabecular meshwork prevents aqueous outflow via the iridocorneal angle, spiking IOP (>25-30 mmHg) and crushing the optic nerve head (optic cupping).")
    ]

    pyqs.extend(more_pyqs)
    
    # Format into standard question objects
    final_list = []
    for idx, item in enumerate(pyqs[:100]):
        final_list.append({
            "id": f"pyq_vpp_{idx+1:03d}",
            "domain": "veterinary_science",
            "year": "2nd_year",
            "subjectId": "vpp",
            "topic": "Veterinary Pathology (ICAR PG PYQ)",
            "questionText": item[0],
            "options": item[1],
            "correctOptionIndex": item[2],
            "explanation": item[3],
            "difficulty": "Hard",
            "tags": ["ICAR PG PYQ", "Pathology", "High-Yield PYQ"],
            "createdAt": 1774000000000 + idx
        })
    return final_list

if __name__ == "__main__":
    qs = get_vpp_pyqs()
    print(f"Loaded {len(qs)} Veterinary Pathology PYQ questions.")
