import os
import sys
import re
import json
import html
import shutil
import random

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
sys.path.insert(0, DATA_DIR)

# Import data sources from scripts/data
from module1_data import MODULE_1_ITEMS as NETC_M1_ITEMS
from module2_data import MODULE_2_ITEMS as NETC_M2_ITEMS
from hmby311_m1_data import HMBY_MODULE_1_ITEMS
from hmby311_m4_data import HMBY_MODULE_4_ITEMS
from hmby311_m5_data import HMBY_MODULE_5_ITEMS
from atfl311_data import (
    ATFL_MODULE_1_ITEMS,
    ATFL_MODULE_2_ITEMS,
    ATFL_MODULE_3_ITEMS,
    ATFL_MODULE_4_ITEMS
)

ALL_COURSES = {
    "NETC311": {
        "title": "Networking Technologies",
        "code": "NETC311",
        "slug": "netc311",
        "modules": [
            {
                "num": 1,
                "title": "Networking Today",
                "items": NETC_M1_ITEMS,
                "html": "module1.html"
            },
            {
                "num": 2,
                "title": "Basic Switch & End Device Configuration",
                "items": NETC_M2_ITEMS,
                "html": "module2.html"
            }
        ]
    },
    "HMBY311": {
        "title": "Human Biology",
        "code": "HMBY311",
        "slug": "hmby311",
        "modules": [
            {
                "num": 1,
                "title": "The Scientific Method & Basic Chemistry",
                "items": HMBY_MODULE_1_ITEMS,
                "html": "module1.html"
            },
            {
                "num": 4,
                "title": "Chromosomes & Cell Division",
                "items": HMBY_MODULE_4_ITEMS,
                "html": "module4.html"
            },
            {
                "num": 5,
                "title": "Genetics, Human Inheritance and Cancer",
                "items": HMBY_MODULE_5_ITEMS,
                "html": "module5.html"
            }
        ]
    },
    "ATFL311": {
        "title": "Automata Theory & Formal Languages",
        "code": "ATFL311",
        "slug": "atfl311",
        "modules": [
            {
                "num": 1,
                "title": "Introduction to Automata Theory & Chomsky Hierarchy",
                "items": ATFL_MODULE_1_ITEMS,
                "html": "module1.html"
            },
            {
                "num": 2,
                "title": "Finite State Machines & Prerequisites",
                "items": ATFL_MODULE_2_ITEMS,
                "html": "module2.html"
            },
            {
                "num": 3,
                "title": "Deterministic Finite Automata (DFA)",
                "items": ATFL_MODULE_3_ITEMS,
                "html": "module3.html"
            },
            {
                "num": 4,
                "title": "Non-Deterministic Finite Automata & Conversions",
                "items": ATFL_MODULE_4_ITEMS,
                "html": "module4.html"
            }
        ]
    }
}

# Read base template from scripts/templates
template_path = os.path.join(SCRIPT_DIR, "templates", "Module_1_NotebookLM_Quiz.html")
with open(template_path, "r", encoding="utf-8") as f:
    base_template = f.read()

