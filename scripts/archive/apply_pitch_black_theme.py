import os
import re
import shutil

base_dir = "/home/javvii/YearIII/NETC311/quiz1"

pitch_black_index_html = """<!DOCTYPE html>
<html lang="en" class="dark-theme">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NETC311 Notebook — Introduction to Networks</title>
  
  <!-- Font Preloading -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    /* =========================================
       Pitch Black Digital Sobriety Theme
       Inspired by jevvii-portfolio.vercel.app
       ========================================= */
    :root {
      /* OLED Blacks */
      --color-bg-base: #000000;
      --color-bg-surface: #0a0a0a;
      --color-bg-surface-elevated: #141414;
      
      /* Earthy Muted Accents */
      --color-accent-primary: #8a9a86;   /* Sage Green */
      --color-accent-secondary: #a89f91; /* Soft Clay */
      --color-focus: #b2c2ae;
      
      /* Text Colors */
      --color-text-main: #f0f0f0;
      --color-text-muted: #a0a0a0;
      --color-text-subtle: #707070;
      --color-text-inverse: #000000;

      /* Borders */
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-medium: rgba(255, 255, 255, 0.16);
      --border-accent: rgba(138, 154, 134, 0.35);

      --radius-sm: 4px;
      --radius-md: 8px;
      --radius-lg: 14px;
      --radius-pill: 9999px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      background-color: var(--color-bg-base);
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--color-bg-base);
      color: var(--color-text-main);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Fixed Glassmorphism Header */
    header.site-header {
      position: sticky;
      top: 0;
      width: 100%;
      z-index: 100;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 14px 28px;
    }

    nav.nav-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      max-width: 960px;
      margin: 0 auto;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--color-text-main);
      font-weight: 600;
      font-size: 0.95rem;
      letter-spacing: -0.01em;
    }

    .brand-sparkle {
      color: var(--color-accent-primary);
      font-size: 1rem;
    }

    .brand-title {
      color: var(--color-accent-primary);
      font-weight: 600;
    }

    .brand-sub {
      color: var(--color-text-muted);
      font-weight: 400;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .nav-link {
      color: var(--color-text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 500;
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      background: transparent;
      transition: all 0.2s ease;
    }

    .nav-link:hover {
      color: var(--color-text-main);
      border-color: var(--border-medium);
      background: rgba(255, 255, 255, 0.04);
    }

    /* Container */
    main.container {
      max-width: 960px;
      margin: 0 auto;
      padding: 3.5rem 1.5rem 5rem;
      width: 100%;
      flex: 1;
    }

    /* Hero Section */
    .hero {
      margin-bottom: 3.5rem;
    }

    .tagline {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.82rem;
      font-weight: 500;
      color: var(--color-accent-primary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1rem;
    }

    h1.title {
      font-size: clamp(2.2rem, 5vw, 3.2rem);
      font-weight: 200;
      letter-spacing: -0.03em;
      color: var(--color-text-main);
      line-height: 1.15;
      margin-bottom: 0.85rem;
    }

    .subtitle {
      font-size: 1.1rem;
      font-weight: 400;
      color: var(--color-accent-secondary);
      margin-bottom: 1.25rem;
    }

    .bio {
      font-size: 0.95rem;
      color: var(--color-text-muted);
      max-width: 680px;
      line-height: 1.7;
      margin-bottom: 1.75rem;
    }

    .meta-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .meta-pill {
      font-size: 0.78rem;
      font-weight: 400;
      color: var(--color-text-muted);
      background: var(--color-bg-surface);
      border: 1px solid var(--border-subtle);
      padding: 4px 12px;
      border-radius: var(--radius-sm);
    }

    .meta-pill strong {
      color: var(--color-accent-primary);
      font-weight: 500;
    }

    /* Section Headers */
    .section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 0.75rem;
    }

    .section-title {
      font-size: 0.85rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--color-accent-secondary);
    }

    /* Quiz Cards */
    .quiz-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 1.5rem;
      margin-bottom: 3.5rem;
    }

    .quiz-card {
      background: var(--color-bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.85rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .quiz-card:hover {
      border-color: var(--color-accent-primary);
      background: var(--color-bg-surface-elevated);
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(138, 154, 134, 0.1);
    }

    .card-top {
      margin-bottom: 1.75rem;
    }

    .card-badge-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }

    .card-badge {
      font-size: 0.72rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--color-accent-primary);
      background: rgba(138, 154, 134, 0.1);
      border: 1px solid rgba(138, 154, 134, 0.25);
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }

    .card-count {
      font-size: 0.8rem;
      color: var(--color-text-subtle);
    }

    .card-title {
      font-size: 1.35rem;
      font-weight: 400;
      color: var(--color-text-main);
      letter-spacing: -0.02em;
      margin-bottom: 0.75rem;
    }

    .card-desc {
      font-size: 0.88rem;
      color: var(--color-text-muted);
      line-height: 1.6;
    }

    .card-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn-primary {
      flex: 1;
      text-align: center;
      background-color: var(--color-accent-primary);
      color: var(--color-text-inverse);
      font-weight: 600;
      font-size: 0.88rem;
      padding: 10px 18px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      border: none;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .btn-primary:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 14px rgba(138, 154, 134, 0.3);
      filter: brightness(1.08);
    }

    .btn-secondary {
      text-align: center;
      background: transparent;
      color: var(--color-text-main);
      font-weight: 500;
      font-size: 0.88rem;
      padding: 9px 16px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-medium);
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .btn-secondary:hover {
      border-color: var(--color-accent-primary);
      color: var(--color-accent-primary);
      background: rgba(138, 154, 134, 0.06);
    }

    /* Sources Section */
    .sources-box {
      background: var(--color-bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.75rem;
    }

    .sources-desc {
      font-size: 0.88rem;
      color: var(--color-text-muted);
      margin-bottom: 1.25rem;
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
      padding: 12px 16px;
      background: #000000;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      flex-wrap: wrap;
      gap: 12px;
      transition: border-color 0.2s ease;
    }

    .source-row:hover {
      border-color: var(--border-medium);
    }

    .source-info {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .source-tag {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--color-accent-primary);
      background: rgba(138, 154, 134, 0.1);
      border: 1px solid rgba(138, 154, 134, 0.2);
      padding: 4px 8px;
      border-radius: var(--radius-sm);
    }

    .source-name {
      font-size: 0.9rem;
      font-weight: 400;
      color: var(--color-text-main);
    }

    .file-badges {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .file-badge {
      font-size: 0.75rem;
      font-weight: 500;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      border: 1px solid var(--border-subtle);
      background: var(--color-bg-surface);
      color: var(--color-text-muted);
      transition: all 0.15s ease;
    }

    .file-badge:hover {
      color: var(--color-text-main);
      border-color: var(--color-accent-primary);
      background: rgba(138, 154, 134, 0.1);
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border-subtle);
      padding: 2rem 1.5rem;
      text-align: center;
      font-size: 0.8rem;
      color: var(--color-text-subtle);
      background: #000000;
      margin-top: auto;
    }

    footer a {
      color: var(--color-accent-primary);
      text-decoration: none;
    }

    footer a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <!-- Pitch Black Header -->
  <header class="site-header">
    <nav class="nav-bar">
      <a href="index.html" class="brand">
        <span class="brand-sparkle">✦</span>
        <span class="brand-title">NETC311</span>
        <span class="brand-sub">Notebook</span>
      </a>
      <div class="nav-links">
        <a href="module1.html" class="nav-link">Module 1 (99 Qs)</a>
        <a href="module2.html" class="nav-link">Module 2 (104 Qs)</a>
      </div>
    </nav>
  </header>

  <main class="container">
    <!-- Hero Section -->
    <section class="hero">
      <div class="tagline">✦ NotebookLM Interactive Reviewer</div>
      <h1 class="title">Introduction to Networks</h1>
      <div class="subtitle">NETC311 &bull; Cisco CCNA v7.0 (ITN)</div>
      <p class="bio">
        A focused digital study notebook containing 203 comprehensive identification questions extracted directly from Modules 1 & 2. Complete with instant AI rationales, hints, and curriculum references.
      </p>
      <div class="meta-strip">
        <span class="meta-pill"><strong>203</strong> Total Items</span>
        <span class="meta-pill"><strong>2</strong> Modules</span>
        <span class="meta-pill"><strong>100%</strong> Explanations</span>
        <span class="meta-pill">Instant Feedback</span>
      </div>
    </section>

    <!-- Quizzes Grid -->
    <div class="section-header">
      <span class="section-title">Interactive Quizzes</span>
    </div>
    
    <div class="quiz-grid">
      
      <!-- Module 1 -->
      <div class="quiz-card">
        <div class="card-top">
          <div class="card-badge-row">
            <span class="card-badge">Module 1</span>
            <span class="card-count">99 Items</span>
          </div>
          <h2 class="card-title">Networking Today</h2>
          <p class="card-desc">
            Host roles, peer-to-peer networks, intermediary devices, transmission media, topologies, LAN vs WAN, reliable networks (Fault Tolerance, Scalability, QoS, Security), and modern networking trends.
          </p>
        </div>
        <div class="card-actions">
          <a href="module1.html" class="btn-primary">Start Quiz &rarr;</a>
          <a href="https://notebooklm.google.com/notebook/a4a23950-074d-4120-bbb5-9a482941d5ba" target="_blank" class="btn-secondary">NotebookLM &nearr;</a>
        </div>
      </div>

      <!-- Module 2 -->
      <div class="quiz-card">
        <div class="card-top">
          <div class="card-badge-row">
            <span class="card-badge">Module 2</span>
            <span class="card-count">104 Items</span>
          </div>
          <h2 class="card-title">Basic Switch & Device Configuration</h2>
          <p class="card-desc">
            Cisco IOS navigation, command modes (User EXEC, Privileged EXEC, Global Config), CLI shortcuts, device naming, password security, banner MOTD, and SVI IP configuration.
          </p>
        </div>
        <div class="card-actions">
          <a href="module2.html" class="btn-primary">Start Quiz &rarr;</a>
          <a href="https://notebooklm.google.com/notebook/0acd2de0-cfc6-4f3a-b38f-8e92376b906e" target="_blank" class="btn-secondary">NotebookLM &nearr;</a>
        </div>
      </div>

    </div>

    <!-- Sources Section -->
    <div class="section-header">
      <span class="section-title">Notebook Sources & Downloads</span>
    </div>

    <div class="sources-box">
      <p class="sources-desc">
        Download the offline questionnaires, answer keys with explanations, and structured datasets.
      </p>

      <div class="source-list">
        
        <div class="source-row">
          <div class="source-info">
            <span class="source-tag">M1</span>
            <span class="source-name">Module 1 — Networking Today Reviewer</span>
          </div>
          <div class="file-badges">
            <a href="downloads/Module 1 - Networking Today - Questionnaire.pdf" download class="file-badge">PDF</a>
            <a href="downloads/Module 1 - Networking Today - Questionnaire.docx" download class="file-badge">DOCX</a>
            <a href="downloads/Module_1_NotebookLM_Quiz.json" download class="file-badge">JSON</a>
            <a href="downloads/Module_1_NotebookLM_Quiz.md" download class="file-badge">Markdown</a>
          </div>
        </div>

        <div class="source-row">
          <div class="source-info">
            <span class="source-tag">M2</span>
            <span class="source-name">Module 2 — Basic Switch & Device Config Reviewer</span>
          </div>
          <div class="file-badges">
            <a href="downloads/Module 2 - Basic Switch and End Device Configuration - Questionnaire.pdf" download class="file-badge">PDF</a>
            <a href="downloads/Module 2 - Basic Switch and End Device Configuration - Questionnaire.docx" download class="file-badge">DOCX</a>
            <a href="downloads/Module_2_NotebookLM_Quiz.json" download class="file-badge">JSON</a>
            <a href="downloads/Module_2_NotebookLM_Quiz.md" download class="file-badge">Markdown</a>
          </div>
        </div>

      </div>
    </div>

  </main>

  <footer>
    <p>NETC311 &bull; Cisco Networking Academy &bull; University Quiz & Review Hub &bull; Powered by NotebookLM</p>
  </footer>

</body>
</html>
"""

