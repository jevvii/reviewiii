import json
import html
import random
import re
import os
import shutil

from atfl311_data import (
    ATFL_MODULE_1_ITEMS,
    ATFL_MODULE_2_ITEMS,
    ATFL_MODULE_3_ITEMS,
    ATFL_MODULE_4_ITEMS
)

MODULE_SPECS = [
    {
        "num": 1,
        "code": "atfl311-m1",
        "short_title": "Intro to Automata",
        "title": "Module 1: Introduction to Automata Theory & Chomsky Hierarchy",
        "items": ATFL_MODULE_1_ITEMS,
        "json_filename": "ATFL311_Module_1_Quiz.json",
        "md_filename": "ATFL311_Module_1_Quiz.md",
        "docx_filename": "Module 1 - Introduction to Automata Theory - Questionnaire.docx",
        "pdf_filename": "Module 1 - Introduction to Automata Theory - Questionnaire.pdf",
        "html_name": "module1.html"
    },
    {
        "num": 2,
        "code": "atfl311-m2",
        "short_title": "FSM & Prerequisites",
        "title": "Module 2: Finite State Machines & Prerequisites",
        "items": ATFL_MODULE_2_ITEMS,
        "json_filename": "ATFL311_Module_2_Quiz.json",
        "md_filename": "ATFL311_Module_2_Quiz.md",
        "docx_filename": "Module 2 - Finite State Machines and Prerequisites - Questionnaire.docx",
        "pdf_filename": "Module 2 - Finite State Machines and Prerequisites - Questionnaire.pdf",
        "html_name": "module2.html"
    },
    {
        "num": 3,
        "code": "atfl311-m3",
        "short_title": "Deterministic FA (DFA)",
        "title": "Module 3: Deterministic Finite Automata (DFA)",
        "items": ATFL_MODULE_3_ITEMS,
        "json_filename": "ATFL311_Module_3_Quiz.json",
        "md_filename": "ATFL311_Module_3_Quiz.md",
        "docx_filename": "Module 3 - Deterministic Finite Automata - Questionnaire.docx",
        "pdf_filename": "Module 3 - Deterministic Finite Automata - Questionnaire.pdf",
        "html_name": "module3.html"
    },
    {
        "num": 4,
        "code": "atfl311-m4",
        "short_title": "Non-Deterministic FA (NFA)",
        "title": "Module 4: Non-Deterministic Finite Automata & Conversion",
        "items": ATFL_MODULE_4_ITEMS,
        "json_filename": "ATFL311_Module_4_Quiz.json",
        "md_filename": "ATFL311_Module_4_Quiz.md",
        "docx_filename": "Module 4 - Non-Deterministic Finite Automata - Questionnaire.docx",
        "pdf_filename": "Module 4 - Non-Deterministic Finite Automata - Questionnaire.pdf",
        "html_name": "module4.html"
    }
]

# Read template HTML from public/quizzes/netc311/module1.html
with open("public/quizzes/netc311/module1.html", "r", encoding="utf-8") as f:
    base_template = f.read()

# Ensure directories exist
for d in ["public/quizzes/atfl311", "quizzes/atfl311", "public/downloads/atfl311", "downloads/atfl311"]:
    os.makedirs(d, exist_ok=True)