def generate_header_and_widget_html(course, current_mod):
    c_code = course["code"]
    c_slug = course["slug"]
    m_num = current_mod["num"]
    m_title = current_mod["title"]
    m_count = len(current_mod["items"])
    all_mods = course["modules"]

    # Desktop module links
    desktop_mod_links = []
    for m in all_mods:
        m_n = m["num"]
        m_c = len(m["items"])
        if m_n == m_num:
            desktop_mod_links.append(
                f'<span class="quiz-nav-pill-active">M{m_n} ({m_c} Qs)</span>'
            )
        else:
            desktop_mod_links.append(
                f'<a href="{m["html"]}" class="quiz-nav-link" title="Switch to Module {m_n}">M{m_n} ({m_c} Qs)</a>'
            )

    # Next module link
    curr_idx = next(i for i, m in enumerate(all_mods) if m["num"] == m_num)
    next_link_html = ""
    if curr_idx + 1 < len(all_mods):
        nxt = all_mods[curr_idx + 1]
        next_link_html = f'<a href="{nxt["html"]}" class="quiz-nav-btn-next" title="Next: Module {nxt["num"]}">Next &rarr;</a>'

    desktop_links_str = "\n        ".join(desktop_mod_links)

    # Mobile Drawer Module Items
    drawer_mod_items = []
    for m in all_mods:
        m_n = m["num"]
        m_c = len(m["items"])
        is_act = (m_n == m_num)
        act_cls = "active" if is_act else ""
        act_beacon = '<span style="color:#8a9a86;font-size:10px;margin-left:auto;margin-right:8px;">● Current</span>' if is_act else ""
        drawer_mod_items.append(f"""
        <a href="{m['html']}" class="drawer-module-item {act_cls}">
          <div class="drawer-item-left">
            <span class="drawer-mod-pill">M{m_n}</span>
            <span class="drawer-mod-title" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:210px;">{m['title']}</span>
          </div>
          {act_beacon}
          <span class="drawer-item-count">{m_c} Qs</span>
        </a>""")

    drawer_items_str = "\n".join(drawer_mod_items)

    header_html = f"""
    <!-- REVIEWIII COMPACT HEADER (Mobile Hamburger UI + Pomodoro Integration) -->
    <header id="quiz-hub-nav">
      <div class="quiz-nav-left">
        <a href="../../index.html" class="quiz-brand" title="Return to ReviewIII Academic Hub">
          <span class="quiz-brand-sparkle">✦</span>
          <span class="quiz-brand-title">ReviewIII</span>
        </a>
        <span class="quiz-crumb-sep">/</span>
        <a href="../../courses/{c_slug}/index.html" class="quiz-sub-code" title="View {c_code} Course Page">{c_code}</a>
        <span class="quiz-crumb-sep">/</span>
        <span class="quiz-mod-title-desktop" title="{m_title}">M{m_num}: {m_title} ({m_count} Qs)</span>
        <span class="quiz-mod-badge-mobile">M{m_num}</span>
        <span id="quiz-session-badge" class="quiz-session-pill" style="display:none;" title="Session progress saved locally">Saved</span>
      </div>

      <div class="quiz-nav-right">
        <!-- Live Focus Pill -->
        <button type="button" class="quiz-focus-pill-btn" id="quiz-focus-pill" title="Toggle Pomodoro Timer">
          <span id="quiz-pill-ping" style="display:none; width:6px; height:6px; border-radius:50%; background:#8a9a86;"></span>
          <span id="quiz-pill-icon">⏱️</span>
          <span id="quiz-pill-time">Focus</span>
        </button>

        <!-- Restart Session Button (Desktop) -->
        <button type="button" class="quiz-restart-pill-btn" id="quiz-restart-btn" title="Reset saved answers & restart with new randomized choices">
          <span>↺ Restart</span>
        </button>

        <!-- Desktop Navigation Links -->
        <div class="quiz-desktop-links">
          <a href="../../index.html" class="quiz-nav-link">Hub</a>
          <a href="../../courses/{c_slug}/index.html" class="quiz-nav-link">Course</a>
          {desktop_links_str}
          {next_link_html}
        </div>

        <!-- Mobile Hamburger Button -->
        <button type="button" id="quiz-menu-btn" class="quiz-hamburger-btn" aria-label="Open Course Menu">
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
        </button>
      </div>
    </header>

    <!-- Mobile Slide-Down Navigation Drawer -->
    <div id="quiz-mobile-drawer" role="dialog" aria-label="Course Menu">
      <div class="drawer-top-row">
        <span class="drawer-title">{c_code} &bull; M{m_num} Navigation</span>
        <button type="button" id="drawer-close-btn" class="drawer-close-btn" aria-label="Close menu">✕</button>
      </div>

      <!-- Mobile Session State Card -->
      <div class="drawer-session-card">
        <div class="drawer-session-meta">
          <span class="drawer-session-title">Session Persistence</span>
          <span id="drawer-session-status" class="drawer-session-val">Ready</span>
        </div>
        <button type="button" id="drawer-restart-btn" class="drawer-restart-btn" title="Reset answers & re-randomize choices">
          ↺ Restart Quiz (Randomize Choices)
        </button>
      </div>

      <div class="drawer-quick-links">
        <a href="../../index.html" class="drawer-link-btn">
          <span>🏠 Hub Overview</span>
        </a>
        <a href="../../courses/{c_slug}/index.html" class="drawer-link-btn">
          <span>📚 {c_code} Page</span>
        </a>
      </div>

      <div class="drawer-modules-section">
        <span class="drawer-section-label">Available Questionnaires</span>
        {drawer_items_str}
      </div>

      <div style="border-top: 1px solid rgba(255,255,255,0.06); padding-top: 8px; margin-top: 4px;">
        <a href="../../courses/{c_slug}/index.html#vault" class="drawer-link-btn" style="width: 100%;">
          <span>📥 Download Offline Questionnaires (PDF/DOCX)</span>
        </a>
      </div>
    </div>
    """

    widget_html = f"""
<!-- REVIEWIII FOCUS SYSTEM WIDGET (Pomodoro + Automatic Time Tracking) -->
<style>
  #quiz-hub-nav {{
    position: sticky;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999999;
    background: rgba(0, 0, 0, 0.94);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    height: 48px;
    padding: 0 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    box-sizing: border-box;
  }}
  .quiz-nav-left {{
    display: flex;
    align-items: center;
    gap: 8px;
    min-width: 0;
    flex: 1 1 auto;
    overflow: hidden;
  }}
  .quiz-brand {{
    color: #f0f0f0;
    text-decoration: none;
    font-weight: 600;
    font-size: 13px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .quiz-brand-sparkle {{
    color: #8a9a86;
    font-size: 14px;
  }}
  .quiz-brand-title {{
    color: #8a9a86;
    letter-spacing: -0.01em;
  }}
  @media (max-width: 520px) {{
    .quiz-brand-title {{
      display: none;
    }}
  }}
  .quiz-crumb-sep {{
    color: #444;
    font-size: 12px;
  }}
  .quiz-sub-code {{
    color: #a89f91;
    font-size: 13px;
    font-weight: 600;
    text-decoration: none;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .quiz-sub-code:hover {{
    color: #f0f0f0;
  }}
  .quiz-mod-title-desktop {{
    color: #888;
    font-size: 12px;
    font-weight: 400;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: none;
  }}
  .quiz-mod-badge-mobile {{
    color: #8a9a86;
    background: rgba(138, 154, 134, 0.12);
    border: 1px solid rgba(138, 154, 134, 0.28);
    font-size: 11px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 4px;
    white-space: nowrap;
  }}
  @media (min-width: 860px) {{
    .quiz-mod-title-desktop {{
      display: inline;
    }}
    .quiz-mod-badge-mobile {{
      display: none;
    }}
  }}
  .quiz-nav-right {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
  }}
  .quiz-desktop-links {{
    display: none;
    align-items: center;
    gap: 6px;
  }}
  @media (min-width: 860px) {{
    .quiz-desktop-links {{
      display: flex;
    }}
  }}
  .quiz-nav-link {{
    color: #a0a0a0;
    text-decoration: none;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 4px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: transparent;
    transition: all 0.15s ease;
    white-space: nowrap;
  }}
  .quiz-nav-link:hover {{
    color: #f0f0f0;
    border-color: rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.04);
  }}
  .quiz-nav-pill-active {{
    color: #000000;
    background: #8a9a86;
    font-size: 12px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 4px;
    white-space: nowrap;
  }}
  .quiz-nav-btn-next {{
    color: #8a9a86;
    text-decoration: none;
    font-size: 12px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 4px;
    background: rgba(138, 154, 134, 0.1);
    border: 1px solid rgba(138, 154, 134, 0.35);
    display: inline-flex;
    align-items: center;
    gap: 4px;
    white-space: nowrap;
  }}
  .quiz-nav-btn-next:hover {{
    background: rgba(138, 154, 134, 0.2);
    color: #f0f0f0;
  }}
  .quiz-hamburger-btn {{
    display: inline-flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 3.5px;
    width: 32px;
    height: 32px;
    padding: 0;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 6px;
    cursor: pointer;
  }}
  .hamburger-line {{
    width: 15px;
    height: 1.5px;
    background: #f0f0f0;
    border-radius: 1px;
  }}
  @media (min-width: 860px) {{
    .quiz-hamburger-btn {{
      display: none;
    }}
  }}
  #quiz-mobile-drawer {{
    position: fixed;
    top: 48px;
    left: 0;
    right: 0;
    background: #090909;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 20px 48px rgba(0, 0, 0, 0.95);
    z-index: 999998;
    padding: 14px 16px;
    display: none;
    flex-direction: column;
    gap: 12px;
    max-height: 80vh;
    overflow-y: auto;
    box-sizing: border-box;
  }}
  #quiz-mobile-drawer.open {{
    display: flex;
  }}
  .drawer-top-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }}
  .drawer-title {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #8a9a86;
  }}
  .drawer-close-btn {{
    background: transparent;
    border: none;
    color: #888;
    font-size: 16px;
    cursor: pointer;
    padding: 2px 6px;
  }}
  .drawer-quick-links {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }}
  .drawer-link-btn {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 8px 10px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 6px;
    color: #f0f0f0;
    text-decoration: none;
    font-size: 12px;
    font-weight: 500;
    text-align: center;
  }}
  .drawer-modules-section {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .drawer-section-label {{
    font-size: 10px;
    color: #707070;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}
  .drawer-module-item {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 10px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 6px;
    text-decoration: none;
    color: #a0a0a0;
    font-size: 12px;
  }}
  .drawer-module-item.active {{
    background: rgba(138, 154, 134, 0.12);
    border-color: rgba(138, 154, 134, 0.35);
    color: #f0f0f0;
    font-weight: 600;
  }}
  .drawer-item-left {{
    display: flex;
    align-items: center;
    gap: 8px;
    min-width: 0;
  }}
  .drawer-mod-pill {{
    font-size: 10px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 3px;
    background: rgba(255, 255, 255, 0.08);
    color: #f0f0f0;
  }}
  .drawer-module-item.active .drawer-mod-pill {{
    background: #8a9a86;
    color: #000;
  }}
  .drawer-item-count {{
    font-size: 11px;
    color: #707070;
    flex-shrink: 0;
  }}

  /* Session Persistence & Restart Controls */
  .quiz-session-pill {{
    display: none;
    align-items: center;
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 2px 7px;
    border-radius: 9999px;
    background: rgba(138, 154, 134, 0.15);
    border: 1px solid rgba(138, 154, 134, 0.35);
    color: #8a9a86;
  }}
  .quiz-restart-pill-btn {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 9px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 500;
    font-family: 'Inter', -apple-system, monospace;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(255, 255, 255, 0.04);
    color: #a0a0a0;
    cursor: pointer;
    transition: all 0.2s ease;
  }}
  .quiz-restart-pill-btn:hover {{
    border-color: rgba(168, 159, 145, 0.4);
    background: rgba(168, 159, 145, 0.12);
    color: #f0f0f0;
  }}
  @media (max-width: 640px) {{
    .quiz-restart-pill-btn {{
      display: none;
    }}
  }}
  .drawer-session-card {{
    margin-bottom: 10px;
    padding: 10px 12px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .drawer-session-meta {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .drawer-session-title {{
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #8a9a86;
  }}
  .drawer-session-val {{
    font-size: 10.5px;
    color: #707070;
  }}
  .drawer-restart-btn {{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 7px 12px;
    font-size: 12px;
    font-weight: 500;
    background: rgba(168, 159, 145, 0.12);
    border: 1px solid rgba(168, 159, 145, 0.3);
    border-radius: 6px;
    color: #f0f0f0;
    cursor: pointer;
    transition: all 0.2s ease;
  }}
  .drawer-restart-btn:hover {{
    background: rgba(168, 159, 145, 0.22);
    border-color: rgba(168, 159, 145, 0.5);
  }}

  /* Focus Pill */
  .quiz-focus-pill-btn {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 11.5px;
    font-weight: 600;
    font-family: 'Inter', -apple-system, monospace;
    font-variant-numeric: tabular-nums;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(255, 255, 255, 0.04);
    color: #a0a0a0;
    cursor: pointer;
    transition: all 0.2s ease;
    text-decoration: none;
  }}
  .quiz-focus-pill-btn:hover {{
    border-color: rgba(138, 154, 134, 0.4);
    background: rgba(138, 154, 134, 0.08);
    color: #f0f0f0;
  }}
  .quiz-focus-pill-btn.running-focus {{
    border-color: rgba(138, 154, 134, 0.5);
    background: rgba(138, 154, 134, 0.15);
    color: #8a9a86;
    box-shadow: 0 0 12px rgba(138, 154, 134, 0.25);
  }}
  .quiz-focus-pill-btn.running-break {{
    border-color: rgba(168, 159, 145, 0.5);
    background: rgba(168, 159, 145, 0.15);
    color: #a89f91;
    box-shadow: 0 0 12px rgba(168, 159, 145, 0.25);
  }}
  #quiz-focus-modal {{
    position: fixed;
    top: 54px;
    right: 16px;
    z-index: 9999999;
    width: 310px;
    background: #0a0a0a;
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 12px;
    padding: 16px 18px;
    box-shadow: 0 18px 48px rgba(0, 0, 0, 0.85);
    font-family: 'Inter', -apple-system, sans-serif;
    color: #f0f0f0;
    display: none;
  }}
  @media (max-width: 640px) {{
    #quiz-focus-modal {{
      right: 10px;
      left: 10px;
      width: auto;
      top: 52px;
    }}
  }}
</style>

<div id="quiz-focus-modal" role="dialog" aria-label="Pomodoro Focus Timer">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <div style="display: flex; align-items: center; gap: 8px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #8a9a86;">
      <span id="modal-phase-emoji">🎯</span>
      <span id="modal-phase-title">FOCUS</span>
      <span id="modal-session-count" style="color: #a0a0a0; font-weight: 400;">· Session 1</span>
    </div>
    <div style="display: flex; align-items: center; gap: 6px;">
      <button type="button" id="modal-sound-btn" style="background: transparent; border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; color: #a0a0a0; font-size: 11px; padding: 2px 6px; cursor: pointer;" title="Toggle chimes">🔊</button>
      <button type="button" id="modal-close-btn" style="background: transparent; border: none; color: #707070; font-size: 16px; cursor: pointer; padding: 0 4px;" title="Close overlay">✕</button>
    </div>
  </div>

  <div style="text-align: center; margin: 10px 0 14px 0;">
    <div id="modal-digits" style="font-size: 40px; font-weight: 700; font-family: 'Inter', monospace; font-variant-numeric: tabular-nums; letter-spacing: -0.04em; color: #f0f0f0; line-height: 1;">25:00</div>
    <div id="modal-status-caption" style="font-size: 11px; color: #707070; text-transform: uppercase; letter-spacing: 0.06em; margin-top: 4px;">ready to study</div>
  </div>

  <div style="display: flex; gap: 8px; justify-content: center; margin-bottom: 14px;">
    <button type="button" id="modal-start-btn" style="background: #8a9a86; color: #000000; border: none; border-radius: 6px; font-size: 13px; font-weight: 600; padding: 8px 18px; cursor: pointer; flex: 1;">▶ Start</button>
    <button type="button" id="modal-reset-btn" style="background: transparent; border: 1px solid rgba(255,255,255,0.14); color: #a0a0a0; border-radius: 6px; font-size: 12px; padding: 8px 12px; cursor: pointer;">Reset</button>
    <button type="button" id="modal-skip-btn" style="background: transparent; border: 1px solid rgba(255,255,255,0.14); color: #a0a0a0; border-radius: 6px; font-size: 12px; padding: 8px 12px; cursor: pointer;">Skip &rarr;</button>
  </div>

  <div style="border-top: 1px solid rgba(255,255,255,0.08); padding-top: 10px; font-size: 11px; color: #707070; display: flex; justify-content: space-between; align-items: center;">
    <span style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 190px;" title="{c_code} &bull; M{m_num}: {m_title}">
      📍 <strong>{c_code}</strong>: M{m_num}
    </span>
    <a href="../../index.html#focus-timer" style="color: #8a9a86; text-decoration: none; font-weight: 500;">Hub Stats &nearr;</a>
  </div>
</div>

<script src="../../scripts/focus-system.js"></script>
<script>
  (function initQuizNavAndFocus() {{
    var subjectCode = "{c_code}";
    var moduleTitle = "Module {m_num}: {m_title}";

    // 1. Mobile Drawer Navigation
    var menuBtn = document.getElementById('quiz-menu-btn');
    var drawer = document.getElementById('quiz-mobile-drawer');
    var drawerCloseBtn = document.getElementById('drawer-close-btn');

    if (menuBtn && drawer) {{
      menuBtn.addEventListener('click', function(e) {{
        e.stopPropagation();
        var isOpen = drawer.classList.contains('open');
        drawer.classList.toggle('open', !isOpen);
      }});

      if (drawerCloseBtn) {{
        drawerCloseBtn.addEventListener('click', function(e) {{
          e.stopPropagation();
          drawer.classList.remove('open');
        }});
      }}

      document.addEventListener('click', function(e) {{
        if (drawer.classList.contains('open') && !drawer.contains(e.target) && e.target !== menuBtn) {{
          drawer.classList.remove('open');
        }}
      }});

      window.addEventListener('keydown', function(e) {{
        if (e.key === 'Escape' && drawer.classList.contains('open')) {{
          drawer.classList.remove('open');
        }}
      }});
    }}

    // 2. Focus Pill & Modal Integration
    var pillBtn = document.getElementById('quiz-focus-pill');
    var pingEl = document.getElementById('quiz-pill-ping');
    var iconEl = document.getElementById('quiz-pill-icon');
    var timeEl = document.getElementById('quiz-pill-time');

    var modal = document.getElementById('quiz-focus-modal');
    var closeBtn = document.getElementById('modal-close-btn');
    var soundBtn = document.getElementById('modal-sound-btn');
    var phaseEmoji = document.getElementById('modal-phase-emoji');
    var phaseTitle = document.getElementById('modal-phase-title');
    var sessionCount = document.getElementById('modal-session-count');
    var digitsEl = document.getElementById('modal-digits');
    var statusCaption = document.getElementById('modal-status-caption');
    var startBtn = document.getElementById('modal-start-btn');
    var resetBtn = document.getElementById('modal-reset-btn');
    var skipBtn = document.getElementById('modal-skip-btn');

    var F = window.ReviewIIIFocus;
    if (!F) return;

    var settings = F.readSettings();
    var snapshot = F.readFocusSnapshot() || {{
      v: 1,
      phase: 'focus',
      running: false,
      focusCount: 0,
      subjectCode: subjectCode,
      moduleTitle: moduleTitle,
      secondsLeft: settings.focusSeconds || 1500,
      endsAt: null,
      updatedAt: Date.now()
    }};

    function getPhaseDuration(phase) {{
      if (phase === 'focus') return settings.focusSeconds || 1500;
      if (phase === 'short') return settings.shortBreakSeconds || 300;
      if (phase === 'long') return settings.longBreakSeconds || 900;
      return 1500;
    }}

    function updatePill(snap) {{
      if (!pillBtn) return;
      if (!snap || !snap.running) {{
        pillBtn.className = 'quiz-focus-pill-btn idle';
        if (pingEl) pingEl.style.display = 'none';
        if (iconEl) iconEl.textContent = '⏱️';
        if (timeEl) timeEl.textContent = snap ? F.formatTime(snap.secondsLeft) : 'Focus';
        return;
      }}
      var isFocus = snap.phase === 'focus';
      pillBtn.className = 'quiz-focus-pill-btn ' + (isFocus ? 'running-focus' : 'running-break');
      if (pingEl) pingEl.style.display = 'inline-block';
      if (iconEl) iconEl.textContent = F.PHASE_EMOJIS[snap.phase] || (isFocus ? '🎯' : '☕');
      if (timeEl) timeEl.textContent = F.formatTime(Math.max(0, snap.secondsLeft));
    }}

    function updateModal(snap) {{
      if (!modal) return;
      if (digitsEl) digitsEl.textContent = F.formatTime(Math.max(0, snap.secondsLeft));
      if (phaseEmoji) phaseEmoji.textContent = F.PHASE_EMOJIS[snap.phase] || '🎯';
      if (phaseTitle) phaseTitle.textContent = F.PHASE_LABELS[snap.phase] || 'FOCUS';
      if (sessionCount) {{
        if (snap.phase === 'focus') {{
          sessionCount.textContent = '· Session ' + (snap.focusCount + 1);
          sessionCount.style.display = 'inline';
        }} else {{
          sessionCount.style.display = 'none';
        }}
      }}
      if (statusCaption) statusCaption.textContent = snap.running ? 'session running' : 'paused';
      if (startBtn) {{
        startBtn.textContent = snap.running ? '⏸ Pause' : '▶ Start';
        startBtn.style.background = snap.running ? '#a89f91' : '#8a9a86';
      }}
      if (soundBtn) soundBtn.textContent = settings.soundEnabled ? '🔊' : '🔇';
    }}

    function tick() {{
      if (!snapshot.running || !snapshot.endsAt) return;
      var now = Date.now();
      var diff = Math.max(0, Math.ceil((snapshot.endsAt - now) / 1000));
      snapshot.secondsLeft = diff;
      snapshot.updatedAt = now;

      if (diff <= 0) {{
        handlePhaseComplete();
      }} else {{
        F.saveFocusSnapshot(snapshot);
        updatePill(snapshot);
        updateModal(snapshot);
      }}
    }}

    function handlePhaseComplete() {{
      if (snapshot.phase === 'focus') {{
        F.playFocusChime('break');
        var mins = Math.max(1, Math.round(getPhaseDuration('focus') / 60));
        F.logTime(mins, snapshot.subjectCode || subjectCode, snapshot.moduleTitle || moduleTitle, 'pomodoro');

        var nextCount = snapshot.focusCount + 1;
        snapshot.focusCount = nextCount;
        var breakPhase = nextCount % 4 === 0 ? 'long' : 'short';
        snapshot.phase = breakPhase;
        var breakDur = getPhaseDuration(breakPhase);
        snapshot.secondsLeft = breakDur;
        snapshot.endsAt = Date.now() + breakDur * 1000;
        snapshot.running = settings.autoStartBreaks !== false;
      }} else if (snapshot.phase === 'long') {{
        F.playFocusChime('set');
        snapshot.focusCount = 0;
        snapshot.phase = 'focus';
        snapshot.secondsLeft = getPhaseDuration('focus');
        snapshot.running = false;
        snapshot.endsAt = null;
      }} else {{
        F.playFocusChime('focus');
        snapshot.phase = 'focus';
        var focusDur = getPhaseDuration('focus');
        snapshot.secondsLeft = focusDur;
        snapshot.endsAt = Date.now() + focusDur * 1000;
        snapshot.running = settings.autoStartFocus !== false;
      }}
      F.saveFocusSnapshot(snapshot);
      updatePill(snapshot);
      updateModal(snapshot);
    }}

    function toggleTimer() {{
      if (!snapshot.running) {{
        snapshot.subjectCode = snapshot.subjectCode || subjectCode;
        snapshot.moduleTitle = snapshot.moduleTitle || moduleTitle;
        F.playFocusChime(snapshot.phase === 'focus' ? 'focus' : 'break');
        snapshot.running = true;
        snapshot.endsAt = Date.now() + snapshot.secondsLeft * 1000;
      }} else {{
        snapshot.running = false;
        snapshot.endsAt = null;
      }}
      F.saveFocusSnapshot(snapshot);
      updatePill(snapshot);
      updateModal(snapshot);
    }}

    function resetTimer() {{
      snapshot.phase = 'focus';
      snapshot.secondsLeft = getPhaseDuration('focus');
      snapshot.running = false;
      snapshot.endsAt = null;
      F.saveFocusSnapshot(snapshot);
      updatePill(snapshot);
      updateModal(snapshot);
    }}

    function skipSegment() {{
      var curTotal = getPhaseDuration(snapshot.phase);
      var elapsed = curTotal - snapshot.secondsLeft;
      if (snapshot.phase === 'focus') {{
        F.playFocusChime('break');
        if (elapsed >= 60) {{
          var mins = Math.max(1, Math.round(elapsed / 60));
          F.logTime(mins, snapshot.subjectCode || subjectCode, snapshot.moduleTitle || moduleTitle, 'pomodoro');
        }}
        var nextCount = snapshot.focusCount + 1;
        snapshot.focusCount = nextCount;
        var breakPhase = nextCount % 4 === 0 && nextCount > 0 ? 'long' : 'short';
        snapshot.phase = breakPhase;
        var breakDur = getPhaseDuration(breakPhase);
        snapshot.secondsLeft = breakDur;
        snapshot.endsAt = Date.now() + breakDur * 1000;
        snapshot.running = true;
      }} else if (snapshot.phase === 'long') {{
        F.playFocusChime('set');
        snapshot.focusCount = 0;
        snapshot.phase = 'focus';
        snapshot.secondsLeft = getPhaseDuration('focus');
        snapshot.running = false;
        snapshot.endsAt = null;
      }} else {{
        F.playFocusChime('focus');
        snapshot.phase = 'focus';
        var focusDur = getPhaseDuration('focus');
        snapshot.secondsLeft = focusDur;
        snapshot.endsAt = Date.now() + focusDur * 1000;
        snapshot.running = true;
      }}
      F.saveFocusSnapshot(snapshot);
      updatePill(snapshot);
      updateModal(snapshot);
    }}

    if (pillBtn && modal) {{
      pillBtn.addEventListener('click', function(e) {{
        e.stopPropagation();
        modal.style.display = modal.style.display === 'block' ? 'none' : 'block';
        updateModal(snapshot);
      }});
    }}

    if (closeBtn && modal) {{
      closeBtn.addEventListener('click', function() {{
        modal.style.display = 'none';
      }});
    }}

    if (startBtn) startBtn.addEventListener('click', toggleTimer);
    if (resetBtn) resetBtn.addEventListener('click', resetTimer);
    if (skipBtn) skipBtn.addEventListener('click', skipSegment);

    if (soundBtn) {{
      soundBtn.addEventListener('click', function() {{
        settings.soundEnabled = !settings.soundEnabled;
        F.saveSettings({{ soundEnabled: settings.soundEnabled }});
        if (settings.soundEnabled) F.playFocusChime('focus', true);
        updateModal(snapshot);
      }});
    }}

    document.addEventListener('visibilitychange', function() {{
      if (document.visibilityState === 'visible' && snapshot.running && snapshot.endsAt != null) {{
        tick();
      }}
    }});

    F.subscribeFocus(function(newSnap) {{
      if (!newSnap) return;
      snapshot = newSnap;
      updatePill(snapshot);
      updateModal(snapshot);
    }});

    // Session Persistence & Restart Handlers
    var quizRestartBtn = document.getElementById('quiz-restart-btn');
    if (quizRestartBtn) {{
      quizRestartBtn.addEventListener('click', function() {{
        if (window.__quiz_restart_session) window.__quiz_restart_session();
      }});
    }}
    var drawerRestartBtn = document.getElementById('drawer-restart-btn');
    if (drawerRestartBtn) {{
      drawerRestartBtn.addEventListener('click', function() {{
        if (window.__quiz_restart_session) window.__quiz_restart_session();
      }});
    }}

    // Check for existing saved session on startup to show indicator
    try {{
      var initSaved = window.__quiz_load_state ? window.__quiz_load_state() : null;
      if (initSaved && initSaved.userAnswers) {{
        var aCount = Object.keys(initSaved.userAnswers).length;
        if (aCount > 0) {{
          var sBadge = document.getElementById('quiz-session-badge');
          if (sBadge) {{
            sBadge.style.display = 'inline-flex';
            sBadge.textContent = 'Saved (' + aCount + ')';
          }}
          var dStatus = document.getElementById('drawer-session-status');
          if (dStatus) {{
            dStatus.textContent = 'Resumed (' + aCount + ' answered)';
          }}
        }}
      }}
    }} catch (e) {{}}

    updatePill(snapshot);
    updateModal(snapshot);
    setInterval(tick, 1000);
  }})();
</script>
"""
    return header_html, widget_html

