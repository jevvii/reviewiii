import re
import os
import shutil

base_dir = "/home/javvii/YearIII/NETC311/quiz1"

def create_nav_html(active_module):
    is_m1 = (active_module == 1)
    is_m2 = (active_module == 2)
    
    m1_style = "color: #ffffff; background: #0284c7; text-decoration: none; font-size: 13px; font-weight: 600; padding: 7px 14px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);" if is_m1 else "color: #cbd5e1; background: rgba(255,255,255,0.08); text-decoration: none; font-size: 13px; font-weight: 600; padding: 7px 14px; border-radius: 6px; transition: all 0.2s;"
    m2_style = "color: #ffffff; background: #0284c7; text-decoration: none; font-size: 13px; font-weight: 600; padding: 7px 14px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);" if is_m2 else "color: #cbd5e1; background: rgba(255,255,255,0.08); text-decoration: none; font-size: 13px; font-weight: 600; padding: 7px 14px; border-radius: 6px; transition: all 0.2s;"
    
    current_title = "Module 1: Networking Today (99 Questions)" if is_m1 else "Module 2: Basic Switch & End Device Config (104 Questions)"
    
    # Next module quick link button
    switch_btn = f'<a href="module2.html" style="color: #38bdf8; text-decoration: none; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 4px; padding: 6px 12px; background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 6px;">Next: Module 2 &rarr;</a>' if is_m1 else f'<a href="module1.html" style="color: #38bdf8; text-decoration: none; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 4px; padding: 6px 12px; background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 6px;">&larr; Switch: Module 1</a>'

    nav = f"""
    <!-- Navigation Bar -->
    <header id="quiz-hub-nav" style="position: sticky; top: 0; left: 0; right: 0; z-index: 999999; background: #00334e; border-bottom: 2px solid #00b4d8; padding: 10px 24px; display: flex; align-items: center; justify-content: space-between; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; box-shadow: 0 4px 12px rgba(0,0,0,0.18);">
      <div style="display: flex; align-items: center; gap: 14px;">
        <a href="index.html" style="color: #ffffff; text-decoration: none; font-weight: 700; font-size: 15px; display: flex; align-items: center; gap: 8px;">
          <svg style="width: 20px; height: 20px; fill: #38bdf8;" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
          <span style="letter-spacing: -0.01em;">NETC311 Quiz Hub</span>
        </a>
        <span style="color: #475569; font-size: 14px;">|</span>
        <span style="color: #94a3b8; font-size: 13px; font-weight: 500;">{current_title}</span>
      </div>
      <div style="display: flex; align-items: center; gap: 10px;">
        <a href="index.html" style="color: #e2e8f0; text-decoration: none; font-size: 13px; font-weight: 600; padding: 7px 12px; border-radius: 6px; background: rgba(255,255,255,0.08); transition: all 0.2s;">🏠 Hub Home</a>
        <a href="module1.html" style="{m1_style}">Module 1 (99 Qs)</a>
        <a href="module2.html" style="{m2_style}">Module 2 (104 Qs)</a>
        {switch_btn}
      </div>
    </header>
    """
    return nav

def inject_nav_into_html(file_path, active_module):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing nav if present
    content = re.sub(r'<!-- Navigation Bar -->.*?</header>', '', content, flags=re.DOTALL)
    
    nav_html = create_nav_html(active_module)
    
    # Insert after <body>
    body_idx = content.find('<body>')
    if body_idx == -1:
        raise ValueError(f"No <body> found in {file_path}")
    
    new_content = content[:body_idx + 6] + "\n" + nav_html + "\n" + content[body_idx + 6:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Injected nav into {file_path}")

inject_nav_into_html(os.path.join(base_dir, "Module_1_NotebookLM_Quiz.html"), 1)
inject_nav_into_html(os.path.join(base_dir, "Module_2_NotebookLM_Quiz.html"), 2)