for spec in MODULE_SPECS:
    m_num = spec["num"]
    m_items = spec["items"]
    item_count = len(m_items)
    print(f"\nProcessing Module {m_num}: {spec['title']} ({item_count} items)...")

    # 1. Build Quiz Questions JSON payload
    quiz_questions = []
    for idx, item in enumerate(m_items, start=1):
        choices = [item["a"]] + item["distractors"]
        rng = random.Random(idx * 7919 + m_num * 104729)
        rng.shuffle(choices)
        letters = ['a', 'b', 'c', 'd']
        correct_letter = letters[choices.index(item["a"])]

        opts = []
        for l_idx, ch in enumerate(choices):
            is_corr = (ch == item["a"])
            if is_corr:
                rationale = f"Correct! [{item['topic']}] {item['explanation']}"
            else:
                rationale = f"Incorrect. '{ch}' is a distractor. The correct answer is '{item['a']}'."
            opts.append({
                "text": f"{letters[l_idx]}.) {ch}",
                "isCorrect": is_corr,
                "rationale": rationale
            })

        quiz_questions.append({
            "question": f"_____ {idx}. {item['q']}",
            "answerOptions": opts,
            "hint": f"Concept: {item['topic']}"
        })

    quiz_payload = {
        "quiz": quiz_questions,
        "topics": {
            "covered": sorted(list(set([item["topic"] for item in m_items]))),
            "followUp": [f"Review missed items on {spec['title']}"]
        }
    }

    # Save JSON to root, public/downloads/atfl311/, and downloads/atfl311/
    full_json = {"title": f"ATFL311: {spec['title']} ({item_count} Questions)", **quiz_payload}
    with open(spec["json_filename"], "w", encoding="utf-8") as f:
        json.dump(full_json, f, indent=2, ensure_ascii=False)
    shutil.copy2(spec["json_filename"], f"public/downloads/atfl311/{spec['json_filename']}")
    shutil.copy2(spec["json_filename"], f"downloads/atfl311/{spec['json_filename']}")
    print(f"Saved {spec['json_filename']}")

    # Save Markdown to root, public/downloads/atfl311/, and downloads/atfl311/
    md_lines = [
        f"# ATFL311: Automata Theory & Formal Languages — {spec['title']}",
        f"*Total Questions: {item_count} Items | Format: Identification with Multiple Choices*\n",
        "---\n"
    ]
    for idx, q in enumerate(quiz_questions, start=1):
        md_lines.append(f"### Question {idx}")
        md_lines.append(f"**{q['question']}**\n")
        for opt in q['answerOptions']:
            marker = "✅ **[CORRECT]**" if opt['isCorrect'] else "❌"
            md_lines.append(f"- {opt['text']} {marker}")
            md_lines.append(f"  > *Rationale:* {opt['rationale']}\n")
        md_lines.append(f"💡 *Hint:* {q['hint']}\n")
        md_lines.append("---\n")

    with open(spec["md_filename"], "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    shutil.copy2(spec["md_filename"], f"public/downloads/atfl311/{spec['md_filename']}")
    shutil.copy2(spec["md_filename"], f"downloads/atfl311/{spec['md_filename']}")
    print(f"Saved {spec['md_filename']}")

    # Sync DOCX and PDF to public/downloads/atfl311/ and downloads/atfl311/
    shutil.copy2(spec["docx_filename"], f"public/downloads/atfl311/{spec['docx_filename']}")
    shutil.copy2(spec["docx_filename"], f"downloads/atfl311/{spec['docx_filename']}")
    shutil.copy2(spec["pdf_filename"], f"public/downloads/atfl311/{spec['pdf_filename']}")
    shutil.copy2(spec["pdf_filename"], f"downloads/atfl311/{spec['pdf_filename']}")

    # Build Standalone HTML Player
    escaped_json = html.escape(json.dumps(quiz_payload, ensure_ascii=False))
    idx = base_template.find('data-app-data="')
    if idx == -1:
        raise ValueError("data-app-data not found in base template!")
    end_idx = base_template.find('"', idx + 15)
    if end_idx == -1:
        raise ValueError("closing quote not found in base template!")

    html_content = base_template[:idx + 15] + escaped_json + base_template[end_idx:]

    # Replace title
    html_content = re.sub(
        r'<title>.*?</title>',
        f'<title>ATFL311 — {spec["title"]}</title>',
        html_content
    )

    # Build Navbar HTML for Module m_num
    nav_tabs = []
    nav_tabs.append('<a href="../../index.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">Hub Overview</a>')
    for other_s in MODULE_SPECS:
        o_num = other_s["num"]
        o_cnt = len(other_s["items"])
        if o_num == m_num:
            nav_tabs.append(f'<span style="color: #000000; background: #8a9a86; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 4px;">M{o_num} ({o_cnt} Qs)</span>')
        else:
            nav_tabs.append(f'<a href="module{o_num}.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">M{o_num} ({o_cnt} Qs)</a>')
    
    if m_num < len(MODULE_SPECS):
        next_num = m_num + 1
        nav_tabs.append(f'<a href="module{next_num}.html" style="color: #8a9a86; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; background: rgba(138, 154, 134, 0.1); border: 1px solid rgba(138, 154, 134, 0.35); display: flex; align-items: center; gap: 4px;">Next &rarr;</a>')

    nav_tabs_html = "\n        ".join(nav_tabs)

    custom_navbar = f"""<!-- Pitch Black Top Nav -->
    <header id="quiz-hub-nav" style="position: sticky; top: 0; left: 0; right: 0; z-index: 999999; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding: 12px 28px; display: flex; align-items: center; justify-content: space-between; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
      <div style="display: flex; align-items: center; gap: 12px;">
        <a href="../../index.html" style="color: #f0f0f0; text-decoration: none; font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 8px;">
          <span style="color: #8a9a86; font-size: 15px;">✦</span>
          <span style="color: #8a9a86; letter-spacing: -0.01em;">ReviewIII</span>
          <span style="color: #f0f0f0;">Hub</span>
        </a>
        <span class="nav-breadcrumbs-slash" style="color: #444444; font-size: 13px;">/</span>
        <span class="nav-sub-code" style="color: #a89f91; font-size: 13px; font-weight: 500;">ATFL311</span>
        <span class="nav-breadcrumbs-slash" style="color: #444444; font-size: 13px;">/</span>
        <span class="nav-breadcrumbs-title" style="color: #a0a0a0; font-size: 13px; font-weight: 400;">Module {m_num}: {spec['short_title']} ({item_count} Qs)</span>
      </div>
      <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
        {nav_tabs_html}
      </div>
    </header>"""

    html_content = re.sub(r'<!-- Pitch Black Top Nav -->.*?</header>', custom_navbar, html_content, flags=re.DOTALL)

    # Save to public/quizzes/atfl311/moduleX.html
    pub_path = f"public/quizzes/atfl311/{spec['html_name']}"
    with open(pub_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved {pub_path}")

    # Save to quizzes/atfl311/moduleX.html
    quiz_path = f"quizzes/atfl311/{spec['html_name']}"
    with open(quiz_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved {quiz_path}")

    # Root HTML with adjusted href
    root_html = html_content.replace('href="../../index.html"', 'href="index.html"')
    root_path = f"ATFL311_Module_{m_num}_Quiz.html"
    with open(root_path, "w", encoding="utf-8") as f:
        f.write(root_html)
    print(f"Saved {root_path}")

print("\nALL ATFL311 Quiz Players, JSON, Markdown, and Download files built successfully!")
