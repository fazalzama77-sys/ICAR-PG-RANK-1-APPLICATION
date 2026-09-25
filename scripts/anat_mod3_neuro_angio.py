# scripts/anat_mod3_neuro_angio.py
# Module 3: Angiology & Neurology (30 Questions)
# Aligned with ICAR AIEEA (PG) M.V.Sc. Syllabus Code 13 Unit I

def get_module3_questions():
    qs = [
        # 1-10: Heart, Great vessels, Circulation
        ("In the domestic Ox and Dog, the coronary circulation is described as 'Left Coronary Artery Predominant' because the subsinuosal interventricular branch originates from the:",
         ["Left circumflex coronary artery", "Right coronary artery", "Directly from the aorta", "Pulmonary trunk"],
         0, "In ruminants and carnivores, the left circumflex coronary artery continues along the caudal coronary groove to supply the subsinuosal interventricular groove (Left Predominance), whereas in the horse and pig, the subsinuosal branch arises from the Right coronary artery (Right/Bilateral Predominance).",
         True, "Angiology (ICAR PG PYQ)"),

        ("The 'Moderator Band' (Septomarginal Trabecula / Trabecula septomarginalis) is a muscular-tendinous cord traversing the lumen of which cardiac chamber to conduct electrical impulses?",
         ["Right Ventricle (connecting the interventricular septum to the base of the parietal wall / anterior papillary muscle)", "Left Atrium", "Right Atrium", "Ascending aorta"],
         0, "The septomarginal trabecula crosses the right ventricular cavity, carrying a Purkinje-fiber conduction bundle from the bundle of His across the septum to the lateral parietal wall and papillary muscles, preventing overdistension.",
         True, "Angiology (ICAR PG PYQ)"),

        ("In the domestic Horse and Ox, the aortic arch gives off which branch or branches supplying the head, neck, and thoracic limbs?",
         ["A single Brachiocephalic Trunk alone (which subsequently divides into left subclavian, bicarotid trunk, and right subclavian)", "Both a Brachiocephalic Trunk and a separate Left Subclavian Artery", "Separate carotid arteries directly from the arch", "Three independent brachiocephalic arteries"],
         0, "In ungulates (equines and ruminants), the aortic arch emits only one single massive common vessel: the Brachiocephalic Trunk; in carnivores (dog/cat) and swine, two independent branches arise from the aortic arch: the Brachiocephalic Trunk and the Left Subclavian Artery.",
         True, "Angiology (ICAR PG PYQ)"),

        ("The 'Rete Mirabile Epidurale' (an extensive intracranial arterial meshwork surrounding the pituitary gland in the cavernous sinus that functions in brain cooling) is present in:",
         ["Ruminants (Ox, Sheep, Goat) and Swine (Pig)", "Horse and Dog (completely absent)", "Cat only", "Birds"],
         0, "Ruminants and pigs possess an extraordinary carotid rete mirabile (rete mirabile epidurale) in the cavernous sinus where the internal carotid artery breaks into a fine network of anastomosing arterioles bathed in venous blood from nasal mucosa, cooling arterial blood entering the brain.",
         True, "Angiology (ICAR PG PYQ)"),

        ("The Left Azygos Vein (Vena hemiazygos / Vena azygos sinistra) drains the thoracic wall and empties directly into the Coronary Sinus in which domestic species?",
         ["Ruminants (Ox, Sheep, Goat) and Swine (Pig)", "Horse and Dog (where the Right Azygos empties into the Cranial Vena Cava)", "Cat only", "Birds"],
         0, "In cattle, sheep, and pigs, the primary functional azygos vein is the Left Azygos Vein, which curves ventrally around the left atrium to enter the right atrium via the coronary sinus; in horses and dogs, it is the Right Azygos vein.",
         True, "Angiology (ICAR PG PYQ)"),

        ("The 'Cisterna Chyli' (the dilated abdominal receiving reservoir for lymph from the pelvis, hindlimbs, and viscera that gives rise to the Thoracic Duct) is located dorsal to the aorta at the level of:",
         ["L1 to L4 (between the crura of the diaphragm)", "C6 to C7", "T5 to T7", "Sacrum"],
         0, "The cisterna chyli is a retroperitoneal lymphatic reservoir situated between the crura of the diaphragm dorsal to the aorta and right of the coeliac and cranial mesenteric arteries, continuing through the aortic hiatus as the Thoracic Duct.",
         False, "Angiology"),

        ("The superficial palpable lymph center of the bovine body located immediately cranial to the shoulder joint beneath the brachiocephalic muscle is the:",
         ["Superficial Cervical Lymph Node (Prescapular lymph node)", "Subiliac lymph node (Prefemoral)", "Popliteal lymph node", "Parotid lymph node"],
         0, "The superficial cervical (prescapular) lymph node lies along the cranial border of the supraspinatus muscle deep to the omotransversarius, draining the skin of the neck, shoulder, and cranial thoracic limb.",
         True, "Angiology (ICAR PG PYQ)"),

        ("In bovine meat inspection, the 'Prefemoral Lymph Node' (Subiliac lymph node) is routinely palpated and incised on the carcass at the cranial border of the:",
         ["Tensor fasciae latae muscle, in the fold of the flank", "Brachialis muscle", "Gastrocnemius muscle", "Trapezius muscle"],
         0, "The subiliac (prefemoral) lymph center is situated subcutaneous in the flank fold along the cranial margin of the tensor fasciae latae muscle, about midway between the tuber coxae and patella.",
         True, "Angiology (ICAR PG PYQ)"),

        ("The portal vein (Vena portae) transports nutrient-rich blood from the digestive viscera to the liver, formed by the convergence of which three major veins?",
         ["Splenic vein, Cranial Mesenteric vein, and Caudal Mesenteric vein (and Gastroduodenal vein)", "Renal vein, Hepatic vein, and Femoral vein", "Jugular vein and Subclavian vein", "Azygos vein and Iliac vein"],
         0, "The portal trunk is formed dorsomedial to the pancreas by the junction of the cranial mesenteric, caudal mesenteric, and splenic/gastroduodenal veins, conveying venous blood from stomach, intestines, pancreas, and spleen directly to the liver sinusoids.",
         False, "Angiology"),

        ("The ductus arteriosus in the mammalian fetus shunts deoxygenated blood from the pulmonary trunk directly into the descending aorta; upon closure at birth, its fibrous adult remnant is the:",
         ["Ligamentum Arteriosum", "Ligamentum Venosum", "Fossa Ovalis", "Round ligament of the liver"],
         0, "Functional closure of the ductus arteriosus occurs within hours of initial pulmonary respiration; anatomical fibrosis over several weeks transforms this vascular shunt into the fibrous ligamentum arteriosum.",
         True, "Comparative Embryology (ICAR PG PYQ)"),

        # 11-20: Cranial Nerves
        ("Cranial Nerve I (Olfactory nerve) fibers pass from the olfactory neuroepithelium into the olfactory bulbs through which perforated bony plate?",
         ["Cribriform plate of the Ethmoid bone", "Petrous temporal bone", "Optic canal", "Hypoglossal canal"],
         0, "The non-myelinated fila olfactoria pass from the nasal mucosa through the multiple fine perforations of the lamina cribrosa (cribriform plate) of the ethmoid bone to terminate in the olfactory bulb of the telencephalon.",
         True, "Neurology (ICAR PG PYQ)"),

        ("The Optic Nerve (Cranial Nerve II) exits the cranial vault through which bony canal?",
         ["Optic Canal (Canalis opticus) of the Presphenoid bone", "Foramen orbitorotundum", "Orbital fissure", "Stylomastoid foramen"],
         0, "The optic nerve (surrounded by extensions of the meninges and CSF) passes through the optic canal of the presphenoid bone to enter the orbital cavity.",
         False, "Neurology"),

        ("Which three cranial nerves supply motor innervation to the extrinsic muscles of the eyeball?",
         ["CN III (Oculomotor), CN IV (Trochlear), and CN VI (Abducent)", "CN II, CN III, and CN V", "CN V, CN VII, and CN IX", "CN IV, CN VI, and CN VIII"],
         0, "Eye muscles are innervated by: CN IV for the Dorsal Oblique muscle; CN VI for the Lateral Rectus and retractor bulbi; and CN III for all other extrinsic ocular muscles (Dorsal, Ventral, Medial Recti, and Ventral Oblique).",
         True, "Neurology (ICAR PG PYQ)"),

        ("In the horse and dog, the Mandibular Nerve (the 3rd division of the Trigeminal nerve, CN V3) exits the cranial cavity through the:",
         ["Foramen Ovale (or notch in the foramen lacerum)", "Foramen rotundum", "Hypoglossal canal", "Stylomastoid foramen"],
         0, "CN V3 (mandibular nerve, providing sensory innervation to the lower jaw and motor innervation to the muscles of mastication) exits via the foramen ovale in dogs and ruminants, or the oval notch of the foramen lacerum in horses.",
         True, "Neurology (ICAR PG PYQ)"),

        ("Motor innervation to all the muscles of facial expression (including orbicularis oculi, orbicularis oris, and levator labii) is provided by:",
         ["Cranial Nerve VII (Facial Nerve), exiting through the Stylomastoid Foramen", "Cranial Nerve V (Trigeminal)", "Cranial Nerve XI (Accessory)", "Cranial Nerve XII (Hypoglossal)"],
         0, "The Facial nerve (CN VII) emerges from the skull at the stylomastoid foramen and divides into dorsal and ventral buccal branches to innervate the superficial facial muscles of expression; CN V provides sensory innervation.",
         True, "Neurology (ICAR PG PYQ)"),

        ("Damage to the Left Recurrent Laryngeal Nerve (a branch of Cranial Nerve X, the Vagus nerve) in horses causes 'Roaring' (Laryngeal Hemiplegia) due to paralysis of which sole abductor muscle of the vocal folds?",
         ["Cricoarytenoideus Dorsalis muscle (CAD)", "Cricoarytenoideus lateralis", "Thyroarytenoideus", "Cricothyroideus"],
         0, "The dorsal cricoarytenoid muscle (CAD) is the ONLY muscle that abducts (opens) the vocal cords during inspiration; neurogenic atrophy of the left CAD muscle due to recurrent laryngeal neuropathy allows the vocal cord to collapse into the airway.",
         True, "Neurology (ICAR PG PYQ)"),

        ("The Hypoglossal Nerve (Cranial Nerve XII) exits through the hypoglossal canal and provides motor innervation to:",
         ["All intrinsic and extrinsic muscles of the Tongue (styloglossus, hyoglossus, genioglossus)", "Muscles of mastication", "Pharyngeal constrictors", "Facial muscles"],
         0, "Cranial Nerve XII (Hypoglossal) provides motor supply to the tongue musculature; unilateral damage causes deviation of the tongue towards the paralyzed side when protruded.",
         True, "Neurology (ICAR PG PYQ)"),

        ("The Sensory innervation to the rostral two-thirds of the tongue for taste (gustatory) is mediated by which specialized cranial nerve branch?",
         ["Chorda Tympani (a branch of the Facial Nerve, CN VII, carried within the lingual nerve)", "Glossopharyngeal nerve (CN IX)", "Hypoglossal nerve (CN XII)", "Mandibular nerve alone"],
         0, "General somatic sensation from the rostral 2/3 of the tongue is carried by the lingual nerve (CN V3), but taste sensation from fungiform papillae is carried by the Chorda Tympani branch of CN VII hitchhiking with the lingual nerve.",
         True, "Neurology (ICAR PG PYQ)"),

        ("The 'Calving Paralysis' syndrome in post-parturient dairy cows, characterized by inability to adduct the hindlimbs ('downer cow' with limbs splayed laterally), is caused by compressive trauma to the:",
         ["Obturator Nerve inside the pelvic canal against the shaft of the ilium during dystocia", "Femoral nerve", "Sciatic nerve", "Pudendal nerve"],
         0, "The obturator nerve (L5-L6) courses subperiosteally along the medial surface of the iliac shaft inside the obturator foramen; during delivery of a large calf, fetal pressure crushes the nerve against the bone, paralyzing the adductor muscles.",
         True, "Neurology (ICAR PG PYQ)"),

        ("In horses and cattle, complete paralysis of the Radial Nerve at the level of the arm produces which pathognomonic postural abnormality?",
         ["'Dropped Elbow' with inability to extend the elbow, carpus, and digits, and knuckling on the fetlock", "Inability to flex the shoulder", "Severe outward rotation of the hock", "Hyperextension of the carpus"],
         0, "The radial nerve innervates all extensors of the elbow, carpus, and digits (triceps brachii, extensor carpi radialis, digital extensors); paralysis causes the elbow to drop and the limb to collapse in flexion upon bearing weight.",
         True, "Neurology (ICAR PG PYQ)"),

        # 21-30: Spinal nerves, plexuses, clinical anatomy
        ("'Sweeny' in draft horses is an equine neurogenic condition characterized by prominent atrophy of the supraspinatus and infraspinatus muscles on the lateral scapula, caused by trauma to the:",
         ["Suprascapular Nerve as it winds around the cranial border (cervical border) of the scapular neck", "Axillary nerve", "Musculocutaneous nerve", "Median nerve"],
         0, "Because the horse lacks an acromion process, the suprascapular nerve courses unprotected around the cranial neck of the scapula; collisions or ill-fitting collar harnesses compress the nerve, causing rapid denervation atrophy ('sweeny').",
         True, "Neurology (ICAR PG PYQ)"),

        ("The 'Patellar Reflex' (knee jerk reflex in dogs) evaluates the integrity of the L4-L6 spinal cord segments and which peripheral spinal nerve?",
         ["Femoral Nerve (innervating the Quadriceps Femoris muscle)", "Sciatic nerve", "Peroneal nerve", "Obturator nerve"],
         0, "Tapping the straight patellar ligament stretches the quadriceps femoris muscle spindle; sensory fibers conduct impulses through the femoral nerve to L4-L6 spinal cord segments, firing motor neurons that extend the stifle.",
         True, "Neurology (ICAR PG PYQ)"),

        ("The 'Horner's Syndrome' in dogs, cats, and horses (characterized by miosis, ptosis, enophthalmos, and protrusion of the third eyelid) results from disruption of the:",
         ["Oculosympathetic (cervical sympathetic) pathway", "Oculomotor parasympathetic pathway", "Facial nerve", "Trigeminal sensory pathway"],
         0, "Loss of sympathetic innervation to the eye and orbit (due to lesions in the cranial cervical ganglion, brachial plexus avulsion, or otitis media) removes dilator tone, resulting in constricted pupil (miosis), drooping upper eyelid (ptosis), and sunken globe.",
         True, "Neurology (ICAR PG PYQ)"),

        ("In cattle, Caudal Epidural Anesthesia is routinely performed by inserting a spinal needle into which intervertebral space?",
         ["First Intercoccygeal space (between Coccygeal 1 and Coccygeal 2) or the Sacrococcygeal space (S5-Co1)", "Lumbosacral space (L6-S1)", "Atlanto-occipital space", "T13-L1 space"],
         0, "Pumping the tail up and down reveals the first prominent movable joint caudal to the sacrum: the Co1-Co2 space (or S5-Co1); injecting local anesthetic into the epidural space desensitizes the perineum, vulva, and rectum without causing hindlimb paralysis.",
         True, "Clinical Anatomy (ICAR PG PYQ)"),

        ("Lumbosacral Epidural Anesthesia in the Dog and Sheep is performed by needle puncture into the epidural space between:",
         ["Lumbar 7 (L7) and Sacral 1 (S1) vertebrae", "L5 and L6", "Co1 and Co2", "T13 and L1"],
         0, "In small animals and small ruminants, the spinal cord terminates cranial to L7 (the conus medullaris terminates at L6 in dogs and L7/S1 in cats); the prominent depression between the dorsal spines of L7 and S1 allows safe lumbosacral epidural injection.",
         True, "Clinical Anatomy (ICAR PG PYQ)"),

        ("Cerebrospinal Fluid (CSF) is collected in horses and cattle from the Cisterna Magna (cerebellomedullary cistern) at which anatomical landmark?",
         ["Atlanto-Occipital Space (articulation between the occipital condyles and the atlas)", "Lumbosacral junction", "C7-T1 junction", "Between thoracic spines"],
         0, "The cerebellomedullary cistern is located dorsal to the medulla oblongata directly beneath the dorsal atlanto-occipital membrane; with the head flexed at 90 degrees, a needle inserted midway between the occipital crest and cranial wings of the atlas enters the subarachnoid space.",
         True, "Clinical Anatomy (ICAR PG PYQ)"),

        ("The Pudendal Nerve (Nervus pudendus) innervates the caudal external genitalia, and in the bull, Pudendal Nerve Block is performed to achieve:",
         ["Relaxation and desensitization of the retractor penis muscle, allowing protrusion and examination of the penis", "Complete hindlimb immobilization", "Ruminal atony", "Flank desensitization"],
         0, "In the bull, bilateral pudendal nerve block (Larson's technique) at the lesser ischiatic foramen paralyzes the retractor penis muscles and desensitizes the glans and sheath, allowing easy manual exteriorization of the penis for surgical repair.",
         True, "Clinical Anatomy (ICAR PG PYQ)"),

        ("The Cornual Nerve (Nervus cornualis), which is blocked with local anesthetic for surgical dehorning in cattle, is a terminal branch of which nerve?",
         ["Zygomaticotemporal nerve (branch of the Ophthalmic division of the Trigeminal nerve, CN V1)", "Infraorbital nerve (CN V2)", "Mandibular nerve (CN V3)", "Facial nerve (CN VII)"],
         0, "The cornual nerve arises from the zygomaticotemporal branch of the ophthalmic nerve; it courses caudally beneath the lateral frontal crest midway between the lateral canthus of the eye and the base of the horn, covered only by skin and frontalis muscle.",
         True, "Clinical Anatomy (ICAR PG PYQ)"),

        ("In cattle, paravertebral nerve block for standing flank laparotomy (such as cesarean section or rumenotomy) requires desensitization of which specific spinal nerves?",
         ["T13 (Last thoracic / costoabdominal), L1 (Iliohypogastric), and L2 (Ilioinguinal) nerves", "T10, T11, and T12", "L4, L5, and L6", "C6, C7, and C8"],
         0, "Farquharson's (proximal) and Magda's (distal) paravertebral blocks desensitize the dorsal and ventral primary branches of T13, L1, and L2 spinal nerves as they emerge from the intervertebral foramina along the transverse processes of L1, L2, and L4.",
         True, "Clinical Anatomy (ICAR PG PYQ)"),

        ("The 'Jugular Furrow' (sulcus jugularis) of the horse and ox, accommodating the external jugular vein for routine venipuncture, is bounded ventrally by which muscle?",
         ["Sternocephalicus muscle (specifically the sternomandibularis in ox and horse)", "Brachiocephalicus muscle", "Omohyoideus muscle", "Splenius muscle"],
         0, "The jugular groove is bounded dorsally by the brachiocephalicus muscle (cleidomastoideus) and ventrally by the sternocephalicus muscle (sternomandibularis); deeply, the omohyoideus separates the vein from the common carotid artery.",
         True, "Angiology (ICAR PG PYQ)")
    ]
    return qs

if __name__ == '__main__':
    qs = get_module3_questions()
    print(f"Anatomy Module 3 loaded: {len(qs)} questions")
