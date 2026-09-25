# scripts/path_mod4_systemic.py
# Module 4: Systemic & Organ Pathology (50 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Units II & III

def get_module4_questions():
    qs = [
        # 1-10: Cardiovascular & Respiratory Pathology
        ("In domestic animals, the most common anatomical site for bacterial vegetative valvular endocarditis in dogs and pigs is the:",
         ["Mitral (bicuspid) valve and Aortic valve", "Tricuspid valve and Pulmonic valve", "Eustachian valve", "Thebesian valve"],
         0, "In dogs, cats, and swine, vegetative endocarditis predominantly affects the high-pressure left heart valves (mitral and aortic valves), whereas in cattle, the tricuspid (right AV) valve is most frequently affected.",
         True, "Cardiovascular Pathology (ICAR PG PYQ)"),

        ("The distinctive 'cauliflower-like' or 'wart-like' vegetative lesions on heart valves in finishing pigs are pathognomonic for chronic infection by:",
         ["Erysipelothrix rhusiopathiae", "Streptococcus suis", "Actinobacillus pleuropneumoniae", "Mycoplasma hyopneumoniae"],
         0, "Chronic swine erysipelas produces large, friable, yellowish-gray, verrucous or cauliflower-like vegetative masses of fibrin and bacteria on the mitral valve, leading to valvular insufficiency and heart failure.",
         True, "Cardiovascular Pathology (ICAR PG PYQ)"),

        ("In cattle, Traumatic Reticulopericarditis (TRP / 'Hardware Disease') is initiated when a swallowed foreign metallic body perforates the:",
         ["Cranial ventral wall of the reticulum, the diaphragm, and the parietal pericardium", "Dorsal sac of the rumen and spleen", "Abomasal fundus and liver", "Omasal laminae and gall bladder"],
         0, "Swallowed wires or nails lodge in the reticulum; forceful ruminal contractions push the sharp wire through the cranioventral reticular wall, through the diaphragm, and into the pericardial sac, introducing mixed anaerobic bacteria.",
         True, "Systemic Pathology (ICAR PG PYQ)"),

        ("The term 'Cor Pulmonale' refers to:",
         ["Right ventricular hypertrophy and dilation secondary to pulmonary hypertension caused by primary chronic lung disease", "Primary congenital stenosis of the aortic valve", "Left ventricular dilation caused by systemic hypertension", "Acute myocardial infarction of the interventricular septum"],
         0, "Cor pulmonale is right heart failure resulting from chronic respiratory disease (e.g. chronic alveolar emphysema, pulmonary fibrosis, or high-altitude brisket disease) that increases pulmonary vascular resistance.",
         True, "Cardiovascular Pathology"),

        ("High Altitude Disease ('Brisket Disease') in cattle grazing at elevations above 2,500 meters is caused by:",
         ["Chronic alveolar hypoxia triggering severe pulmonary arteriolar vasoconstriction, medial hypertrophy, pulmonary hypertension, and right heart failure", "Severe carbon monoxide toxicity from thin atmosphere", "Congenital deficiency of carbonic anhydrase", "Acute ruminal bloat"],
         0, "Hypoxic pulmonary vasoconstriction is a physiological reflex in cattle; at high altitudes, chronic generalized hypoxia leads to severe pulmonary hypertension, right ventricular hypertrophy, and massive dependent edema of the brisket.",
         True, "Cardiopulmonary Pathology (ICAR PG PYQ)"),

        ("In cats, hypertrophic cardiomyopathy (HCM) is the most frequent cardiac disease, commonly accompanied by which severe vascular complication?",
         ["Aortic 'saddle thrombus' at the iliac trifurcation causing hindlimb paresis and ischemic necrosis", "Coronary artery rupture with hemopericardium", "Renal vein thrombosis leading to nephrotic syndrome", "Dissecting aneurysm of the pulmonary trunk"],
         0, "Left atrial enlargement and endothelial injury in feline HCM promote thrombus formation; fragments detach and lodge at the termination of the abdominal aorta (aortic bifurcation / saddle thrombus), suddenly cutting off femoral pulses.",
         True, "Cardiovascular Pathology (ICAR PG PYQ)"),

        ("Bronchopneumonia in domestic animals is pathologically characterized by:",
         ["Cranioventral consolidation of the lungs with primary aerogenous entry via the bronchial tree", "Diffuse caudodorsal rubbery consolidation without airway exudation", "Exclusive hematogenous dissemination to pleura only", "Absence of any exudate in bronchioles"],
         0, "Bronchopneumonia originates from inhaled pathogens that settle at the bronchiolar-alveolar junction under gravity, producing firm, consolidated, dark red or gray lesions confined to the cranioventral lung lobes.",
         True, "Respiratory Pathology (ICAR PG PYQ)"),

        ("In feedlot cattle, 'Shipping Fever' (Bovine Pneumonic Pasteurellosis) caused by Mannheimia haemolytica produces which specific type of pneumonia?",
         ["Acute fibrinous bronchopneumonia (pleuropneumonia) with coagulative necrosis and oat-shaped degenerate leukocytes", "Chronic interstitial pneumonia with cuffing", "Pure granulomatous pneumonia with Langhans giant cells", "Diffuse verminous atelectasis"],
         0, "Mannheimia haemolytica elaborates an RTX leukotoxin that lyses ruminant neutrophils and platelets, producing severe fibrinous pleuropneumonia, extensive interlobular edema, and streaming, elongated 'oat cells' (altered necrotic leukocytes).",
         True, "Respiratory Pathology (ICAR PG PYQ)"),

        ("Enzootic Pneumonia in pigs, caused by Mycoplasma hyopneumoniae, is histopathologically characterized by:",
         ["Marked peribronchiolar and perivascular lymphoid hyperplasia ('cuffing pneumonia')", "Severe diffuse alveolar hemorrhage without lymphocytes", "Massive fibrinous pleuritis with lung marbling", "Extensive caseous granulomas throughout the diaphragmatic lobes"],
         0, "Mycoplasma hyopneumoniae colonizes the ciliated respiratory epithelium, destroying the mucociliary escalator and inciting massive, dense peribronchial, peribronchiolar, and perivascular cuffs of lymphoid follicles ('cuffing pneumonia').",
         True, "Respiratory Pathology (ICAR PG PYQ)"),

        ("Aspiration pneumonia in ruminants (e.g. from faulty drenching or cleft palate) is characterized by acute necrotizing bronchopneumonia with a foul putrid odor, caused by secondary anaerobic invasion by:",
         ["Fusobacterium necrophorum and Trueperella pyogenes", "Bacillus anthracis", "Brucella abortus", "Mycobacterium bovis"],
         0, "Inhaled milk, mineral oil, or rumen contents cause chemical necrosis; secondary saprophytic invasion by oral anaerobes like Fusobacterium necrophorum and Trueperella pyogenes causes rapid gangrenous necrosis and cavitation.",
         True, "Respiratory Pathology"),

        # 11-20: Alimentary & Hepatobiliary Pathology
        ("Bovine Neonatal Enteritis caused by Enterotoxigenic Escherichia coli (ETEC) produces diarrhea through which pathological mechanism?",
         ["Secretory diarrhea with no microscopic damage to the enterocyte brush border (intact villi)", "Severe villus blunting and crypt cell necrosis", "Extensive diphtheritic pseudomembrane formation", "Granulomatous infiltration of the lamina propria"],
         0, "ETEC adhesins (K99/F5) bind enterocytes, and its enterotoxins (STa) stimulate membrane-bound guanylate cyclase, increasing intracellular cGMP and triggering active secretion of water and electrolytes without structural villus damage.",
         True, "Alimentary Pathology (ICAR PG PYQ)"),

        ("Rotaviral and Coronaviral enteritis in calves and piglets produce malabsorptive diarrhea by selectively causing necrosis and sloughing of:",
         ["Mature absorptive enterocytes covering the tips and sides of intestinal villi, sparing the crypts", "Undifferentiated stem cells inside the crypts of Lieberkühn", "Submucosal lymphoid follicles only", "Smooth muscle layers of the muscularis"],
         0, "Both Rotavirus and Coronavirus replicate in mature enterocytes on the upper two-thirds of intestinal villi, causing villus atrophy, fusion, and osmotic/malabsorptive diarrhea, while crypt cells remain intact to regenerate the epithelium.",
         True, "Alimentary Pathology (ICAR PG PYQ)"),

        ("Winter Dysentery in adult dairy cattle is an acute contagious disease characterized by dark, watery, fetid diarrhea containing blood and mucus, caused by:",
         ["Bovine Coronavirus (BCoV)", "Rotavirus", "Torovirus", "Astrovirus"],
         0, "Bovine Coronavirus is the recognized etiological agent of Winter Dysentery in housed adult dairy cattle, causing acute catarrhal to hemorrhagic enterocolitis with sudden drops in milk yield.",
         False, "Alimentary Pathology"),

        ("In sheep and cattle, acute Ruminal Lactic Acidosis (Grain Overload / Carbohydrate Engorgement) leads to which chemical and microbiological cascade?",
         ["Sudden ingestion of non-structural carbs -> Streptococcus bovis proliferation -> lactic acid production -> ruminal pH drops < 5.0 -> rumen atony and chemical ruminitis", "Excessive fiber intake -> methanogenic archaea proliferation -> ruminal alkalosis pH > 8.0", "Urea breakdown into ammonia -> toxic ruminal alkalosis", "Excessive water intake -> ruminal hypoosmolarity and lysis"],
         0, "Rapid fermentation of readily fermentable starches by Streptococcus bovis and Lactobacillus produces high concentrations of D- and L-lactic acid, driving rumen pH below 5.0, destroying normal protozoa, and causing severe hydropic and ulcerative chemical ruminitis.",
         True, "Alimentary Pathology (ICAR PG PYQ)"),

        ("A frequent fatal sequela of acute chemical ruminitis in cattle is mycotic ruminitis and metastatic liver abscesses, where fungi and bacteria enter the portal vein following mucosal ulceration. The primary fungus and bacterium involved are:",
         ["Rhizopus/Mucor (zygomycetes) and Fusobacterium necrophorum", "Aspergillus fumigatus and Salmonella Dublin", "Candida albicans and E. coli", "Blastomyces dermatitidis and Trueperella pyogenes"],
         0, "Ulceration of the stratified squamous ruminal epithelium allows opportunistic Zygomycetes (Rhizopus, Mucor) to invade blood vessels, causing angioinvasion, thrombosis, and wedge-shaped infarcts, while Fusobacterium necrophorum enters the portal circulation, producing liver abscesses.",
         True, "Alimentary Pathology (ICAR PG PYQ)"),

        ("Bovine Leukosis Virus (BLV) causes malignant lymphoma with a strong anatomical predilection for the abomasum, classically producing:",
         ["Thickened, pale, neoplastic lymphoid infiltration of the abomasal wall with deep crater-like bleeding peptic ulcers", "Fibrous stricture of the pyloric sphincter", "Diffuse squamous papillomas in the omasum", "Total atrophy of parietal cells with no mass formation"],
         0, "In adult enzootic bovine leukosis, the abomasal wall (along with right atrium, uterus, and retrobulbar space) is a classic predilection site; neoplastic lymphocytes expand the submucosa, compromising mucosal perfusion and creating large, bleeding ulcers.",
         True, "Systemic Pathology (ICAR PG PYQ)"),

        ("In dogs with Acute Pancreatitis, the development of systemic hypocalcemia (tetany) is directly caused by:",
         ["Precipitation of circulating ionized calcium into retroperitoneal fat necrosis as insoluble calcium soaps (saponification)", "Suppression of parathyroid hormone secretion by glucagon", "Excessive urinary excretion of calcium due to tubular necrosis", "Impaired intestinal calcium absorption"],
         0, "Hydrolysis of peripancreatic perirenal fat by pancreatic lipase liberates free fatty acids, which avidly bind serum calcium to form chalky white calcium soaps, sequestering large amounts of calcium from the vascular space.",
         True, "Systemic Pathology (ICAR PG PYQ)"),

        ("The definitive microscopic lesion of chronic toxic hepatitis caused by Pyrrolizidine alkaloid (Senecio, Crotalaria, Heliotropium) ingestion in cattle and horses is the classic triad of:",
         ["Megalocytosis of hepatocytes, bridging periportal fibrosis, and biliary ductular hyperplasia", "Coagulative centrilobular necrosis without fibrosis", "Diffuse fatty change with glycogen vacuolation", "Amyloidosis with Langhans giant cells"],
         0, "Pyrrolizidine alkaloids are bioactivated by hepatic CYP450 into toxic pyrroles that cross-link DNA, inhibiting mitosis while protein synthesis continues (producing giant megalocytes), accompanied by extensive bridging fibrosis and bile duct proliferation.",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("Lantana camara poisoning in grazing cattle produces severe secondary (hepatogenous) photosensitization through hepatic retention of which photodynamic metabolite?",
         ["Phylloerythrin (a porphyrin breakdown product of chlorophyll)", "Hypericin", "Fagopyrin", "Porphobilinogen"],
         0, "Lantadene A and B cause intrahepatic cholestasis and hepatocellular injury; phylloerythrin (normally produced by ruminal microbes from chlorophyll and excreted in bile) accumulates in peripheral capillaries and, when activated by sunlight, generates free radicals that slough non-pigmented skin.",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("Congenital Portosystemic Shunts (PSS) in dogs are characterized histopathologically in the liver by:",
         ["Microhepatica with hypoplastic portal veins, absence of visible intrahepatic portal branches, and compensatory arteriolar tortuosity/hyperplasia", "Massive hepatic cirrhosis with marked nodular regeneration", "Diffuse centrilobular coagulative necrosis", "Extensive peliosis hepatis"],
         0, "Because blood bypasses the liver, the liver lacks hepatotrophic factors (insulin, glucagon), remaining abnormally small (microhepatica); histology reveals small or absent portal vein branches and proliferating, tortuous arterioles in portal triads.",
         True, "Systemic Pathology (ICAR PG PYQ)"),

        # 21-30: Urinary & Genital Pathology
        ("In dogs, the pathognomonic lesion of Nephrotic Syndrome (proteinuria, hypoalbuminemia, generalized edema, and hypercholesterolemia) is caused by severe:",
         ["Glomerulonephritis or Glomerular Amyloidosis compromising the glomerular filtration barrier", "Renal medullary amyloidosis", "Acute tubular necrosis from ethylene glycol", "Ascending pyelonephritis"],
         0, "Loss of the negative charge and structural integrity of the podocyte foot processes and glomerular basement membrane (due to immune-complex deposition or amyloid) allows massive leakage of albumin into the filtrate, triggering the nephrotic triad.",
         True, "Urinary Pathology (ICAR PG PYQ)"),

        ("Ethylene glycol (antifreeze) toxicity in dogs and cats produces acute oliguric renal failure with pathognomonic histological presence of:",
         ["Birefringent, pale-yellow, fan-shaped or prism-shaped Calcium Oxalate monohydrate crystals in proximal renal tubular lumens", "Amorphous hemosiderin casts", "Dense amyloid deposits in Bowman's space", "Eosinophilic intranuclear inclusion bodies in podocytes"],
         0, "Hepatic alcohol dehydrogenase oxidizes ethylene glycol to glycolic acid and oxalic acid; oxalate complexes with calcium to form insoluble calcium oxalate crystals that lodge in and destroy proximal tubular epithelium, displaying brilliant birefringence under polarized light.",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("The pathognomonic renal lesion of 'White Spotted Kidney' observed in slaughtered calves is caused by focal interstitial nephritis induced by:",
         ["Leptospira interrogans (serovar Hardjo or Pomona) or Escherichia coli bacteremia", "Corynebacterium renale", "Trueperella pyogenes", "Clostridium perfringens"],
         0, "'White spotted kidney' is subacute to chronic focal non-suppurative interstitial nephritis, characterized by 1-5 mm pale white/gray cortical nodules consisting of lymphocytes, plasma cells, and macrophages following Leptospira or coliform septicemia.",
         True, "Urinary Pathology (ICAR PG PYQ)"),

        ("Bovine Contagious Pyelonephritis is an ascending suppurative urinary infection in postpartum dairy cows caused by:",
         ["Corynebacterium renale (along with C. pilosum and C. cystitidis)", "Escherichia coli alone", "Pseudomonas aeruginosa", "Staphylococcus aureus"],
         0, "Corynebacterium renale uses its pili for adherence to urogenital epithelium and produces high amounts of urease; hydrolyzed urea forms ammonia that irritates mucosal barriers, facilitating ascending colonization from the vulva up to the renal pelvis.",
         True, "Urinary Pathology (ICAR PG PYQ)"),

        ("In male cats, feline lower urinary tract disease (FLUTD / FUS) causing fatal urethral obstruction is most frequently caused by a urethral plug composed of:",
         ["A proteinaceous colloid matrix mixed with Struvite (Magnesium Ammonium Phosphate) crystals", "Calcium oxalate dihydrate calculi", "Pure cystine stones", "Ammonium urate calculi"],
         0, "Urethral plugs in tomcats typically consist of a mucoid protein/inflammatory matrix packed with struvite (triple phosphate) microcrystals, forming a paste that impacts in the narrow penile urethra.",
         True, "Urinary Pathology (ICAR PG PYQ)"),

        ("In bulls, infectious pustular balanoposthitis (IPB) is caused by Bovine Herpesvirus-1 (BHV-1), which simultaneously causes which respiratory disease?",
         ["Infectious Bovine Rhinotracheitis (IBR)", "Bovine Viral Diarrhea (BVD)", "Bovine Respiratory Syncytial Virus (BRSV)", "Contagious Bovine Pleuropneumonia (CBPP)"],
         0, "Bovine alphaherpesvirus 1 (BHV-1) is the etiological agent of both Infectious Bovine Rhinotracheitis (respiratory tract) and Infectious Pustular Vulvovaginitis/Balanoposthitis (genital tract), establishing latency in the sacral and trigeminal ganglia.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("Freemartinism in bovine twins (a sterile heifer co-twin to a bull) results from placental vascular anastomoses in utero that allow which factor to arrest female tract development?",
         ["Anti-Müllerian Hormone (AMH) and testosterone from the male fetal testes", "Excess maternal progesterone", "Fetal cortisol surge", "Placental lactogen"],
         0, "Vascular chorionic fusion between twin fetuses permits exchange of hematogenous stem cells (chimerism); Anti-Müllerian Hormone (AMH) from the earlier-developing male testes suppresses development of the paramesonephric (Müllerian) ducts in the female.",
         True, "Genital Pathology (ICAR PG PYQ)"),

        ("In sheep, contagious pustular dermatitis ('Orf' / 'Scabby Mouth') affecting the lips, muzzle, and teats is caused by a Parapoxvirus producing characteristic:",
         ["Proliferative and scabby epidermal lesions with ballooning degeneration and intracytoplasmic eosinophilic inclusions", "Depigmentation without epidermal hyperplasia", "Extensive subcutaneous edema without scabs", "Squamous cell carcinoma in 90% of cases"],
         0, "Orf virus (Parapoxvirus) produces acute papulovesicular eruptions followed by exuberant epidermal hyperplasia and thick, tenacious scabs, showing hydropic ballooning of stratum spinosum cells with intracytoplasmic inclusions.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("In bitches, Ovarian Follicular Cysts produce persistent hyperestrogenism that leads pathologically to:",
         ["Cystic endometrial hyperplasia, prolonged estrus behavior, and symmetrical non-pruritic alopecia", "Immediate bilateral adrenal cortical atrophy", "Persistent anestrus with masculinization", "Spontaneous mammary gland regression"],
         0, "Failure of the preovulatory LH surge leads to mature anovulatory follicles that continually secrete estrogens, driving profound endometrial gland hyperplasia, vulvar enlargement, and bilaterally symmetrical endocrine alopecia.",
         True, "Genital Pathology"),

        ("In mares, Granulosa Cell Tumor (GCT) of the ovary is clinically and pathologically distinguished by producing high circulating levels of:",
         ["Inhibin and Testosterone, accompanied by nymphomania or stallion-like aggressiveness and contralateral ovarian atrophy", "Progesterone and prolactin", "Luteinizing hormone", "Thyroxine"],
         0, "Equine GCTs are benign stromal neoplasms that secrete inhibin (which suppresses pituitary FSH, causing atrophy of the contralateral ovary) and testosterone/estrogen, triggering persistent behavioral changes (anestrus, nymphomania, or virilism).",
         True, "Genital Pathology (ICAR PG PYQ)"),

        # 31-40: Nervous & Musculoskeletal Pathology
        ("The primary histological difference between Scrapie in sheep and Bovine Spongiform Encephalopathy (BSE) in cattle is that Scrapie:",
         ["Exhibits prominent astrocytic gliosis and neuronal vacuolation in the brainstem alongside vacuolation in both neuronal cell bodies and the neuropil", "Produces massive purulent microabscesses in the cerebral cortex", "Is caused by a Lentivirus rather than a prion", "Is accompanied by severe demyelinating meningitis"],
         0, "Both are transmissible spongiform encephalopathies (TSEs) with PrPSc accumulation, but scrapie displays extensive, prominent intracytoplasmic vacuolation in neurons and intense astrogliosis, particularly in the dorsal vagal nucleus and obex.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("In horses, 'Wobbler Syndrome' (Cervical Vertebral Malformation / CVM) causes progressive bilateral hindlimb ataxia due to:",
         ["Dynamic or static stenotic compression of the cervical spinal cord by malformed cervical vertebrae (C3-C7)", "Clostridial neurotoxin binding at the neuromuscular junction", "Primary degeneration of cerebellar Purkinje cells", "Sarcocystis neurona schizont multiplication"],
         0, "CVM involves malalignment, asymmetric articular facets, or osteochondrosis in cervical vertebrae, producing focal stenosis of the vertebral canal and compression myelopathy with Wallerian axonal degeneration in spinal tracts.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("Equine Protozoal Myeloencephalitis (EPM) is caused by infection of the central nervous system by schizonts and merozoites of:",
         ["Sarcocystis neurona (or Neospora hughesi)", "Babesia caballi", "Toxoplasma gondii", "Theileria equi"],
         0, "Sarcocystis neurona is the primary cause of EPM in equids (opossum is the definitive host); the protozoa multiply within neurons, microglial cells, and astrocytes in the brain and spinal cord, causing multifocal asymmetric necrotizing myeloencephalitis.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("Canine Canine Degenerative Myelopathy (DM), an adult-onset progressive neurodegenerative disease in German Shepherd dogs, is strongly associated with an inherited mutation in:",
         ["Superoxide Dismutase 1 (SOD1) gene", "Dystrophin gene", "Myostatin gene", "P-glycoprotein (MDR1) gene"],
         0, "A point mutation in the SOD1 gene (similar to human ALS) leads to toxic protein misfolding, free-radical damage, and progressive non-inflammatory axonopathy and myelin loss in the dorsal and lateral funiculi of the thoracolumbar spinal cord.",
         False, "Neuropathology"),

        ("In calves and lambs, Nutritional Myopathy ('White Muscle Disease') caused by Vitamin E and Selenium deficiency is characterized grossly by:",
         ["Bilateral symmetrical, pale, chalky, dry streaks in heavily worked skeletal muscles (thigh, shoulder) and the subendocardium of the left ventricle", "Diffuse suppurative myositis with gas crepitation", "Asymmetric hypertrophy of pectoral muscles", "Multiple dark red hematomas in abdominal muscles"],
         0, "Glutathione peroxidase (Se-dependent) and Vitamin E protect cell membranes from lipid peroxidation; deficiency causes calcium influx, mitochondrial calcification, and Zenker's degeneration, producing chalky pale muscle streaks.",
         True, "Musculoskeletal Pathology (ICAR PG PYQ)"),

        ("Canine Masticatory Muscle Myositis (MMM) is an autoimmune myopathy targeting the temporalis and masseter muscles, caused by autoantibodies directed against:",
         ["Type 2M muscle myosin fibers", "Type 1 slow-twitch fibers", "Acetylcholine receptors", "Dystrophin-associated glycoproteins"],
         0, "The muscles of mastication (temporalis, masseter) are derived from the first branchial arch and uniquely express Type 2M myosin; autoantibodies against 2M fibers produce severe acute swelling, eosinophilic/lymphocytic inflammation, and subsequent trismus.",
         True, "Musculoskeletal Pathology (ICAR PG PYQ)"),

        ("Equine Exertional Rhabdomyolysis ('Azoturia' / 'Monday Morning Disease' / 'Tying-Up') is characterized by acute myonecrosis accompanied by which diagnostic urine abnormality?",
         ["Dark red to brown urine containing Myoglobin (myoglobinuria) without intact erythrocytes in urine sediment", "Bright yellow urine with bilirubinuria", "Chyluria with free lipid droplets", "Milky urine loaded with struvite crystals"],
         0, "Exertional breakdown of glycogen-stored muscle fibers produces acute rhabdomyolysis and release of myoglobin into the circulation. Myoglobin passes the glomerulus, imparting a dark brown/port-wine color to the urine (myoglobinuria).",
         True, "Musculoskeletal Pathology (ICAR PG PYQ)"),

        ("Fibrous Osteodystrophy ('Rubber Jaw' / Osteodystrophia fibrosa) in dogs and horses is a metabolic bone disorder caused by:",
         ["Prolonged secondary hyperparathyroidism (renal in dogs, nutritional in horses) stimulating excessive osteoclastic bone resorption and replacement by fibrovascular stroma", "Primary dietary deficiency of calcium in adult horses", "Excessive secretion of calcitonin by C cells", "Lead poisoning"],
         0, "Chronic renal disease (retention of phosphate, reduced calcitriol) or diets with low Ca / high P (e.g. bran diets in horses / 'big head') triggers parathyroid hyperplasia and high PTH, causing osteoclasts to resorb cortical bone of the jaws, replaced by loose fibrous tissue.",
         True, "Skeletal Pathology (ICAR PG PYQ)"),

        ("Hypertrophic Osteopathy (Marie's Disease) in dogs is characterized by bilateral symmetrical, periosteal new bone formation along the diaphysis of distal limb bones, triggered by:",
         ["A space-occupying intrathoracic mass (such as pulmonary neoplasm or granuloma) stimulating reflex vagal neurovascular proliferation", "Primary bacterial osteomyelitis caused by Brucella canis", "Congenital growth hormone deficiency", "Deficiency of Vitamin C"],
         0, "Thoracic masses stimulate sensory fibers of the vagus nerve, initiating a neural reflex that increases blood flow and connective tissue periosteal proliferation in the distal extremities (metacarpals, metatarsals, radius, tibia).",
         True, "Skeletal Pathology (ICAR PG PYQ)"),

        ("In dogs, Osteochondrosis Dissecans (OCD) represents a focal failure of endochondral ossification leading to cartilage cleft formation and joint mice, with the most common anatomical site being the:",
         ["Caudal aspect of the humeral head", "Distal lateral condyle of the femur", "Medial malleolus of the tibia", "Trochlea of the talus"],
         0, "In rapidly growing large-breed dogs, ischemic necrosis of growing articular cartilage leads to failure of mineralization, fissure formation, and detachment of a cartilage flap ('dissecans') most commonly on the caudal humeral head.",
         True, "Skeletal Pathology (ICAR PG PYQ)"),

        # 41-50: Endocrine & Special pathology
        ("Pituitary Pars Intermedia Dysfunction (PPID / Equine Cushing's Disease) in aged horses is caused by:",
         ["Loss of dopaminergic inhibitory input from the hypothalamus due to neurodegeneration, causing adenoma or hyperplasia of the pars intermedia producing POMC peptides", "Primary functional adrenocortical adenoma", "Iatrogenic corticosteroid administration", "Thyroid follicular carcinoma"],
         0, "PPID results from oxidative damage and loss of periventricular dopaminergic neurons that normally tonically inhibit the pars intermedia; melanotrophs undergo hyperplasia/adenoma, oversecreting CLIP, ACTH, and beta-endorphins, causing hirsutism and laminitis.",
         True, "Endocrine Pathology (ICAR PG PYQ)"),

        ("Canine Hypoadrenocorticism (Addison's Disease) is characterized by bilateral idiopathic atrophy of the adrenal cortex, leading to the diagnostic electrolyte hallmark of:",
         ["Hyponatremia and Hyperkalemia with a Na+:K+ ratio dropping below 27:1 (or 20:1)", "Hypernatremia and Hypokalemia", "Severe hypercalcemia with normal sodium", "Hypomagnesemia with hyperphosphatemia"],
         0, "Immune-mediated destruction of all three adrenocortical zones depletes aldosterone (zona glomerulosa) and cortisol (zona fasciculata); lack of aldosterone impairs renal Na+ reabsorption and K+ excretion, plummeting the Na+:K+ ratio.",
         True, "Endocrine Pathology (ICAR PG PYQ)"),

        ("In diabetic cats, the underlying pancreatic pathology responsible for Type 2 diabetes mellitus is characterized by:",
         ["Deposition of Islet Amyloid Polypeptide (IAPP / Amylin) causing progressive loss of beta cells in the islets of Langerhans", "Acute necrotizing hemorrhagic pancreatitis", "Complete congenital agenesis of the pancreas", "Autoimmune destruction by anti-insulin antibodies"],
         0, "Feline Type 2 diabetes mellitus is strongly associated with co-secretion of amylin with insulin by beta cells; amylin aggregates into toxic oligomers and amyloid fibrils that replace and destroy beta cells.",
         True, "Endocrine Pathology (ICAR PG PYQ)"),

        ("Primary hyperparathyroidism in dogs is most frequently caused by a:",
         ["Solitary functional benign parathyroid adenoma of chief cells", "Malignant parathyroid carcinoma with lung metastasis", "Dietary calcium excess", "Diffuse C-cell hyperplasia"],
         0, "In >85% of canine primary hyperparathyroidism cases, a single benign chief cell adenoma autonomous oversecretes PTH, driving hypercalcemia, hypophosphatemia, and extensive metastatic mineralization.",
         False, "Endocrine Pathology"),

        ("In dogs, Sertoli Cell Tumor of the testis produces a paraneoplastic feminization syndrome caused by secretion of:",
         ["Estrogen (and inhibin)", "Testosterone", "Progesterone", "Thyroxine"],
         0, "Sertoli cell tumors (especially in cryptorchid testes) synthesize and release estrogens, causing gynecomastia, pendulous prepuce, bilateral symmetrical endocrine alopecia, squamous metaplasia of the prostate, and potential bone marrow aplasia.",
         True, "Genital Pathology (ICAR PG PYQ)"),

        ("The primary macroscopic lesion of 'Infectious Bovine Keratoconjunctivitis' (IBK / 'Pinkeye') caused by Moraxella bovis is:",
         ["Central corneal ulceration, marked corneal edema ('steamy cornea'), and deep neovascularization", "Subretinal hemorrhage without corneal involvement", "Complete ossification of the lens", "Atrophy of the optic chiasm"],
         0, "Moraxella bovis utilizes type IV pili and RTX hemolysin/cytotoxin (Mbx) to lyse corneal epithelial cells, producing an acute central corneal ulcer surrounded by dense inflammatory edema and perilimbal vascular infiltration.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("Panophthalmitis differs pathologically from Endophthalmitis in that Panophthalmitis:",
         ["Involves purulent inflammation extending beyond the ocular cavities into the fibrous tunics (sclera and cornea)", "Is strictly limited to the anterior and posterior chambers", "Involves only the crystalline lens", "Is exclusively caused by viral agents"],
         0, "Endophthalmitis is purulent inflammation of the intraocular cavities (aqueous and vitreous humors) sparing the ocular coats; Panophthalmitis is extensive inflammation extending into the cornea, sclera, and surrounding orbital tissues.",
         False, "Systemic Pathology"),

        ("In cattle, 'Hydrops Allantois' (Hydrallantois) is distinguished from 'Hydrops Amnii' (Hydramnios) because Hydrallantois:",
         ["Involves massive, rapid accumulation of fluid (up to 150-200 L) within the allantoic sac due to adventitious placentation or maternal vascular pathology", "Is a slow accumulation of amniotic fluid due to a fetal monster unable to swallow", "Always results in delivery of a normal viable calf", "Involves no uterine enlargement"],
         0, "Hydrallantois is a maternal-placental defect where inadequate caruncles (adventitious placentation) impair transplacental electrolyte transport, rapidly accumulating 100-200 liters of watery allantoic fluid in late gestation.",
         True, "Genital Pathology (ICAR PG PYQ)"),

        ("In dogs, Canine Atopic Dermatitis (CAD) is pathologically characterized as which type of hypersensitivity reaction?",
         ["Type I hypersensitivity (IgE-mediated mast cell degranulation) along with late-phase Th2-driven cutaneous inflammation", "Type II cytotoxic hypersensitivity", "Type III immune-complex vasculitis", "Type IV delayed-type granulomatous hypersensitivity"],
         0, "CAD is a genetically predisposed allergic pruritic dermatopathy triggered by environmental allergens penetrating a defective epidermal barrier, binding allergen-specific IgE on dermal mast cells and triggering histamine/cytokine release.",
         True, "Integumentary Pathology (ICAR PG PYQ)"),

        ("The distinctive histological hallmark of Pemphigus Foliaceus in dogs and horses is the formation of:",
         ["Subcorneal pustules containing intact and degenerate neutrophils alongside Acantholytic Keratinocytes", "Subepidermal bullae with complete detachment of the basal layer", "Dense perivascular cuffing by eosinophils in deep dermis without epidermal lesions", "Diffuse granulomas in subcutaneous fat"],
         0, "Autoantibodies (IgG) bind desmocollin-1 (or desmoglein-1) in desmosomes of the upper epidermis, disrupting intercellular adhesion (acantholysis); detached, round, nucleated keratinocytes float freely inside subcorneal pustules.",
         True, "Integumentary Pathology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module4_questions()
    print(f"Pathology Module 4 loaded: {len(qs)} questions")
