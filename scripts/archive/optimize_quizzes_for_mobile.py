import re
import os

base_dir = "/home/javvii/YearIII/NETC311/quiz1"

mobile_quiz_css = """
<style id="mobile-responsive-quiz-styles">
  /* Mobile Viewport Optimizations for Quiz Player */
  @media (max-width: 768px) {
    #quiz-hub-nav {
      padding: 10px 14px !important;
      gap: 8px !important;
    }

    .nav-breadcrumbs-title {
      display: none !important;
    }

    .nav-breadcrumbs-slash {
      display: none !important;
    }

    #quiz-hub-nav a, #quiz-hub-nav span {
      padding: 6px 11px !important;
      font-size: 12px !important;
    }

    #quiz-loader {
      top: 46px !important;
    }

    .app-container {
      padding: 0.5rem 0.25rem !important;
      max-width: 100% !important;
    }

    /* Touch-friendly answer choices */
    .answer-options .answer-btn,
    .answer-btn,
    .answer-option-button,
    button[class*="answer"] {
      padding: 12px 14px !important;
      min-height: 48px !important;
      font-size: 14.5px !important;
      line-height: 1.45 !important;
      margin-bottom: 8px !important;
      border-radius: 6px !important;
    }

    /* Feedback Cards */
    .feedback-card, [class*="feedback-card"] {
      padding: 12px 14px !important;
      margin-top: 12px !important;
    }

    /* Navigation buttons */
    .navigation-buttons-container,
    .navigation-buttons-container-mobile {
      padding-top: 12px !important;
      gap: 8px !important;
    }

    .navigation-buttons-container .next-btn,
    .navigation-buttons-container-mobile .next-btn,
    .navigation-buttons-container .back-btn,
    .navigation-buttons-container-mobile .back-btn {
      min-height: 44px !important;
      font-size: 14px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }
  }

  @media (max-width: 420px) {
    #quiz-hub-nav {
      padding: 8px 10px !important;
    }
    
    .nav-sub-code {
      display: none !important;
    }
  }
</style>
"""

def patch_quiz_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add mobile classes to nav elements
    content = content.replace('<span style="color: #444444; font-size: 13px;">/</span>', '<span class="nav-breadcrumbs-slash" style="color: #444444; font-size: 13px;">/</span>')
    content = re.sub(
        r'<span style="color: #a0a0a0; font-size: 13px; font-weight: 400;">(.*?)</span>',
        r'<span class="nav-breadcrumbs-title" style="color: #a0a0a0; font-size: 13px; font-weight: 400;">\1</span>',
        content
    )
    content = re.sub(
        r'<span style="color: #a89f91; font-size: 13px; font-weight: 500;">(.*?)</span>',
        r'<span class="nav-sub-code" style="color: #a89f91; font-size: 13px; font-weight: 500;">\1</span>',
        content
    )

    # Remove previous mobile styles if present
    content = re.sub(r'<style id="mobile-responsive-quiz-styles">.*?</style>', '', content, flags=re.DOTALL)

    # Inject into head
    head_idx = content.find('</head>')
    if head_idx != -1:
        content = content[:head_idx] + mobile_quiz_css + "\n" + content[head_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Mobile-optimized: {file_path}")

targets = [
    "public/quizzes/netc311/module1.html",
    "public/quizzes/netc311/module2.html",
    "public/quizzes/hmby311/module1.html",
    "quizzes/netc311/module1.html",
    "quizzes/netc311/module2.html",
    "quizzes/hmby311/module1.html"
]

for t in targets:
    p = os.path.join(base_dir, t)
    if os.path.exists(p):
        patch_quiz_file(p)

print("All quiz players mobile-optimized successfully!")
