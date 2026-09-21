import os
import json
import html
import random
from module1_data import MODULE_1_ITEMS
from module2_data import MODULE_2_ITEMS

def build_quiz_json(items, code, title):
    rng = random.Random(101 + int(code))
    questions = []
    
    for idx, item in enumerate(items, 1):
        q_text = item["q"]
        correct_ans = item["a"]
        distractors = item["distractors"]
        topic = item["topic"]
        explanation = item["explanation"]
        
        all_options = [correct_ans] + distractors
        rng.shuffle(all_options)
        
        letters = ['a', 'b', 'c', 'd']
        answer_options = []
        for l, opt in zip(letters, all_options):
            is_correct = (opt == correct_ans)
            if is_correct:
                rationale = f"Correct! [{topic}] {explanation}"
            else:
                rationale = f"Incorrect. '{opt}' is a distractor. The correct answer is '{correct_ans}'."
                
            answer_options.append({
                "text": f"{l}.) {opt}",
                "isCorrect": is_correct,
                "rationale": rationale
            })
            
        questions.append({
            "question": f"_____ {idx}. {q_text}",
            "answerOptions": answer_options,
            "hint": f"Concept: {topic}"
        })
        
    return {
        "title": title,
        "questions": questions
    }

def build_quiz_markdown(quiz_data):
    lines = [f"# {quiz_data['title']}", "", f"*Total Questions: {len(quiz_data['questions'])}*", ""]
    for q in quiz_data["questions"]:
        lines.append(f"### {q['question']}")
        lines.append("")
        for opt in q["answerOptions"]:
            marker = "[x]" if opt["isCorrect"] else "[ ]"
            lines.append(f"- {marker} {opt['text']}")
        lines.append("")
        lines.append(f"**Hint:** {q['hint']}")
        # Include rationale in an expandable detail block
        correct_opt = next(o for o in q["answerOptions"] if o["isCorrect"])
        lines.append(f"<details><summary>Explanation</summary>{correct_opt['rationale']}</details>")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)

def build_interactive_html(template_path, quiz_data, output_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
        
    idx = template.find('data-app-data="')
    if idx == -1:
        raise ValueError("Could not find data-app-data in template")
    end_idx = template.find('"', idx + 15)
    
    app_data = {
        "quiz": quiz_data["questions"],
        "topics": {
            "covered": [q["hint"] for q in quiz_data["questions"][:15]],
            "followUp": ["Review missed items and consult lecture slides"]
        }
    }
    
    escaped_json = html.escape(json.dumps(app_data, ensure_ascii=False))
    new_html = template[:idx + 15] + escaped_json + template[end_idx:]
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Generated Interactive HTML: {output_path} ({len(quiz_data['questions'])} questions)")

print("Script defined.")

if __name__ == "__main__":
    base_dir = "/home/javvii/YearIII/NETC311/quiz1"
    template_path = os.path.join(base_dir, "test_quiz.html")
    
    # Module 1
    m1_title = "NETC311: Module 1 — Networking Today Identification Quiz"
    m1_quiz = build_quiz_json(MODULE_1_ITEMS, "1", m1_title)
    
    m1_json_path = os.path.join(base_dir, "Module_1_NotebookLM_Quiz.json")
    with open(m1_json_path, 'w', encoding='utf-8') as f:
        json.dump(m1_quiz, f, indent=2, ensure_ascii=False)
    print(f"Saved {m1_json_path}")
    
    m1_md_path = os.path.join(base_dir, "Module_1_NotebookLM_Quiz.md")
    with open(m1_md_path, 'w', encoding='utf-8') as f:
        f.write(build_quiz_markdown(m1_quiz))
    print(f"Saved {m1_md_path}")
    
    m1_html_path = os.path.join(base_dir, "Module_1_NotebookLM_Quiz.html")
    build_interactive_html(template_path, m1_quiz, m1_html_path)
    
    # Module 2
    m2_title = "NETC311: Module 2 — Basic Switch and End Device Configuration Identification Quiz"
    m2_quiz = build_quiz_json(MODULE_2_ITEMS, "2", m2_title)
    
    m2_json_path = os.path.join(base_dir, "Module_2_NotebookLM_Quiz.json")
    with open(m2_json_path, 'w', encoding='utf-8') as f:
        json.dump(m2_quiz, f, indent=2, ensure_ascii=False)
    print(f"Saved {m2_json_path}")
    
    m2_md_path = os.path.join(base_dir, "Module_2_NotebookLM_Quiz.md")
    with open(m2_md_path, 'w', encoding='utf-8') as f:
        f.write(build_quiz_markdown(m2_quiz))
    print(f"Saved {m2_md_path}")
    
    m2_html_path = os.path.join(base_dir, "Module_2_NotebookLM_Quiz.html")
    build_interactive_html(template_path, m2_quiz, m2_html_path)

