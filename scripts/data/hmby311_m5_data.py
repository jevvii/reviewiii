"""
HMBY311 Module 5 Dataset: Genetics, Human Inheritance and Cancer
Based on: /home/javvii/YearIII/HMBY311/module5/Genetics, Human Inheritance and Cancer.pptx
"""

HMBY_MODULE_5_ITEMS = [
    {
        "q": "What biological discipline is defined as the scientific study of heredity in general and of genes in particular?",
        "a": "Genetics",
        "distractors": ["Genomics", "Cytology", "Histology"],
        "explanation": "Genetics is the study of heredity in general and of genes in particular, forming a central pillar of biology.",
        "topic": "Genetics Fundamentals"
    },
    {
        "q": "Gregor Mendel referred to the inherited units passed onto descendants as 'factors', which are now scientifically known as what?",
        "a": "Genes",
        "distractors": ["Chromatids", "Histones", "Enzymes"],
        "explanation": "Inheritance of traits is determined by factors passed to descendants, now designated as genes.",
        "topic": "Genetics Fundamentals"
    },
    {
        "q": "What term describes the alternative or different forms of the same gene located at the same locus on homologous chromosomes?",
        "a": "Alleles",
        "distractors": ["Histones", "Codons", "Autosomes"],
        "explanation": "Alleles are different forms of the same gene.",
        "topic": "Alleles & Zygosity"
    },
    {
        "q": "An individual that possesses a pair of identical alleles for a particular gene (such as AA or aa) is described as what?",
        "a": "Homozygous",
        "distractors": ["Heterozygous", "Hemizygous", "Polygenic"],
        "explanation": "An individual with a pair of the same alleles is identified as homozygous.",
        "topic": "Alleles & Zygosity"
    },
    {
        "q": "An individual that possesses two different alleles for a particular gene (such as Aa) is described as what?",
        "a": "Heterozygous",
        "distractors": ["Homozygous", "Aneuploid", "Monohybrid"],
        "explanation": "An individual with different alleles for a gene is referred to as heterozygous.",
        "topic": "Alleles & Zygosity"
    },
    {
        "q": "In a heterozygous condition, what term describes the allele that masks the other allele and is phenotypically expressed?",
        "a": "Dominant",
        "distractors": ["Recessive", "Codominant", "Incomplete"],
        "explanation": "In heterozygous individuals, the allele that is expressed is described as being dominant.",
        "topic": "Alleles & Zygosity"
    },
    {
        "q": "In a heterozygous condition, what term describes the allele whose phenotypic expression is masked or suppressed?",
        "a": "Recessive",
        "distractors": ["Dominant", "Codominant", "Carrier"],
        "explanation": "The allele that is not expressed (masked) in a heterozygote is called recessive.",
        "topic": "Alleles & Zygosity"
    },
    {
        "q": "At the molecular level, what does a recessive allele typically produce compared to a dominant allele?",
        "a": "A nonfunctional protein or no protein at all",
        "distractors": ["A toxic protein", "An identical duplicate protein", "A structural lipid"],
        "explanation": "The dominant allele usually produces a functional protein, while the recessive allele produces either a nonfunctional protein or no protein at all.",
        "topic": "Alleles & Zygosity"
    },
    {
        "q": "Which Mendelian law states that allele pairs separate during gamete formation so that each gamete carries only one allele for each gene?",
        "a": "Law of Segregation",
        "distractors": ["Law of Independent Assortment", "Law of Dominance", "Law of Polygenic Inheritance"],
        "explanation": "The Law of Segregation states that allele pairs separate during gamete formation, with half receiving one allele and half the other.",
        "topic": "Mendelian Principles"
    },
    {
        "q": "Which Mendelian law states that each pair of alleles located on one kind of chromosome separates into gametes independently of alleles on different chromosomes?",
        "a": "Law of Independent Assortment",
        "distractors": ["Law of Segregation", "Law of Continuous Variation", "Law of Dominance"],
        "explanation": "The Law of Independent Assortment dictates that genes on different chromosomes segregate independently into gametes.",
        "topic": "Mendelian Principles"
    },
    {
        "q": "What genetic term refers to the precise genetic makeup or combination of alleles present within an individual?",
        "a": "Genotype",
        "distractors": ["Phenotype", "Karyotype", "Pedigree"],
        "explanation": "The genotype refers to the specific alleles present and combined in an individual (e.g., AA, Aa, aa).",
        "topic": "Genotype vs Phenotype"
    },
    {
        "q": "What term describes the observable physical, physiological, or biochemical traits expressed by an individual?",
        "a": "Phenotype",
        "distractors": ["Genotype", "Genome", "Allele frequency"],
        "explanation": "The phenotype refers to the observable physical or physiological traits expressed in the individual.",
        "topic": "Genotype vs Phenotype"
    },
    {
        "q": "What diagrammatic tool is used in genetics to calculate and predict the probabilities of offspring genotypes and phenotypes from parental gametes?",
        "a": "Punnett square",
        "distractors": ["Pedigree chart", "Karyotype diagram", "Chomsky grid"],
        "explanation": "A Punnett square is used to determine the probability that each gamete cross will occur.",
        "topic": "Genetic Crosses"
    },
    {
        "q": "If a homozygous dominant individual (AA) crosses with a homozygous recessive individual (aa), what will be the genotype of all their offspring?",
        "a": "100% Heterozygous (Aa)",
        "distractors": ["50% AA, 50% aa", "25% AA, 75% aa", "100% Homozygous dominant (AA)"],
        "explanation": "Crossing AA x aa yields 100% heterozygous (Aa) offspring expressing the dominant phenotype.",
        "topic": "Genetic Crosses"
    },
    {
        "q": "When two heterozygous individuals (Aa x Aa) mate, what is the expected genotypic ratio among their offspring?",
        "a": "25% AA, 50% Aa, 25% aa",
        "distractors": ["75% Aa, 25% aa", "50% AA, 50% aa", "100% Aa"],
        "explanation": "An Aa x Aa cross produces 25% homozygous dominant (AA), 50% heterozygous (Aa), and 25% homozygous recessive (aa).",
        "topic": "Genetic Crosses"
    },
    {
        "q": "When two heterozygous individuals (Aa x Aa) mate, what is the expected phenotypic ratio for a trait following complete dominance?",
        "a": "75% dominant, 25% recessive",
        "distractors": ["50% dominant, 50% recessive", "100% dominant", "25% dominant, 75% recessive"],
        "explanation": "Because AA and Aa both show the dominant phenotype, 75% exhibit the dominant trait and 25% show the recessive trait.",
        "topic": "Genetic Crosses"
    },
    {
        "q": "What term is given to a heterozygous individual who displays a normal/dominant phenotype but carries a recessive allele for a genetic disorder?",
        "a": "Carrier",
        "distractors": ["Mutant", "Vector", "Proband"],
        "explanation": "A heterozygous individual that shows the dominant phenotype while carrying a recessive allele is called a carrier.",
        "topic": "Genetic Crosses"
    },
    {
        "q": "What is a chart constructed to illustrate genetic relationships, ancestral lineages, and inheritance patterns among individuals in an extended family?",
        "a": "Pedigree",
        "distractors": ["Punnett square", "Cladogram", "Karyogram"],
        "explanation": "Pedigrees are diagrams constructed to show genetic relationships among individuals in an extended family.",
        "topic": "Pedigrees"
    },
    {
        "q": "What type of non-Mendelian inheritance occurs when both alleles are simultaneously and clearly apparent in the heterozygous phenotype?",
        "a": "Codominance",
        "distractors": ["Incomplete dominance", "Complete dominance", "Polygenic inheritance"],
        "explanation": "Codominance takes place when both alleles are fully and distinctly expressed in the phenotype (e.g., AB blood type).",
        "topic": "Non-Mendelian Inheritance"
    },
    {
        "q": "What pattern of inheritance occurs when a heterozygous phenotype is intermediate between the two homozygous phenotypes (e.g., wavy hair from curly and straight)?",
        "a": "Incomplete dominance",
        "distractors": ["Codominance", "Pleiotropy", "Sex-linkage"],
        "explanation": "Incomplete dominance occurs when expression in a heterozygote is intermediate between homozygous dominant and homozygous recessive.",
        "topic": "Non-Mendelian Inheritance"
    },
    {
        "q": "What genetic scenario occurs when there are three or more distinct alleles for a single gene existing within a population, as exemplified by the ABO blood group system?",
        "a": "Multiple alleles",
        "distractors": ["Polygenic inheritance", "Gene duplication", "Epistasis"],
        "explanation": "Multiple alleles refers to the condition where three or more alleles exist for a particular gene in a population, such as ABO blood types (IA, IB, i).",
        "topic": "Non-Mendelian Inheritance"
    },
    {
        "q": "What form of inheritance occurs when two or more distinct genes govern the expression of a single continuous phenotypic trait such as height, skin color, or eye color?",
        "a": "Polygenic inheritance",
        "distractors": ["Multiple alleles", "Incomplete dominance", "Monogenic inheritance"],
        "explanation": "Polygenic inheritance occurs when more than one gene controls the trait. Examples include human height, skin pigmentation, and eye color.",
        "topic": "Non-Mendelian Inheritance"
    },
    {
        "q": "Traits whose phenotypic expression depends on both the presence of specific alleles and the levels of circulating sex hormones (such as male-pattern baldness) are called what?",
        "a": "Sex-influenced traits",
        "distractors": ["Sex-linked traits", "Autosomal recessive traits", "Mitochondrial traits"],
        "explanation": "The expression of sex-influenced traits depends on both the presence of the allele and circulating sex hormones (e.g. testosterone).",
        "topic": "Non-Mendelian Inheritance"
    },
    {
        "q": "In the human genetic traits inventory, which earlobe phenotype is dominant over attached earlobes?",
        "a": "Free earlobes",
        "distractors": ["Attached earlobes", "Pointed earlobes", "Lobeless"],
        "explanation": "Definite free earlobes are dominant; attached earlobes are recessive.",
        "topic": "Human Genetic Traits"
    },
    {
        "q": "In human traits, is having a widow's peak hairline dominant or recessive to a straight hairline?",
        "a": "Dominant",
        "distractors": ["Recessive", "Codominant", "Polygenic"],
        "explanation": "A widow's peak is a dominant trait; a straight hairline is recessive.",
        "topic": "Human Genetic Traits"
    },
    {
        "q": "In human hand genetics, is the presence of six fingers (polydactyly) dominant or recessive to having five fingers?",
        "a": "Dominant",
        "distractors": ["Recessive", "Codominant", "Sex-linked"],
        "explanation": "Having six fingers (polydactyly) is genetically dominant; five fingers is recessive.",
        "topic": "Human Genetic Traits"
    },
    {
        "q": "When clasping hands with thumbs crossed, which thumb placement is genetically dominant in humans?",
        "a": "Left thumb over right thumb",
        "distractors": ["Right thumb over left thumb", "Parallel thumbs", "Interlocked thumbs"],
        "explanation": "Placing the left thumb over the right thumb when crossing thumbs is dominant; right over left is recessive.",
        "topic": "Human Genetic Traits"
    },
    {
        "q": "In human facial genetics, is the presence of facial dimples dominant or recessive?",
        "a": "Dominant",
        "distractors": ["Recessive", "Incomplete dominant", "Sex-influenced"],
        "explanation": "Presence of dimples is dominant; absence of dimples is recessive.",
        "topic": "Human Genetic Traits"
    },
    {
        "q": "In tongue genetics, is the ability to roll the side edges of the tongue upward dominant or recessive?",
        "a": "Dominant",
        "distractors": ["Recessive", "Codominant", "Incompletely penetrant"],
        "explanation": "The ability to roll the lateral edges of the tongue upward is a dominant trait; inability is recessive.",
        "topic": "Human Genetic Traits"
    },
    {
        "q": "In toe anatomy, which condition is genetically dominant regarding toe length in humans?",
        "a": "Second toe longer than first toe",
        "distractors": ["First toe longer than second toe", "Equal length toes", "Third toe longer than first toe"],
        "explanation": "Having the second toe longer than the big toe (Morton's toe) is dominant; first toe longer is recessive.",
        "topic": "Human Genetic Traits"
    },
    {
        "q": "Which prenatal diagnostic procedure involves sampling and analyzing amniotic fluid and floating fetal cells from within the pregnant mother to detect genetic disorders?",
        "a": "Amniocentesis",
        "distractors": ["Chorionic villi sampling (CVS)", "Ultrasound imaging", "Fetoscopy"],
        "explanation": "In amniocentesis, a sample of amniotic fluid containing fetal cells is withdrawn from the uterus and analyzed for genetic problems.",
        "topic": "Detecting Genetic Disorders"
    },
    {
        "q": "Which prenatal diagnostic technique samples cells directly from the placental projections to detect chromosomal and genetic abnormalities in a developing fetus?",
        "a": "Chorionic villi sampling (CVS)",
        "distractors": ["Amniocentesis", "CT scanning", "PET scanning"],
        "explanation": "Chorionic villi sampling (CVS) involves sampling tissue from the chorionic villi of the placenta for genetic diagnosis.",
        "topic": "Detecting Genetic Disorders"
    },
    {
        "q": "What fundamental biological characteristic is universally shared by all forms of cancer?",
        "a": "Uncontrolled cell division",
        "distractors": ["Programmed cell death", "Bacterial infection", "Decreased protein synthesis"],
        "explanation": "All cancers share one universal hallmark: uncontrolled and unregulated cell division.",
        "topic": "Cancer Biology"
    },
    {
        "q": "What is an abnormal mass of tissue resulting from uncontrolled cell division, also known medically as a neoplasm?",
        "a": "Tumor",
        "distractors": ["Cyst", "Polyp", "Histone"],
        "explanation": "A tumor (or neoplasm, meaning 'new growth') is an abnormal growth of cells that forms a tissue mass.",
        "topic": "Tumors & Neoplasms"
    },
    {
        "q": "What type of tumor is enclosed within a capsule of connective tissue and does not invade surrounding tissues or spread to distant sites?",
        "a": "Benign tumor",
        "distractors": ["Malignant tumor", "Carcinoma in situ", "Metastatic tumor"],
        "explanation": "A benign tumor is surrounded by a connective tissue capsule and does not invade adjacent tissues or metastasize.",
        "topic": "Tumors & Neoplasms"
    },
    {
        "q": "What type of tumor lacks a capsule, invades surrounding tissues, can spread throughout the body, and is properly classified as cancerous?",
        "a": "Malignant tumor",
        "distractors": ["Benign tumor", "Dysplastic cyst", "Adenoma"],
        "explanation": "Malignant tumors can invade neighboring tissues and colonize distant body locations; they are properly termed cancerous.",
        "topic": "Tumors & Neoplasms"
    },
    {
        "q": "What term defines the migration and spread of cancer cells from their primary tumor site to distant locations throughout the body?",
        "a": "Metastasis",
        "distractors": ["Dysplasia", "Angiogenesis", "Apoptosis"],
        "explanation": "Metastasis refers to the spread of cancer cells from one part of the body to another via the bloodstream or lymphatic system.",
        "topic": "Cancer Progression"
    },
    {
        "q": "What term describes the precancerous histological state marked by abnormal changes in cell shape, enlarged nuclei, and disorganized tissue architecture?",
        "a": "Dysplasia",
        "distractors": ["Hyperplasia", "Carcinoma in situ", "Metastasis"],
        "explanation": "Dysplasia describes abnormal changes in cell shape, nuclei, and internal tissue organization in precancerous tissue.",
        "topic": "Stages of Cancer Development"
    },
    {
        "q": "What term refers to a localized malignant tumor that has reached a critical mass of roughly 1 million cells but has not yet penetrated the basement membrane?",
        "a": "Carcinoma in situ",
        "distractors": ["Dysplasia", "Invasive carcinoma", "Benign neoplasm"],
        "explanation": "Carcinoma in situ is a localized tumor of roughly 1 million cells where the interior experiences nutrient starvation and waste poisoning.",
        "topic": "Stages of Cancer Development"
    },
    {
        "q": "What process is initiated when tumor cells secrete chemical signals that stimulate the formation and ingrowth of new blood vessels?",
        "a": "Angiogenesis",
        "distractors": ["Apoptosis", "Metastasis", "Cytokinesis"],
        "explanation": "Cancer cells release chemicals that initiate the growth of new blood vessels, delivering nutrients, removing wastes, and providing a route for metastasis.",
        "topic": "Cancer Progression"
    },
    {
        "q": "What is the physiological process of programmed cell death that eliminates cells with severe, irreparable genetic damage?",
        "a": "Apoptosis",
        "distractors": ["Necrosis", "Dysplasia", "Mitosis"],
        "explanation": "Apoptosis is programmed cell death triggered when genetic damage is too severe to be repaired.",
        "topic": "Control of Cancer"
    },
    {
        "q": "What category of cellular genes acts as the cell's damage control system by detecting DNA damage and halting division or initiating repair?",
        "a": "Tumor suppressor genes",
        "distractors": ["Proto-oncogenes", "Oncogenes", "Histone genes"],
        "explanation": "Tumor suppressor genes help detect damaged DNA, pause the cell cycle, and manage the repair of genetic defects.",
        "topic": "Cancer Genetics"
    },
    {
        "q": "Normal regulatory genes that stimulate cell division in response to growth factors under controlled conditions are called what?",
        "a": "Proto-oncogenes",
        "distractors": ["Oncogenes", "Tumor suppressor genes", "Histones"],
        "explanation": "Proto-oncogenes produce growth factors or signal transducers that stimulate normal, orderly cell division.",
        "topic": "Cancer Genetics"
    },
    {
        "q": "What is a mutated, cancer-causing form of a proto-oncogene that drives continuous, uncontrolled cell division without normal external growth signals?",
        "a": "Oncogene",
        "distractors": ["Tumor suppressor gene", "Allele", "Autosome"],
        "explanation": "Mutation of a proto-oncogene results in an oncogene, which accelerates cell division without regulatory stimuli.",
        "topic": "Cancer Genetics"
    },
    {
        "q": "Which two types of immune cells normally patrol the body and directly destroy emerging cancerous cells?",
        "a": "Natural killer cells and cytotoxic T cells",
        "distractors": ["Erythrocytes and platelets", "B cells and basophils", "Neutrophils and eosinophils"],
        "explanation": "Natural killer (NK) cells and cytotoxic T cells recognize and destroy abnormal or cancerous cells.",
        "topic": "Immune Surveillance"
    },
    {
        "q": "Any environmental, chemical, physical, or biological agent that promotes genetic mutations and fosters the development of cancer is termed a what?",
        "a": "Carcinogen",
        "distractors": ["Allergen", "Pathogen", "Histone"],
        "explanation": "A carcinogen is an environmental agent that fosters cancer development by inducing genetic mutations.",
        "topic": "Cancer Causes"
    },
    {
        "q": "Which virus is a well-established biological cause of cervical, anal, and throat cancers in humans?",
        "a": "Human Papilloma Virus (HPV)",
        "distractors": ["Rhinovirus", "Influenza virus", "Norovirus"],
        "explanation": "HPV is a DNA virus known to cause cervical and other genital/oropharyngeal cancers.",
        "topic": "Cancer Causes"
    },
    {
        "q": "Which two viral pathogens that cause chronic liver inflammation are established etiologic agents of hepatocellular carcinoma (liver cancer)?",
        "a": "Hepatitis B and Hepatitis C viruses",
        "distractors": ["Hepatitis A and Hepatitis E viruses", "Rotavirus and Adenovirus", "Cytomegalovirus and Rabies"],
        "explanation": "Chronic infections with Hepatitis B and C viruses significantly increase the risk of liver cancer.",
        "topic": "Cancer Causes"
    },
    {
        "q": "Which herpesvirus family member is causally linked to mononucleosis, Burkitt lymphoma, and nasopharyngeal carcinoma?",
        "a": "Epstein-Barr virus (EBV)",
        "distractors": ["Human Papilloma Virus", "Varicella Zoster virus", "Hepatitis A virus"],
        "explanation": "Epstein-Barr virus (EBV) is linked to infectious mononucleosis and specific malignancies such as Burkitt lymphoma.",
        "topic": "Cancer Causes"
    },
    {
        "q": "What type of environmental radiation, commonly emitted by the sun and tanning beds, damages cellular DNA and increases the risk of skin cancers?",
        "a": "Ultraviolet (UV) radiation",
        "distractors": ["Infrared radiation", "Microwave radiation", "Radio waves"],
        "explanation": "Exposure to ultraviolet (UV) radiation causes pyrimidine dimers in DNA, elevating the risk of melanoma and other skin carcinomas.",
        "topic": "Cancer Causes"
    },
    {
        "q": "What diagnostic procedure involves extracting a small tissue specimen via needle or minor surgery for microscopic evaluation by a pathologist?",
        "a": "Biopsy",
        "distractors": ["Endoscopy", "Amniocentesis", "Angiography"],
        "explanation": "A biopsy involves removing a small piece of tissue to examine whether cells display the characteristic architectural features of malignancy.",
        "topic": "Diagnosing Cancer"
    },
    {
        "q": "What diagnostic blood tests detect specific proteins or chemicals synthesized by tumor cells or produced by body tissues in response to a neoplasm?",
        "a": "Tumor marker tests",
        "distractors": ["Complete blood count (CBC)", "Hematocrit test", "Electrolyte panel"],
        "explanation": "Tumor marker tests detect circulating substances produced either directly by cancer cells or by host tissues reacting to a tumor.",
        "topic": "Diagnosing Cancer"
    },
    {
        "q": "Which bodily secretion is analyzed cytologically or genetically for malignant cells when screening for lung cancer?",
        "a": "Sputum",
        "distractors": ["Urine", "Feces", "Saliva"],
        "explanation": "Sputum cytology and DNA testing are used to detect early signs of lung cancer.",
        "topic": "Diagnosing Cancer"
    },
    {
        "q": "Testing a patient's urine for atypical cells and specific mutational markers is primarily used to detect which type of malignancy?",
        "a": "Bladder cancer",
        "distractors": ["Colon cancer", "Lung cancer", "Breast cancer"],
        "explanation": "Urine cytology and marker tests are utilized to detect signs of bladder cancer.",
        "topic": "Diagnosing Cancer"
    },
    {
        "q": "Analysis of fecal samples for occult blood and exfoliated mutant DNA markers is routinely employed to screen for which cancer?",
        "a": "Colon cancer",
        "distractors": ["Lung cancer", "Bladder cancer", "Brain cancer"],
        "explanation": "Fecal immunochemical tests and stool DNA analyses are used to detect early signs of colorectal cancer.",
        "topic": "Diagnosing Cancer"
    },
    {
        "q": "Which cancer treatment modality utilizes high-energy beams directed at malignant tissue to cause catastrophic double-strand DNA breaks and trigger apoptosis?",
        "a": "Radiation therapy",
        "distractors": ["Chemotherapy", "Surgery", "Immunotherapy"],
        "explanation": "Radiation therapy causes extensive DNA damage within tumor cells, triggering programmed cell death.",
        "topic": "Treating Cancer"
    },
    {
        "q": "Which systemic cancer therapy employs pharmacological agents that circulate throughout the bloodstream to eliminate rapidly proliferating cells body-wide?",
        "a": "Chemotherapy",
        "distractors": ["Surgery", "Radiation therapy", "Cryotherapy"],
        "explanation": "Chemotherapy drugs reach all parts of the body via the vascular system and selectively destroy rapidly dividing cells.",
        "topic": "Treating Cancer"
    },
    {
        "q": "Which modern therapeutic approach boosts, trains, or genetically engineers a patient's immune system to recognize and eradicate malignant cells?",
        "a": "Immunotherapy",
        "distractors": ["Radiation therapy", "Chemotherapy", "Surgery"],
        "explanation": "Immunotherapy enhances the host immune response against cancer cells using cancer vaccines, checkpoint inhibitors, or cytokine factors.",
        "topic": "Treating Cancer"
    },
    {
        "q": "What cancer treatment strategy starves growing tumors by administering drugs that block the signaling pathways responsible for recruiting new capillaries?",
        "a": "Inhibition of blood vessel formation (anti-angiogenesis)",
        "distractors": ["Chemotherapy", "Gene therapy", "Radiation therapy"],
        "explanation": "Inhibition of blood vessel formation (anti-angiogenic therapy) prevents vascularization, depriving tumors of oxygen and nutrients.",
        "topic": "Treating Cancer"
    },
    {
        "q": "What emerging therapeutic paradigm seeks to modify, replace, or repair defective genetic sequences inside malignant cells to halt their proliferation or induce apoptosis?",
        "a": "Gene therapy",
        "distractors": ["Surgery", "Chemotherapy", "Radiation therapy"],
        "explanation": "Gene therapy alters the genetic material of cancer cells with the goal of repairing defective regulatory pathways or triggering death.",
        "topic": "Treating Cancer"
    }
]

print(f"Total HMBY Module 5 items crafted: {len(HMBY_MODULE_5_ITEMS)}")
