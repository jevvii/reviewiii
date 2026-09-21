import subprocess
import re
import os

base_dir = "/home/javvii/YearIII/NETC311/quiz1"

pitch_black_theme_css = """
<style id="custom-pitch-black-theme">
  :root, html, body {
    color-scheme: dark !important;
    background-color: #000000 !important;
    color: #f0f0f0 !important;
    
    /* Digital Sobriety Palette */
    --color-bg-base: #000000 !important;
    --color-bg-surface: #0a0a0a !important;
    --color-bg-surface-elevated: #141414 !important;
    --color-accent-primary: #8a9a86 !important;
    --color-accent-secondary: #a89f91 !important;
    --color-text-main: #f0f0f0 !important;
    --color-text-muted: #a0a0a0 !important;
    
    /* NotebookLM UI Custom Property Overrides */
    --surface-color: #000000 !important;
    --surface-variant-color: #0a0a0a !important;
    --primary-text-color: #f0f0f0 !important;
    --body-text-color: #a0a0a0 !important;
    --answer-btn-background: #0a0a0a !important;
    --answer-text-color: #f0f0f0 !important;
    --secondary-button-border-color: rgba(255, 255, 255, 0.12) !important;
    --button-hover-color: #141414 !important;
    --hint-btn-background: #141414 !important;
    --hint-btn-color: #8a9a86 !important;
    --hint-container-background: #0a0a0a !important;
    --stat-card-background-color: #0a0a0a !important;
    --stat-card-color: #f0f0f0 !important;
    --topics-background: #0a0a0a !important;
    --score-summary-background-color: #0a0a0a !important;
    --score-summary-got-it-color: #8a9a86 !important;
    --score-summary-missed-it-color: #272e4d !important;
    --score-summary-progress-bar-background-color: #141414 !important;
    --follow-up-chip-selected-background: #141414 !important;
    --follow-up-chip-hover-background: #1a1a1a !important;
    --follow-up-chip-background: #0a0a0a !important;
    --generate-button-background: #8a9a86 !important;
    --generate-button-hover-background: #9ab096 !important;
    --feedback-correct-background-color: #0d1a10 !important;
    --feedback-correct-border-color: #8a9a86 !important;
    --feedback-correct-text-color: #8a9a86 !important;
    --feedback-incorrect-background-color: #1a0a0a !important;
    --feedback-incorrect-border-color: #b3261e !important;
    --feedback-incorrect-text-color: #f2b8b5 !important;
    --feedback-rationale-text-color: #a0a0a0 !important;
    --feedback-primary-text-color: #f0f0f0 !important;
    --correct-color: #8a9a86 !important;
    --not-correct-color: #a0a0a0 !important;
    --nlm-fills-surface-page: #000000 !important;
    --nlm-fills-surface-page-grey: #000000 !important;
    --nlm-fills-surface-card: #0a0a0a !important;
    --nlm-fills-surface-panel: #0a0a0a !important;
    --nlm-fills-surface-landing: #000000 !important;
    --nlm-fills-ui-light-grey-fill: #000000 !important;
    --nlm-fills-ui-grey-fill: #141414 !important;
    --nlm-fills-ui-blue-fill: #0e1217 !important;
    --nlm-stroke-default: rgba(255, 255, 255, 0.08) !important;
    --nlm-text-titles-and-labels: #f0f0f0 !important;
    --nlm-text-body-text: #e0e0e0 !important;
    --nlm-text-secondary-text: #a0a0a0 !important;
    --nlm-text-ghost-text: #707070 !important;
    --mat-sys-surface: #0a0a0a !important;
    --mat-sys-background: #000000 !important;
    --mat-sys-on-surface: #f0f0f0 !important;
    --mat-sys-on-background: #f0f0f0 !important;
  }

  html, body, app-root, .app-root, .app-container {
    background-color: #000000 !important;
    color: #f0f0f0 !important;
  }

  /* Choices / answer buttons */
  .answer-option-button, button[class*="answer"], .choice-button, .mat-mdc-button-base {
    background-color: #0a0a0a !important;
    color: #f0f0f0 !important;
    border-color: rgba(255, 255, 255, 0.1) !important;
  }

  /* Next / Submit buttons */
  .navigation-buttons-container .next-btn,
  .navigation-buttons-container-mobile .next-btn {
    background: #8a9a86 !important;
    border: none !important;
    color: #000000 !important;
    font-weight: 600 !important;
    border-radius: 4px !important;
  }

  .navigation-buttons-container .back-btn,
  .navigation-buttons-container .secondary-button,
  .secondary-button {
    background: transparent !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: #a0a0a0 !important;
    border-radius: 4px !important;
  }
</style>
"""

