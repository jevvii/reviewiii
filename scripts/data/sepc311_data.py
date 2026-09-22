"""
SEPC311: Social, Ethical, and Professional Issues in Computing
Comprehensive Questionnaires & Answer Keys
Based on:
- /home/javvii/YearIII/SEPC311/week2-3/ethical_theories.txt
- /home/javvii/YearIII/SEPC311/week4-5/computer_ethics.txt
- Activities 2, 3, and 4 in SEPC311
- "Social, Ethical, Legal and Professional Issues in Computing" by Dr. Charlemagne Laviña
"""

SEPC_MODULE_1_ITEMS = [
    {
        "q": "The word 'ethics' is derived from the ancient Greek word 'ethos', which literally translates to what?",
        "a": "character",
        "distractors": [
            "knowledge",
            "law",
            "duty"
        ],
        "topic": "Etymology of Ethics",
        "explanation": "Ethics comes from the Greek word 'ethos', which means character, representing the foundational disposition and moral principles of an individual or community."
    },
    {
        "q": "What discipline is also known interchangeably as Moral Philosophy, involving the systematizing, defending, and recommending of concepts of right and wrong conduct?",
        "a": "Ethics",
        "distractors": [
            "Epistemology",
            "Aesthetics",
            "Ontology"
        ],
        "topic": "Moral Philosophy",
        "explanation": "Ethics, also known as Moral Philosophy, is the philosophical study that systematizes, defends, and recommends concepts of right and wrong conduct."
    },
    {
        "q": "Ethics broadly describes the way in which human beings examine and understand life in terms of good and bad or ____ and wrong.",
        "a": "right",
        "distractors": [
            "legal",
            "profitable",
            "customary"
        ],
        "topic": "Definition of Ethics",
        "explanation": "Ethics broadly describes how we evaluate human actions, understanding existence through the dualities of good versus bad and right versus wrong."
    },
    {
        "q": "Which major philosophical endeavor within ethics focuses on defending and recommending concepts of honorable and proper conduct rather than merely describing customs?",
        "a": "systematizing",
        "distractors": [
            "monetizing",
            "legislating",
            "obfuscating"
        ],
        "topic": "Branches of Philosophy",
        "explanation": "Ethics involves systematizing, defending, and recommending concepts of right and wrong conduct to guide human decision-making."
    },
    {
        "q": "Which ethical theory asserts that there is no universal moral norm of right and wrong, allowing opposing moral judgments to both be valid?",
        "a": "Relativism",
        "distractors": [
            "Kantianism",
            "Divine Command Theory",
            "Ethical Egoism"
        ],
        "topic": "Relativism Overview",
        "explanation": "Relativism is the ethical theory holding that there is no universal moral truth; different individuals or societies can hold opposite moral views and both be considered right."
    },
    {
        "q": "Into what two primary categories is the doctrine of Relativism commonly divided?",
        "a": "Subjective Relativism and Cultural Relativism",
        "distractors": [
            "Act Relativism and Rule Relativism",
            "Divine Relativism and Secular Relativism",
            "Psychological Relativism and Ethical Relativism"
        ],
        "topic": "Two Kinds of Relativism",
        "explanation": "Relativism is categorized into Subjective Relativism (individual-centered) and Cultural Relativism (society-centered)."
    },
    {
        "q": "Which ethical stance holds that each individual person decides right and wrong exclusively for himself or herself?",
        "a": "Subjective Relativism",
        "distractors": [
            "Cultural Relativism",
            "Kantianism",
            "Deontology"
        ],
        "topic": "Subjective Relativism",
        "explanation": "Subjective Relativism holds that each individual person is the supreme arbiter of morality for themselves, rejecting any objective moral standards."
    },
    {
        "q": "The popular colloquial expression 'What's right for you, may not be right for me' encapsulates the core mindset of which ethical perspective?",
        "a": "Subjective Relativism",
        "distractors": [
            "Divine Command Theory",
            "Kantian Deontology",
            "Utilitarianism"
        ],
        "topic": "Subjective Relativism Maxim",
        "explanation": "The slogan 'What's right for you may not be right for me' is the definitive philosophical motto of Subjective Relativism."
    },
    {
        "q": "In the context of Subjective Relativism, heated political and societal debates regarding the Reproductive Health (RH) Bill in the Philippines demonstrate that moral stances often depend on individual ____.",
        "a": "beliefs",
        "distractors": [
            "statutes",
            "algorithms",
            "tariffs"
        ],
        "topic": "Subjective Relativism Examples",
        "explanation": "Debates over controversial measures like the RH Bill in the Philippines illustrate subjective relativism, where deeply personal convictions guide individual moral evaluations."
    },
    {
        "q": "Why is the distinction between what a person thinks is right and doing whatever they want to do considered a major critique against Subjective Relativism?",
        "a": "It is not sharply drawn",
        "distractors": [
            "It is strictly codified",
            "It is enforced by police",
            "It guarantees universal consensus"
        ],
        "topic": "Critique of Subjective Relativism",
        "explanation": "A primary argument against Subjective Relativism is that the line between moral conviction and personal selfish desire is not sharply drawn, reducing morality to mere caprice."
    },
    {
        "q": "What psychological tendency makes Subjective Relativism dangerous when applied to unethical personal conduct?",
        "a": "Rationalizing bad behavior",
        "distractors": [
            "Objective introspection",
            "Strict duty adherence",
            "Universal empathy"
        ],
        "topic": "Rationalization in Relativism",
        "explanation": "Humans are adept at rationalizing bad behavior; if morality is entirely subjective, any selfish or destructive act can be conveniently rationalized as 'right for me'."
    },
    {
        "q": "In Philippine elections, when an impoverished voter justifies selling their vote for quick cash to feed their family by claiming it feels right in their mind, they are demonstrating ____ relativism.",
        "a": "subjective",
        "distractors": [
            "cultural",
            "divine",
            "categorical"
        ],
        "topic": "Philippine Applied Ethics - Vote Selling",
        "explanation": "Vote-selling rationalized under the guise that 'survival makes it right for me' is an applied manifestation of Subjective Relativism."
    },
    {
        "q": "Which ethical theory states that the meaning of 'right' and 'wrong' rests entirely with a given society's actual moral guidelines and customs?",
        "a": "Cultural Relativism",
        "distractors": [
            "Subjective Relativism",
            "Ethical Egoism",
            "Kantianism"
        ],
        "topic": "Cultural Relativism Definition",
        "explanation": "Cultural Relativism asserts that ethical norms are shaped and validated by the collective cultural traditions and guidelines of a specific society."
    },
    {
        "q": "Under Cultural Relativism, ethics is fundamentally based on the ____ of the social environment.",
        "a": "culture",
        "distractors": [
            "genetics",
            "divine scripture",
            "pure reason"
        ],
        "topic": "Basis of Cultural Relativism",
        "explanation": "Cultural Relativism roots moral authority in the evolving culture, shared customs, and communal practices of the surrounding environment."
    },
    {
        "q": "In Philippine politics, the customary practice of appointing a losing election candidate to a government post after the one-year ban by their winning party-mate reflects which ethical phenomenon?",
        "a": "Cultural Relativism",
        "distractors": [
            "Kantian Deontology",
            "Divine Command Theory",
            "Absolute Objectivism"
        ],
        "topic": "Philippine Political Culture",
        "explanation": "Political patronage and the appointment of losing party-mates after the constitutional one-year ban illustrate cultural relativism embedded in Philippine political culture."
    },
    {
        "q": "The socially accepted practice in Filipino culture of telling 'white lies' to protect family harmony and preserve smooth interpersonal relationships (SIR) is an example of ____ relativism.",
        "a": "cultural",
        "distractors": [
            "subjective",
            "deontological",
            "categorical"
        ],
        "topic": "Cultural Traditions - White Lies",
        "explanation": "Telling white lies for the emotional well-being of family and friends is accepted in specific cultural milieus to maintain relational harmony, exemplifying Cultural Relativism."
    },
    {
        "q": "The informal collegiate practice known as the 'F2 Epidemic' among students sharing answers or shortcuts stems from peer solidarity analyzed under which ethical theory?",
        "a": "Cultural Relativism",
        "distractors": [
            "Divine Command Theory",
            "Kantianism",
            "Ethical Egoism"
        ],
        "topic": "Academic Culture - F2 Phenomenon",
        "explanation": "Peer-endorsed academic shortcuts shared among students reflect a subculture's localized norms, viewed through Cultural Relativism."
    },
    {
        "q": "Which ethical framework posits that good actions are those aligned with the will of God, and bad actions are contrary to God's will?",
        "a": "Divine Command Theory",
        "distractors": [
            "Ethical Egoism",
            "Consequentialism",
            "Subjective Relativism"
        ],
        "topic": "Divine Command Theory",
        "explanation": "Divine Command Theory grounds morality in divine will, stating that what is morally right is commanded by God, and what is wrong is forbidden by God."
    },
    {
        "q": "In Divine Command Theory, the ultimate moral authority and standard of righteous conduct originates from which entity?",
        "a": "God",
        "distractors": [
            "Society",
            "The State",
            "The Individual"
        ],
        "topic": "Divine Authority",
        "explanation": "Divine Command Theory derives all moral authority directly from the commandments and revealed will of God."
    },
    {
        "q": "Louie attends Holy Mass every Sunday, listens intently to the homily, and strives to apply the teachings of the Holy Gospel to his daily conduct. Louie is guided by which ethical theory?",
        "a": "Divine Command Theory",
        "distractors": [
            "Ethical Egoism",
            "Cultural Relativism",
            "Consequentialism"
        ],
        "topic": "Divine Command Case Study",
        "explanation": "Louie's deliberate obedience to religious scripture and gospel teachings exemplifies the application of Divine Command Theory."
    },
    {
        "q": "Which philosophy holds that each individual person ought to pursue exclusively his or her own self-interest?",
        "a": "Ethical Egoism",
        "distractors": [
            "Utilitarianism",
            "Altruism",
            "Cultural Relativism"
        ],
        "topic": "Ethical Egoism Definition",
        "explanation": "Ethical Egoism is the normative ethical position that moral agents ought to act exclusively in their own self-interest."
    },
    {
        "q": "According to Ethical Egoism, the morally right action in any particular situation is the one that will provide the person with the maximum ____ benefit.",
        "a": "long-term",
        "distractors": [
            "momentary",
            "collective",
            "societal"
        ],
        "topic": "Egoistic Maximization",
        "explanation": "Ethical Egoism defines righteousness as that which yields the greatest long-term advantage and benefit to the individual agent."
    },
    {
        "q": "An individual who publicly endorses and campaigns for a political candidate solely to secure a lucrative government appointment or business favor is operating under ____ egoism.",
        "a": "ethical",
        "distractors": [
            "deontological",
            "altruistic",
            "cultural"
        ],
        "topic": "Ethical Egoism in Politics",
        "explanation": "Backing a candidate strictly for personal reward and self-advancement is a classic illustration of Ethical Egoism."
    },
    {
        "q": "Insincerely hitting 'Like' on a colleague's or supervisor's social media post merely to curry favor, gain visibility, or avoid friction is colloquially described as 'The Like that You Don't Like' under which framework?",
        "a": "Ethical Egoism",
        "distractors": [
            "Kantianism",
            "Divine Command Theory",
            "Categorical Imperative"
        ],
        "topic": "Social Media Egoism",
        "explanation": "Fawning or flattering someone online solely to advance one's personal interests exemplifies the calculating nature of Ethical Egoism."
    },
    {
        "q": "A mother who has only one piece of bread and willingly deprives herself of food so her starving child may eat represents an act of self-sacrifice that directly contradicts which philosophy?",
        "a": "Ethical Egoism",
        "distractors": [
            "Altruism",
            "Divine Command Theory",
            "Kantianism"
        ],
        "topic": "Altruism vs Egoism",
        "explanation": "Maternal self-sacrifice is pure altruism, serving as a powerful counter-example to the claim that human morality is solely governed by Ethical Egoism."
    },
    {
        "q": "A father who continually works grueling overtime shifts solely to finance his family's survival, expecting no selfish luxury in return, acts in opposition to the core premise of ____ egoism.",
        "a": "ethical",
        "distractors": [
            "deontological",
            "pragmatic",
            "normative"
        ],
        "topic": "Paternal Sacrifice vs Egoism",
        "explanation": "Selfless labor for family welfare demonstrates altruistic love and duty, contradicting the self-absorbed focus of Ethical Egoism."
    },
    {
        "q": "When a senior sibling voluntarily stops schooling to work and fund the education of younger siblings due to poverty, their sacrifice exemplifies ____, the polar opposite of Ethical Egoism.",
        "a": "altruism",
        "distractors": [
            "relativism",
            "hedonism",
            "egoism"
        ],
        "topic": "Sibling Sacrifice",
        "explanation": "Voluntarily sacrificing one's own educational prospects for the advancement of others is an act of altruism, directly refuting pure egoism."
    },
    {
        "q": "Which ethical doctrine asserts that the morality of an action is judged solely by the acceptability and desirability of its results or outcomes?",
        "a": "Consequentialism",
        "distractors": [
            "Deontology",
            "Divine Command Theory",
            "Subjective Relativism"
        ],
        "topic": "Consequentialism Definition",
        "explanation": "Consequentialism holds that the consequences of an action are the ultimate basis for any moral judgment about the rightness or wrongness of that action."
    },
    {
        "q": "Which famous philosophical aphorism best summarizes the foundational principle of Consequentialism?",
        "a": "The end justifies the means",
        "distractors": [
            "Duty for duty's sake",
            "What is right for you is right for me",
            "Do unto others as you would have them do unto you"
        ],
        "topic": "Consequentialist Maxim",
        "explanation": "'The end justifies the means' asserts that morally questionable actions are acceptable if they yield a superior or desirable final outcome."
    },
    {
        "q": "In sports and politics, when an actor executes a deliberate foul or questionable tactical maneuver to secure team victory or political survival, they are adopting a ____ moral approach.",
        "a": "consequentialist",
        "distractors": [
            "Kantian",
            "deontological",
            "divine"
        ],
        "topic": "Applied Consequentialism",
        "explanation": "Prioritizing the final victory or political outcome over strict rule adherence is the hallmark of consequentialist reasoning."
    },
    {
        "q": "The historic political resignation of President Joseph 'Erap' Estrada during the EDSA Dos uprising was debated as a necessity to avert nationwide chaos, reflecting which ethical reasoning?",
        "a": "Consequentialism",
        "distractors": [
            "Ethical Egoism",
            "Cultural Relativism",
            "Divine Command Theory"
        ],
        "topic": "EDSA II Consequentialism",
        "explanation": "Justifying a leader's extra-constitutional departure to prevent widespread bloodshed and restore stability is rooted in consequentialist ethics."
    },
    {
        "q": "If a math student ignores a teacher's mandatory long method and uses an unauthorized shorter algebraic formula to arrive at the correct answer quickly, the student is thinking like a ____.",
        "a": "consequentialist",
        "distractors": [
            "Kantian",
            "deontologist",
            "divine ethicist"
        ],
        "topic": "Algebraic Shortcut Dilemma",
        "explanation": "A student who prioritizes arriving at the correct final solution regardless of bypassing the mandated procedure embodies consequentialism."
    },
    {
        "q": "Who was the renowned 18th-century German philosopher who formulated the duty-based ethical framework known as Kantianism?",
        "a": "Immanuel Kant",
        "distractors": [
            "John Stuart Mill",
            "Friedrich Nietzsche",
            "Aristotle"
        ],
        "topic": "Immanuel Kant",
        "explanation": "Immanuel Kant was the German philosopher who pioneered deontology, establishing that morality is grounded in pure reason and duty."
    },
    {
        "q": "Kantianism is classified as what kind of theory, which evaluates actions based on adherence to moral obligations rather than results?",
        "a": "obligation-based",
        "distractors": [
            "outcome-based",
            "pleasure-based",
            "custom-based"
        ],
        "topic": "Deontology Nature",
        "explanation": "Kantianism is an obligation-based (deontological) theory where moral actions are determined by duty rather than consequences."
    },
    {
        "q": "According to Immanuel Kant, true morality must be grounded on which human cognitive faculty rather than emotional desires or consequences?",
        "a": "pure reason",
        "distractors": [
            "cultural tradition",
            "emotional impulse",
            "divine revelation"
        ],
        "topic": "Basis of Morality in Reason",
        "explanation": "Kant argued that moral principles are universal truths derived from pure reason, accessible to all rational human beings."
    },
    {
        "q": "In Kantian deontology, performing an action purely because it is one's moral obligation is known as acting from ____.",
        "a": "duty",
        "distractors": [
            "sympathy",
            "convenience",
            "greed"
        ],
        "topic": "Concept of Duty",
        "explanation": "In Kantian ethics, moral worth exists only when an action is performed strictly for the sake of duty ('duty for duty's sake')."
    },
    {
        "q": "A defense attorney who zealously defends an unpopular accused criminal in court to uphold the legal right to counsel, regardless of personal feelings, is upholding ____ ethics.",
        "a": "Kantian",
        "distractors": [
            "subjective relativist",
            "egoist",
            "hedonist"
        ],
        "topic": "Legal Duty Case",
        "explanation": "A lawyer fulfilling their sworn professional duty to defend a client, irrespective of personal sentiment or public backlash, embodies Kantian deontology."
    },
    {
        "q": "Soldiers and law enforcement officers who maintain peace, order, and constitutional loyalty even in mortal danger act from a professional sense of ____.",
        "a": "duty",
        "distractors": [
            "profit",
            "personal benefit",
            "cultural custom"
        ],
        "topic": "Sworn Duty",
        "explanation": "Law enforcers sworn to protect the public exhibit deontological duty, honoring their oath above personal safety or comfort."
    },
    {
        "q": "In the classroom parable of the dying wealthy friend who entrusted three envelopes of cash to his priest, doctor, and lawyer to bury with him, which professional strictly honored his sworn contractual obligation?",
        "a": "The lawyer",
        "distractors": [
            "The priest",
            "The doctor",
            "The nurse"
        ],
        "topic": "Parable of the Coffin",
        "explanation": "The lawyer honored his sworn contractual obligation by placing a check for the full million dollars in the coffin, unlike the priest and doctor who diverted the funds."
    },
    {
        "q": "In the coffin parable, why did the priest and doctor violate their deceased friend's explicit instructions?",
        "a": "They redirected funds to parish charity and medical operations",
        "distractors": [
            "They stole the funds for luxury cars",
            "They lost the envelopes in transit",
            "They burned the envelopes"
        ],
        "topic": "Consequentialist Divergence in Parable",
        "explanation": "The priest gave 75% to parish poor and the doctor gave 50% to save patients, acting as consequentialists while breaching their solemn duty."
    },
    {
        "q": "Under the separation of powers in the Philippine government, which branch has the primary constitutional duty to make, amend, and repeal laws?",
        "a": "Legislative Branch",
        "distractors": [
            "Executive Branch",
            "Judicial Branch",
            "Commission on Audit"
        ],
        "topic": "Three Branches of Government",
        "explanation": "The Legislative branch (Congress of the Philippines) holds the exclusive constitutional duty to craft, amend, and repeal laws."
    },
    {
        "q": "Which branch of the Philippine government bears the solemn constitutional duty to execute, implement, and enforce the laws enacted by Congress?",
        "a": "Executive Branch",
        "distractors": [
            "Legislative Branch",
            "Judicial Branch",
            "Constitutional Commission"
        ],
        "topic": "Executive Duty",
        "explanation": "The Executive branch, led by the President and administrative departments, is tasked with executing and administering the law."
    },
    {
        "q": "Which branch of the Philippine government is endowed with the sole constitutional power to interpret laws and adjudicate legal controversies?",
        "a": "Judicial Branch",
        "distractors": [
            "Executive Branch",
            "Legislative Branch",
            "Military Branch"
        ],
        "topic": "Judicial Power",
        "explanation": "The Judicial branch (Supreme Court and lower courts) possesses the exclusive constitutional power to interpret laws and settle legal disputes."
    },
    {
        "q": "Which article and section of the 1987 Philippine Constitution states that 'The State shall guarantee equal access to opportunities for public service and prohibit political dynasties as may be defined by law'?",
        "a": "Article II, Section 26",
        "distractors": [
            "Article III, Section 1",
            "Article VII, Section 10",
            "Article XII, Section 5"
        ],
        "topic": "Philippine Constitution Section 26",
        "explanation": "Article II (Declaration of Principles and State Policies), Section 26 of the 1987 Philippine Constitution mandates equal access to public service and the prohibition of political dynasties."
    },
    {
        "q": "Why is Congress's prolonged failure to pass an enabling anti-dynasty law considered an ethical failure of duty from a Kantian perspective?",
        "a": "It violates their sworn constitutional mandate",
        "distractors": [
            "It increases national tax revenues",
            "It eliminates political parties",
            "It enforces term limits automatically"
        ],
        "topic": "Kantian Failure in Governance",
        "explanation": "Under Kantianism, legislators have a categorical duty to enact laws mandated by the Constitution; evading the anti-dynasty law for self-preservation breaches duty."
    },
    {
        "q": "Between Ethics and Law, which possesses coercive enforcement power backed by state sanctions, police, and imprisonment?",
        "a": "The Law",
        "distractors": [
            "Ethics",
            "Moral Philosophy",
            "Conscience"
        ],
        "topic": "Ethics vs Law",
        "explanation": "Law is codified and enforceable by state sanctions, courts, and police power, whereas ethics operates through moral suasion, personal integrity, and societal conscience."
    },
    {
        "q": "A freshman college student from an affluent home with housemaids is required to practice the '5S' system of cleanliness at OLFU. Upholding cleanliness despite personal privilege aligns with adapting to institutional ____.",
        "a": "duty",
        "distractors": [
            "relativism",
            "egoism",
            "nepotism"
        ],
        "topic": "5S Cleanliness Dilemma",
        "explanation": "Implementing 5S cleanliness regardless of personal upbringing upholds communal standards and civic duty over individual privilege."
    },
    {
        "q": "A 10-year-old child who completes his school homework promptly solely because his mother promised he can watch television cartoons afterwards is motivated by ____.",
        "a": "self-interest",
        "distractors": [
            "pure reason",
            "deontological duty",
            "categorical imperative"
        ],
        "topic": "Homework Reward Dilemma",
        "explanation": "Performing a required task strictly for an external reward or entertainment embodies the incentive-driven calculation of Ethical Egoism."
    },
    {
        "q": "A child told to cook beef sinigang using their mother's cookbook recipe searches YouTube instead when the cookbook is missing. If the mother loves the dish anyway and the child honestly confesses, the positive reception reflects ____, while the honesty reflects moral character.",
        "a": "consequentialism",
        "distractors": [
            "cultural relativism",
            "divine command",
            "nihilism"
        ],
        "topic": "Sinigang Cooking Dilemma",
        "explanation": "Judging the dish as acceptable because it tasted great and satisfied dinner is consequentialist, though the child demonstrated integrity by telling the truth."
    },
    {
        "q": "A student who refrains from expressing a well-reasoned, divergent opinion on the K-to-12 educational program out of fear that the professor will give them a low grade is allowing self-preservation to compromise their ____.",
        "a": "integrity",
        "distractors": [
            "relativism",
            "curriculum",
            "syllabus"
        ],
        "topic": "Academic Freedom Dilemma",
        "explanation": "Suppressing honest intellectual truth due to fear of grading retaliation demonstrates egoistic self-preservation triumphing over academic integrity."
    },
    {
        "q": "Professor Ma'am Grace is known for kindness, but student Buchukoy never attends class and fails all requirements. If Ma'am Grace assigns Buchukoy a failing grade, her decision is justified under Kantianism because she has a duty to uphold ____ standards.",
        "a": "academic",
        "distractors": [
            "subjective",
            "relativist",
            "personal"
        ],
        "topic": "Grading Duty Dilemma",
        "explanation": "In Kantian deontology, educators possess a non-negotiable duty to evaluate students fairly and truthfully based on objective academic standards."
    }
]

