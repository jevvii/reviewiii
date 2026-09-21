import os
import re
import shutil

base_dir = "/home/javvii/YearIII/NETC311/quiz1"

# 1. Redesign index.html
minimalist_index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NETC311 Notebook — Introduction to Networks</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #f9f9fb;
      --surface: #ffffff;
      --text-main: #1f1f1f;
      --text-sub: #5e6266;
      --text-muted: #747775;
      --border: #e3e3e3;
      --border-subtle: #eeeff1;
      --blue-accent: #0b57d0;
      --blue-subtle: #e8f0fe;
      --radius-lg: 20px;
      --radius-md: 14px;
      --radius-pill: 9999px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Minimalist Top Nav */
    nav.top-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(249, 249, 251, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
      padding: 14px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--text-main);
      font-weight: 600;
      font-size: 0.95rem;
      letter-spacing: -0.01em;
    }

    .brand-icon {
      width: 22px;
      height: 22px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 6px;
      background: var(--blue-subtle);
      color: var(--blue-accent);
    }

    .brand-icon svg {
      width: 15px;
      height: 15px;
      fill: var(--blue-accent);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .nav-btn {
      font-size: 0.85rem;
      font-weight: 500;
      text-decoration: none;
      color: var(--text-sub);
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border);
      background: var(--surface);
      transition: all 0.15s ease;
    }

    .nav-btn:hover {
      color: var(--text-main);
      border-color: #c4c7c5;
      background: #f1f3f4;
    }

    /* Layout Container */
    .container {
      max-width: 860px;
      margin: 0 auto;
      padding: 3rem 1.5rem 4rem;
      width: 100%;
      flex: 1;
    }

    /* Hero Section */
    .hero {
      margin-bottom: 2.75rem;
    }

    .gemini-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 4px 12px;
      border-radius: var(--radius-pill);
      font-size: 0.8rem;
      font-weight: 500;
      color: var(--text-sub);
      margin-bottom: 1.25rem;
    }

    .gemini-sparkle {
      color: #7c3aed;
      font-size: 0.85rem;
    }

    h1.title {
      font-size: 2.25rem;
      font-weight: 700;
      letter-spacing: -0.025em;
      color: var(--text-main);
      margin-bottom: 0.6rem;
      line-height: 1.25;
    }

    p.subtitle {
      font-size: 1.05rem;
      color: var(--text-sub);
      max-width: 620px;
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .meta-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .pill {
      font-size: 0.8rem;
      font-weight: 500;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      background: rgba(0, 0, 0, 0.04);
      color: var(--text-sub);
    }

    /* Quizzes Section */
    .section-label {
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }

    .quiz-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 1.25rem;
      margin-bottom: 3rem;
    }

    .quiz-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
    }

    .quiz-card:hover {
      border-color: #c4c7c5;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
      transform: translateY(-2px);
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }

    .module-badge {
      font-size: 0.75rem;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 6px;
      background: var(--blue-subtle);
      color: var(--blue-accent);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .item-count {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .card-title {
      font-size: 1.2rem;
      font-weight: 600;
      color: var(--text-main);
      letter-spacing: -0.015em;
      margin-bottom: 0.5rem;
    }

    .card-desc {
      font-size: 0.88rem;
      color: var(--text-sub);
      line-height: 1.55;
      margin-bottom: 1.5rem;
    }

    .card-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .btn-primary {
      flex: 1;
      text-align: center;
      background: var(--text-main);
      color: #ffffff;
      font-size: 0.88rem;
      font-weight: 500;
      padding: 9px 16px;
      border-radius: var(--radius-pill);
      text-decoration: none;
      transition: background-color 0.15s ease;
    }

    .btn-primary:hover {
      background: #3c4043;
    }

    .btn-secondary {
      text-align: center;
      background: transparent;
      color: var(--text-sub);
      font-size: 0.88rem;
      font-weight: 500;
      padding: 8px 14px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border);
      text-decoration: none;
      transition: all 0.15s ease;
    }

    .btn-secondary:hover {
      color: var(--text-main);
      border-color: #c4c7c5;
      background: #f1f3f4;
    }

    /* Sources / Downloads Box */
    .sources-box {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
    }

    .sources-header {
      margin-bottom: 1.25rem;
    }

    .sources-header h3 {
      font-size: 1rem;
      font-weight: 600;
      color: var(--text-main);
      letter-spacing: -0.01em;
      margin-bottom: 0.25rem;
    }

    .sources-header p {
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    .source-list {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    .source-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 14px;
      background: #fafafc;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      flex-wrap: wrap;
      gap: 10px;
    }

    .source-info {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .source-icon {
      width: 28px;
      height: 28px;
      border-radius: 6px;
      background: #ffffff;
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
    }

    .source-name {
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--text-main);
    }

    .file-badges {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .file-badge {
      font-size: 0.75rem;
      font-weight: 500;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      text-decoration: none;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text-sub);
      transition: all 0.15s ease;
    }

    .file-badge:hover {
      border-color: #0b57d0;
      color: #0b57d0;
      background: var(--blue-subtle);
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border);
      padding: 1.75rem 1.5rem;
      text-align: center;
      font-size: 0.8rem;
      color: var(--text-muted);
      background: var(--surface);
      margin-top: auto;
    }

    footer a {
      color: var(--text-sub);
      text-decoration: none;
    }

    footer a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <!-- Minimalist Top Nav -->
  <nav class="top-nav">
    <a href="index.html" class="brand">
      <div class="brand-icon">
        <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
      </div>
      <span>NETC311 Notebook</span>
    </a>
    <div class="nav-actions">
      <a href="module1.html" class="nav-btn">Module 1 (99 Qs)</a>
      <a href="module2.html" class="nav-btn">Module 2 (104 Qs)</a>
    </div>
  </nav>

  <main class="container">
    <!-- Hero -->
    <section class="hero">
      <div class="gemini-pill">
        <span class="gemini-sparkle">✦</span>
        <span>NotebookLM Interactive Reviewer</span>
      </div>
      <h1 class="title">Introduction to Networks</h1>
      <p class="subtitle">An exhaustive study notebook of 203 identification quiz items across Cisco ITN Modules 1 and 2, featuring real-time rationales and instant feedback.</p>
      
      <div class="meta-pills">
        <span class="pill">203 Total Questions</span>
        <span class="pill">2 Modules</span>
        <span class="pill">Full Explanations & Hints</span>
        <span class="pill">Cisco CCNA v7.0</span>
      </div>
    </section>

    <!-- Quizzes Grid -->
    <div class="section-label">Interactive Quizzes</div>
    <div class="quiz-grid">
      
      <!-- Module 1 -->
      <div class="quiz-card">
        <div>
          <div class="card-header">
            <span class="module-badge">Module 1</span>
            <span class="item-count">99 Items</span>
          </div>
          <h2 class="card-title">Networking Today</h2>
          <p class="card-desc">Host roles, intermediary devices, network media, topologies, LAN vs WAN, internet connections, reliable networks (Fault Tolerance, Scalability, QoS, Security), and modern trends.</p>
        </div>
        <div class="card-actions">
          <a href="module1.html" class="btn-primary">Start Quiz &rarr;</a>
          <a href="https://notebooklm.google.com/notebook/a4a23950-074d-4120-bbb5-9a482941d5ba" target="_blank" class="btn-secondary">NotebookLM &nearr;</a>
        </div>
      </div>

      <!-- Module 2 -->
      <div class="quiz-card">
        <div>
          <div class="card-header">
            <span class="module-badge">Module 2</span>
            <span class="item-count">104 Items</span>
          </div>
          <h2 class="card-title">Switch & Device Configuration</h2>
          <p class="card-desc">Cisco IOS navigation, command modes (User EXEC, Privileged EXEC, Global Config), hotkeys, device naming, password security, banner MOTD, and SVI setup.</p>
        </div>
        <div class="card-actions">
          <a href="module2.html" class="btn-primary">Start Quiz &rarr;</a>
          <a href="https://notebooklm.google.com/notebook/0acd2de0-cfc6-4f3a-b38f-8e92376b906e" target="_blank" class="btn-secondary">NotebookLM &nearr;</a>
        </div>
      </div>

    </div>

    <!-- Offline Sources & Downloads -->
    <div class="section-label">Study Sources & Offline Reviewers</div>
    <div class="sources-box">
      <div class="sources-header">
        <h3>Curated Materials</h3>
        <p>Download printable question sheets, answer keys with explanations, or structured datasets.</p>
      </div>

      <div class="source-list">
        
        <div class="source-row">
          <div class="source-info">
            <div class="source-icon">M1</div>
            <div>
              <div class="source-name">Module 1 — Networking Today Reviewer</div>
            </div>
          </div>
          <div class="file-badges">
            <a href="downloads/Module 1 - Networking Today - Questionnaire.pdf" download class="file-badge">PDF</a>
            <a href="downloads/Module 1 - Networking Today - Questionnaire.docx" download class="file-badge">Word (.docx)</a>
            <a href="downloads/Module_1_NotebookLM_Quiz.json" download class="file-badge">JSON</a>
            <a href="downloads/Module_1_NotebookLM_Quiz.md" download class="file-badge">Markdown</a>
          </div>
        </div>

        <div class="source-row">
          <div class="source-info">
            <div class="source-icon">M2</div>
            <div>
              <div class="source-name">Module 2 — Basic Switch & Device Config Reviewer</div>
            </div>
          </div>
          <div class="file-badges">
            <a href="downloads/Module 2 - Basic Switch and End Device Configuration - Questionnaire.pdf" download class="file-badge">PDF</a>
            <a href="downloads/Module 2 - Basic Switch and End Device Configuration - Questionnaire.docx" download class="file-badge">Word (.docx)</a>
            <a href="downloads/Module_2_NotebookLM_Quiz.json" download class="file-badge">JSON</a>
            <a href="downloads/Module_2_NotebookLM_Quiz.md" download class="file-badge">Markdown</a>
          </div>
        </div>

      </div>
    </div>
  </main>

  <footer>
    <p>NETC311: Introduction to Networks v7.0 (ITN) &bull; Academic Review Hub &bull; Powered by NotebookLM</p>
  </footer>

</body>
</html>
"""

# 2. Minimalist Google NotebookLM Top Navbar for module1.html and module2.html
def get_minimalist_navbar(active_mod):
    is_m1 = (active_mod == 1)
    is_m2 = (active_mod == 2)
    
    m1_style = "color: #0b57d0; background: #e8f0fe; text-decoration: none; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 9999px; border: 1px solid #d3e3fd;" if is_m1 else "color: #444746; background: transparent; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 9999px; border: 1px solid #e3e3e3; transition: all 0.15s ease;"
    m2_style = "color: #0b57d0; background: #e8f0fe; text-decoration: none; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 9999px; border: 1px solid #d3e3fd;" if is_m2 else "color: #444746; background: transparent; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 9999px; border: 1px solid #e3e3e3; transition: all 0.15s ease;"
    
    switch_btn = f'<a href="module2.html" style="color: #1f1f1f; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 9999px; background: #f0f4f9; display: flex; align-items: center; gap: 4px; border: 1px solid #e1e3e1; transition: all 0.15s ease;">Module 2 &rarr;</a>' if is_m1 else f'<a href="module1.html" style="color: #1f1f1f; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 9999px; background: #f0f4f9; display: flex; align-items: center; gap: 4px; border: 1px solid #e1e3e1; transition: all 0.15s ease;">&larr; Module 1</a>'
    
    current_title = "Module 1: Networking Today (99 Qs)" if is_m1 else "Module 2: Basic Switch & End Device Config (104 Qs)"

    return f"""
    <!-- Minimalist NotebookLM Top Nav -->
    <header id="quiz-hub-nav" style="position: sticky; top: 0; left: 0; right: 0; z-index: 999999; background: rgba(255, 255, 255, 0.94); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-bottom: 1px solid #e3e3e3; padding: 10px 24px; display: flex; align-items: center; justify-content: space-between; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
      <div style="display: flex; align-items: center; gap: 12px;">
        <a href="index.html" style="color: #1f1f1f; text-decoration: none; font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 8px;">
          <div style="width: 22px; height: 22px; border-radius: 6px; background: #e8f0fe; display: flex; align-items: center; justify-content: center;">
            <svg style="width: 14px; height: 14px; fill: #0b57d0;" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
          </div>
          <span style="letter-spacing: -0.01em;">NETC311 Notebook</span>
        </a>
        <span style="color: #c4c7c5; font-size: 13px;">/</span>
        <span style="color: #5e6266; font-size: 13px; font-weight: 500;">{current_title}</span>
      </div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <a href="index.html" style="color: #444746; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 12px; border-radius: 9999px; border: 1px solid #e3e3e3; background: #ffffff; transition: all 0.15s ease;">Overview</a>
        <a href="module1.html" style="{m1_style}">Module 1 (99 Qs)</a>
        <a href="module2.html" style="{m2_style}">Module 2 (104 Qs)</a>
        {switch_btn}
      </div>
    </header>
    """

def update_quiz_html(file_path, active_mod):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any existing nav header
    content = re.sub(r'<!-- (?:Navigation Bar|Minimalist NotebookLM Top Nav) -->.*?</header>', '', content, flags=re.DOTALL)
    
    nav = get_minimalist_navbar(active_mod)
    body_idx = content.find('<body>')
    new_content = content[:body_idx + 6] + "\n" + nav + "\n" + content[body_idx + 6:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_path}")

# Update raw quiz files
m1_src = os.path.join(base_dir, "Module_1_NotebookLM_Quiz.html")
m2_src = os.path.join(base_dir, "Module_2_NotebookLM_Quiz.html")
update_quiz_html(m1_src, 1)
update_quiz_html(m2_src, 2)

# Write index.html in root, public/, and docs/
for target in [os.path.join(base_dir, "index.html"), os.path.join(base_dir, "public", "index.html"), os.path.join(base_dir, "docs", "index.html")]:
    with open(target, 'w', encoding='utf-8') as f:
        f.write(minimalist_index_html)
    print(f"Wrote minimalist index to {target}")

# Sync module1.html and module2.html across root, public, and docs
for folder in [base_dir, os.path.join(base_dir, "public"), os.path.join(base_dir, "docs")]:
    shutil.copy2(m1_src, os.path.join(folder, "module1.html"))
    shutil.copy2(m2_src, os.path.join(folder, "module2.html"))
    print(f"Synced module files to {folder}")

print("Minimalist Gemini Notebook theme applied across all files!")