def build_quiz_html(course, mod):
    c_code = course["code"]
    m_num = mod["num"]
    m_title = mod["title"]
    items = mod["items"]

    # 1. Prepare JSON questions
    quiz_questions = []
    for idx, item in enumerate(items, start=1):
        choices = [item["a"]] + item["distractors"]
        rng = random.Random(idx * 7919)
        rng.shuffle(choices)

        opts = []
        for ch in choices:
            is_corr = (ch == item["a"])
            rationale = f"Correct! [{item['topic']}] {item['explanation']}" if is_corr else f"Incorrect. '{ch}' is a distractor. Correct answer is '{item['a']}'."
            # Clean string without leading 'a.) '
            opts.append({
                "text": ch,
                "isCorrect": is_corr,
                "rationale": rationale
            })

        quiz_questions.append({
            "question": f"_____ {idx}. {item['q']}",
            "answerOptions": opts,
            "hint": f"Topic: {item['topic']}"
        })

    quiz_payload = {
        "quiz": quiz_questions,
        "topics": {
            "covered": list(set([it["topic"] for it in items])),
            "followUp": [f"Review materials for {c_code} Module {m_num}"]
        }
    }

    escaped_json = html.escape(json.dumps(quiz_payload, ensure_ascii=False))

    # Insert payload into base_template
    idx = base_template.find('data-app-data="')
    if idx == -1:
        raise ValueError("data-app-data not found in base_template")
    end_idx = base_template.find('"', idx + 15)
    if end_idx == -1:
        raise ValueError("closing quote not found in base_template")

    content = base_template[:idx + 15] + escaped_json + base_template[end_idx:]

    # Replace Title
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{c_code} — Module {m_num}: {m_title}</title>',
        content
    )

    # Apply choice randomization patch
    target_sN = 'function sN(a,b){a=[...a];var c=0;if(b.length!==0)for(var d=0;d<b.length;d++)c=(c<<5)-c+b.charCodeAt(d),c|=0;b=c;b=tN(b);for(c=a.length-1;c>0;c--)d=Math.floor(b()*(c+1)),[a[c],a[d]]=[a[d],a[c]];return a}'
    replacement_sN = 'function sN(a,b){a=[...a];var c=(typeof window!=="undefined"&&window.__quiz_session_seed!=null)?window.__quiz_session_seed:0;if(b.length!==0)for(var d=0;d<b.length;d++)c=(c<<5)-c+b.charCodeAt(d),c|=0;b=c;b=tN(b);for(c=a.length-1;c>0;c--)d=Math.floor(b()*(c+1)),[a[c],a[d]]=[a[d],a[c]];return a}'
    content = content.replace(target_sN, replacement_sN)

    # Apply database persistence patch (qN)
    target_persistence = 'hN(a=>({Jr:async()=>{if(a.zg?.getAppState)try{let b=await a.zg.getAppState();if(b){let c={tc:!1,...b.timerState};c.zj&&Date.now()-c.zj>864E5&&(c.zj=void 0);aN(a,{userAnswers:oN(b.userAnswers||{}),currentQuestionIndex:b.currentQuestionIndex||\n0,hiddenQuestionIndices:b.hiddenQuestionIndices||[],currentView:b.currentView||\"question\",performanceAnalysis:b.performanceAnalysis,latestCompletion:b.latestCompletion,activeSessionQuestionIndices:b.activeSessionQuestionIndices||null,timerState:c})}}catch(b){console.error(\"Failed to load initial state:\",b)}finally{aN(a,{nc:!1})}else aN(a,{nc:!1})},Yr:async()=>{if(a.zg?.setAppState){var b={userAnswers:pN(a.userAnswers()),currentQuestionIndex:a.currentQuestionIndex(),hiddenQuestionIndices:a.hiddenQuestionIndices(),\ncurrentView:a.currentView(),performanceAnalysis:a.performanceAnalysis?a.performanceAnalysis():void 0,latestCompletion:a.latestCompletion?a.latestCompletion():void 0,activeSessionQuestionIndices:a.activeSessionQuestionIndices?a.activeSessionQuestionIndices():null,timerState:a.timerState?a.timerState():void 0};try{await a.zg.setAppState(b)}catch(c){console.error(\"Failed to save state:\",c)}}},Jc:()=>{a.zg?.setAppState&&a.ak.next()}}))'
    replacement_persistence = 'hN(a=>({Jr:async()=>{try{let b=null;if(typeof window!=="undefined"&&window.__quiz_load_state){b=window.__quiz_load_state()}if(!b&&a.zg?.getAppState){b=await a.zg.getAppState()}if(b){let c={tc:!1,...b.timerState};c.zj&&Date.now()-c.zj>864E5&&(c.zj=void 0);aN(a,{userAnswers:oN(b.userAnswers||{}),currentQuestionIndex:b.currentQuestionIndex||0,hiddenQuestionIndices:b.hiddenQuestionIndices||[],currentView:b.currentView||"question",performanceAnalysis:b.performanceAnalysis,latestCompletion:b.latestCompletion,activeSessionQuestionIndices:b.activeSessionQuestionIndices||null,timerState:c})}}catch(b){console.error("Failed to load initial state:",b)}finally{aN(a,{nc:!1})}},Yr:async()=>{var b={userAnswers:pN(a.userAnswers()),currentQuestionIndex:a.currentQuestionIndex(),hiddenQuestionIndices:a.hiddenQuestionIndices(),currentView:a.currentView(),performanceAnalysis:a.performanceAnalysis?a.performanceAnalysis():void 0,latestCompletion:a.latestCompletion?a.latestCompletion():void 0,activeSessionQuestionIndices:a.activeSessionQuestionIndices?a.activeSessionQuestionIndices():null,timerState:a.timerState?a.timerState():void 0};try{if(typeof window!=="undefined"&&window.__quiz_save_state){window.__quiz_save_state(b)}if(a.zg?.setAppState)await a.zg.setAppState(b)}catch(c){console.error("Failed to save state:",c)}},Jc:()=>{try{a.Yr()}catch(e){}a.ak.next()}}))'
    content = content.replace(target_persistence, replacement_persistence)

    # Inject ReviewIII Session Persistence Script before </head>
    storage_key = f"reviewiii_quiz_{c_code}_{m_num}"
    session_script = f"""
<script id="reviewiii-quiz-persistence">
  (function() {{
    var key = "{storage_key}";
    window.__quiz_storage_key = key;

    // 1. Initialize session seed for choice randomization
    try {{
      var savedRaw = localStorage.getItem(key);
      var saved = savedRaw ? JSON.parse(savedRaw) : null;
      if (saved && typeof saved.sessionSeed === 'number') {{
        window.__quiz_session_seed = saved.sessionSeed;
      }} else {{
        var queuedSeed = localStorage.getItem(key + '_seed');
        if (queuedSeed) {{
          window.__quiz_session_seed = parseInt(queuedSeed, 10);
          localStorage.removeItem(key + '_seed');
        }} else {{
          window.__quiz_session_seed = Math.floor(Math.random() * 2147483647) + 1;
        }}
      }}
    }} catch (e) {{
      window.__quiz_session_seed = Math.floor(Math.random() * 2147483647) + 1;
    }}

    // 2. Load state interface (called on init)
    window.__quiz_load_state = function() {{
      try {{
        var raw = localStorage.getItem(key);
        if (!raw) return null;
        var data = JSON.parse(raw);
        if (!data || typeof data !== 'object') return null;
        var timerState = {{ tc: false }};
        if (data.timerState) {{
          timerState = Object.assign({{}}, data.timerState, {{ tc: false }});
        }}
        return {{
          userAnswers: data.userAnswers || {{}},
          currentQuestionIndex: typeof data.currentQuestionIndex === 'number' ? data.currentQuestionIndex : 0,
          hiddenQuestionIndices: Array.isArray(data.hiddenQuestionIndices) ? data.hiddenQuestionIndices : [],
          currentView: data.currentView || 'question',
          performanceAnalysis: data.performanceAnalysis,
          latestCompletion: data.latestCompletion,
          activeSessionQuestionIndices: data.activeSessionQuestionIndices || null,
          timerState: timerState
        }};
      }} catch (e) {{
        console.error('Failed to load quiz state:', e);
        return null;
      }}
    }};

    // 3. Save state interface (called whenever answers/views change)
    window.__quiz_save_state = function(state) {{
      try {{
        if (!state) return;
        var toSave = Object.assign({{}}, state, {{
          sessionSeed: window.__quiz_session_seed,
          savedAt: Date.now()
        }});
        localStorage.setItem(key, JSON.stringify(toSave));

        var count = state.userAnswers ? Object.keys(state.userAnswers).length : 0;
        var badge = document.getElementById('quiz-session-badge');
        if (badge) {{
          if (count > 0) {{
            badge.style.display = 'inline-flex';
            badge.textContent = 'Saved (' + count + ')';
          }} else {{
            badge.style.display = 'none';
          }}
        }}
        var drawerStatus = document.getElementById('drawer-session-status');
        if (drawerStatus) {{
          drawerStatus.textContent = count > 0 ? 'Saved (' + count + ' answered)' : 'Ready';
        }}
      }} catch (e) {{
        console.error('Failed to save quiz state:', e);
      }}
    }};

    // 4. Restart session interface
    window.__quiz_restart_session = function() {{
      if (confirm('Restart this quiz session? All saved answers will be cleared and choices will be freshly randomized.')) {{
        try {{
          localStorage.removeItem(key);
          var freshSeed = Math.floor(Math.random() * 2147483647) + 1;
          localStorage.setItem(key + '_seed', String(freshSeed));
        }} catch (e) {{}}
        window.location.reload();
      }}
    }};

    // 5. Auto-pause quiz timer on exit (beforeunload and pagehide)
    function pauseQuizTimerOnExit() {{
      try {{
        var raw = localStorage.getItem(key);
        if (!raw) return;
        var data = JSON.parse(raw);
        if (data && data.timerState && data.timerState.tc) {{
          var elapsed = data.timerState.Ok || 0;
          if (data.timerState.zj) {{
            elapsed += Math.max(0, Math.floor((Date.now() - data.timerState.zj) / 1000));
          }}
          data.timerState.tc = false;
          data.timerState.Ok = elapsed;
          delete data.timerState.zj;
          data.savedAt = Date.now();
          localStorage.setItem(key, JSON.stringify(data));
        }}
      }} catch (e) {{}}
    }}
    window.addEventListener('beforeunload', pauseQuizTimerOnExit);
    window.addEventListener('pagehide', pauseQuizTimerOnExit);
  }})();
</script>
"""

    head_idx = content.find('</head>')
    if head_idx != -1:
        content = content[:head_idx] + "\n" + session_script + "\n" + content[head_idx:]

    header_html, widget_html = generate_header_and_widget_html(course, mod)

    # Remove any old header or widgets if present
    content = re.sub(r'<!-- Pitch Black Top Nav -->.*?</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- REVIEWIII COMPACT HEADER.*?<!-- Mobile Slide-Down Navigation Drawer -->\s*<div id="quiz-mobile-drawer".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- REVIEWIII FOCUS SYSTEM WIDGET.*?</body>', '</body>', content, flags=re.DOTALL)

    # Insert header right after <body> or at top of body
    body_idx = content.find('<body')
    if body_idx != -1:
        body_close = content.find('>', body_idx)
        content = content[:body_close + 1] + "\n" + header_html + content[body_close + 1:]

    # Insert widget before </body>
    closing_body = content.rfind('</body>')
    if closing_body != -1:
        content = content[:closing_body] + "\n" + widget_html + "\n" + content[closing_body:]

    return content