SEPC_MODULE_2_ITEMS = [
    {
        "q": "A set of guidelines designed to set out acceptable behavior and ethical standards for members of a particular group, association, or profession is called a professional code of ____.",
        "a": "ethics",
        "distractors": [
            "algorithms",
            "by-laws",
            "regulations"
        ],
        "topic": "Professional Code Definition",
        "explanation": "A professional code of ethics sets out explicit standards of acceptable behavior, responsibility, and integrity for practitioners in a profession."
    },
    {
        "q": "Which of the following is recognized as one of the four foundational benefits of ethical guidelines for professionals?",
        "a": "Ethical Decision Making",
        "distractors": [
            "Guaranteed Profitability",
            "Exemption from Lawsuits",
            "Monopolistic Control"
        ],
        "topic": "Benefits of Ethical Guidelines",
        "explanation": "Ethical guidelines provide structured frameworks that assist practitioners in navigating complex moral dilemmas through ethical decision-making."
    },
    {
        "q": "Professional codes of ethics instill high standards of practice and ethical behavior, fostering trust and ____ from the general public.",
        "a": "respect",
        "distractors": [
            "fear",
            "indifference",
            "skepticism"
        ],
        "topic": "Public Trust and Respect",
        "explanation": "Adhering to strict professional codes establishes credibility, earning the enduring trust and respect of clients and the general public."
    },
    {
        "q": "A professional code of ethics serves as an evaluation ____ against which the competence, conduct, and accountability of a practitioner can be measured.",
        "a": "benchmark",
        "distractors": [
            "obstacle",
            "monopoly",
            "arbitrage"
        ],
        "topic": "Evaluation Benchmark",
        "explanation": "Codes of ethics provide an objective evaluation benchmark for auditing professional performance and disciplining malpractice."
    },
    {
        "q": "According to Tenet 1 of the Code of Ethics of the Filipino IT Professionals, members pledge to promote public knowledge, understanding, and ____ of Information Technology.",
        "a": "appreciation",
        "distractors": [
            "taxation",
            "monopolization",
            "regulation"
        ],
        "topic": "Filipino IT Code - Tenet 1",
        "explanation": "Tenet 1: 'I will promote public knowledge, understanding and appreciation of I.T.'"
    },
    {
        "q": "According to Tenet 2 of the Filipino IT Code, what must an IT professional always consider in the performance of their professional work?",
        "a": "General welfare and public good",
        "distractors": [
            "Corporate revenue and profit",
            "Personal prestige and fame",
            "Political party interests"
        ],
        "topic": "Filipino IT Code - Tenet 2",
        "explanation": "Tenet 2: 'I will consider the general welfare and public welfare and public good in the performance of my work.'"
    },
    {
        "q": "Tenet 3 of the Filipino IT Code states that professionals must advertise goods or professional services in a clear and ____ manner.",
        "a": "truthful",
        "distractors": [
            "aggressive",
            "secretive",
            "lucrative"
        ],
        "topic": "Filipino IT Code - Tenet 3",
        "explanation": "Tenet 3: 'I will advertise goods or professional services in a clear and truthful manner.'"
    },
    {
        "q": "Tenet 4 of the Filipino IT Code mandates strict compliance and adherence to intellectual property laws, ____ laws, and other related technology statutes.",
        "a": "patent",
        "distractors": [
            "maritime",
            "corporate tax",
            "zoning"
        ],
        "topic": "Filipino IT Code - Tenet 4",
        "explanation": "Tenet 4: 'I will comply and strictly abide by the intellectual property laws, patent laws and other related laws in respect of I.T.'"
    },
    {
        "q": "Under Tenet 5 of the Filipino IT Code, practitioners must accept full responsibility for work undertaken and utilize their skills with competence and ____.",
        "a": "professionalism",
        "distractors": [
            "haste",
            "frugality",
            "leverage"
        ],
        "topic": "Filipino IT Code - Tenet 5",
        "explanation": "Tenet 5: 'I will accept the full responsibility for the work undertaken and utilize my skills with competence and professionalism.'"
    },
    {
        "q": "Tenet 6 of the Filipino IT Code obligates professionals to make truthful statements regarding what aspect of their qualifications and offerings?",
        "a": "Areas of competence and product qualities",
        "distractors": [
            "Personal political affiliations",
            "Competitors' vulnerabilities",
            "Stock market projections"
        ],
        "topic": "Filipino IT Code - Tenet 6",
        "explanation": "Tenet 6: 'I will make truthful statements on my areas of competence as well as the capabilities and qualities of my product and services.'"
    },
    {
        "q": "Under Tenet 7 of the Filipino IT Code, an IT professional must never disclose or use confidential information obtained during duty without consent, except when required by ____.",
        "a": "the law",
        "distractors": [
            "their employer",
            "their family",
            "a journalist"
        ],
        "topic": "Filipino IT Code - Tenet 7",
        "explanation": "Tenet 7: 'I will not disclose or use any confidential information obtained in course of professional duties without the consent of the parties concerned except when required by the laws.'"
    },
    {
        "q": "Tenet 8 of the Filipino IT Code requires members to strive to attain the highest ____ in both the products and services that they offer.",
        "a": "quality",
        "distractors": [
            "price",
            "speed",
            "market share"
        ],
        "topic": "Filipino IT Code - Tenet 8",
        "explanation": "Tenet 8: 'I will strive to attain the highest quality in both the products and services that offer.'"
    },
    {
        "q": "Tenet 9 of the Filipino IT Code emphasizes active industry advancement by pledging to knowingly participate in the ____ of Information Technology.",
        "a": "development",
        "distractors": [
            "commercialization",
            "monopolization",
            "obfuscation"
        ],
        "topic": "Filipino IT Code - Tenet 9",
        "explanation": "Tenet 9: 'I will knowingly participate in the development of the Information Technology.'"
    },
    {
        "q": "Tenet 10 of the Filipino IT Code requires practitioners to uphold and enhance standards through continuing professional ____ to elevate the profession.",
        "a": "education",
        "distractors": [
            "licensing fees",
            "political lobbying",
            "marketing"
        ],
        "topic": "Filipino IT Code - Tenet 10",
        "explanation": "Tenet 10 mandates continuous learning to uphold and improve professional standards across the computing industry."
    },
    {
        "q": "What does the professional acronym AITP stand for in computing ethics?",
        "a": "Association of Information Technology Professionals",
        "distractors": [
            "American Institute of Technology Programmers",
            "Association of Internet Technology Pioneers",
            "Alliance of Information Technology Producers"
        ],
        "topic": "AITP Acronym",
        "explanation": "AITP stands for the Association of Information Technology Professionals, a key organization defining computing ethical standards."
    },
    {
        "q": "How many key institutional obligations does a member solemnly accept in the AITP Code of Ethics?",
        "a": "Six obligations",
        "distractors": [
            "Ten obligations",
            "Four obligations",
            "Eight obligations"
        ],
        "topic": "AITP Obligations Count",
        "explanation": "The AITP Code specifies 6 primary obligations: to management, fellow members, society, university/college, employer, and country."
    },
    {
        "q": "Which of the following is an explicit obligation declared in the AITP Code of Ethics acknowledging institutional academic roots?",
        "a": "Obligation to my College or University",
        "distractors": [
            "Obligation to my Software Vendor",
            "Obligation to my Cloud Provider",
            "Obligation to my Social Network"
        ],
        "topic": "AITP Academic Obligation",
        "explanation": "The AITP Code explicitly highlights 'an obligation to my College or University' to honor academic foundations and mentor future professionals."
    },
    {
        "q": "In the AITP Code of Ethics, members explicitly acknowledge holding a fiduciary trust toward whom?",
        "a": "Employer",
        "distractors": [
            "Shareholder",
            "Banker",
            "Subcontractor"
        ],
        "topic": "AITP Employer Trust",
        "explanation": "AITP members pledge: 'That I have an obligation to my employer whose trust I hold.'"
    },
    {
        "q": "According to the ACM/IEEE Software Engineering Code of Ethics, how many core principles govern professional practice?",
        "a": "Eight Principles",
        "distractors": [
            "Ten Principles",
            "Five Principles",
            "Twelve Principles"
        ],
        "topic": "ACM Principles Count",
        "explanation": "The ACM/IEEE Software Engineering Code of Ethics contains 8 core principles: Public, Client & Employer, Product, Judgement, Management, Profession, Colleagues, Self."
    },
    {
        "q": "Which ACM Principle states that software engineers shall act consistently with the public interest as their paramount obligation?",
        "a": "Principle 1: Public",
        "distractors": [
            "Principle 2: Client and Employer",
            "Principle 5: Management",
            "Principle 8: Self"
        ],
        "topic": "ACM Principle 1",
        "explanation": "Principle 1 (Public) mandates that software engineers shall act consistently with the safety, health, and welfare of the public."
    },
    {
        "q": "Which ACM Principle requires that software engineers ensure their software products and modifications meet the highest professional standards possible?",
        "a": "Principle 3: Product",
        "distractors": [
            "Principle 4: Judgement",
            "Principle 6: Profession",
            "Principle 7: Colleagues"
        ],
        "topic": "ACM Principle 3",
        "explanation": "Principle 3 (Product) requires software engineers to strive for high quality, acceptable costs, and rigorous testing."
    },
    {
        "q": "Which ACM Principle dictates that software engineers maintain integrity and independence in their professional evaluations?",
        "a": "Principle 4: Judgement",
        "distractors": [
            "Principle 1: Public",
            "Principle 5: Management",
            "Principle 8: Self"
        ],
        "topic": "ACM Principle 4",
        "explanation": "Principle 4 (Judgement) requires software engineers to maintain integrity and objectivity, refusing to endorse compromised technical assessments."
    },
    {
        "q": "Which ACM Principle obligates practitioners to participate in lifelong learning to enhance their professional capabilities?",
        "a": "Principle 8: Self",
        "distractors": [
            "Principle 2: Client and Employer",
            "Principle 6: Profession",
            "Principle 7: Colleagues"
        ],
        "topic": "ACM Principle 8",
        "explanation": "Principle 8 (Self) states that software engineers shall participate in lifelong professional education to keep pace with technological advancement."
    },
    {
        "q": "Which organization formulated the globally recognized 'Ten Commandments of Computer Ethics'?",
        "a": "Computer Ethics Institute",
        "distractors": [
            "Association for Computing Machinery",
            "IEEE Computer Society",
            "Federal Bureau of Investigation"
        ],
        "topic": "CEI Ten Commandments",
        "explanation": "The Ten Commandments of Computer Ethics were created in 1992 by the Computer Ethics Institute (CEI) to govern responsible computer usage."
    },
    {
        "q": "What is the 1st Commandment of Computer Ethics?",
        "a": "Thou shalt not use a computer to harm other people",
        "distractors": [
            "Thou shalt not use a computer to steal",
            "Thou shalt not snoop around in other people's files",
            "Thou shalt not copy proprietary software"
        ],
        "topic": "Commandment 1",
        "explanation": "Commandment 1: 'Thou shalt not use a computer to harm other people', prohibiting harassment, physical injury, and cyber attacks."
    },
    {
        "q": "Commandment 2 states that computer users must not interfere with other people's computer ____.",
        "a": "work",
        "distractors": [
            "finances",
            "hardware",
            "entertainment"
        ],
        "topic": "Commandment 2",
        "explanation": "Commandment 2: 'Thou shalt not interfere with other people's computer work', barring denial-of-service attacks, malware, and disruptive tactics."
    },
    {
        "q": "Commandment 3 explicitly forbids users from snooping around in other people's computer ____.",
        "a": "files",
        "distractors": [
            "monitors",
            "desks",
            "cables"
        ],
        "topic": "Commandment 3",
        "explanation": "Commandment 3: 'Thou shalt not snoop around in other people's computer files', protecting digital privacy and data confidentiality."
    },
    {
        "q": "Which Commandment prohibits the use of computer technologies to commit theft of money, data, or electronic assets?",
        "a": "Commandment 4: Thou shalt not use a computer to steal",
        "distractors": [
            "Commandment 2",
            "Commandment 7",
            "Commandment 9"
        ],
        "topic": "Commandment 4",
        "explanation": "Commandment 4: 'Thou shalt not use a computer to steal', prohibiting financial fraud, unauthorized data harvesting, and cyber robbery."
    },
    {
        "q": "Commandment 5 ('Thou shalt not use a computer to bear false witness') directly outlaws which modern digital misconduct?",
        "a": "Spreading online disinformation, defamation, and fake news",
        "distractors": [
            "Writing optimized search algorithms",
            "Hosting web servers",
            "Running peer-to-peer torrents"
        ],
        "topic": "Commandment 5",
        "explanation": "Commandment 5 prohibits online slander, perjury, forged documentation, and spreading malicious disinformation."
    },
    {
        "q": "Which Commandment prohibits software piracy and the illegal downloading or copying of proprietary software without paying licensing fees?",
        "a": "Commandment 6",
        "distractors": [
            "Commandment 1",
            "Commandment 3",
            "Commandment 8"
        ],
        "topic": "Commandment 6",
        "explanation": "Commandment 6: 'Thou shalt not copy or use proprietary software for which you have not paid.'"
    },
    {
        "q": "Commandment 7 prohibits using other people's computer resources without authorization or proper ____.",
        "a": "compensation",
        "distractors": [
            "invitation",
            "applause",
            "encryption"
        ],
        "topic": "Commandment 7",
        "explanation": "Commandment 7: 'Thou shalt not use other people's computer resources without authorization or proper compensation.'"
    },
    {
        "q": "Commandment 8 specifically forbids appropriating other people's intellectual output, which is known academically as ____.",
        "a": "plagiarism",
        "distractors": [
            "phishing",
            "cryptomining",
            "debugging"
        ],
        "topic": "Commandment 8",
        "explanation": "Commandment 8 protects intellectual property, forbidding users from claiming another person's code, design, or research as their own."
    },
    {
        "q": "Commandment 9 directs developers to think about the social ____ of the program they are writing or system they are designing.",
        "a": "consequences",
        "distractors": [
            "revenues",
            "syntax",
            "compilation speeds"
        ],
        "topic": "Commandment 9",
        "explanation": "Commandment 9: 'Thou shalt think about the social consequences of the program you are writing or the system you are designing.'"
    },
    {
        "q": "What does the 10th Commandment of Computer Ethics exhort all computer users to always insure when using technology?",
        "a": "Consideration and respect for your fellow humans",
        "distractors": [
            "Maximum computation bandwidth",
            "Flawless battery endurance",
            "Highest social media follower count"
        ],
        "topic": "Commandment 10",
        "explanation": "Commandment 10: 'Thou shalt always use a computer in ways that insure consideration and respect for your fellow humans.'"
    },
    {
        "q": "The declaration known as the Hacking Community's Constitution serves as a digital bill of rights that hackers argue should be interpreted in relation to what other ethical document?",
        "a": "The Ten Commandments of Computer Ethics",
        "distractors": [
            "The Magna Carta",
            "The US Copyright Act",
            "The Berne Convention"
        ],
        "topic": "Hacker Constitution Relationship",
        "explanation": "The Hacking Community's Constitution declares 14 principles akin to a cyber bill of rights, intended to be read alongside the Ten Commandments."
    },
    {
        "q": "According to the Hacking Constitution, hacking is legitimately viewed as a tool to test the ____ of networks that safeguard valuable information.",
        "a": "integrity",
        "distractors": [
            "monetization",
            "bandwidth",
            "physical wiring"
        ],
        "topic": "Hacker Tool for Network Integrity",
        "explanation": "Hackers view ethical hacking as an essential diagnostic tool to stress-test network integrity and uncover critical vulnerabilities before adversaries do."
    },
    {
        "q": "Which movement does the Hacking Community's Constitution passionately support, advocating that governments avoid closed proprietary software?",
        "a": "Open Source Movement",
        "distractors": [
            "Proprietary Licensing Guild",
            "Closed Cloud Initiative",
            "Digital Rights Management Alliance"
        ],
        "topic": "Hacker Open Source Stance",
        "explanation": "The constitution strongly supports open-source software, arguing that government reliance on proprietary software stifles public innovation."
    },
    {
        "q": "The Hacking Community's Constitution declares that three instruments\u2014hacking, cracking, and ____\u2014can be leveraged to promote direct democracy and free information.",
        "a": "phreaking",
        "distractors": [
            "spamming",
            "spearphishing",
            "ransomware"
        ],
        "topic": "Hacking Instruments",
        "explanation": "The constitution cites hacking, cracking, and phreaking (telecom exploration) as tools for exploring systems and democratizing information."
    },
    {
        "q": "Which philosopher wrote the seminal 1985 paper 'What Is Computer Ethics?', establishing computer ethics as a distinct field of applied ethics?",
        "a": "James H. Moor",
        "distractors": [
            "Norbert Wiener",
            "Deborah Johnson",
            "Luciano Floridi"
        ],
        "topic": "James Moor (1985)",
        "explanation": "James H. Moor pioneered foundational computer ethics in 1985, analyzing policy vacuums and the unique nature of computing technology."
    },
    {
        "q": "James Moor argued that computer ethics problems typically arise because computers create a '____ vacuum' regarding how technology should be used.",
        "a": "policy",
        "distractors": [
            "silicon",
            "hardware",
            "financial"
        ],
        "topic": "Policy Vacuum",
        "explanation": "A 'policy vacuum' occurs when novel computer capabilities arise before society, laws, or institutions have established rules to govern their use."
    },
    {
        "q": "Which unique property of computers describes their capability to be shaped and molded to perform any activity characterized by inputs, outputs, and logical operations?",
        "a": "Logical Malleability",
        "distractors": [
            "Invisibility Factor",
            "Analog Continuity",
            "Silicon Rigidity"
        ],
        "topic": "Logical Malleability",
        "explanation": "Logical malleability is the computer's universal capacity to execute any computable process that can be formulated in logic."
    },
    {
        "q": "According to James Moor, which property of computers refers to the fact that most internal operational processes take place completely out of human sight?",
        "a": "Invisibility Factor",
        "distractors": [
            "Logical Malleability",
            "Impact on Society",
            "Physical Obfuscation"
        ],
        "topic": "Invisibility Factor",
        "explanation": "The Invisibility Factor emphasizes that internal micro-operations, algorithmic decisions, and data transactions are invisible to human perception."
    },
    {
        "q": "Which dimension of Moor's Invisibility Factor describes the covert, unauthorized, and undetectable misuse of computing power (such as digital embezzlement or espionage)?",
        "a": "Invisible Abuse",
        "distractors": [
            "Invisible Programming Values",
            "Invisible Complex Calculations",
            "Logical Malleability"
        ],
        "topic": "Invisible Abuse",
        "explanation": "Invisible abuse occurs when a programmer or user exploits the hidden nature of digital systems to execute unauthorized or criminal operations unnoticed."
    },
    {
        "q": "When a programmer intentionally or subconsciously embeds personal biases, moral judgments, or unfair algorithmic assumptions into software code, it illustrates ____.",
        "a": "Invisible Programming Values",
        "distractors": [
            "Invisible Abuse",
            "Invisible Complex Calculations",
            "Logical Malleability"
        ],
        "topic": "Invisible Programming Values",
        "explanation": "Invisible programming values are the hidden philosophical, ethical, or discriminatory assumptions silently encoded into algorithms by developers."
    },
    {
        "q": "Complex financial automated trading or spacecraft telemetry calculations that exceed human capacity to inspect or audit by hand exemplify which aspect of the Invisibility Factor?",
        "a": "Invisible Complex Calculations",
        "distractors": [
            "Invisible Abuse",
            "Invisible Programming Values",
            "Open Source Logic"
        ],
        "topic": "Invisible Complex Calculations",
        "explanation": "Invisible complex calculations involve software processing so vast and intricate that human operators must blindly trust the machine's conclusions."
    },
    {
        "q": "Which level of computer ethics consists of sensationalized reporting, public curiosity, and news coverage in magazines, newspapers, and television programs?",
        "a": "POP Computer Ethics",
        "distractors": [
            "PARA Computer Ethics",
            "THEORETICAL Computer Ethics",
            "Meta-Ethics"
        ],
        "topic": "POP Computer Ethics",
        "explanation": "Pop computer ethics encompasses mainstream media discussions, sensational viral news, and popular public discourse on cyber issues."
    },
    {
        "q": "Which level of computer ethics is practiced by people who take a dedicated interest in cyber cases, collect examples, analyze similarities, and attend professional conferences?",
        "a": "PARA Computer Ethics",
        "distractors": [
            "POP Computer Ethics",
            "THEORETICAL Computer Ethics",
            "Normative Ethics"
        ],
        "topic": "PARA Computer Ethics",
        "explanation": "Para computer ethics is practiced by dedicated enthusiasts and professionals who systematically collect and analyze computing cases."
    },
    {
        "q": "Which level of computer ethics applies rigorous, scholarly philosophical frameworks (such as Kantianism and Utilitarianism) to technological dilemmas?",
        "a": "THEORETICAL Computer Ethics",
        "distractors": [
            "POP Computer Ethics",
            "PARA Computer Ethics",
            "Colloquial Ethics"
        ],
        "topic": "THEORETICAL Computer Ethics",
        "explanation": "Theoretical computer ethics is the academic discipline that integrates classical normative philosophy with computing dilemmas."
    },
    {
        "q": "Due to exceptionally high internet usage, mobile messaging volume, and viral social engagement, the Philippines has earned what global title?",
        "a": "Social Media Capital of the World",
        "distractors": [
            "Silicon Valley of Asia",
            "E-Commerce Capital of the World",
            "Hardware Manufacturing Hub"
        ],
        "topic": "Philippine Social Media Capital",
        "explanation": "The Philippines is recognized globally as the 'Social Media Capital of the World' due to its unprecedented per-capita social media engagement."
    },
    {
        "q": "In digital social networking etiquette, if a friend willingly poses and smiles with you in a joint group photo or selfie, do you legally and ethically need to ask separate written permission before posting it?",
        "a": "Not anymore, because consent is implied",
        "distractors": [
            "Yes, notarized consent is mandatory",
            "Yes, copyright fees must be paid",
            "No, because photos have no rights"
        ],
        "topic": "Photo Consent Rules",
        "explanation": "Voluntarily participating in a mutual group photo or selfie carries implied consent to share, provided it is not maliciously altered or defamatory."
    },
    {
        "q": "Secretly recording or photographing a private individual in a private setting without their knowledge or consent and uploading it to social media is generally ____.",
        "a": "unethical and improper",
        "distractors": [
            "acceptable under Fair Use",
            "mandated by the Cybercrime Act",
            "fully legal without exception"
        ],
        "topic": "Unauthorized Recording",
        "explanation": "Capturing and broadcasting photos/videos of private individuals without consent violates privacy and ethical norms unless specific legal exemptions apply."
    },
    {
        "q": "Which legal exemption permits the unauthorized publication of photos or videos if the material captures breaking news of the day and press information (e.g., a rescue operation on EDSA)?",
        "a": "Exemption No. 1: News of the day and items of press information",
        "distractors": [
            "Exemption for Celebrity Monetization",
            "Exemption for Clickbait Marketing",
            "Exemption for Private Commercial Gain"
        ],
        "topic": "Exemption 1 - Press Information",
        "explanation": "Exemption 1 permits broadcasting recordings that constitute legitimate news of the day and press information in the public interest."
    },
    {
        "q": "If a citizen captures a video of an abusive traffic enforcer illegally extorting and threatening a delivery truck driver, publishing it is ethically and legally justified under which exemption?",
        "a": "Exemption No. 2: Done for the general welfare and public good",
        "distractors": [
            "Exemption for Entertainment Comedy",
            "Exemption for Personal Revenge",
            "Exemption for Commercial Slander"
        ],
        "topic": "Exemption 2 - General Welfare",
        "explanation": "Exemption 2 justifies publishing unauthorized recordings when exposing abuse or corruption to protect the general welfare and public interest."
    },
    {
        "q": "Photographing or filming the popular Filipino pop group BINI while they are performing or walking in a public shopping mall is legally permissible under which exemption?",
        "a": "Exemption No. 3: Public personalities in a public setting",
        "distractors": [
            "Exemption for Private Surveillance",
            "Exemption for Secret Intellectual Theft",
            "Exemption for Corporate Monopolies"
        ],
        "topic": "Exemption 3 - Public Personalities",
        "explanation": "Exemption 3 recognizes that public figures and celebrities appearing in public venues possess reduced expectations of privacy regarding public photography."
    },
    {
        "q": "Which comprehensive textbook serves as the foundational academic reference for SEPC311 at OLFU, written by Dr. Charlemagne Lavi\u00f1a?",
        "a": "Social, Ethical, Legal and Professional Issues in Computing",
        "distractors": [
            "Computer Networks and Topologies",
            "Automata and Formal Computation",
            "Modern Software Architecture"
        ],
        "topic": "Course Textbook Reference",
        "explanation": "The core textbook referenced throughout the course is 'Social, Ethical, Legal and Professional Issues in Computing' by Dr. Charlemagne Lavi\u00f1a."
    }
]
