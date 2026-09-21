import os
import shutil
import re

base_dir = "/home/javvii/YearIII/NETC311/quiz1"

# 1. Update public/index.html with top navbar
index_path = os.path.join(base_dir, "public", "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    idx_content = f.read()

navbar_hub = """
  <!-- Top Navigation Bar -->
  <nav id="hub-nav" style="background: #002235; border-bottom: 1px solid rgba(255,255,255,0.1); padding: 12px 24px; display: flex; align-items: center; justify-content: space-between; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; position: sticky; top: 0; z-index: 10000; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
    <div style="display: flex; align-items: center; gap: 10px;">
      <a href="index.html" style="color: #ffffff; text-decoration: none; font-weight: 700; font-size: 15px; display: flex; align-items: center; gap: 8px;">
        <svg style="width: 20px; height: 20px; fill: #38bdf8;" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
        <span style="letter-spacing: -0.01em;">NETC311 Quiz Hub</span>
      </a>
    </div>
    <div style="display: flex; align-items: center; gap: 12px;">
      <a href="module1.html" style="color: #38bdf8; background: rgba(56,189,248,0.12); border: 1px solid rgba(56,189,248,0.3); text-decoration: none; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 6px; transition: all 0.2s;">Module 1 (99 Qs) &rarr;</a>
      <a href="module2.html" style="color: #38bdf8; background: rgba(56,189,248,0.12); border: 1px solid rgba(56,189,248,0.3); text-decoration: none; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 6px; transition: all 0.2s;">Module 2 (104 Qs) &rarr;</a>
    </div>
  </nav>
"""

if 'id="hub-nav"' not in idx_content:
    body_idx = idx_content.find('<body>')
    idx_content = idx_content[:body_idx + 6] + "\n" + navbar_hub + "\n" + idx_content[body_idx + 6:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(idx_content)
    print("Added navbar to public/index.html")

# 2. Sync to root and docs/
m1_src = os.path.join(base_dir, "Module_1_NotebookLM_Quiz.html")
m2_src = os.path.join(base_dir, "Module_2_NotebookLM_Quiz.html")

# Copy quizzes to public/
shutil.copy2(m1_src, os.path.join(base_dir, "public", "module1.html"))
shutil.copy2(m2_src, os.path.join(base_dir, "public", "module2.html"))

# Copy quizzes and index to root /
shutil.copy2(m1_src, os.path.join(base_dir, "module1.html"))
shutil.copy2(m2_src, os.path.join(base_dir, "module2.html"))
shutil.copy2(index_path, os.path.join(base_dir, "index.html"))

# Copy to docs/
os.makedirs(os.path.join(base_dir, "docs"), exist_ok=True)
shutil.copy2(m1_src, os.path.join(base_dir, "docs", "module1.html"))
shutil.copy2(m2_src, os.path.join(base_dir, "docs", "module2.html"))
shutil.copy2(index_path, os.path.join(base_dir, "docs", "index.html"))

# Copy downloads to root downloads/
os.makedirs(os.path.join(base_dir, "downloads"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "docs", "downloads"), exist_ok=True)
for item in os.listdir(os.path.join(base_dir, "public", "downloads")):
    src_file = os.path.join(base_dir, "public", "downloads", item)
    shutil.copy2(src_file, os.path.join(base_dir, "downloads", item))
    shutil.copy2(src_file, os.path.join(base_dir, "docs", "downloads", item))

# 3. Create .nojekyll files
for folder in [base_dir, os.path.join(base_dir, "public"), os.path.join(base_dir, "docs")]:
    nojekyll_file = os.path.join(folder, ".nojekyll")
    with open(nojekyll_file, 'w') as f:
        f.write("")
    print(f"Created {nojekyll_file}")

print("Sync completed successfully!")
