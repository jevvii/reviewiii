import re

def patch_netc1(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    navbar = """
    <!-- Pitch Black Top Nav -->
    <header id="quiz-hub-nav" style="position: sticky; top: 0; left: 0; right: 0; z-index: 999999; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding: 12px 28px; display: flex; align-items: center; justify-content: space-between; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
      <div style="display: flex; align-items: center; gap: 12px;">
        <a href="../../index.html" style="color: #f0f0f0; text-decoration: none; font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 8px;">
          <span style="color: #8a9a86; font-size: 15px;">✦</span>
          <span style="color: #8a9a86; letter-spacing: -0.01em;">ReviewIII</span>
          <span style="color: #f0f0f0;">Hub</span>
        </a>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a89f91; font-size: 13px; font-weight: 500;">NETC311</span>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a0a0a0; font-size: 13px; font-weight: 400;">Module 1: Networking Today (99 Qs)</span>
      </div>
      <div style="display: flex; align-items: center; gap: 10px;">
        <a href="../../index.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">Hub Overview</a>
        <span style="color: #000000; background: #8a9a86; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 4px;">Module 1 (99 Qs)</span>
        <a href="module2.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">Module 2 (104 Qs)</a>
        <a href="module2.html" style="color: #8a9a86; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; background: rgba(138, 154, 134, 0.1); border: 1px solid rgba(138, 154, 134, 0.35); display: flex; align-items: center; gap: 4px;">Module 2 &rarr;</a>
      </div>
    </header>
    """
    text = re.sub(r'<!-- Pitch Black Top Nav -->.*?</header>', navbar, text, flags=re.DOTALL)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Patched {path}")

def patch_netc2(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    navbar = """
    <!-- Pitch Black Top Nav -->
    <header id="quiz-hub-nav" style="position: sticky; top: 0; left: 0; right: 0; z-index: 999999; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding: 12px 28px; display: flex; align-items: center; justify-content: space-between; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
      <div style="display: flex; align-items: center; gap: 12px;">
        <a href="../../index.html" style="color: #f0f0f0; text-decoration: none; font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 8px;">
          <span style="color: #8a9a86; font-size: 15px;">✦</span>
          <span style="color: #8a9a86; letter-spacing: -0.01em;">ReviewIII</span>
          <span style="color: #f0f0f0;">Hub</span>
        </a>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a89f91; font-size: 13px; font-weight: 500;">NETC311</span>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a0a0a0; font-size: 13px; font-weight: 400;">Module 2: Basic Switch & End Device Config (104 Qs)</span>
      </div>
      <div style="display: flex; align-items: center; gap: 10px;">
        <a href="../../index.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">Hub Overview</a>
        <a href="module1.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">Module 1 (99 Qs)</a>
        <span style="color: #000000; background: #8a9a86; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 4px;">Module 2 (104 Qs)</span>
        <a href="module1.html" style="color: #8a9a86; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; background: rgba(138, 154, 134, 0.1); border: 1px solid rgba(138, 154, 134, 0.35); display: flex; align-items: center; gap: 4px;">&larr; Module 1</a>
      </div>
    </header>
    """
    text = re.sub(r'<!-- Pitch Black Top Nav -->.*?</header>', navbar, text, flags=re.DOTALL)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Patched {path}")

def patch_hmby1(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    navbar = """
    <!-- Pitch Black Top Nav -->
    <header id="quiz-hub-nav" style="position: sticky; top: 0; left: 0; right: 0; z-index: 999999; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding: 12px 28px; display: flex; align-items: center; justify-content: space-between; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
      <div style="display: flex; align-items: center; gap: 12px;">
        <a href="../../index.html" style="color: #f0f0f0; text-decoration: none; font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 8px;">
          <span style="color: #8a9a86; font-size: 15px;">✦</span>
          <span style="color: #8a9a86; letter-spacing: -0.01em;">ReviewIII</span>
          <span style="color: #f0f0f0;">Hub</span>
        </a>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a89f91; font-size: 13px; font-weight: 500;">HMBY311</span>
        <span style="color: #444444; font-size: 13px;">/</span>
        <span style="color: #a0a0a0; font-size: 13px; font-weight: 400;">Module 1: Scientific Method & Chemistry (82 Qs)</span>
      </div>
      <div style="display: flex; align-items: center; gap: 10px;">
        <a href="../../index.html" style="color: #a0a0a0; text-decoration: none; font-size: 13px; font-weight: 500; padding: 6px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08); background: transparent; transition: all 0.2s;">Hub Overview</a>
        <span style="color: #000000; background: #8a9a86; font-size: 13px; font-weight: 600; padding: 6px 14px; border-radius: 4px;">Module 1 (82 Qs)</span>
      </div>
    </header>
    """
    text = re.sub(r'<!-- Pitch Black Top Nav -->.*?</header>', navbar, text, flags=re.DOTALL)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Patched {path}")

patch_netc1("public/quizzes/netc311/module1.html")
patch_netc2("public/quizzes/netc311/module2.html")
patch_hmby1("public/quizzes/hmby311/module1.html")
