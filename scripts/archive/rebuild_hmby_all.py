import json
import html
import random
import re
import os
import shutil
from hmby311_m1_data import HMBY_MODULE_1_ITEMS

total_items = len(HMBY_MODULE_1_ITEMS)
print(f"Loaded {total_items} items from hmby311_m1_data.py")

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
        "covered": sorted(list(set([item["topic"] for item in HMBY_MODULE_1_ITEMS]))),
        "followUp": ["Review missed items and lecture notes on Scientific Method & Basic Chemistry"]
    }
}

# 2. Write JSON datasets
json_data = {"title": f"HMBY311: Module 1 — The Scientific Method & Basic Chemistry ({total_items} Questions)", **quiz_payload}
with open("HMBY311_Module_1_Quiz.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)
print("Saved root HMBY311_Module_1_Quiz.json")

# 3. Write Markdown datasets
md_lines = [
    f"# HMBY311: Human Biology — Module 1 Identification Quiz",
    f"## The Scientific Method and Basic Chemistry",
    f"*Total Questions: {total_items} Items | Format: Identification with Multiple Choices*\n",
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
print("Saved root HMBY311_Module_1_Quiz.md")

# 4. Read base html from public/quizzes/hmby311/module1.html
with open("public/quizzes/hmby311/module1.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace data-app-data
escaped_json = html.escape(json.dumps(quiz_payload, ensure_ascii=False))
idx = html_content.find('data-app-data="')
if idx == -1:
    raise ValueError("data-app-data not found in public/quizzes/hmby311/module1.html!")
end_idx = html_content.find('"', idx + 15)
if end_idx == -1:
    raise ValueError("closing quote of data-app-data not found!")

updated_html = html_content[:idx + 15] + escaped_json + html_content[end_idx:]

# Update question count in title & nav header
updated_html = re.sub(
    r'Module 1: Scientific Method & Chemistry \(\d+ Qs\)',
    f'Module 1: Scientific Method & Chemistry ({total_items} Qs)',
    updated_html
)
updated_html = re.sub(
    r'Module 1 \(\d+ Qs\)',
    f'Module 1 ({total_items} Qs)',
    updated_html
)

# Save to public/quizzes/hmby311/module1.html
with open("public/quizzes/hmby311/module1.html", "w", encoding="utf-8") as f:
    f.write(updated_html)
print(f"Updated public/quizzes/hmby311/module1.html with {total_items} questions")

# Save to quizzes/hmby311/module1.html
os.makedirs("quizzes/hmby311", exist_ok=True)
with open("quizzes/hmby311/module1.html", "w", encoding="utf-8") as f:
    f.write(updated_html)
print(f"Updated quizzes/hmby311/module1.html with {total_items} questions")

# Also create root HMBY311_Module_1_Quiz.html (with hrefs adjusted for root)
root_html = updated_html.replace('href="../../index.html"', 'href="index.html"')
with open("HMBY311_Module_1_Quiz.html", "w", encoding="utf-8") as f:
    f.write(root_html)
print(f"Updated root HMBY311_Module_1_Quiz.html with {total_items} questions")

# 5. Sync downloads to public/downloads/hmby311/ and downloads/hmby311/
for target_dir in ["public/downloads/hmby311", "downloads/hmby311"]:
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy2("HMBY311_Module_1_Quiz.json", os.path.join(target_dir, "HMBY311_Module_1_Quiz.json"))
    shutil.copy2("HMBY311_Module_1_Quiz.md", os.path.join(target_dir, "HMBY311_Module_1_Quiz.md"))
    shutil.copy2("Module 1 - Human Biology - Scientific Method and Basic Chemistry.docx", 
                 os.path.join(target_dir, "Module 1 - Human Biology - Scientific Method and Basic Chemistry.docx"))
    shutil.copy2("Module 1 - Human Biology - Scientific Method and Basic Chemistry.pdf", 
                 os.path.join(target_dir, "Module 1 - Human Biology - Scientific Method and Basic Chemistry.pdf"))
    print(f"Synced files to {target_dir}/")

print("All HMBY311 rebuild tasks completed successfully!")
