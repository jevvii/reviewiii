<div align="center">

```
  ██████╗ ███████╗██╗   ██╗██╗███████╗██╗    ██╗██╗██╗██╗
  ██╔══██╗██╔════╝██║   ██║██║██╔════╝██║    ██║██║██║██║
  ██████╔╝█████╗  ██║   ██║██║█████╗  ██║ █╗ ██║██║██║██║
  ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║██║██║██║
  ██║  ██║███████╗ ╚████╔╝ ██║███████╗╚███╔███╔╝██║██║██║
  ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝╚═╝
```

### **Hyper-Modern Computer Science Reviewer & Academic Study Portal**
*Year III — 1st Semester Comprehensive Exam Reviewer, Interactive Quiz Engine & Pomodoro Workstation*

[![Astro](https://img.shields.io/badge/Astro-5.0-BC52EE?style=for-the-badge&logo=astro&logoColor=white)](https://astro.build/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Bun](https://img.shields.io/badge/Bun-1.1-FBF0DF?style=for-the-badge&logo=bun&logoColor=black)](https://bun.sh/)
[![OLED Black](https://img.shields.io/badge/Theme-OLED%20Pitch%20Black-000000?style=for-the-badge&logo=target&logoColor=8a9a86)](#-design-system--oled-aesthetic)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-2ea44f?style=for-the-badge&logo=github&logoColor=white)](https://jevvii.github.io/reviewiii/)
[![Questions](https://img.shields.io/badge/Questions-830%20Curated-8a9a86?style=for-the-badge)](#-curriculum-matrix--questionnaires)
[![Offline Vault](https://img.shields.io/badge/Offline%20Vault-48%20Files-a89f91?style=for-the-badge)](#-consolidated-offline-download-vault)
[![GitHub Auth](https://img.shields.io/badge/Auth-Multi--User%20GitHub-2ea44f?style=for-the-badge&logo=github&logoColor=white)](#-multi-user-github-authentication--isolated-sessions)

---

[🌐 **Explore Live Production Portal**](https://jevvii.github.io/reviewiii/) &bull;
[⏱️ **Pomodoro Workstation**](https://jevvii.github.io/reviewiii/#focus-timer) &bull;
[📥 **Download Vault**](https://jevvii.github.io/reviewiii/#downloads) &bull;
[📖 **Course Directory**](#-curriculum-matrix--questionnaires)

---

</div>

## ✦ Overview

**ReviewIII** is an ultra-fast, static academic study hub and interactive quiz workstation developed for 3rd-year Computer Science students. Engineered with an **OLED pitch-black Digital Sobriety aesthetic**, it unifies rigorous lecture extractions, Google NotebookLM quiz players, an automated Pomodoro focus logger, multi-user GitHub session management, and a comprehensive 48-file offline document vault into a seamless, distraction-free environment.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          REVIEWIII ACADEMIC HUB                             │
├───────────────────────┬─────────────────────────────┬───────────────────────┤
│  ⚡ INTERACTIVE QUIZ   │  ⏱️ POMODORO WORKSTATION    │  📥 OFFLINE VAULT     │
│  • 12 Standalone Apps │  • 25/5/15 Interval Loops   │  • 48 Total Files     │
│  • 830 Total Items    │  • Multi-User GitHub Auth   │  • PDF Questionnaires │
│  • 48px Mobile Header │  • Isolated Sessions        │  • Word DOCX Files    │
│  • Hamburger Drawer   │  • Multi-Tab BroadcastSync  │  • JSON Datasets      │
│  • Zero-Letter Dupes  │  • Web Audio Chimes         │  • Markdown Keys      │
└───────────────────────┴─────────────────────────────┴───────────────────────┘
```

---

## ⚡ Core Features

### 1. 🐙 Multi-User GitHub Authentication & Isolated Sessions
- **Zero-Friction GitHub Login**: Connect instantly via your GitHub username using public API profile synchronization (fetches verified avatar, bio, and repo stats) or optionally enter a GitHub Personal Access Token (PAT).
- **Multi-Account Switcher**: Connect multiple student accounts on a shared device. Seamlessly switch between accounts or revert to anonymous Guest Mode at any time directly from the glassmorphic header pill.
- **Isolated User Sessions**: Quiz progress, saved answers, timer state, target subject, and Asia/Manila study logs are completely partitioned into isolated storage namespaces (`reviewiii_u_{userId}_...`).
- **Reactive Cross-Tab Sync**: Uses `BroadcastChannel('reviewiii_auth_channel')` and custom events to instantly propagate account switches and session states across all open tabs and active quiz players.

### 2. 🎯 Interactive NotebookLM Quiz Players
- **12 Standalone Interactive Engines**: Dedicated offline-first quiz players for each module with progress saving, instant answer feedback, hints, and randomized choices.
- **Zero-Letter Duplication**: Strict regex sanitization prevents ugly multiple-choice artifacts (e.g. `A. A.) Answer` &rarr; `A. Answer`).
- **Compact Mobile UI Header (48px)**: Fixed-height navigation bar locked to `48px` with backdrop blur (`rgba(0, 0, 0, 0.94)`). Questions and choices start directly below the header on small devices, keeping answer cards above the fold.
- **Slide-Down Mobile Drawer**: Tapping `☰` displays a sleek slide-down drawer showing full course navigation, module switchers with active indicators (`● Current`), and download shortcuts.

### 3. ⏱️ Integrated Pomodoro Focus & Time Tracking
- **Automated Subject Attribution**: Tracks study sessions directly to specific course codes and modules (e.g. `NETC311 • Module 3: Protocols and Models`).
- **Auto-Redirect on Start**: Selecting a specific quiz module and starting the timer automatically redirects the browser directly to the quiz player and begins ticking immediately.
- **Cross-Tab Synchronization**: Uses `BroadcastChannel('reviewiii_focus_channel')` and `localStorage` to keep timer countdowns in sync across multiple browser tabs.
- **Zero-Asset Web Audio Synthesizer**: Produces harmonious sine-wave chimes for focus starts, break transitions, and set completions without external MP3 dependencies.
- **Daily Analytics**: Real-time breakdown chips, session history feed, and quick manual time logger.

### 4. 📥 48-File Consolidated Download Vault
- **100% Offline Parity**: Every module provides 4 file formats:
  - 📄 **Printable PDF**: High-contrast, beautifully formatted for tablet annotations and printouts.
  - 📝 **Word DOCX**: Fully editable questionnaires with formatted tables and answer keys.
  - 📊 **JSON Dataset**: Structured arrays of questions, choices, answers, and explanations.
  - 📑 **Markdown (.md)**: Plaintext documentation optimized for LLMs and Obsidian vaults.

### 5. 🔍 Instant Search & Filter Toolbar
- Real-time client-side search across subject titles, course codes, module names, and core topic tags.
- Quick keyboard shortcut: Press <kbd>/</kbd> anywhere to focus search; press <kbd>Esc</kbd> to clear.

---

## 📚 Curriculum Matrix & Questionnaires

ReviewIII features **830 rigorously verified multiple-choice & identification items** across active core subjects:

| Course | Title | Modules | Items | Interactive Quiz | Printable PDF | Word DOCX | Dataset |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **NETC311** | Networking Technologies (CCNA ITN) | 3 | **298** | [Module 1](https://jevvii.github.io/reviewiii/quizzes/netc311/module1.html) &bull; [Module 2](https://jevvii.github.io/reviewiii/quizzes/netc311/module2.html) &bull; [Module 3](https://jevvii.github.io/reviewiii/quizzes/netc311/module3.html) | [M1](https://jevvii.github.io/reviewiii/downloads/netc311/Module%201%20-%20Networking%20Today%20-%20Questionnaire.pdf) &bull; [M2](https://jevvii.github.io/reviewiii/downloads/netc311/Module%202%20-%20Basic%20Switch%20and%20End%20Device%20Configuration%20-%20Questionnaire.pdf) &bull; [M3](https://jevvii.github.io/reviewiii/downloads/netc311/Module%203%20-%20Protocols%20and%20Models%20-%20Questionnaire.pdf) | [M1](https://jevvii.github.io/reviewiii/downloads/netc311/Module%201%20-%20Networking%20Today%20-%20Questionnaire.docx) &bull; [M2](https://jevvii.github.io/reviewiii/downloads/netc311/Module%202%20-%20Basic%20Switch%20and%20End%20Device%20Configuration%20-%20Questionnaire.docx) &bull; [M3](https://jevvii.github.io/reviewiii/downloads/netc311/Module%203%20-%20Protocols%20and%20Models%20-%20Questionnaire.docx) | [JSON](https://jevvii.github.io/reviewiii/downloads/netc311/Module_1_NotebookLM_Quiz.json) &bull; [MD](https://jevvii.github.io/reviewiii/downloads/netc311/Module_1_NotebookLM_Quiz.md) |
| **HMBY311** | Human Biology | 3 | **252** | [Module 1](https://jevvii.github.io/reviewiii/quizzes/hmby311/module1.html) &bull; [Module 4](https://jevvii.github.io/reviewiii/quizzes/hmby311/module4.html) &bull; [Module 5](https://jevvii.github.io/reviewiii/quizzes/hmby311/module5.html) | [M1](https://jevvii.github.io/reviewiii/downloads/hmby311/Module%201%20-%20Human%20Biology%20-%20Scientific%20Method%20and%20Basic%20Chemistry.pdf) &bull; [M4](https://jevvii.github.io/reviewiii/downloads/hmby311/Module%204%20-%20Human%20Biology%20-%20Chromosomes%20and%20Cell%20Division.pdf) &bull; [M5](https://jevvii.github.io/reviewiii/downloads/hmby311/Module%205%20-%20Human%20Biology%20-%20Genetics%20Human%20Inheritance%20and%20Cancer.pdf) | [M1](https://jevvii.github.io/reviewiii/downloads/hmby311/Module%201%20-%20Human%20Biology%20-%20Scientific%20Method%20and%20Basic%20Chemistry.docx) &bull; [M4](https://jevvii.github.io/reviewiii/downloads/hmby311/Module%204%20-%20Human%20Biology%20-%20Chromosomes%20and%20Cell%20Division.docx) &bull; [M5](https://jevvii.github.io/reviewiii/downloads/hmby311/Module%205%20-%20Human%20Biology%20-%20Genetics%20Human%20Inheritance%20and%20Cancer.docx) | [JSON](https://jevvii.github.io/reviewiii/downloads/hmby311/HMBY311_Module_1_Quiz.json) &bull; [MD](https://jevvii.github.io/reviewiii/downloads/hmby311/HMBY311_Module_1_Quiz.md) |
| **ATFL311** | Automata Theory & Formal Languages | 4 | **174** | [Module 1](https://jevvii.github.io/reviewiii/quizzes/atfl311/module1.html) &bull; [Module 2](https://jevvii.github.io/reviewiii/quizzes/atfl311/module2.html) &bull; [Module 3](https://jevvii.github.io/reviewiii/quizzes/atfl311/module3.html) &bull; [Module 4](https://jevvii.github.io/reviewiii/quizzes/atfl311/module4.html) | [M1](https://jevvii.github.io/reviewiii/downloads/atfl311/Module%201%20-%20Introduction%20to%20Automata%20Theory%20-%20Questionnaire.pdf) &bull; [M2](https://jevvii.github.io/reviewiii/downloads/atfl311/Module%202%20-%20Finite%20State%20Machines%20and%20Prerequisites%20-%20Questionnaire.pdf) &bull; [M3](https://jevvii.github.io/reviewiii/downloads/atfl311/Module%203%20-%20Deterministic%20Finite%20Automata%20-%20Questionnaire.pdf) &bull; [M4](https://jevvii.github.io/reviewiii/downloads/atfl311/Module%204%20-%20Non-Deterministic%20Finite%20Automata%20-%20Questionnaire.pdf) | [M1](https://jevvii.github.io/reviewiii/downloads/atfl311/Module%201%20-%20Introduction%20to%20Automata%20Theory%20-%20Questionnaire.docx) &bull; [M2](https://jevvii.github.io/reviewiii/downloads/atfl311/Module%202%20-%20Finite%20State%20Machines%20and%20Prerequisites%20-%20Questionnaire.docx) &bull; [M3](https://jevvii.github.io/reviewiii/downloads/atfl311/Module%203%20-%20Deterministic%20Finite%20Automata%20-%20Questionnaire.docx) &bull; [M4](https://jevvii.github.io/reviewiii/downloads/atfl311/Module%204%20-%20Non-Deterministic%20Finite%20Automata%20-%20Questionnaire.docx) | [JSON](https://jevvii.github.io/reviewiii/downloads/atfl311/ATFL311_Module_1_Quiz.json) &bull; [MD](https://jevvii.github.io/reviewiii/downloads/atfl311/ATFL311_Module_1_Quiz.md) |
| **SEPC311** | Social & Ethical Issues in Computing | 2 | **106** | [Module 1](https://jevvii.github.io/reviewiii/quizzes/sepc311/module1.html) &bull; [Module 2](https://jevvii.github.io/reviewiii/quizzes/sepc311/module2.html) | [M1](https://jevvii.github.io/reviewiii/downloads/sepc311/Module%201%20-%20Common%20Ethical%20Theories%20-%20Questionnaire.pdf) &bull; [M2](https://jevvii.github.io/reviewiii/downloads/sepc311/Module%202%20-%20Computer%20Ethics%20and%20Professional%20Codes%20-%20Questionnaire.pdf) | [M1](https://jevvii.github.io/reviewiii/downloads/sepc311/Module%201%20-%20Common%20Ethical%20Theories%20-%20Questionnaire.docx) &bull; [M2](https://jevvii.github.io/reviewiii/downloads/sepc311/Module%202%20-%20Computer%20Ethics%20and%20Professional%20Codes%20-%20Questionnaire.docx) | [JSON](https://jevvii.github.io/reviewiii/downloads/sepc311/SEPC311_Module_1_Quiz.json) &bull; [MD](https://jevvii.github.io/reviewiii/downloads/sepc311/SEPC311_Module_1_Quiz.md) |
| **TOTALS** | *4 Core Academic Courses* | **12** | **830** | *12 Interactive Players* | *12 Formatted PDFs* | *12 Editable DOCXs* | *24 Datasets* |

### Detailed Course Modules

<details>
<summary><b>NETC311: Networking Technologies (Cisco CCNA v7.0 ITN)</b> — 298 Items</summary>

- **Module 1 — Networking Today (99 Items)**: Host roles (clients, servers, peers), peer-to-peer architectures, intermediary devices, transmission media representations, network topologies (physical vs logical), LANs vs WANs, internet access technologies (DSL, Cable, Cellular, Satellite), network reliability (Fault Tolerance, Scalability, QoS, Security), trends (BYOD, Cloud, WISP), network security threats, and Cisco CCNA certifications.
- **Module 2 — Basic Switch and End Device Configuration (104 Items)**: Cisco IOS navigation and modes (User EXEC, Privileged EXEC, Global Configuration, Line Config), CLI syntax structure, context-sensitive help (`?`), command completion (`Tab`), CLI shortcuts, hostname naming conventions, password protection (`secret`, `console`, `vty`), `service password-encryption`, login banners (`banner motd`), configuration files (`running-config` vs `startup-config`), IPv4/IPv6 addressing fundamentals, subnet masks, default gateways, and Switch Virtual Interface (`interface vlan 1`) configuration.
- **Module 3 — Protocols and Models (95 Items)**: Communication rules (message source/destination, channel, encoding, formatting/encapsulation, size, timing, flow control, timeout, unicast/multicast/broadcast), network protocol suites (TCP/IP protocol stack, OSI reference model, legacy AppleTalk and Novell NetWare), standards organizations (IEEE, IETF, ISO, ITU, TIA/EIA, ICANN, IANA), OSI 7 layers vs TCP/IP 4 layers comparison, data encapsulation/decapsulation workflows, Protocol Data Units (PDUs: Data, Segment, Packet, Frame, Bits), data access & addressing (Source/Destination MAC at Data Link, Source/Destination IP at Network Layer, default gateways, Address Resolution Protocol (ARP) concepts, same-network delivery vs remote-network routing).
</details>

<details>
<summary><b>HMBY311: Human Biology</b> — 252 Items</summary>

- **Module 1 — The Scientific Method & Basic Chemistry (152 Items)**: Steps of the scientific method (Observation, Hypothesis, Prediction, Experimentation, Conclusion), deductive vs inductive reasoning, controlled experiments (independent, dependent, controlled variables), atomic structure, isotopes and half-life, chemical bonding (covalent, ionic, hydrogen), properties of water (polarity, high heat capacity, cohesion/adhesion), pH scale and buffers, biomacromolecules (dehydration synthesis vs hydrolysis), carbohydrates (monosaccharides, disaccharides, glycogen/starch/cellulose), lipids (triglycerides, phospholipids, steroids), protein structures (primary, secondary, tertiary, quaternary), enzyme kinetics, nucleic acids (DNA vs RNA structure, base-pairing rules).
- **Module 4 — Chromosomes & Cell Division (40 Items)**: Chromatin vs condensed chromosomes, histones and nucleosomes, somatic cells ($2n$) vs gametes ($n$), homologous autosomes vs sex chromosomes ($XX/XY$), karyotypes, cell cycle phases ($G_1, S, G_2$, Mitosis), stages of mitosis (prophase, metaphase, anaphase, telophase), spindle fibers and asters, cytokinesis mechanisms (cleavage furrow in animal cells vs cell plate in plant cells).
- **Module 5 — Genetics, Human Inheritance and Cancer (60 Items)**: Gregor Mendel's principles (Law of Segregation, Law of Independent Assortment), genotypes vs phenotypes, homozygous vs heterozygous, Punnett squares, monohybrid and dihybrid crosses, non-Mendelian inheritance (incomplete dominance, codominance, multiple alleles, sex-linked traits), human genetic disorders (Huntington's, cystic fibrosis, PKU, Tay-Sachs, sickle-cell, hemophilia, Turner syndrome $XO$, Klinefelter syndrome $XXY$, Down syndrome trisomy 21), prenatal testing (amniocentesis vs CVS), cancer biology (benign vs malignant neoplasms, metastasis, contact inhibition loss, oncogenes, tumor suppressor genes, chemotherapy, radiation).
</details>

<details>
<summary><b>ATFL311: Automata Theory & Formal Languages</b> — 174 Items</summary>

- **Module 1 — Introduction to Automata Theory & Chomsky Hierarchy (40 Items)**: Central concepts of formal languages, alphabet ($\Sigma$), strings ($w$), empty string ($\varepsilon$), string operations (length $|w|$, concatenation, reversal $w^R$), Kleene star ($\Sigma^*$) vs positive closure ($\Sigma^+$), Chomsky hierarchy (Type 0 Unrestricted, Type 1 Context-Sensitive, Type 2 Context-Free, Type 3 Regular), grammar formal definitions $(V, T, P, S)$.
- **Module 2 — Finite State Machines & Prerequisites (48 Items)**: Finite State Machines (FSMs) with output (Moore vs Mealy machines), state transition tables and state diagrams, equivalence and conversion between Moore and Mealy, mathematical prerequisites (set operations, relations, functions, proof by induction).
- **Module 3 — Deterministic Finite Automata (DFA) (41 Items)**: Formal 5-tuple definition $M = (Q, \Sigma, \delta, q_0, F)$, deterministic transition function $\delta: Q \times \Sigma \to Q$, extended transition function $\hat{\delta}$, language acceptance $L(M)$, designing DFAs for specific string conditions (ends with, contains substring, even/odd parity), DFA minimization using table-filling algorithm.
- **Module 4 — Non-Deterministic Finite Automata & Conversions (45 Items)**: Non-deterministic transitions $\delta: Q \times \Sigma \to \mathcal{P}(Q)$, NFAs with $\varepsilon$-transitions, $\varepsilon$-closure computation, subset construction algorithm (Powerset construction for NFA to DFA conversion), dead states, regular expressions to NFA equivalence.
</details>

<details>
<summary><b>SEPC311: Social & Ethical Issues in Computing</b> — 106 Items</summary>

- **Module 1 — Common Ethical Theories (51 Items)**: Nature of ethics/moral philosophy (Greek *ethos*), normative tasks (systematizing, defending, recommending), Subjective Relativism (individual moral truth, "what's right for you", vote-selling rationalization), Cultural Relativism (society-centered guidelines, Philippine political appointments post-ban, white lies for family harmony, student F2 epidemic), Divine Command Theory (will of God, scripture, Louie's religious devotion), Ethical Egoism (exclusive self-interest, maximum long-term benefit, political patronage, "Like that you don't like", altruistic counter-examples: parental and sibling sacrifices), Consequentialism (end justifies means, Atoy Co tactical play, President Erap EDSA II resignation, algebraic shortcut methods), Kantian Deontology (Immanuel Kant, pure reason, duty for duty's sake, lawyer defending client, police peacekeeping, coffin money parable), Philippine governance duties (Congress makes laws, Executive enforces, Judiciary interprets), Article II Section 26 of 1987 Philippine Constitution (anti-dynasty mandate), and practical classroom dilemmas.
- **Module 2 — Computer Ethics and Professional Codes (55 Items)**: Professional Code of Ethics (definition and 4 core benefits: ethical decision-making, high standards, public trust/respect, evaluation benchmark), Code of Ethics of Filipino IT Professionals (10 tenets: public appreciation, public good, truthful advertising, IP/patent compliance, competence/responsibility, truthful capability statements, non-disclosure of confidential data, highest quality, IT development, continuing professional education), AITP Code of Ethics (6 obligations: management, fellow members, society, university/college, employer, country), ACM/IEEE Software Engineering Code (8 principles: Public, Client/Employer, Product, Judgement, Management, Profession, Colleagues, Self), Ten Commandments of Computer Ethics (CEI 1992: harm, interference, snooping, theft, false witness, pirated proprietary software, unauthorized resource usage, plagiarism/appropriation, social consequences, consideration/respect), Hacking Community Constitution (14 beliefs: free speech, freedom from oppressive state control, direct democracy, hacking to test integrity, open source movement, friction-free capitalism), James Moor's foundation (1985 paper, policy vacuums, 3 unique computer properties: Logical Malleability, Impact on Society, Invisibility Factor with its 3 dimensions: Invisible Abuse, Invisible Programming Values, Invisible Complex Calculations), Three Levels of Computer Ethics (Pop, Para, Theoretical), Philippine social networking context (Social Media Capital of the World, photo consent etiquette), and three legal exemptions for unauthorized photo/video publication (news of the day, general welfare/public good, public personalities in public).
</details>

<details>
<summary><b>Upcoming Year III Subjects (In Preparation)</b></summary>

- **SOFE311**: Software Engineering (Agile, Scrum, Design Patterns, CI/CD)
- **ITPM311**: IT Project Management (Project Life Cycle, Risk, Cost Estimation, Gantt)
- **CSEL311**: CS Professional Elective
- **SFCR311**: Systems Fundamentals & Cyber Risk (Threat Modeling, Cryptography, NIST Framework)
</details>

---

## 🎨 Design System — OLED Aesthetic

ReviewIII is styled around an intentional **Digital Sobriety & OLED Pitch-Black palette**:

```css
:root {
  --color-bg-base:        #000000; /* Pure Pitch Black */
  --color-surface-card:   #0a0a0a; /* Subtle Elevated Surface */
  --color-surface-hover:  #141414; /* Interactive Hover */
  --color-border-subtle:  #1f1f1f; /* Hairline Dividing Borders */
  --color-accent-primary: #8a9a86; /* Sage Green / Focus State */
  --color-accent-warm:    #a89f91; /* Soft Clay / Secondary Accent */
  --color-text-primary:   #f0f0f0; /* Crisp Off-White */
  --color-text-muted:     #888888; /* Calm Dimmed Reading Text */
}
```

- **True OLED Black**: Saves battery on OLED/AMOLED screens, eliminates light bleed, and minimizes eye fatigue during late-night study sessions.
- **Micro-Interactions**: Glassmorphic blur bars (`backdrop-filter: blur(16px)`), tactile hover transitions, and clean typography.
- **Zero Distractions**: No ads, no tracking scripts, no unnecessary third-party CDN bloat.

---

## 📁 Clean Repository Architecture

The project maintains a structured directory layout:

```
reviewiii/
├── astro.config.mjs             # Astro SSG build configuration (base: /reviewiii/)
├── package.json                 # Bun/Node package configuration & scripts
├── bun.lock                     # Bun dependency lockfile
├── README.md                    # This documentation portal
│
├── materials/                   # Raw Lecture Source Materials
│   └── netc311/                 # Original PowerPoint & PDF slide decks
│
├── scripts/                     # Generator & Data Processing Engine
│   ├── data/                    # Python item banks & verified questionnaires
│   │   ├── module1_data.py      # NETC311 Module 1 (99 Items)
│   │   ├── module2_data.py      # NETC311 Module 2 (104 Items)
│   │   ├── module3_data.py      # NETC311 Module 3 (95 Items)
│   │   ├── hmby311_m1_data.py   # HMBY311 Module 1 (152 Items)
│   │   ├── hmby311_m4_data.py   # HMBY311 Module 4 (40 Items)
│   │   ├── hmby311_m5_data.py   # HMBY311 Module 5 (60 Items)
│   │   ├── atfl311_data.py      # ATFL311 Modules 1-4 (174 Items)
│   │   └── sepc311_data.py      # SEPC311 Modules 1-2 (106 Items)
│   ├── templates/               # Standalone NotebookLM quiz player template
│   ├── build_all_quizzes.py     # Master quiz generator (injects 48px header & focus)
│   ├── build_hmby_m4_m5.py      # DOCX/PDF generator for HMBY Modules 4 & 5
│   ├── generate_*.py            # Subject-specific questionnaire generators
│   ├── deploy_github.sh         # Production build & deployment script
│   └── archive/                 # Historical migration & patch utilities
│
├── src/                         # Astro Modern Source Code
│   ├── components/              # Header, SubjectCard, ModuleCard, FocusTimer
│   ├── data/                    # Structured TypeScript curriculum database
│   ├── layouts/                 # Root HTML shell & meta configurations
│   ├── lib/                     # Client focus engine, auth engine, Web Audio
│   └── pages/                   # Hub portal (/) and course detail routes (/courses/*)
│
├── public/                      # Static Assets Served by Vite/Astro
│   ├── downloads/               # 48 organized offline files (netc311, hmby311, atfl311, sepc311)
│   ├── quizzes/                 # 12 interactive standalone quiz HTML applications
│   └── scripts/                 # Client-side focus-system.js & auth-system.js
│
└── docs/                        # Static Build Mirror for GitHub Pages Serving
    ├── courses/                 # Rendered subject pages
    ├── downloads/               # Direct download links
    ├── quizzes/                 # Live interactive quiz players
    └── index.html               # Main production application shell
```

---

## 💻 Developer Guide & Commands

ReviewIII is built with [Astro](https://astro.build/) and runs on the ultra-fast [Bun](https://bun.sh/) JavaScript runtime.

### Prerequisites
- [Bun](https://bun.sh/) (`v1.1+`)
- [Python](https://www.python.org/) (`3.10+` with `python-docx` for document generation)
- [LibreOffice](https://www.libreoffice.org/) (`soffice` CLI for automated DOCX &rarr; PDF compilation)

### Quickstart

```bash
# 1. Clone the repository
git clone git@github.com:jevvii/reviewiii.git
cd reviewiii

# 2. Install dependencies
bun install

# 3. Start local development server
bun run dev
# Server running at: http://localhost:4321/reviewiii/

# 4. Build static distribution for production
bun run build

# 5. Preview production build locally
bun run preview
```

### Automation Scripts

```bash
# Rebuild all 9 interactive quiz engines with latest data & UI
bun run build:quizzes
# (or python3 scripts/build_all_quizzes.py)

# Generate offline DOCX, PDF, JSON, and MD files for HMBY M4 & M5
bun run build:hmby
# (or python3 scripts/build_hmby_m4_m5.py)

# Full production build, docs sync, and GitHub push
bun run deploy
# (or bash scripts/deploy_github.sh)
```

---

## ⌨️ Keyboard Shortcuts Reference

Navigate and operate ReviewIII efficiently using built-in keyboard hotkeys:

| Key | Action | Scope |
| :---: | :--- | :--- |
| <kbd>/</kbd> | Focus global subject & module search input | Study Hub |
| <kbd>Esc</kbd> | Dismiss mobile navigation drawer or focus modal | Anywhere |
| <kbd>Space</kbd> | Toggle Start / Pause on Pomodoro timer | Study Hub & Quizzes |
| <kbd>R</kbd> | Reset current Pomodoro phase to default | Study Hub & Quizzes |
| <kbd>S</kbd> | Skip to next Pomodoro interval segment | Study Hub & Quizzes |

---

## 🔒 Offline Integrity & Privacy

ReviewIII runs **entirely on client-side technology**:
- No remote telemetry or user tracking.
- Study session logs and timer states persist safely in your browser's private `localStorage`.
- All quizzes and documents are self-contained and run seamlessly without an internet connection.

---

<div align="center">

**ReviewIII Academic Project** &bull; Crafted with precision for Computer Science undergraduates.

*Licensed under the [MIT License](LICENSE).*

</div>
