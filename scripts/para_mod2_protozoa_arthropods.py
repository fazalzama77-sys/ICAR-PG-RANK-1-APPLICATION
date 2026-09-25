# scripts/para_mod2_protozoa_arthropods.py
# Module 2: Veterinary Protozoology, Entomology & Acarology (30 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II (Sub-subject 13.4)

def get_module2_questions():
    qs = [
        # 1-10: Hemoprotozoa
        ("In bovine babesiosis ('Red Water' / Texas Cattle Fever), Babesia bigemina is differentiated morphologically in Giemsa-stained thin blood smears from Babesia bovis because Babesia bigemina is:",
         ["A large piroplasm (>2.5 µm) that pairs at an acute angle inside the erythrocyte", "A small piroplasm (<1.5 µm) pairing at an obtuse angle centrally", "A signet-ring intra-erythrocytic schizont", "A motile flagellated trypomastigote"],
         0, "Babesia bigemina is a large piroplasm (approx. 4-5 µm long) typically seen as pairs of pear-shaped trophozoites joined at their pointed ends at an acute angle; Babesia bovis is small (approx. 1.5-2.0 µm) and pairs at an obtuse angle.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("The primary biological vector responsible for transmitting Babesia bigemina and Anaplasma marginale to cattle in India is the one-host tick:",
         ["Rhipicephalus (Boophilus) microplus", "Hyalomma anatolicum", "Rhipicephalus sanguineus", "Argas persicus"],
         0, "Rhipicephalus (Boophilus) microplus is an obligate one-host ixodid tick in tropical and subtropical climates, transmitting Babesia bigemina via transovarial transmission across generations and Anaplasma marginale via transstadial/mechanical routes.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("Cerebral babesiosis in cattle, characterized by terminal hyperesthesia, paddling, convulsions, and cerebral capillary sludging / sequestration of parasitized RBCs, is uniquely caused by:",
         ["Babesia bovis", "Babesia bigemina", "Theileria annulata", "Trypanosoma theileri"],
         0, "Babesia bovis induces surface modifications on infected erythrocytes that bind endothelial adhesion receptors (cytoadherence), leading to microvascular sludge, brain ischemia, and fatal cerebral babesiosis; brain squash smear is the diagnostic post-mortem method of choice.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("In Tropical Bovine Theileriosis caused by Theileria annulata, the diagnostic hallmark observed in Giemsa-stained lymph node biopsy smears is the presence of:",
         ["Koch's Blue Bodies (Macroschizonts within transformed mononuclear leukocytes)", "Negri bodies in neural tissue", "Leishman-Donovan bodies in neutrophils", "Signet-ring trophozoites in plasma"],
         0, "Theileria annulata sporozoites invade naive B cells and macrophages, transforming them into proliferative lymphoblastic cells harboring multi-nucleated multinucleate macroschizonts ('Koch's Blue Bodies'), which stain characteristic purplish-blue with Giemsa.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("The principal vector transmitting Tropical Theileriosis (Theileria annulata) to cattle in India through transstadial (stage-to-stage) transmission is:",
         ["Hyalomma anatolicum (Hyalomma anatolicum anatolicum)", "Rhipicephalus microplus", "Haemaphysalis bispinosa", "Amblyomma variegatum"],
         0, "Hyalomma anatolicum (a two- or three-host tick with striped legs and an ornate scutum) is the proven field vector of Theileria annulata in India; infection is acquired in the larval or nymphal stage and transmitted in the subsequent stage (transstadial).",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("The protozoan parasite causing 'Surra' in camels, horses, cattle, and dogs in India is:",
         ["Trypanosoma evansi", "Trypanosoma brucei", "Trypanosoma congolense", "Trypanosoma equiperdum"],
         0, "Trypanosoma evansi is the monomorphic salivarian trypanosome that causes Surra, causing recurrent paroxysmal fever, marked anemia, dependent edema, and death in domestic animals across Asia and Africa.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("The transmission of Trypanosoma evansi (Surra) in livestock is primarily non-cyclical and mechanical, mediated by the interrupted bites of:",
         ["Tabanus (Horse flies) and Stomoxys calcitrans (Stable flies)", "Tsetse flies (Glossina species)", "Culicoides midges", "Black flies (Simulium)"],
         0, "Unlike African trypanosomes which develop cyclically in Glossina, Trypanosoma evansi is transmitted mechanically through contaminated mouthparts of tabanid flies (Tabanus, Haematopota) and Stomoxys when feeding is interrupted on an infected host and resumed on a susceptible host.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("The venereally transmitted protozoan disease of equines known as 'Dourine' (Covering Sickness / Mal du Coit), characterized by edema of external genitalia and pathognomonic cutaneous 'Dollar Plaques' (Silver Dollar spots), is caused by:",
         ["Trypanosoma equiperdum", "Trypanosoma evansi", "Babesia caballi", "Theileria equi"],
         0, "Trypanosoma equiperdum is transmitted directly during coitus without requiring an insect vector; it causes genital discharge, ulceration, paraplegia, and circular edematous urticarial cutaneous plaques ('silver dollar plaques').",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("Bovine Anaplasmosis caused by Anaplasma marginale is clinically distinguished from Bovine Babesiosis (Babesia bigemina) by the:",
         ["Absence of hemoglobinuria (No red water) in Anaplasmosis despite severe extravascular hemolytic anemia", "Presence of bloody urine in Anaplasmosis only", "Rapid cerebral signs in Anaplasmosis", "Absence of fever in Babesiosis"],
         0, "Anaplasma marginale causes extravascular phagocytosis of damaged erythrocytes in the spleen and liver (no intravascular lysis), so hemoglobin is converted to bilirubin (causing profound icterus and anemia WITHOUT hemoglobinuria); Babesia causes massive intravascular hemolysis WITH acute hemoglobinuria ('red water').",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("Canine Visceral Leishmaniasis is transmitted biologically by the bite of phlebotomine sandflies, wherein the diagnostic intracellular stage residing within host macrophages is the:",
         ["Amastigote (Leishman-Donovan body / LD body)", "Promastigote", "Epimastigote", "Trypomastigote"],
         0, "In vertebrate macrophage cytoplasm, Leishmania infantum/donovani exists as a non-motile, oval, aflagellated amastigote (LD body, 2-4 µm) containing a nucleus and distinct rod-like kinetoplast; sandflies harbor the flagellated promastigote form in their proboscis.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        # 11-20: Enteric and Tissue Protozoa
        ("In poultry, acute cecal coccidiosis characterized by severe bloody droppings, high mortality, and coagulated blood cores distending both ceca in 3- to 6-week-old chicks is caused by:",
         ["Eimeria tenella", "Eimeria necatrix", "Eimeria acervulina", "Eimeria maxima"],
         0, "Eimeria tenella develops deep in the lamina propria and submucosa of the ceca; its large 2nd-generation schizonts disrupt mucosal capillaries, causing massive sloughing, exsanguinating hemorrhage, and solid cecal blood cores.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("The structural difference between a fully sporulated oocyst of the genus Eimeria versus the genus Isospora (Cystoisospora) is:",
         ["Eimeria contains 4 sporocysts with 2 sporozoites each (Total 8 sporozoites); Isospora contains 2 sporocysts with 4 sporozoites each (Total 8 sporozoites)", "Eimeria has 2 sporocysts; Isospora has 4 sporocysts", "Eimeria has no sporocysts", "Eimeria contains 16 sporozoites"],
         0, "Both genera yield 8 sporozoites per sporulated oocyst, but Eimeria packages them into 4 sporocysts containing 2 sporozoites each (Formula: 1 x 4 x 2 = 8), while Isospora packages them into 2 sporocysts containing 4 sporozoites each (Formula: 1 x 2 x 4 = 8).",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("Hepatic coccidiosis in domestic rabbits, characterized by multiple discrete yellowish-white nodular or cord-like lesions along the bile ducts and hepatomegaly, is caused by:",
         ["Eimeria stiedae", "Eimeria intestinalis", "Eimeria perforans", "Eimeria magna"],
         0, "Eimeria stiedae sporozoites penetrate intestinal mesenteric venules/lymphatics and migrate to the liver, parasitizing the epithelial lining of intrahepatic bile ducts, inciting massive papillomatous hyperplasia and creamy white biliary nodules containing millions of oocysts.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("Cryptosporidium parvum, an important cause of profuse watery diarrhea in neonatal calves (5-15 days of age) and immunodeficient humans, occupies which unique cellular niche in the enterocyte?",
         ["Intracellular but Extracytoplasmic (located in the microvillar brush border enclosed in a parasitophorous vacuole)", "Deep nuclear matrix", "Free in the intestinal lumen", "Inside the mitochondrial matrix"],
         0, "Cryptosporidium organisms are intracellular yet extracytoplasmic: they displace the host cell's microvilli and reside at the apical cell surface enveloped by host cell membrane, visible as tiny round 4-5 µm bodies staining acid-fast bright red with modified Ziehl-Neelsen stain.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("The definitive host of Toxoplasma gondii, which alone sheds unsporulated oocysts in feces that contaminate pastures, feed, and water, is the:",
         ["Domestic Cat and other members of the Felidae family", "Dog and canids", "Sheep and goats", "Cattle and equines"],
         0, "The sexual cycle (gametogony and oocyst formation) of Toxoplasma gondii occurs exclusively in the intestinal epithelium of felids (cats); all other warm-blooded vertebrates act as intermediate hosts developing asexual tissue cysts (bradyzoites) and tachyzoites.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("In pregnant ewes, abortion due to Toxoplasma gondii typically displays pathognomonic gross placental lesions described as:",
         ["Bright red cotyledons studded with small, discrete, white focal calcified necrotic plaques ('Strawberry jam' / 'Frosted' cotyledons)", "Uniform diffuse leathery brownish cotyledons", "Hydatid cysts on the placenta", "Complete absence of gross lesions"],
         0, "Toxoplasmosis in sheep causes focal necrosis and calcification of placental cotyledons, which appear hyperemic and peppered with tiny white necrotic foci against bright red maternal caruncles ('strawberry jam' or 'frosted' appearance), while the intercotyledonary chorioallantois remains normal.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("Neospora caninum is a major cause of mid-to-late gestation (5th to 7th month) abortion storms in dairy cattle herds globally. The definitive host that sheds oocysts in its feces is the:",
         ["Dog (Canis familiaris)", "Cat (Felis catus)", "Cow (Bos taurus)", "Pigeon"],
         0, "The domestic dog (along with wild canids such as coyotes) serves as the definitive host for Neospora caninum, shedding infectious oocysts that contaminate feed; cattle can also maintain the infection across generations through highly efficient endogenous transplacental transmission.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("The poultry disease known as 'Blackhead' or 'Infectious Enterohepatitis' in turkeys, characterized by cecal ulceration and pathognomonic circular depressed 'target-like' / saucer-shaped necrotic liver lesions, is caused by:",
         ["Histomonas meleagridis", "Trichomonas gallinae", "Eimeria meleagrimitis", "Pasteurella multocida"],
         0, "Histomonas meleagridis is a flagellated protozoan causing fatal enterohepatitis in turkeys; it is transmitted via the eggs of the cecal nematode Heterakis gallinarum, producing circumscribed sunken necrotic hepatic rings with raised borders.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("Bovine Venereal Trichomoniasis, causing post-coital pyometra, early embryonic death, and repeat breeding in cows, is caused by Tritrichomonas foetus, which morphologically exhibits:",
         ["Three anterior flagella, one trailing recurrent flagellum with an undulating membrane, and an axostyle", "Eight flagella and two nuclei", "No flagella and amoeboid pseudopodia", "Two flagella and an apical complex"],
         0, "Tritrichomonas foetus is a pyriform flagellate (10-25 µm long) possessing 3 anterior flagella, an undulating membrane along its dorsal side with a posterior trailing flagellum, and a prominent rigid rod (axostyle) projecting from its caudal end.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        ("Equine Protozoal Myeloencephalitis (EPM), causing asymmetric ataxia, focal muscle atrophy, and cranial nerve deficits in horses, is caused by the apicomplexan parasite:",
         ["Sarcocystis neurona", "Theileria equi", "Babesia caballi", "Trypanosoma equiperdum"],
         0, "Sarcocystis neurona has the Virginia opossum (Didelphis virginiana) as its definitive host; horses are dead-end aberrant hosts that ingest sporocysts in feed/water, where schizonts and merozoites invade the spinal cord and brainstem parenchyma.",
         True, "Veterinary Protozoology (ICAR PG PYQ)"),

        # 21-30: Entomology and Acarology
        ("The 'Fowl Tick' or 'Blue Bug' (Argas persicus) is a soft tick (Argasidae) that hides in cracks and crevices during daylight, feeds nocturnally on birds, and is the biological vector of:",
         ["Borrelia anserina (Fowl Spirochaetosis) and Aegyptianella pullorum", "Newcastle Disease Virus", "Infectious Bursal Disease", "Avian Leucosis"],
         0, "Argas persicus lacks a dorsal scutum and its mouthparts are located ventrally; nocturnal blood-feeding causes severe anemia and tick paralysis, and it is the notorious vector of Borrelia anserina (spirochaetosis) and the piroplasm Aegyptianella pullorum.",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("In veterinary parasitology, Sarcoptic Mange (Sarcoptes scabiei) is distinguished morphologically from Psoroptic Mange (Psoroptes ovis) under a microscope by:",
         ["Sarcoptes is a burrowing mite with short legs and long, unjointed pedicels (stalks) bearing suckers", "Sarcoptes has long three-jointed pedicels with trumpet suckers", "Sarcoptes has no legs", "Sarcoptes is a visible macroparasite"],
         0, "Sarcoptes scabiei (burrowing mite of skin) has round bodies, dorsal triangular spines, and unjointed pretarsi/pedicels bearing suckers; Psoroptes ovis (non-burrowing scab mite) has pointed mouthparts and long, three-segmented pretarsi with trumpet-shaped suckers.",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("The unique microscopic morphology of Demodex canis, which resides in the hair follicles and sebaceous glands of dogs to cause localized or generalized demodicosis ('Red Mange'), is described as:",
         ["Elongated, cigar-shaped or alligator-shaped with 4 pairs of short stumpy anterior legs and a striated abdomen", "Globular, tortoise-like with long dorsal spines", "Dorsally flattened with prominent lateral combs", "Segmented worm-like without legs"],
         0, "Demodex canis is an obligate follicle mite possessing an elongated, tapering, cigar-like body with four pairs of short stumpy legs clustered on the podosoma and a transversely striated opisthosoma (abdomen), reproducing deep within hair follicles.",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("The 'Red Mite' of poultry (Dermanyssus gallinae) is clinically differentiated from the 'Northern Fowl Mite' (Ornithonyssus sylviarum) because Dermanyssus gallinae:",
         ["Feeds on the bird only at night and hides in crevices/roosts of the poultry house during the day", "Lives permanently on the bird's feathers day and night", "Burrows beneath the scales of the shanks and feet", "Attacks only the feather quill base"],
         0, "Dermanyssus gallinae spends the daylight hours off the host hiding in cage crevices, emerging at night to engorge on roosting birds (turning bright red to grey-black), whereas Ornithonyssus sylviarum completes its entire life cycle continuously on the feathers of the host.",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("'Scaly Leg' in domestic fowls, characterized by thick crusty proliferation, lifting of shank scales, and lameness, is caused by the burrowing mite:",
         ["Knemidocoptes mutans", "Knemidocoptes gallinae", "Dermanyssus gallinae", "Laminosioptes cysticola"],
         0, "Knemidocoptes mutans burrows under the epidermal scales of the unfeathered lower legs and feet of chickens and turkeys, causing vesicular hyperkeratosis, crust formation ('scaly leg'), and deformed feet; Knemidocoptes gallinae causes depluming itch.",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("The 'Sheep Nasal Bot Fly' (Oestrus ovis) is larviparous, depositing live larvae (L1) around the nostrils of sheep; these larvae migrate to which anatomical site to develop into mature dark-banded bots, causing catarrhal sinusitis and 'False Gid'?",
         ["The frontal sinuses and nasal cavities", "The abomasal mucosa", "The alveoli of the lungs", "The subcutaneous tissues of the back"],
         0, "Oestrus ovis female flies dart at sheep's muzzles, shooting living L1 into the nostrils; larvae crawl through nasal turbinates into the frontal and maxillary sinuses, irritating the mucosa, causing mucopurulent discharge and head tossing ('false gid').",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("In horses, larvae of the Stomach Bot Fly (Gasterophilus intestinalis) attach characteristically by strong mouth hooks to which region of the equine digestive tract?",
         ["The non-glandular stratified squamous mucosa (margo plicatus / pars cardiaca) of the stomach", "The glandular abomasum", "The terminal cecum", "The small colon"],
         0, "Gasterophilus intestinalis females glue eggs to hair of the horse's forelegs; larvae are licked into the mouth, burrow through the tongue, and migrate to attach in dense clusters to the non-glandular squamo-columnar mucosa (margo plicatus and pars cardiaca) of the stomach.",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("In cattle, the larvae of the 'Ox Warble Fly' (Hypoderma bovis and Hypoderma lineatum) migrate through internal organs before emerging to form painful subcutaneous cysts ('warbles') with breathing pores along the animal's back. During migration, Hypoderma bovis characteristically travels through the:",
         ["Epidural fat of the spinal canal", "Submucosa of the esophagus", "Peritoneal cavity", "Pulmonary parenchyma"],
         0, "First-stage larvae of Hypoderma lineatum migrate through the connective tissue of the esophageal submucosa, whereas Hypoderma bovis larvae migrate characteristically through the epidural fat of the lumbar spinal canal before reaching the dorsal back skin.",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("Biting midges of the genus Culicoides are tiny crepuscular dipterans that serve as the principal biological vectors of which major veterinary viral diseases?",
         ["Bluetongue Virus (BTV) and African Horse Sickness Virus (AHSV)", "Foot-and-Mouth Disease (FMD) and Swine Fever", "Rinderpest and Peste des Petits Ruminants", "Rabies and Canine Parvovirus"],
         0, "Culicoides species (e.g., C. oxystoma, C. imicola) are the obligate biological vectors of orbiviruses causing Bluetongue in sheep/cattle and African Horse Sickness in equines, as well as Bovine Ephemeral Fever and filarial Onchocerca nematodes.",
         True, "Veterinary Entomology (ICAR PG PYQ)"),

        ("Lice of the suborder Anoplura (Sucking Lice) are distinguished from lice of the suborder Mallophaga (Biting / Chewing Lice) by possessing:",
         ["A pointed head that is distinctly narrower than the thorax and piercing-sucking mouthparts for blood feeding", "A broad head that is wider than the thorax and chewing mandibles", "Wings and halteres", "Four pairs of legs and no antennae"],
         0, "Anoplura (e.g., Haematopinus suis, Linognathus vituli) have narrow heads narrower than the prothorax, feed exclusively on host blood, and parasitize only placental mammals; Mallophaga (e.g., Damalinia/Bovicola, Menacanthus) have broad heads wider than the thorax and chew epidermal debris and feathers.",
         True, "Veterinary Entomology (ICAR PG PYQ)")
    ]
    return qs
