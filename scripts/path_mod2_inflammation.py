# scripts/path_mod2_inflammation.py
# Module 2: Infectious Pathology & Pathognomonic Lesions (50 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II

def get_module2_questions():
    qs = [
        # 1-10: Classical bacterial lesions & pathognomonic findings
        ("The pathognomonic gross lesion of Classical Swine Fever (Hog Cholera) seen in the spleen of affected pigs is:",
         ["Marginal, wedge-shaped, hemorrhagic splenic infarcts", "Diffuse splenomegaly with soft blackberry jam pulp", "Extensive caseous granulomas in red pulp", "Total splenic atrophy with capsular wrinkling"],
         0, "Marginal splenic infarcts (dark red, elevated, wedge-shaped areas along the borders of the spleen) occur due to pestivirus-induced endothelial necrosis and microvascular thrombosis, pathognomonic of Classical Swine Fever.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("The distinctive 'onion-ring' appearance (concentric lamellae of fibrous tissue around dry caseous necrosis) in lymph nodes is pathognomonic for:",
         ["Caseous Lymphadenitis in sheep and goats (Corynebacterium pseudotuberculosis)", "Bovine Farcy (Mycobacterium farcinogenes)", "Glanders in horses (Burkholderia mallei)", "Strangles in horses (Streptococcus equi)"],
         0, "In sheep and goats, Corynebacterium pseudotuberculosis produces slowly progressive concentric waves of caseation necrosis encased by fibrous capsules, imparting a characteristic laminated onion-ring pattern in lymph nodes.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("In cattle affected by Contagious Bovine Pleuropneumonia (CBPP), the pathognomonic 'marbled lung' appearance is produced by:",
         ["Severe widening of interlobular septa by serofibrinous exudate and lymph thrombi alongside hepatized lung lobules in various stages", "Diffuse granulomatous consolidation with extensive Langhans giant cells", "Diffuse emphysema with rupture of alveolar septa", "Multifocal pulmonary abscesses caused by Trueperella pyogenes"],
         0, "Mycoplasma mycoides subsp. mycoides causes severe serofibrinous pleuropneumonia with marked distension of interlobular septa (interstitial edema and thrombosis of lymph vessels) surrounding lobules showing red, grey, and necrotic hepatization.",
         True, "Respiratory Pathology (ICAR PG PYQ)"),

        ("The 'sulfur granules' found within pus discharging from chronic granulomatous lesions in cattle with 'Lumpy Jaw' are macroscopic colonies of:",
         ["Actinomyces bovis surrounded by Splendore-Hoeppli material", "Actinobacillus lignieresii", "Staphylococcus aureus", "Trueperella pyogenes"],
         0, "Actinomyces bovis causes rarefying osteomyelitis of the mandible. Pus contains firm, yellowish-white gritty particles ('sulfur granules') that microscopically consist of tangled Gram-positive filaments surrounded by club-shaped eosinophilic precipitates.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("In Johne's Disease (Paratuberculosis) in cattle, the corrugated mucosal folds of the ileum that cannot be smoothed out by stretching result from infiltration of the lamina propria by:",
         ["Sheets of epithelioid macrophages packed with acid-fast bacilli and multinucleated giant cells", "Dense infiltrates of eosinophils and mast cells", "Extensive fibrous scar tissue in the muscularis layer", "Hyperplastic crypts of Lieberkühn"],
         0, "Mycobacterium avium subsp. paratuberculosis multiplies inside macrophages within the ileal lamina propria and submucosa, inducing a diffuse non-caseating granulomatous enteritis with thick, cerebriform mucosal corrugations.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("The primary diagnostic finding in tissues from cattle dying acutely of Anthrax is:",
         ["Complete failure of blood to clot, lack of rigor mortis, dark tarry blood from orifices, and marked splenomegaly", "Extensive fibrinous pericarditis and lung marbling", "Multiple button ulcers in the cecum", "Severe caseous necrosis of mesenteric lymph nodes"],
         0, "Bacillus anthracis causes fulminant septicemia, release of lethal and edema toxins, vascular endothelial destruction, and extensive hemolysis, resulting in uncoagulated tarry black blood, absent rigor mortis, and massive splenic engorgement.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("The dark, dry, crepitant skeletal muscle lesion emitting a characteristic 'rancid butter' odor in calves suffering from Blackleg is caused by:",
         ["Clostridium chauvoei", "Clostridium septicum", "Clostridium novyi", "Clostridium perfringens Type D"],
         0, "Spores of Clostridium chauvoei germinate in damaged muscle, releasing necrotizing, hemolytic, and saccharolytic toxins that ferment muscle glycogen, generating gas bubbles (crepitation) and volatile butyric acid ('rancid butter' odor).",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("The specific histological lesion in the brain of sheep suffering from Listeriosis ('Circling disease') consists of:",
         ["Microabscesses in the brainstem (medulla oblongata and pons) with perivascular mononuclear cuffing", "Laminar cortical necrosis in the cerebral cortex", "Extensive vacuolation of the neuropil in the obex", "Demyelinating plaques in the cerebellar peduncles"],
         0, "Listeria monocytogenes ascends the trigeminal and facial nerves to the brainstem, producing localized focal suppurative encephalitis with characteristic neutrophilic microabscesses and mononuclear perivascular cuffs.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("In 'Black Disease' (Infectious Necrotic Hepatitis) of sheep, the trigger allowing Clostridium novyi Type B spores to germinate in the liver is:",
         ["Parenchymal necrosis and anaerobic tracts created by migrating immature Fasciola hepatica flukes", "Severe biliary obstruction by adult Dicrocoelium dendriticum", "Acute copper poisoning", "Massive ingestion of urea"],
         0, "Migrating immature Fasciola hepatica flukes produce necrotic migratory tracts in the hepatic parenchyma, creating localized anaerobic zones where dormant C. novyi Type B spores germinate and elaborate lethal alpha-toxin.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("The pathognomonic renal lesion observed at necropsy in sheep dying of Enterotoxemia (Pulpy Kidney disease) is:",
         ["Rapid post-mortem cortical liquefaction and softening of the kidneys ('pulpy kidney')", "Multiple wedge-shaped pale infarcts in the renal cortex", "Ascending suppurative pyelonephritis with hydronephrosis", "Severe glomerular amyloidosis"],
         0, "Clostridium perfringens Type D produces epsilon toxin (activated by intestinal trypsin), which increases capillary permeability, causes hyperglycemia/glucosuria, and accelerates post-mortem autolysis of the renal cortex into a soft, mushy pulp.",
         True, "Systemic Pathology (ICAR PG PYQ)"),

        # 11-20: Viral pathognomonic lesions, inclusion bodies
        ("Negri bodies, the pathognomonic intracytoplasmic viral inclusion bodies of Rabies, are most reliably demonstrated in carnivores in which neuroanatomical structure?",
         ["Ammon's horn (Hippocampus)", "Purkinje cell layer of the cerebellum", "Motor neurons of the ventral horn of the spinal cord", "Occipital cerebral cortex"],
         0, "Negri bodies are sharply defined, eosinophilic, round-to-oval intracytoplasmic inclusion bodies. They are located with highest frequency in hippocampal pyramidal neurons in dogs and cats, and cerebellar Purkinje cells in cattle and herbivores.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("In young calves that die acutely of Foot and Mouth Disease (FMD) without developing the classic vesicular stomatitis, the cause of death is:",
         ["Severe acute necrotizing myocarditis producing a 'tiger heart' (cor tigrinum)", "Fulminant hemorrhagic gastroenteritis", "Acute interstitial pulmonary emphysema", "Severe nephrotic renal failure"],
         0, "The aphthovirus has high affinity for immature cardiomyocytes in calves, producing acute multifocal non-suppurative necrotizing myocarditis with pale grayish-yellow necrotic streaks on the epicardium and myocardium ('tiger heart').",
         True, "Cardiovascular Pathology (ICAR PG PYQ)"),

        ("The pathognomonic microscopic finding in the liver of dogs suffering from Infectious Canine Hepatitis (CAV-1) is the presence of:",
         ["Large basophilic intranuclear inclusion bodies within hepatocytes and Kupffer cells", "Eosinophilic intracytoplasmic inclusions in biliary epithelial cells", "Perivascular eosinophilic cuffs in portal triads", "Negri bodies in hepatic stellate cells"],
         0, "Canine Adenovirus 1 (CAV-1) infects hepatocytes and endothelial cells, causing centrilobular hepatic necrosis and pathognomonic large, centrally located basophilic or amphophilic intranuclear inclusion bodies.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("Intracytoplasmic inclusion bodies termed 'Bollinger bodies' containing smaller elementary bodies ('Borrel bodies') are pathognomonic for:",
         ["Fowl Pox (Avipoxvirus)", "Marek's Disease", "Infectious Laryngotracheitis", "Avian Encephalomyelitis"],
         0, "Fowl pox virus produces large, eosinophilic, lipid-rich intracytoplasmic inclusion bodies (Bollinger bodies) in hyperplastic epidermal cells; inside them reside the actual infectious virions known as Borrel bodies.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Canine Distemper Virus (CDV) is uniquely recognized in veterinary histopathology because it produces:",
         ["Both intracytoplasmic and intranuclear eosinophilic inclusion bodies", "Exclusively intranuclear basophilic inclusions", "Exclusively intracytoplasmic inclusion bodies in hepatocytes only", "No inclusion bodies of any type"],
         0, "Canine Distemper Virus (Morbillivirus) infects epithelial, lymphoid, and neural tissues, producing diagnostic eosinophilic inclusion bodies both in the cytoplasm and in the nucleus (e.g. in bladder transitional epithelium, astrocytes, neurons).",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("In calves with Poxvirus infection (Bovine Papular Stomatitis), histological examination of oral mucosal lesions reveals:",
         ["Intracytoplasmic eosinophilic inclusion bodies within hydropic, ballooned keratinocytes", "Cowdry Type A intranuclear inclusion bodies", "Epithelioid granulomas with Langhans giant cells", "Diffuse purulent microabscesses in submucosa"],
         0, "Parapoxviruses cause ballooning degeneration of keratinocytes in the stratum spinosum with pathognomonic intracytoplasmic, eosinophilic, halo-surrounded inclusion bodies.",
         False, "Infectious Pathology"),

        ("Infectious Laryngotracheitis (ILT) of chickens is pathologically characterized by acute hemorrhagic tracheitis with pathognomonic:",
         ["Intranuclear eosinophilic inclusion bodies (Cowdry Type A) in syncytial tracheal epithelial cells", "Intracytoplasmic Bollinger bodies", "Intracytoplasmic Negri-like inclusions", "Basophilic inclusion bodies in hepatocytes"],
         0, "Gallid alphaherpesvirus 1 induces syncytial giant cell formation in tracheal mucosa with pathognomonic Cowdry Type A intranuclear eosinophilic inclusions during early stages (up to 4-5 days post-infection).",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In Canine Parvoviral enteritis (CPV-2), the virus selectively causes necrosis and collapse of which anatomical compartment of the intestine?",
         ["Crypts of Lieberkühn (crypt epithelium)", "Villus tips exclusively", "Muscularis externa", "Serosal mesothelium"],
         0, "Parvoviruses require cells in the S-phase of the cell cycle to replicate. CPV-2 targets the rapidly proliferating intestinal crypt cells of Lieberkühn, leading to crypt necrosis, failure of enterocyte replacement, villus collapse, and hemorrhagic enteritis.",
         True, "Systemic Pathology (ICAR PG PYQ)"),

        ("Persistent Bovine Viral Diarrhea Virus (BVDV) infection leads to fatal 'Mucosal Disease' when:",
         ["A persistently infected (PI) non-cytopathic animal is superinfected by or mutates to a homologous cytopathic (CP) BVDV strain", "A seropositive adult cow is infected by Bovine Herpesvirus-1", "The animal receives an inactivated BVD vaccine", "The animal develops chronic copper poisoning"],
         0, "Mucosal disease occurs exclusively in immunotolerant persistently infected (PI) cattle carrying non-cytopathic (ncp) BVDV; when a mutation generates or superinfection introduces a homologous cytopathic (cp) strain, acute systemic epithelial necrosis occurs.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("The gross post-mortem lesion of 'button ulcers' in the cecum and colon of swine suffering from chronic Classical Swine Fever results from:",
         ["Ischemic necrosis around mucosal lymphoid follicles followed by secondary bacterial invasion (Salmonella)", "Direct invasion by Balantidium coli cysts", "Heavy infestation by Oesophagostomum dentatum larvae", "Mycotic invasion by Aspergillus fumigatus"],
         0, "Button ulcers represent concentric circular sloughs of necrotic mucosa over ileocecal and colonic lymphoid patches where pestivirus-induced microvascular infarction allows secondary bacterial saprophytes to produce laminated necrotic plaques.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        # 21-30: Classical pathology of other livestock diseases
        ("The 'water deprivation / salt poisoning' syndrome in pigs is characterized by which pathognomonic microscopic lesion in the cerebral cortex?",
         ["Eosinophilic meningoencephalitis with laminar cortical necrosis", "Suppurative microabscesses in the medulla", "Extensive vacuolation of the neuropil without inflammation", "Demyelination of the corpus callosum"],
         0, "Hypernatremia followed by unrestricted water intake causes cerebral edema and a pathognomonic heavy infiltration of eosinophils in the meninges and perivascular spaces of cerebral sulci, leading to laminar necrosis.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("In horses with Glanders (Burkholderia mallei), the cutaneous manifestation characterized by nodular lesions along lymphatic vessels that ulcerate and discharge oily honey-like pus is known as:",
         ["Farcy (Farcy pipes and Farcy buds)", "Guttural pouch mycosis", "Dourine", "African Horse Sickness"],
         0, "Cutaneous glanders is historically called 'Farcy'. Nodules along subcutaneous lymph vessels are 'farcy buds', and the thickened, cord-like, ulcerated lymphatics are referred to as 'farcy pipes'.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("The Straus reaction, used historically as an in vivo diagnostic test for Burkholderia mallei, is characterized by:",
         ["Acute purulent orchitis and periorchitis in male guinea pigs following intraperitoneal inoculation", "Sudden death of mice within 6 hours with splenomegaly", "Keratoconjunctivitis in rabbits", "Localized dermal necrosis in calves"],
         0, "Intraperitoneal injection of clinical material containing Burkholderia mallei into male guinea pigs produces intense purulent orchitis and scrotal enlargement within 2-4 days (positive Straus reaction).",
         True, "Diagnostic Pathology (ICAR PG PYQ)"),

        ("The characteristic lesion of 'laminar cortical necrosis' (autofluorescence of the cerebral cortex under UV light at 365 nm) in ruminants is pathognomonic for:",
         ["Polioencephalomalacia (PEM / Cerebrocortical Necrosis CCN)", "Bovine Spongiform Encephalopathy (BSE)", "Enterotoxemia", "Lead poisoning"],
         0, "PEM results from thiamine deficiency or high dietary sulfur intake. Dead cortical neurons and necrotic neuropil undergo liquefactive necrosis and exhibit diagnostic autofluorescence under 365 nm UV light.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("In Bovine Spongiform Encephalopathy (BSE), the hallmark histopathological lesion is:",
         ["Bilateral symmetrical spongiform vacuolation of neuronal perikarya and neuropil in the obex of the medulla oblongata without inflammatory infiltration", "Severe non-suppurative lymphoplasmacytic meningoencephalitis with perivascular cuffing", "Extensive purulent microabscesses with gliosis in the midbrain", "Focal demyelination with gitter cell infiltration in the cerebellum"],
         0, "Prion accumulation causes neurodegeneration without any inflammatory response, producing pathognomonic round, empty vacuoles inside the neuronal cytoplasm and gray matter neuropil, especially in the solitary tract nucleus of the obex.",
         True, "Neuropathology (ICAR PG PYQ)"),

        ("Equine Infectious Anemia (EIA / Swamp Fever) is characterized by intravascular hemolysis and erythrophagocytosis caused by:",
         ["Lentivirus-induced immune-mediated destruction of erythrocytes coated with antibody and complement", "Direct erythrocytic lysis by bacterial hemolysins", "Severe dietary iron deficiency", "Babesia caballi merozoite multiplication"],
         0, "EIA is a Lentivirus infection where chronic antigenic drift produces immune complexes that adhere to erythrocyte membranes, triggering complement-mediated hemolysis and massive phagocytosis by splenic and hepatic macrophages.",
         True, "Hemolymphatic Pathology (ICAR PG PYQ)"),

        ("The primary macroscopic necropsy finding in cattle with acute Pteridium aquilinum (Bracken fern) poisoning is:",
         ["Severe bone marrow aplasia leading to widespread hemorrhages, thrombocytopenia, and urinary bladder enzootic hematuria", "Massive hepatic cirrhosis with ascites", "Diffuse osteomalacia with spontaneous fractures", "Ulcerative stomatitis with bloat"],
         0, "Bracken fern contains ptaquiloside, a radiomimetic toxin that destroys hematopoietic progenitor cells in the bone marrow, causing severe thrombocytopenia, leukopenia, and widespread hemorrhages, alongside bladder transitional cell carcinoma in chronic forms.",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("The distinctive histological feature of 'Wooden Tongue' in cattle caused by Actinobacillus lignieresii is:",
         ["Granulomatous glossitis with Splendore-Hoeppli phenomenon around Gram-negative coccobacilli in soft tissue", "Suppurative osteomyelitis of the mandible with sulfur granules", "Focal coagulative necrosis of the ruminal mucosa", "Severe interstitial glossal amyloidosis"],
         0, "Unlike Actinomyces bovis (which invades bone and consists of Gram-positive branching rods), Actinobacillus lignieresii invades soft tissues (especially the tongue) and consists of Gram-negative rods forming granules with radiating eosinophilic clubs.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        ("In sheep and goats, Caprine Arthritis Encephalitis (CAE) and Maedi-Visna are caused by Lentiviruses that produce chronic:",
         ["Interstitial pneumonia with prominent peribronchiolar lymphoid hyperplasia ('cuffing') and non-suppurative synovitis/encephalitis", "Purulent bronchopneumonia with pulmonary abscessation", "Fibrinous lobar pneumonia with marbling", "Granulomatous pleuritis with caseous necrosis"],
         0, "Small ruminant lentiviruses induce chronic lymphocytic-plasmacytic interstitial pneumonia (Maedi) with massive perivascular and peribronchiolar lymphoid cuffing, causing heavy, grayish-pink, non-collapsing lungs.",
         True, "Respiratory Pathology (ICAR PG PYQ)"),

        ("A definitive post-mortem diagnosis of African Swine Fever (ASF) is differentiated from Classical Swine Fever (CSF) primarily by the presence of:",
         ["Extremely severe, friable, dark-red/black splenomegaly (megalospleen) enlarged up to 3 to 6 times normal size with extensive hemorrhage", "Marginal splenic infarcts on normal-sized spleen", "Button ulcers in the colon exclusively", "Absence of any visceral lymph node hemorrhages"],
         0, "Both pestivirus and asfavirus cause hemorrhages, but ASF causes extreme, friable hemorrhagic splenomegaly (gorged with uncoagulated blood, enlarged 3-6x) and severe hemorrhagic necrosis of gastrohepatic and renal lymph nodes resembling blood clots.",
         True, "Infectious Pathology (ICAR PG PYQ)"),

        # 31-40: Avian infectious pathology details
        ("In poultry, Marek's Disease is distinguished from Avian Leukosis at necropsy by which of the following pathognomonic features?",
         ["Unilateral enlargement and loss of cross-striations of peripheral nerves (sciatic, brachial) and lack of bursal enlargement", "Tumorous nodular enlargement of the Bursa of Fabricius in birds under 14 weeks", "Exclusive involvement of bone marrow without visceral lesions", "Absence of T-lymphocyte infiltration"],
         0, "Marek's Disease is a herpesvirus-induced T-cell lymphoma that characteristically causes enlargement of peripheral nerves (sciatic nerve 2-3x normal with loss of striations), whereas Avian Leukosis (retrovirus) is a B-cell lymphoma that almost invariably produces nodular bursal tumors.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The primary target organ and earliest gross lesion in chickens suffering from acute Infectious Bursal Disease (IBD / Gumboro) is:",
         ["Bursa of Fabricius, which is enlarged, edematous, hyperemic, and covered with a gelatinous yellowish transudate", "Thymus, which undergoes complete calcification", "Proventriculus, which develops perforated ulcers", "Spleen, which undergoes total atrophy on day 1"],
         0, "IBD virus destroys dividing B-lymphocytes in the Bursa of Fabricius; by day 3-4 post-infection, the bursa is markedly enlarged (double normal weight), edematous, hyperemic, and often hemorrhagic, followed by rapid atrophy by day 8.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The pathognomonic macroscopic lesion in the alimentary tract of chickens infected with velogenic viscerotropic Newcastle Disease (vvND) is:",
         ["Pinpoint petechial hemorrhages on the tips of the proventricular papillae and necrotic button-like ulcers on cecal tonsils", "Diffuse fibrous stricture of the gizzard", "Caseous diphtheritic plaques confined to the cloaca", "Extensive pseudomembranous enteritis of the duodenal loop only"],
         0, "Velogenic viscerotropic Newcastle disease produces severe hemorrhagic lesions on the tips of proventricular papillae, along with hemorrhagic necrotizing enteritis over intestinal lymphoid aggregates and cecal tonsils.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In layer hens, infection with nephropathogenic strains of Infectious Bronchitis Virus (IBV) causes which combination of pathology?",
         ["Swollen pale kidneys with tubules distended with urates, along with cystic oviducts producing watery albumin and wrinkled eggshells ('false layers')", "Fibrinous pericarditis and perihepatitis with intact kidneys", "Severe granulomatous osteomyelitis with normal egg laying", "Exclusive enlargement of the sciatic nerve"],
         0, "Nephropathogenic IBV strains target renal tubular epithelium, producing severe interstitial nephritis with chalky urates; damage to the developing oviduct causes 'false layers' and misshapen, thin-shelled, rough eggs with watery albumen.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("Hydropericardium Syndrome ('Litchi Heart Disease' / Angara Disease) in broiler chicks is caused by:",
         ["Fowl Adenovirus serotype 4 (FAdV-4)", "Avian Reovirus", "Chicken Anemia Virus", "Avian Metapneumovirus"],
         0, "FAdV-4 produces massive accumulation of clear straw-colored fluid (up to 10-20 mL) in the pericardial sac (resembling a peeled litchi fruit) along with swollen, friable, yellowish liver with basophilic intranuclear inclusions.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("In young chicks, 'Curled-Toe Paralysis' characterized by inward curling of the toes and sciatic nerve enlargement with demyelination is caused by deficiency of:",
         ["Vitamin B2 (Riboflavin)", "Vitamin B1 (Thiamine)", "Vitamin E (Tocopherol)", "Vitamin B6 (Pyridoxine)"],
         0, "Riboflavin deficiency in chicks causes swelling and myelin degeneration of the sciatic and brachial nerves, resulting in walking on hocks with digits curled inward ('curled-toe paralysis').",
         True, "Nutritional Pathology (ICAR PG PYQ)"),

        ("'Crazy Chick Disease' (Nutritional Encephalomalacia) in broiler chicks is caused by deficiency of:",
         ["Vitamin E (frequently precipitated by high dietary unsaturated fatty acids)", "Vitamin A", "Vitamin C", "Vitamin K"],
         0, "Vitamin E deficiency causes free radical-mediated vascular thrombosis and ischemic liquefactive necrosis of the cerebellum in chicks, manifesting as ataxia, head retraction, backward falling ('crazy chick disease'), and petechiae on the cerebellum.",
         True, "Nutritional Pathology (ICAR PG PYQ)"),

        ("Avian Tuberculosis caused by Mycobacterium avium is distinguished from other avian granulomatous diseases by forming:",
         ["Non-calcifying caseous granulomas with abundant acid-fast bacilli predominantly in the liver, spleen, and intestines, with lungs rarely affected", "Heavily calcified pulmonary nodules like in human TB", "Exclusive involvement of the comb and wattles", "Massive neutrophilic abscesses in the bursa"],
         0, "Unlike mammalian TB, avian TB granulomas typically do not undergo calcification; because infection is oral, lesions predominate in the intestines, liver, and spleen, while the avian respiratory tract is relatively spared.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The distinctive pathological finding in 'Fowl Cholera' (Pasteurella multocida) in turkeys and chickens at necropsy is:",
         ["Petechial hemorrhages on the epicardium and proventricular fat, multiple focal necrotic white spots in the liver, and consolidated lungs", "Severe thickening and corrugation of the colon mucosa", "Multiple osteochondromas in the tibiotarsus", "Enlarged Bursa of Fabricius with caseous plug"],
         0, "Acute fowl cholera produces vascular endothelial damage and bacteremia, resulting in petechiae on the heart, fibrinous perihepatitis, and pathognomonic miliary white pinpoint necrotic foci throughout the liver parenchyma.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        ("The 'colisepriceptic triad' observed at necropsy in broiler chickens suffering from systemic Escherichia coli infection comprises:",
         ["Fibrinous pericarditis, fibrinous perihepatitis, and fibrinous air sacculitis", "Gastritis, enteritis, and colitis", "Myocarditis, endocarditis, and vasculitis", "Nephritis, cystitis, and ureteritis"],
         0, "In broiler chickens, systemic colibacillosis (often secondary to Mycoplasma gallisepticum airsacculitis or IBV) produces the classical diagnostic triad: fibrinous pericarditis, fibrinous perihepatitis, and air sacculitis.",
         True, "Avian Pathology (ICAR PG PYQ)"),

        # 41-50: Parasitic pathology & clinical pathology
        ("In cattle, 'Morocco leather' appearance (nodular cobblestone appearance of the abomasal mucosa) is pathognomonic for:",
         ["Ostertagia ostertagi (Ostertagiasis)", "Haemonchus placei", "Trichostrongylus axei", "Cooperia oncophora"],
         0, "Larvae of Ostertagia ostertagi invade and develop within the gastric glands of the abomasum, causing mucosal hyperplasia, loss of parietal cells (hypochlorhydria), and pathognomonic 1-2 mm nodular mucosal umbilicated elevations resembling Morocco leather.",
         True, "Parasitic Pathology (ICAR PG PYQ)"),

        ("Pipe-stem liver (extensive periductal fibrosis and calcification of bile ducts) in cattle is caused by chronic infection with:",
         ["Fasciola hepatica (Liver fluke)", "Dicrocoelium dendriticum", "Paramphistomum cervi", "Schistosoma bovis"],
         0, "Chronic residence of adult Fasciola hepatica in the bile ducts induces mechanical irritation and proline secretion, causing marked adenomatous hyperplasia, severe concentric periductal fibrosis, and calcification ('pipe-stem liver').",
         True, "Parasitic Pathology (ICAR PG PYQ)"),

        ("In sheep, the gross lesion known as 'pimply gut' (multiple caseous or calcified submucosal nodules in the intestines) is caused by:",
         ["Oesophagostomum columbianum (Nodular worm)", "Bunostomum trigonocephalum", "Nematodirus battus", "Chabertia ovina"],
         0, "Third-stage larvae of Oesophagostomum columbianum penetrate the intestinal wall, inciting a localized eosinophilic and granulomatous immune reaction that forms 2-5 mm caseocalcareous nodules ('pimply gut') in the submucosa.",
         True, "Parasitic Pathology (ICAR PG PYQ)"),

        ("In dogs with Canine Heartworm disease, Dirofilaria immitis adults predominantly inhabit:",
         ["Pulmonary arteries and right ventricle of the heart", "Left ventricle and ascending aorta", "Portal vein and caudal vena cava exclusively", "Coronary sinus and carotid artery"],
         0, "Adult Dirofilaria immitis reside in the pulmonary arterial trunk and right ventricle, inducing chronic pulmonary endarteritis, villous intimal proliferation, pulmonary hypertension, and cor pulmonale (right-sided congestive heart failure).",
         True, "Cardiovascular Pathology (ICAR PG PYQ)"),

        ("The pathognomonic post-mortem finding in sheep suffering from acute copper poisoning is:",
         ["Severe intravascular hemolysis, port-wine colored urine (hemoglobinuria), and a gun-metal dark spleen ('blackberry jam')", "Acute fibrinous pneumonia with marbling", "Extensive caseous lymphadenitis of mesenteric nodes", "Severe bilateral hydronephrosis"],
         0, "Chronic copper accumulation in the liver suddenly overwhelms lysosomal storage, causing massive release of copper into the bloodstream, severe oxidative hemolysis, hemoglobinuria, icterus, and a dark 'gun-metal' swollen spleen.",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("In horses, verminous arteritis and thrombosis of the cranial mesenteric artery resulting in thromboembolic colic is caused by migrating larvae of:",
         ["Strongylus vulgaris (4th-stage larvae)", "Strongylus edentatus", "Strongylus equinus", "Parascaris equorum"],
         0, "L4 larvae of Strongylus vulgaris migrate within the intima and media of the cranial mesenteric artery and its branches, causing arteritis, aneurysm, thrombosis, and subsequent intestinal ischemia and colic.",
         True, "Parasitic Pathology (ICAR PG PYQ)"),

        ("In dogs with chronic lead poisoning (plumbism), the pathognomonic histological lesion found in the kidneys is:",
         ["Acid-fast intranuclear inclusion bodies in renal proximal tubular epithelial cells", "Basophilic intracytoplasmic inclusions in glomeruli", "Extensive amyloid deposition in the mesangium", "Severe suppurative glomerulonephritis"],
         0, "Lead ions bind to non-histone nuclear proteins in renal proximal convoluted tubular cells, forming distinctive dense, acid-fast, intranuclear inclusion bodies (positive on Ziehl-Neelsen staining).",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("The characteristic post-mortem finding in cattle suffering from acute cyanide (HCN / prussic acid) poisoning (e.g. from immature sorghum ingestion) is:",
         ["Bright cherry-red blood that fails to clot normally and congestion of mucous membranes", "Dark chocolate-brown blood due to methemoglobinemia", "Pale, watery, translucent blood", "Thick tarry black blood with splenomegaly"],
         0, "Cyanide inhibits cytochrome c oxidase in the mitochondrial electron transport chain, blocking cellular oxygen utilization. Tissues cannot extract oxygen from blood, leaving venous blood fully saturated with oxyhemoglobin (bright cherry-red).",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("In contrast to cyanide, acute nitrate/nitrite poisoning in ruminants produces blood that is pathognomonic for having a:",
         ["Dark chocolate-brown color due to extensive conversion of hemoglobin to methemoglobin", "Bright cherry-red color", "Pale pink color with fat droplets", "Milky white lipemic appearance"],
         0, "Ruminal microbes reduce nitrate to nitrite, which oxidizes ferrous iron (Fe2+) in hemoglobin to ferric iron (Fe3+), forming methemoglobin. Methemoglobin cannot bind oxygen, turning blood a diagnostic dark chocolate-brown color.",
         True, "Toxicologic Pathology (ICAR PG PYQ)"),

        ("Sweating Sickness in calves is an acute epidermotrophic tick-borne toxicosis caused by the saliva of:",
         ["Hyalomma truncatum", "Rhipicephalus microplus", "Amblyomma hebraeum", "Haemaphysalis bispinosa"],
         0, "Sweating sickness is an epitheliotropic toxicosis of cattle produced by an epitheliotrophic toxin secreted in the saliva of the bont-legged tick, Hyalomma truncatum, causing hyperhidrosis and extensive moist eczema.",
         True, "Infectious Pathology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module2_questions()
    print(f"Pathology Module 2 loaded: {len(qs)} questions")