# 2. Pitch Black Top Nav for module1.html and module2.html
def get_pitch_black_navbar(active_mod):
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

# 3. Custom CSS Overrides to make the NotebookLM Quiz Player match the OLED pitch black theme
pitch_black_quiz_css = """
<style id="custom-pitch-black-theme">
  :root, html.dark-theme, body.dark-theme {
    color-scheme: dark !important;
    background-color: #000000 !important;
    color: #f0f0f0 !important;
    --color-bg-base: #000000 !important;
    --color-bg-surface: #0a0a0a !important;
    --color-bg-surface-elevated: #141414 !important;
    --color-accent-primary: #8a9a86 !important;
    --color-accent-secondary: #a89f91 !important;
    
    /* NotebookLM UI Overrides */
    --nlm-fills-surface-page: #000000 !important;
    --nlm-fills-surface-page-grey: #000000 !important;
    --nlm-fills-surface-card: #0a0a0a !important;
    --nlm-fills-surface-panel: #0a0a0a !important;
    --nlm-fills-surface-landing: #000000 !important;
    --nlm-fills-ui-light-grey-fill: #000000 !important;
    --nlm-fills-ui-grey-fill: #111111 !important;
    --nlm-fills-ui-blue-fill: #0d1217 !important;
    --nlm-stroke-default: rgba(255, 255, 255, 0.08) !important;
    --nlm-text-titles-and-labels: #f0f0f0 !important;
    --nlm-text-body-text: #e0e0e0 !important;
    --nlm-text-secondary-text: #a0a0a0 !important;
    --nlm-text-ghost-text: #707070 !important;
    --mat-sys-surface: #0a0a0a !important;
    --mat-sys-background: #000000 !important;
    --mat-sys-on-surface: #f0f0f0 !important;
    --mat-sys-on-background: #f0f0f0 !important;
    --surface-color: #000000 !important;
    --surface-variant-color: #0a0a0a !important;
  }

  html, body, app-root, .app-root {
    background-color: #000000 !important;
    color: #f0f0f0 !important;
  }

  /* Force OLED pitch black on quiz background containers */
  main, .quiz-container, .question-container, .card, .mat-card {
    background-color: #0a0a0a !important;
    border-color: rgba(255, 255, 255, 0.08) !important;
  }
</style>
"""

