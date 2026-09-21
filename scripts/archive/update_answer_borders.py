import re
import os

base_dir = "/home/javvii/YearIII/NETC311/quiz1"

vibrant_borders_css = """
<style id="vibrant-answer-borders">
  /* High-Contrast Popping Borders for Correct and Wrong Answers */
  
  :root, html, body {
    --feedback-correct-border-color: #22c55e !important;
    --feedback-correct-text-color: #4ade80 !important;
    --feedback-correct-background-color: rgba(34, 197, 94, 0.14) !important;
    --correct-color: #22c55e !important;
    
    --feedback-incorrect-border-color: #ef4444 !important;
    --feedback-incorrect-text-color: #f87171 !important;
    --feedback-incorrect-background-color: rgba(239, 68, 68, 0.14) !important;
    --not-correct-color: #ef4444 !important;
  }

  /* 1. Correct Answer Choices (Glowing Pop) */
  .answer-options .answer-btn.correct,
  .answer-options .answer-btn.background-correct,
  .answer-options .answer-btn.outline-correct,
  .answer-btn.correct,
  .answer-btn.background-correct,
  .answer-btn.outline-correct,
  button.correct,
  .answer-option-button.correct {
    border: 2px solid #22c55e !important;
    background-color: rgba(34, 197, 94, 0.14) !important;
    color: #f0fdf4 !important;
    box-shadow: 0 0 16px rgba(34, 197, 94, 0.4), inset 0 0 10px rgba(34, 197, 94, 0.15) !important;
    transform: scale(1.008) !important;
  }

  .answer-options .answer-btn.correct .answer-content,
  .answer-btn.correct .answer-content,
  .answer-btn.correct span {
    color: #f0fdf4 !important;
    font-weight: 500 !important;
  }

  /* 2. Wrong / Incorrect Answer Choices (Crimson Pop) */
  .answer-options .answer-btn.incorrect,
  .answer-options .answer-btn.background-incorrect,
  .answer-options .answer-btn.outline-incorrect,
  .answer-btn.incorrect,
  .answer-btn.background-incorrect,
  .answer-btn.outline-incorrect,
  button.incorrect,
  .answer-option-button.incorrect {
    border: 2px solid #ef4444 !important;
    background-color: rgba(239, 68, 68, 0.14) !important;
    color: #fef2f2 !important;
    box-shadow: 0 0 16px rgba(239, 68, 68, 0.4), inset 0 0 10px rgba(239, 68, 68, 0.15) !important;
    transform: scale(1.008) !important;
  }

  .answer-options .answer-btn.incorrect .answer-content,
  .answer-btn.incorrect .answer-content,
  .answer-btn.incorrect span {
    color: #fef2f2 !important;
    font-weight: 500 !important;
  }

  /* 3. Feedback Banner Card (Summary Banner below question) */
  .feedback-card.correct,
  [class*="feedback-card"][class*="correct"] {
    border: 2px solid #22c55e !important;
    background: #09180c !important;
    box-shadow: 0 4px 20px rgba(34, 197, 94, 0.25) !important;
    border-radius: 8px !important;
  }

  .feedback-card.correct .feedback-header,
  .feedback-card.correct .feedback-sub-title,
  .feedback-card.correct .icon-container {
    color: #4ade80 !important;
    font-weight: 600 !important;
  }

  .feedback-card.incorrect,
  [class*="feedback-card"][class*="incorrect"] {
    border: 2px solid #ef4444 !important;
    background: #180909 !important;
    box-shadow: 0 4px 20px rgba(239, 68, 68, 0.25) !important;
    border-radius: 8px !important;
  }

  .feedback-card.incorrect .feedback-header,
  .feedback-card.incorrect .feedback-sub-title,
  .feedback-card.incorrect .icon-container {
    color: #f87171 !important;
    font-weight: 600 !important;
  }

  /* 4. Normal Unselected Answer Options (OLED Pitch Black Surface) */
  .answer-options .answer-btn:not(.correct):not(.incorrect),
  .answer-btn:not(.correct):not(.incorrect),
  .answer-option-button:not(.correct):not(.incorrect) {
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    background-color: #0a0a0a !important;
    color: #f0f0f0 !important;
    transition: all 0.2s ease !important;
  }

  .answer-options .answer-btn:not(.correct):not(.incorrect):hover,
  .answer-btn:not(.correct):not(.incorrect):hover,
  .answer-option-button:not(.correct):not(.incorrect):hover {
    border-color: #8a9a86 !important;
    background-color: #141414 !important;
    box-shadow: 0 0 12px rgba(138, 154, 134, 0.2) !important;
  }
</style>
"""

def update_file(filename):
    path = os.path.join(base_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    # Remove previous vibrant-answer-borders if present
    text = re.sub(r'<style id="vibrant-answer-borders">.*?</style>', '', text, flags=re.DOTALL)
    
    # Inject into head
    head_idx = text.find('</head>')
    if head_idx != -1:
        text = text[:head_idx] + vibrant_borders_css + "\n" + text[head_idx:]
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated {filename} with vibrant popping borders!")

update_file("Module_1_NotebookLM_Quiz.html")
update_file("Module_2_NotebookLM_Quiz.html")
