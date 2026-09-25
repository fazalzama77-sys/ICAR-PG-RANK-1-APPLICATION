# scripts/para_mod1_helminths.py
# Module 1: Veterinary Helminthology (30 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit II (Sub-subject 13.4)

def get_module1_questions():
    qs = [
        # 1-10: Trematodes (Flukes)
        ("In ruminant fasciolosis caused by Fasciola gigantica and Fasciola hepatica, the infective stage that encysts on aquatic vegetation and is ingested by grazing animals is the:",
         ["Metacercaria", "Cercaria", "Miracidium", "Redia"],
         0, "The life cycle of Fasciola involves: Egg -> Miracidium (penetrates snail) -> Sporocyst -> Redia -> Cercaria (emerges from snail) -> Metacercaria (encysts on vegetation, serving as the infective stage for definitive hosts).",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The primary intermediate freshwater snail host for the common liver fluke (Fasciola hepatica) in temperate regions and Fasciola gigantica in tropical India are, respectively:",
         ["Lymnaea truncatula and Lymnaea auricularia (L. rufescens)", "Indoplanorbis exustus and Bulinus truncatus", "Planorbis planorbis and Bithynia tentaculata", "Zebrina detrita and Helicella"],
         0, "Lymnaea truncatula is the principal snail host of F. hepatica globally, whereas in India, Lymnaea auricularia (sensu lato, including L. rufescens and L. acuminata) is the primary snail vector for F. gigantica.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("Severe, fatal acute fasciolosis in sheep is pathologically caused by:",
         ["Traumatic migration of numerous immature flukes through hepatic parenchyma, rupturing capillaries", "Obstruction of major bile ducts by adult flukes", "Chronic calcification and pipe-stem liver", "Bacterial fermentation in the gallbladder"],
         0, "Acute fasciolosis occurs 6-8 weeks post-ingestion when thousands of juvenile flukes burrow aggressively through the liver parenchyma, causing extensive hemorrhage, coagulative necrosis, and traumatic hepatitis (often triggering Clostridium novyi Type B Black Disease).",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The pathognomonic clinical condition known as 'Immature Amphistomiasis' (Paramphistomosis) in sheep and cattle is characterized by fetid watery diarrhea, severe hypoproteinemia, and submandibular edema ('bottle jaw') caused by:",
         ["Massive plug-feeding and mucosal destruction by immature paramphistomes in the duodenum and abomasum", "Adult flukes attaching to the rumen papillae", "Rupture of the gallbladder", "Biliary duct fibrosis"],
         0, "While adult amphistomes (e.g., Cotylophoron cotylophorum, Gastrothylax crumenifer) in the rumen are relatively benign, excysted juvenile flukes attach to the duodenal and abomasal mucosa, plug-feeding and causing severe catarrhal/erosive duodenitis, fatal hypoproteinemia, and diarrhea.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The intermediate snail host for the common amphistomes (Cotylophoron cotylophorum and Paramphistomum cervi) in India is:",
         ["Indoplanorbis exustus", "Lymnaea truncatula", "Gyraulus convexiusculus", "Viviparus bengalensis"],
         0, "Indoplanorbis exustus (a planorbid freshwater snail with a discoidal shell) is the principal intermediate host for Cotylophoron cotylophorum and Gastrothylax in the Indian subcontinent.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The Lancet fluke (Dicrocoelium dendriticum) requires two intermediate hosts to complete its life cycle. The second intermediate host, in which metacercariae encyst and alter host behavior, is:",
         ["The Brown Wood Ant (Formica fusca)", "The freshwater snail (Lymnaea truncatula)", "The water flea (Cyclops)", "The dung beetle (Aphodius)"],
         0, "Dicrocoelium uses a terrestrial snail (1st host) and the brown ant Formica fusca (2nd host). One metacercaria encysts in the ant's subesophageal ganglion ('brainworm'), inducing temperature-dependent tetanic clamping of the ant's jaws onto grass tips at dawn/dusk to facilitate ingestion by ruminants.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("In cattle, 'Nasal Schistosomiasis' (Nasal granuloma / 'Snoring Disease') characterized by cauliflower-like nodular granulomas on the nasal septum is caused by:",
         ["Schistosoma nasale", "Schistosoma spindale", "Schistosoma bovis", "Schistosoma japonicum"],
         0, "Schistosoma nasale resides in the veins of the nasal mucosa of cattle, goats, and horses; its characteristic boomerang-shaped eggs with a terminal spine trigger pseudo-tuberculous granulomas and snoring dyspnea.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The eggs of Schistosoma nasale are microscopically recognized in nasal discharge by their characteristic:",
         ["Boomerang shape with a subterminal or terminal spine", "Oval operculated yellowish shell with a knob", "Spindle shape with flattened sides", "Barrel shape with polar plugs"],
         0, "Schistosoma nasale eggs are distinctly boomerang- or curved shoehorn-shaped with a terminal point/spine, whereas Schistosoma spindale eggs are elongated spindle-shaped with a terminal spine.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("Which species of mammalian blood fluke exhibits an elongated spindle-shaped egg with a sharp terminal spine and causes visceral schistosomiasis and mesenteric phlebitis in Indian ruminants?",
         ["Schistosoma spindale", "Schistosoma nasale", "Schistosoma incognitum", "Schistosoma rodhaini"],
         0, "Schistosoma spindale inhabits the mesenteric veins of cattle, buffalo, sheep, and goats; its characteristic spindle-shaped eggs with a straight spine induce granulomatous nodules, thrombosis, and hepatic periportal fibrosis.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The definitive infective stage of blood flukes (Schistosoma species) that actively penetrates the intact skin of the definitive mammalian host in water is the:",
         ["Fork-tailed cercaria (Furcocercous cercaria)", "Encysted metacercaria", "Redia", "Amphistome miracidium"],
         0, "Schistosomes do not have a metacercarial encystment stage on vegetation; instead, free-swimming furcocercous (fork-tailed) cercariae shed by aquatic snails actively penetrate the skin of animals entering water bodies, shedding their tails to become schistosomula.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        # 11-20: Cestodes (Tapeworms)
        ("'Measly Pork' (Porcine cysticercosis) is caused by the intermediate larval stage (Cysticercus cellulosae) of which human tapeworm?",
         ["Taenia solium", "Taenia saginata", "Taenia hydatigena", "Echinococcus granulosus"],
         0, "Taenia solium (the pork tapeworm of humans) produces the intermediate metacestode Cysticercus cellulosae in the striated muscle of pigs (measly pork); humans become infected by ingesting undercooked pork or develop human neurocysticercosis via autoinfection.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("'Measly Beef' (Bovine cysticercosis) is caused by the intermediate bladder worm stage (Cysticercus bovis) of which human tapeworm?",
         ["Taenia saginata", "Taenia solium", "Taenia pisiformis", "Taenia ovis"],
         0, "Taenia saginata (the unarmed beef tapeworm of humans) forms Cysticercus bovis in the masseter, heart, tongue, and diaphragm muscles of cattle; unlike T. solium, the scolex lacks hooks (unarmed rostellum).",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The neurological syndrome known as 'Gid' or 'Sturdy' in sheep (circling, head deviation, blindness, and skull softening) is caused by the intracranial intermediate coenurus stage (Coenurus cerebralis) of:",
         ["Taenia multiceps", "Taenia hydatigena", "Taenia ovis", "Echinococcus granulosus"],
         0, "Taenia multiceps (adult in the canine small intestine) produces Coenurus cerebralis (a large fluid-filled bladder with multiple invaginated scolices) in the brain and spinal cord of sheep and goats, causing pressure necrosis and neurological 'gid'.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The large fluid-filled larval bladder worm (Cysticercus tenuicollis) commonly found attached to the mesentery, omentum, and liver capsules of slaughtered sheep and goats is the larval stage of:",
         ["Taenia hydatigena", "Taenia pisiformis", "Taenia taeniaeformis", "Dipylidium caninum"],
         0, "Taenia hydatigena is a common tapeworm of dogs; its metacestode (Cysticercus tenuicollis, the slender-necked bladder worm) migrates through the liver of ruminants, leaving fibrous tracts ('hepatitis cysticercosa') before encysting on the peritoneal serosa.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("In hydatid disease (Echinococcosis), the adult tapeworm consisting of only 3 to 4 proglottids and a hooked scolex resides in the small intestine of:",
         ["Dogs and other canids (Definitive Host)", "Ruminants and horses", "Cats and felids", "Rodents"],
         0, "Echinococcus granulosus adults (only 3-6 mm long, having a scolex and 3-4 segments) live exclusively in the small intestine of dogs and wild canids; herbivores and humans act as intermediate hosts developing large unilocular hydatid cysts.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The characteristic microscopic diagnostic feature of Moniezia expansa eggs found in ruminant fecal sedimentation is the presence of a:",
         ["Triangular shape containing a specialized Pyriform Apparatus enclosing the onchosphere", "Bipolar plug at each end", "Heavy thick-walled radial striation with hooks", "Operculated lid with a ciliated miracidium"],
         0, "Moniezia expansa eggs are triangular (whereas M. benedeni eggs are quadrangular/square) and contain a distinct internal, horn-like protective structure termed the 'Pyriform Apparatus' harboring the hexacanth onchosphere.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The intermediate host required for the transmission and development of ruminant tapeworms (Moniezia species) and equine tapeworms (Anoplocephala species) on pasture is:",
         ["Oribatid pasture mites (Free-living soil mites)", "Aquatic freshwater snails", "Biting midges (Culicoides)", "Pasture ticks"],
         0, "Oribatid soil mites (e.g., Scheloribates, Galumna) ingest tapeworm eggs on pasture; cysticercoids develop within the mites, and grazing livestock become infected by ingesting the mites along with grass.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The equine tapeworm Anoplocephala perfoliata characteristically clusters at which anatomical site, predisposing horses to ulceration, perforation, and ileocecal intussusception / colic?",
         ["The Ileocecal junction (Ileocecal valve and cecum)", "The glandular fundus of the stomach", "The terminal descending colon", "The bile duct"],
         0, "Anoplocephala perfoliata possesses rounded lappets behind each of its 4 suckers and characteristically anchors in dense clusters at the ileocecal orifice, causing localized ulceration, mucosal hypertrophy, and spasmodic or intussusceptive colic.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The 'Double-pored Dog Tapeworm' (Dipylidium caninum) produces cucumber-seed shaped proglottids containing egg packets, and is transmitted to dogs and cats by the ingestion of infected:",
         ["Fleas (Ctenocephalides felis / canis) and biting lice (Trichodectes canis)", "Ticks (Rhipicephalus sanguineus)", "Oribatid pasture mites", "Earthworms"],
         0, "Dipylidium caninum cysticercoids develop inside the larvae of fleas (Ctenocephalides canis/felis) and chewing lice (Trichodectes canis); pets ingest grooming fleas containing cysticercoids, acquiring infection.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("In poultry, the microscopic, highly pathogenic tapeworm consisting of only 4 to 9 proglottids that penetrates deep into the duodenal crypts causing severe hemorrhagic enteritis is:",
         ["Davainea proglottina", "Raillietina cesticillus", "Raillietina tetragona", "Amoebotaenia sphenoides"],
         0, "Davainea proglottina is tiny (0.5 to 3 mm long, with 4-9 segments); its scolex possesses hammer-shaped hooks that deeply penetrate duodenal villi, causing hemorrhagic enteritis and wasting in young chicks; intermediate hosts are terrestrial slugs and snails.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        # 21-30: Nematodes (Roundworms)
        ("The highly pathogenic abomasal nematode of sheep and goats known as the 'Barber's Pole Worm' that causes severe blood loss, microcytic anemia, and submandibular edema ('bottle jaw') without diarrhea is:",
         ["Haemonchus contortus", "Ostertagia ostertagi", "Trichostrongylus axei", "Cooperia curticei"],
         0, "Haemonchus contortus possesses a lancet in its buccal cavity that lacerates abomasal microvessels, consuming up to 0.05 ml blood/worm/day. The female exhibits red blood-filled gut coiled around white ovaries ('barber's pole'). Infection causes marked hypoproteinemia, anemia, and bottle jaw with absence of diarrhea.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("In cattle, 'Type II Ostertagiasis' occurs during late winter or spring and results from:",
         ["Synchronous emergence of thousands of hypobiotic (arrested L4) larvae from gastric glands into the abomasal lumen", "Rapid ingestion of massive numbers of infective L3 from pasture during monsoon", "Ascending migration of larvae into bile ducts", "Direct transplacental infection of fetuses"],
         0, "In Type II ostertagiasis, thousands of dormant, hypobiotic L4 larvae that accumulated in the gastric pits synchronously emerge, destroying parietal cells, causing abomasal pH to rise from 2.0 to >7.0 (loss of pepsinogen activation), creating a pathognomonic 'Moroccan leather' / 'cobblestone' mucosa.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The equine nematode whose migrating larvae (L4) cause severe verminous arteritis, thrombosis, and thromboembolic infarction / colic of the cranial mesenteric artery is:",
         ["Strongylus vulgaris", "Strongylus edentatus", "Strongylus equinus", "Parascaris equorum"],
         0, "Strongylus vulgaris is the most pathogenic equine large strongyle; ingested L3 penetrate the intestinal wall, molt to L4, and migrate against arterial flow along the intima to the cranial mesenteric artery, causing thrombosis, aneurysm, and fatal thromboembolic colic.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("In swine, 'Milk Spot Liver' lesions (multifocal fibrous scars on the hepatic capsule and parenchyma) are pathognomonic of migrating larvae of which ascarid?",
         ["Ascaris suum", "Oesophagostomum dentatum", "Stephanurus dentatus", "Hyostrongylus rubidus"],
         0, "Ingested embryonated eggs of Ascaris suum hatch in the intestine; larvae burrow into mesenteric veins, reaching the liver via portal blood where eosinophilic infiltration and subsequent repair create milky-white fibrous capsular patches ('milk spots').",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The canine ascarid Toxocara canis undergoes which predominant route of transmission that results in puppies being born with patent roundworm infections in their intestines?",
         ["Transplacental (Prenatal) transmission of somatic arrested larvae across the placenta after Day 42 of pregnancy", "Transovarial transmission", "Percutaneous penetration of unbroken paw skin", "Oral ingestion of infective adults in colostrum only"],
         0, "In pregnant bitches, dormant somatic larvae mobilize during late gestation (around day 42) and cross the placenta to enter fetal liver/lungs; at birth, larvae migrate to the puppy's trachea and are swallowed into the intestine, maturing to patency by 2-3 weeks of age.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("Visceral Larva Migrans (VLM) and Ocular Larva Migrans (OLM) in young children are serious zoonotic syndromes caused by accidental ingestion of embryonated eggs of:",
         ["Toxocara canis (or Toxocara cati)", "Ancylostoma caninum", "Ascaris suum", "Trichuris vulpis"],
         0, "Humans are aberrant paratenic hosts for Toxocara canis; ingested eggs release larvae that cannot complete development into adults, wandering through human liver, lungs, brain (VLM) or retina (OLM), inciting eosinophilic granulomas.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The canine hookworm Ancylostoma caninum causes severe, life-threatening hemorrhagic microcytic anemia in young puppies primarily transmitted through:",
         ["Transmammary (Galactogenic) transmission in maternal colostrum and milk", "Transovarial transmission", "Direct fecal-oral ingestion of unembryonated eggs", "Mosquito bites"],
         0, "In nursing bitches, dormant somatic larvae activate and are shed directly into colostrum and milk during the first 3 weeks of lactation (transmammary route), leading to acute exsanguinating anemia in 2- to 3-week-old pups.",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("In horses, cutaneous habronemiasis ('Summer Sores' / Granular Dermatitis) presenting as non-healing granulomatous wound ulcerations with exuberant granulation tissue is caused by larvae of Habronema and Draschia megastoma deposited by:",
         ["Biting flies and house flies (Musca domestica and Stomoxys calcitrans)", "Culicoides midges", "Tabanid horse flies", "Mosquitoes"],
         0, "Habronema microstoma, H. muscae, and Draschia megastoma larvae develop in Musca domestica and Stomoxys calcitrans; when flies feed on existing cutaneous wounds or eye medial canthi, deposited larvae fail to migrate to the stomach and incite intense eosinophilic granulation tissue ('summer sores').",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The canine esophageal worm that induces granulomatous esophageal nodules that can neoplastic transform into fibrosarcoma or osteosarcoma, and causes aortic aneurysms, is:",
         ["Spirocerca lupi", "Dirofilaria immitis", "Filaroides osleri", "Angiostrongylus vasorum"],
         0, "Spirocerca lupi larvae migrate through the thoracic aortic wall (causing scarring and aneurysms) into the distal esophagus, forming granulomatous nodules; in a significant percentage of cases, chronic inflammation induces malignant transformation into esophageal fibrosarcoma/osteosarcoma and secondary hypertrophic osteopathy (Marie's disease).",
         True, "Veterinary Helminthology (ICAR PG PYQ)"),

        ("The bovine lungworm Dictyocaulus viviparus, which causes verminous bronchitis ('Husk' / 'Hoose') in calves, utilizes which coprophilic fungus to propel its infective L3 larvae away from cattle dung pats onto surrounding pasture?",
         ["Pilobolus kleinii (Pilobolus fungus)", "Aspergillus flavus", "Fusarium moniliforme", "Candida albicans"],
         0, "Dictyocaulus viviparus L3 larvae climb onto the sporangiophores of the dung fungus Pilobolus; when the fungal sporangium bursts towards light, larvae are forcefully discharged up to 3 meters across pasture, enhancing grazing transmission.",
         True, "Veterinary Helminthology (ICAR PG PYQ)")
    ]
    return qs