def get_navbar(active_mod):
    is_m1 = (active_mod == 1)
    is_m2 = (active_mod == 2)
    m1_style = "color: #000000; background: #8a9a86; text-decoration: none; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 4px;" if is_m1 else "color: #a0a0a0; background: transparent; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s;"
    m2_style = "color: #000000; background: #8a9a86; text-decoration: none; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 4px;" if is_m2 else "color: #a0a0a0; background: transparent; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s;"
    switch_btn = f'<a href="module2.html" style="color: #8a9a86; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; background: rgba(138, 154, 134, 0.1); border: 1px solid rgba(138, 154, 134, 0.35); display: flex; align-items: center; gap: 4px; transition: all 0.2s;">Module 2 &rarr;</a>' if is_m1 else f'<a href="module1.html" style="color: #8a9a86; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; background: rgba(138, 154, 134, 0.1); border: 1px solid rgba(138, 154, 134, 0.35); display: flex; align-items: center; gap: 4px; transition: all 0.2s;">&larr; Module 1</a>'
    current_title = "Module 1: Networking Today (99 Qs)" if is_m1 else "Module 2: Basic Switch & End Device Config (104 Qs)"

    return f"""
    <!-- Pitch Black Top Nav -->
    <header id="quiz-hub-nav" style="position: sticky; top: 0; left: 0; right: 0; z-index: 999999; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding: 12px 28px; display: flex; align-items: center; justify-content: space-between; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
      <div style="display: flex; align-items: center; gap: 12px;">
        <a href="index.html" style="color: #f0f0f0; text-decoration: none; font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 8px;">
          <span style="color: #8a9a86; font-size: 15px;">✦</span>
          <span style="color: #8a9a86; letter-spacing: -0.01em;">NETC311</span>
          <span style="color: #f0f0f0;">Notebook</span>
        </a>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a0a0a0; font-size: 13px; font-weight: 400;">{current_title}</span>
      </div>
      <div style="display: flex; align-items: center; gap: 10px;">
        <a href="index.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">Overview</a>
        <a href="module1.html" style="{m1_style}">Module 1 (99 Qs)</a>
        <a href="module2.html" style="{m2_style}">Module 2 (104 Qs)</a>
        {switch_btn}
      </div>
    </header>
    """

loading_animation_html = """
<!-- Minimal Non-Blocking Loading Animation -->
<div id="quiz-loader" style="position: fixed; inset: 0; top: 52px; background: #000000; display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 99998; transition: opacity 0.35s ease, visibility 0.35s ease;">
  <div style="width: 32px; height: 32px; border: 2px solid rgba(138, 154, 134, 0.15); border-top-color: #8a9a86; border-radius: 50%; animation: quiz-spin 0.75s linear infinite;"></div>
  <div style="margin-top: 16px; font-size: 13px; color: #a0a0a0; font-family: 'Inter', -apple-system, sans-serif; letter-spacing: 0.03em;">Loading Notebook Quiz...</div>
</div>
<style>
  @keyframes quiz-spin { to { transform: rotate(360deg); } }
</style>
<script>
  (function() {
    function dismissLoader() {
      var loader = document.getElementById('quiz-loader');
      if (loader && loader.style.visibility !== 'hidden') {
        loader.style.opacity = '0';
        loader.style.visibility = 'hidden';
        setTimeout(function() { if (loader && loader.parentNode) loader.parentNode.removeChild(loader); }, 400);
      }
    }
    // Poll for Angular app-root content rendering
    var timer = setInterval(function() {
      var root = document.querySelector('app-root');
      if (root && root.children && root.children.length > 0) {
        clearInterval(timer);
        dismissLoader();
      }
    }, 40);
    // Fallback safety dismissal
    setTimeout(function() {
      clearInterval(timer);
      dismissLoader();
    }, 3500);
  })();
</script>
"""

def rebuild(git_path, output_filename, active_mod):
    raw = subprocess.check_output(['git', 'show', f'cdd074c:{git_path}']).decode('utf-8')
    
    # 1. REMOVE the restrictive Content-Security-Policy meta tag
    raw = re.sub(r'<meta\s+http-equiv=["\']Content-Security-Policy["\'][^>]*>', '', raw, flags=re.IGNORECASE)
    
    # 2. Inject pitch black theme CSS into </head>
    head_idx = raw.find('</head>')
    raw = raw[:head_idx] + pitch_black_theme_css + "\n" + raw[head_idx:]
    
    # 3. Inject Navbar and Loading animation right after <body>
    body_idx = raw.find('<body>')
    nav = get_navbar(active_mod)
    raw = raw[:body_idx + 6] + "\n" + nav + "\n" + loading_animation_html + "\n" + raw[body_idx + 6:]
    
    # Write to local file
    out_path = os.path.join(base_dir, output_filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(raw)
    print(f"Rebuilt {output_filename} successfully (CSP removed, theme & loader injected)")

rebuild("public/module1.html", "Module_1_NotebookLM_Quiz.html", 1)
rebuild("public/module2.html", "Module_2_NotebookLM_Quiz.html", 2)