def update_quiz_html(file_path, active_mod):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Ensure <html lang="en" dir="ltr" class="dark-theme">
    content = re.sub(r'<html([^>]*)>', r'<html\1 class="dark-theme">', content)
    # Deduplicate class if repeated
    content = content.replace('class="dark-theme" class="dark-theme"', 'class="dark-theme"')
    
    # 2. Ensure <body class="dark-theme">
    content = re.sub(r'<body([^>]*)>', r'<body class="dark-theme">', content)
    
    # 3. Remove any previous custom styles or navbars
    content = re.sub(r'<style id="custom-pitch-black-theme">.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- (?:Navigation Bar|Minimalist NotebookLM Top Nav|Pitch Black Top Nav) -->.*?</header>', '', content, flags=re.DOTALL)
    
    # 4. Inject pitch_black_quiz_css before </head>
    head_idx = content.find('</head>')
    if head_idx != -1:
        content = content[:head_idx] + pitch_black_quiz_css + "\n" + content[head_idx:]
    
    # 5. Inject nav right after <body>
    nav = get_pitch_black_navbar(active_mod)
    body_idx = content.find('<body class="dark-theme">')
    if body_idx == -1:
        body_idx = content.find('<body>')
    
    tag_end = content.find('>', body_idx) + 1
    content = content[:tag_end] + "\n" + nav + "\n" + content[tag_end:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Applied Pitch Black theme to {file_path}")

# Update raw quiz files
m1_src = os.path.join(base_dir, "Module_1_NotebookLM_Quiz.html")
m2_src = os.path.join(base_dir, "Module_2_NotebookLM_Quiz.html")
update_quiz_html(m1_src, 1)
update_quiz_html(m2_src, 2)

# Write index.html in root, public/, and docs/
for target in [os.path.join(base_dir, "index.html"), os.path.join(base_dir, "public", "index.html"), os.path.join(base_dir, "docs", "index.html")]:
    with open(target, 'w', encoding='utf-8') as f:
        f.write(pitch_black_index_html)
    print(f"Wrote pitch black index to {target}")

# Sync module files across root, public, and docs
for folder in [base_dir, os.path.join(base_dir, "public"), os.path.join(base_dir, "docs")]:
    shutil.copy2(m1_src, os.path.join(folder, "module1.html"))
    shutil.copy2(m2_src, os.path.join(folder, "module2.html"))
    print(f"Synced module files to {folder}")

print("Pitch Black theme successfully applied across entire site!")
