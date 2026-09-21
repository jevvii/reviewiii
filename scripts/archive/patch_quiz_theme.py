import re
import os

base_dir = "/home/javvii/YearIII/NETC311/quiz1"

pitch_black_vars = """--gem-sys-spacing--xs:0.25rem;--gem-sys-spacing--s:0.5rem;--gem-sys-spacing--m:0.75rem;--gem-sys-spacing--l:1rem;--gem-sys-spacing--xl:1.25rem;--gem-sys-spacing--xxl:1.5rem;--gem-sys-spacing--xxxl:2rem;--quiz-content:640px;--gem-sys-shape--corner-medium:8px;--feedback-correct-text-color:#8a9a86;--feedback-incorrect-text-color:#f2b8b5;--feedback-rationale-text-color:#a0a0a0;--feedback-primary-text-color:#f0f0f0;--feedback-correct-background-color:#0d1a10;--feedback-incorrect-background-color:#1a0a0a;--feedback-correct-border-color:#8a9a86;--feedback-incorrect-border-color:#b3261e;--correct-color:#8a9a86;--not-correct-color:#a0a0a0;--nlm-fills-surface-page-dark:#000000;--button-hover-color:#141414;--primary-text-color:#f0f0f0;--focus-ring-color:#8a9a86;--surface-color:#000000;--surface-variant-color:#0a0a0a;--secondary-button-border-color:rgba(255,255,255,0.12);--answer-btn-background:#0a0a0a;--answer-text-color:#f0f0f0;--hint-btn-background:#141414;--hint-btn-color:#8a9a86;--hint-container-background:#0a0a0a;--stat-card-background-color:#0a0a0a;--stat-card-color:#a0a0a0;--body-text-color:#a0a0a0;--topics-background:#0a0a0a;--score-summary-background-color:#0a0a0a;--score-summary-got-it-color:#8a9a86;--score-summary-missed-it-color:#2a2a2a;--score-summary-progress-bar-background-color:#141414;--follow-up-chip-selected-background:#141414;--follow-up-chip-hover-background:#1a1a1a;--follow-up-chip-background:#0a0a0a;--generate-button-background:#8a9a86;--generate-button-hover-background:#9bb097;--button-disabled-fill:rgba(255,255,255,0.06);--button-disabled-text:rgba(255,255,255,0.2);--summary-timer-background:#0a0a0a;--app-timer-background:#0a0a0a;color-scheme:dark;background-color:#000000"""

def patch_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Force JS to default to dark theme
    text = text.replace('this.i=is("light")', 'this.i=is("dark")')
    
    # 2. Patch sQ function to always enforce dark-theme
    old_sq = 'b==="dark"?(a.body.classList.add("dark-theme"),a.body.classList.remove("light-theme")):(a.body.classList.remove("dark-theme"),a.body.classList.add("light-theme"))'
    new_sq = 'a.body.classList.add("dark-theme"),a.body.classList.remove("light-theme")'
    text = text.replace(old_sq, new_sq)
    
    # 3. Replace body.light-theme,html.light-theme{...} with pitch black vars
    text = re.sub(r'body\.light-theme,html\.light-theme\{[^}]+\}', f'body.light-theme,html.light-theme{{{pitch_black_vars}}}', text)
    
    # 4. Replace body.dark-theme,html.dark-theme{...} with pitch black vars
    text = re.sub(r'body\.dark-theme,html\.dark-theme\{[^}]+\}', f'body.dark-theme,html.dark-theme{{{pitch_black_vars}}}', text)
    
    # 5. Patch Next button in quiz
    text = text.replace('.navigation-buttons-container .next-btn{background:#4259ff;border:none;color:#fff}',
                        '.navigation-buttons-container .next-btn{background:#8a9a86;border:none;color:#000000;font-weight:600;}')
    text = text.replace('.navigation-buttons-container-mobile .next-btn{background:#4259ff;border:none;color:#fff}',
                        '.navigation-buttons-container-mobile .next-btn{background:#8a9a86;border:none;color:#000000;font-weight:600;}')
    
    # 6. Additional styling overrides for quiz cards and options
    extra_quiz_dark_css = """
<style id="pitch-black-quiz-overrides">
  html, body {
    background-color: #000000 !important;
    color: #f0f0f0 !important;
  }
  
  app-root, .app-root, .app-container {
    background-color: #000000 !important;
  }
  
  /* Answer buttons / choices */
  .answer-option-button, .answer-btn, button[class*="answer"], .choice-button {
    background-color: #0a0a0a !important;
    color: #f0f0f0 !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 6px !important;
    transition: all 0.2s ease !important;
  }
  
  .answer-option-button:hover, .answer-btn:hover {
    background-color: #141414 !important;
    border-color: #8a9a86 !important;
  }

  /* Question text */
  .question-text, .question-title, h2, h3 {
    color: #f0f0f0 !important;
  }

  /* Hint box & Explanation container */
  .hint-container, .rationale-container, .explanation-container {
    background-color: #0a0a0a !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: #a0a0a0 !important;
  }

  /* Material buttons & navigation */
  .secondary-button, .back-btn, .summary-btn, .retake-quiz-btn, .review-quiz-btn {
    background-color: transparent !important;
    color: #a0a0a0 !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 4px !important;
  }

  .secondary-button:hover, .back-btn:hover, .summary-btn:hover {
    background-color: rgba(255, 255, 255, 0.05) !important;
    color: #f0f0f0 !important;
    border-color: var(--color-accent-primary, #8a9a86) !important;
  }

  .next-btn {
    background-color: #8a9a86 !important;
    color: #000000 !important;
    font-weight: 600 !important;
    border-radius: 4px !important;
  }

  .next-btn:hover {
    filter: brightness(1.1) !important;
    box-shadow: 0 4px 12px rgba(138, 154, 134, 0.3) !important;
  }
</style>
"""
    # Remove old override if present
    text = re.sub(r'<style id="pitch-black-quiz-overrides">.*?</style>', '', text, flags=re.DOTALL)
    head_idx = text.find('</head>')
    if head_idx != -1:
        text = text[:head_idx] + extra_quiz_dark_css + "\n" + text[head_idx:]
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Successfully patched quiz theme in {file_path}")

for f in ["Module_1_NotebookLM_Quiz.html", "Module_2_NotebookLM_Quiz.html"]:
    patch_file(os.path.join(base_dir, f))