# Execute building for all courses
for c_key, course in ALL_COURSES.items():
    c_slug = course["slug"]
    print(f"\n================ Building {course['code']} Quizzes ================")
    pub_dir = os.path.join(BASE_DIR, f"public/quizzes/{c_slug}")
    q_dir = os.path.join(BASE_DIR, f"quizzes/{c_slug}")
    docs_q_dir = os.path.join(BASE_DIR, f"docs/quizzes/{c_slug}")

    os.makedirs(pub_dir, exist_ok=True)
    os.makedirs(q_dir, exist_ok=True)
    os.makedirs(docs_q_dir, exist_ok=True)

    for mod in course["modules"]:
        html_str = build_quiz_html(course, mod)
        fname = mod["html"]

        p_path = os.path.join(pub_dir, fname)
        with open(p_path, "w", encoding="utf-8") as f:
            f.write(html_str)

        q_path = os.path.join(q_dir, fname)
        with open(q_path, "w", encoding="utf-8") as f:
            f.write(html_str)

        d_path = os.path.join(docs_q_dir, fname)
        with open(d_path, "w", encoding="utf-8") as f:
            f.write(html_str)

        print(f"✓ Built {course['code']} M{mod['num']}: {mod['title']} ({len(mod['items'])} Qs) -> {fname}")

print("\nAll 9 quizzes successfully built with compact mobile hamburger UI and Focus integration!")
