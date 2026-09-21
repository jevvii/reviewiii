import json
import html
import random
import re
from hmby311_m1_data import HMBY_MODULE_1_ITEMS

# 1. Build Quiz Questions JSON
quiz_questions = []
for idx, item in enumerate(HMBY_MODULE_1_ITEMS, start=1):
    choices = [item["a"]] + item["distractors"]
    rng = random.Random(idx * 7919)
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
        "covered": list(set([item["topic"] for item in HMBY_MODULE_1_ITEMS])),
        "followUp": ["Review missed items and lecture slides on Scientific Method & Basic Chemistry"]
    }
}

# Save JSON
with open("HMBY311_Module_1_Quiz.json", "w", encoding="utf-8") as f:
    json.dump({"title": "HMBY311: Module 1 — The Scientific Method & Basic Chemistry", **quiz_payload}, f, indent=2)
print("Saved HMBY311_Module_1_Quiz.json")

# Save Markdown
md_lines = [
    "# HMBY311: Human Biology — Module 1 Identification Quiz",
    "## The Scientific Method and Basic Chemistry",
    f"*Total Questions: {len(quiz_questions)} Items | Format: Identification with Multiple Choices*\n",
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

with open("HMBY311_Module_1_Quiz.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
print("Saved HMBY311_Module_1_Quiz.md")

# 2. Build Standalone HTML Quiz Player from Module_1_NotebookLM_Quiz.html template
with open("Module_1_NotebookLM_Quiz.html", "r", encoding="utf-8") as f:
    template = f.read()

# Update page title
template = re.sub(r'<title>.*?</title>', '<title>HMBY311 — Module 1: The Scientific Method & Basic Chemistry</title>', template)

# Replace data-app-data
escaped_json = html.escape(json.dumps(quiz_payload))
app_root_pattern = r'<app-root\s+data-app-data="[^"]*">'
template = re.sub(app_root_pattern, f'<app-root data-app-data="{escaped_json}">', template)

# Update the Top Navigation Bar for HMBY311
navbar_html = """
    <!-- Pitch Black Top Nav -->
    <header id="quiz-hub-nav" style="position: sticky; top: 0; left: 0; right: 0; z-index: 999999; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding: 12px 28px; display: flex; align-items: center; justify-content: space-between; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
      <div style="display: flex; align-items: center; gap: 12px;">
        <a href="../index.html" style="color: #f0f0f0; text-decoration: none; font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 8px;">
          <span style="color: #8a9a86; font-size: 15px;">✦</span>
          <span style="color: #8a9a86; letter-spacing: -0.01em;">ReviewIII</span>
          <span style="color: #f0f0f0;">Hub</span>
        </a>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a89f91; font-size: 13px; font-weight: 500;">HMBY311</span>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a0a0a0; font-size: 13px; font-weight: 400;">Module 1: Scientific Method & Chemistry (82 Qs)</span>
      </div>
      <div style="display: flex; align-items: center; gap: 10px;">
        <a href="../index.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">Hub Overview</a>
        <span style="color: #000000; background: #8a9a86; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 4px;">Module 1 Active</span>
      </div>
    </header>
"""
template = re.sub(r'<!-- Pitch Black Top Nav -->.*?</header>', navbar_html, template, flags=re.DOTALL)

with open("HMBY311_Module_1_Quiz.html", "w", encoding="utf-8") as f:
    f.write(template)
print("Saved HMBY311_Module_1_Quiz.html successfully!")
