import os
import re

QUIZ_SPECS = {
    "netc311/module1.html": {
        "subject": "NETC311",
        "module": "Module 1: Networking Today"
    },
    "netc311/module2.html": {
        "subject": "NETC311",
        "module": "Module 2: Basic Switch & End Device Configuration"
    },
    "hmby311/module1.html": {
        "subject": "HMBY311",
        "module": "Module 1: The Scientific Method & Basic Chemistry"
    },
    "atfl311/module1.html": {
        "subject": "ATFL311",
        "module": "Module 1: Introduction to Automata Theory & Chomsky Hierarchy"
    },
    "atfl311/module2.html": {
        "subject": "ATFL311",
        "module": "Module 2: Finite State Machines & Prerequisites"
    },
    "atfl311/module3.html": {
        "subject": "ATFL311",
        "module": "Module 3: Deterministic Finite Automata (DFA)"
    },
    "atfl311/module4.html": {
        "subject": "ATFL311",
        "module": "Module 4: Non-Deterministic Finite Automata & Conversions"
    },
}

BASE_DIR = "/home/javvii/YearIII/NETC311/quiz1"

def build_widget_html(subject_code, module_title):
    return f"""
<!-- REVIEWIII FOCUS SYSTEM WIDGET (Pomodoro + Automatic Time Tracking) -->
<style>
  @keyframes quiz-pill-ping {{
    75%, 100% {{
      transform: scale(2.2);
      opacity: 0;
    }}
  }}
  .quiz-focus-pill-btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    border-radius: 9999px;
    font-size: 12px;
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
    box-shadow: 0 0 14px rgba(138, 154, 134, 0.25);
  }}
  .quiz-focus-pill-btn.running-break {{
    border-color: rgba(168, 159, 145, 0.5);
    background: rgba(168, 159, 145, 0.15);
    color: #a89f91;
    box-shadow: 0 0 14px rgba(168, 159, 145, 0.25);
  }}
  #quiz-focus-modal {{
    position: fixed;
    top: 58px;
    right: 18px;
    z-index: 9999999;
    width: 320px;
    background: #0a0a0a;
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 12px;
    padding: 18px 20px;
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
      top: 56px;
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
    <div id="modal-digits" style="font-size: 42px; font-weight: 700; font-family: 'Inter', monospace; font-variant-numeric: tabular-nums; letter-spacing: -0.04em; color: #f0f0f0; line-height: 1;">25:00</div>
    <div id="modal-status-caption" style="font-size: 11px; color: #707070; text-transform: uppercase; letter-spacing: 0.06em; margin-top: 4px;">ready to study</div>
  </div>

  <div style="display: flex; gap: 8px; justify-content: center; margin-bottom: 14px;">
    <button type="button" id="modal-start-btn" style="background: #8a9a86; color: #000000; border: none; border-radius: 6px; font-size: 13px; font-weight: 600; padding: 8px 18px; cursor: pointer; flex: 1;">▶ Start</button>
    <button type="button" id="modal-reset-btn" style="background: transparent; border: 1px solid rgba(255,255,255,0.14); color: #a0a0a0; border-radius: 6px; font-size: 12px; padding: 8px 12px; cursor: pointer;">Reset</button>
    <button type="button" id="modal-skip-btn" style="background: transparent; border: 1px solid rgba(255,255,255,0.14); color: #a0a0a0; border-radius: 6px; font-size: 12px; padding: 8px 12px; cursor: pointer;">Skip &rarr;</button>
  </div>

  <div style="border-top: 1px solid rgba(255,255,255,0.08); padding-top: 10px; font-size: 11px; color: #707070; display: flex; justify-content: space-between; align-items: center;">
    <span style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 190px;" title="{subject_code} &bull; {module_title}">
      📍 <strong>{subject_code}</strong>: {module_title}
    </span>
    <a href="../../index.html#focus-timer" style="color: #8a9a86; text-decoration: none; font-weight: 500;">Hub Stats &nearr;</a>
  </div>
</div>

<script src="../../scripts/focus-system.js"></script>
<script>
  (function initQuizFocusIntegration() {{
    var subjectCode = "{subject_code}";
    var moduleTitle = "{module_title}";

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
      if (phase === 'short') return settings.shortBreakSeconds || 300;
      if (phase === 'long') return settings.longBreakSeconds || 900;
      return settings.focusSeconds || 1500;
    }}

    function updatePill(snap) {{
      if (!pillBtn) return;
      if (!snap || !snap.running) {{
        pillBtn.className = 'quiz-focus-pill-btn';
        if (pingEl) pingEl.style.display = 'none';
        if (iconEl) iconEl.textContent = '⏱️';
        if (timeEl) timeEl.textContent = 'Focus';
        return;
      }}
      var now = Date.now();
      var remaining = snap.endsAt ? Math.max(0, Math.ceil((snap.endsAt - now) / 1000)) : snap.secondsLeft;
      var isFocus = snap.phase === 'focus';
      pillBtn.className = 'quiz-focus-pill-btn ' + (isFocus ? 'running-focus' : 'running-break');
      if (pingEl) pingEl.style.display = 'inline-flex';
      if (iconEl) iconEl.textContent = F.PHASE_EMOJIS[snap.phase] || (isFocus ? '🎯' : '☕');
      if (timeEl) timeEl.textContent = F.formatTime(remaining);
    }}

    function updateModal(snap) {{
      if (!modal) return;
      var isFocus = snap.phase === 'focus';
      var now = Date.now();
      var remaining = snap.endsAt ? Math.max(0, Math.ceil((snap.endsAt - now) / 1000)) : snap.secondsLeft;

      if (digitsEl) digitsEl.textContent = F.formatTime(remaining);
      if (phaseEmoji) phaseEmoji.textContent = F.PHASE_EMOJIS[snap.phase] || (isFocus ? '🎯' : '☕');
      if (phaseTitle) phaseTitle.textContent = F.PHASE_LABELS[snap.phase] || 'FOCUS';
      if (sessionCount) {{
        sessionCount.textContent = isFocus ? ('· Session ' + (snap.focusCount + 1)) : '';
      }}
      if (statusCaption) {{
        statusCaption.textContent = snap.running ? 'running' : 'paused';
      }}
      if (startBtn) {{
        if (snap.running) {{
          startBtn.textContent = '⏸ Pause';
          startBtn.style.background = '#a89f91';
        }} else {{
          startBtn.textContent = '▶ Start';
          startBtn.style.background = '#8a9a86';
        }}
      }}
      if (soundBtn) {{
        soundBtn.textContent = settings.soundEnabled ? '🔊' : '🔇';
      }}
    }}

    function tick() {{
      if (!snapshot.running || snapshot.endsAt == null) return;
      var now = Date.now();
      var remaining = Math.ceil((snapshot.endsAt - now) / 1000);
      if (remaining <= 0) {{
        snapshot.secondsLeft = 0;
        snapshot.endsAt = null;
        completeSegment();
      }} else {{
        snapshot.secondsLeft = remaining;
      }}
      updatePill(snapshot);
      updateModal(snapshot);
    }}

    function completeSegment() {{
      if (snapshot.phase === 'focus') {{
        F.playFocusChime('break');
        var durationSecs = getPhaseDuration('focus');
        var mins = Math.max(1, Math.round(durationSecs / 60));
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
      var curTot = getPhaseDuration(snapshot.phase);
      var elap = curTot - snapshot.secondsLeft;
      if (snapshot.phase === 'focus') {{
        F.playFocusChime('break');
        if (elap >= 60) {{
          var mins = Math.max(1, Math.round(elap / 60));
          F.logTime(mins, snapshot.subjectCode || subjectCode, snapshot.moduleTitle || moduleTitle, 'pomodoro');
        }}
        var breakPhase = snapshot.focusCount % 4 === 0 && snapshot.focusCount > 0 ? 'long' : 'short';
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

    // Listeners
    if (pillBtn && modal) {{
      pillBtn.addEventListener('click', function(e) {{
        e.preventDefault();
        var isHidden = modal.style.display === 'none' || !modal.style.display;
        modal.style.display = isHidden ? 'block' : 'none';
        if (isHidden) updateModal(snapshot);
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

    // Visibility sync
    document.addEventListener('visibilitychange', function() {{
      if (document.visibilityState === 'visible' && snapshot.running && snapshot.endsAt != null) {{
        tick();
      }}
    }});

    // Subscribe to multi-tab focus events
    F.subscribeFocus(function(newSnap) {{
      if (!newSnap) return;
      snapshot = newSnap;
      updatePill(snapshot);
      updateModal(snapshot);
    }});

    // Initial render & interval
    updatePill(snapshot);
    updateModal(snapshot);
    setInterval(tick, 1000);
  }})();
</script>
"""

def process_file(rel_path, spec):
    full_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(full_path):
        print(f"Skipping {rel_path} (not found)")
        return
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Clean out existing widget if previously injected
    content = re.sub(r'<!-- REVIEWIII FOCUS SYSTEM WIDGET.*?initQuizFocusIntegration\(\);\s*</script>', '', content, flags=re.DOTALL)

    # 2. Inject pill into header: find the right buttons group inside #quiz-hub-nav
    # In #quiz-hub-nav, there's `<div style="display: flex; align-items: center; gap: ...;">`
    # Check if quiz-focus-pill is already in nav; if not, add it
    if 'id="quiz-focus-pill"' not in content:
        pill_html = """
        <!-- Focus Pill Injected into Quiz Header -->
        <button id="quiz-focus-pill" type="button" class="quiz-focus-pill-btn" title="Open Focus Timer & Time Tracker">
          <span id="quiz-pill-ping" style="display: none; position: relative; width: 8px; height: 8px;">
            <span style="position: absolute; width: 100%; height: 100%; border-radius: 50%; background: currentColor; opacity: 0.6; animation: quiz-pill-ping 1.5s infinite;"></span>
            <span style="position: relative; width: 8px; height: 8px; border-radius: 50%; background: currentColor;"></span>
          </span>
          <span id="quiz-pill-icon">⏱️</span>
          <span id="quiz-pill-time">Focus</span>
        </button>
        """
        # Insert pill at the beginning of the right-hand nav group
        # Look for `<a href="../../index.html" ...>Hub Overview</a>`
        m = re.search(r'(<a\s+href="\.\./\.\./index\.html"[^>]*>Hub Overview</a>)', content)
        if m:
            content = content[:m.start()] + pill_html + content[m.start():]
        else:
            # Fallback: search for #quiz-hub-nav closing </header>
            m_header = re.search(r'</header>', content)
            if m_header:
                content = content[:m_header.start()] + pill_html + content[m_header.start():]

    # 3. Inject Widget & Script right before </body>
    widget_code = build_widget_html(spec["subject"], spec["module"])
    body_close_idx = content.rfind('</body>')
    if body_close_idx != -1:
        content = content[:body_close_idx] + widget_code + "\n" + content[body_close_idx:]
    else:
        content += widget_code

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {rel_path} with Focus Widget!")

for rel_subpath, spec in QUIZ_SPECS.items():
    # Update in public/quizzes/
    process_file(os.path.join("public/quizzes", rel_subpath), spec)
    # Update in quizzes/
    process_file(os.path.join("quizzes", rel_subpath), spec)

print("All quiz files successfully updated with Focus & Time Tracking system!")
