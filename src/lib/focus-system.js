// ============================================================================
// ReviewIII Focus System & Automatic Time Tracking
// Inspired by Study Tracker (focus-timer, focus-session, focus-audio, time)
// Digital Sobriety & Pitch-Black OLED compatible
// ============================================================================

export const FOCUS_STORAGE_KEY = 'reviewiii_focus:v1';
export const TIME_LOGS_STORAGE_KEY = 'reviewiii_timelogs:v1';
export const SETTINGS_STORAGE_KEY = 'reviewiii_settings:v1';

export const DEFAULT_SECONDS = {
  focus: 1500, // 25 minutes
  short: 300,  // 5 minutes
  long: 900    // 15 minutes
};

export const PHASE_LABELS = {
  focus: 'Focus',
  short: 'Short Break',
  long: 'Long Break'
};

export const PHASE_EMOJIS = {
  focus: '🎯',
  short: '☕',
  long: '☕'
};

export const MANILA_TZ = 'Asia/Manila';

/**
 * Returns YYYY-MM-DD calendar date in Asia/Manila (UTC+8) for the given instant.
 */
export function manilaDateKey(d = new Date()) {
  try {
    return new Intl.DateTimeFormat('en-CA', {
      timeZone: MANILA_TZ,
      year: 'numeric',
      month: '2-digit',
      day: '2-digit'
    }).format(d);
  } catch (e) {
    return d.toISOString().slice(0, 10);
  }
}

/**
 * Formats seconds into MM:SS (or HH:MM:SS if >= 3600)
 */
export function formatTime(seconds) {
  const s = Math.max(0, Math.floor(seconds));
  const hrs = Math.floor(s / 3600);
  const mins = Math.floor((s % 3600) / 60);
  const secs = s % 60;
  const pad = (n) => (n < 10 ? `0${n}` : `${n}`);
  if (hrs > 0) {
    return `${hrs}:${pad(mins)}:${pad(secs)}`;
  }
  return `${pad(mins)}:${pad(secs)}`;
}

/**
 * Formats minutes into e.g. "45m" or "1h 30m"
 */
export function formatMinutes(mins) {
  const m = Math.max(0, Math.round(mins));
  if (m < 60) return `${m}m`;
  const h = Math.floor(m / 60);
  const rem = m % 60;
  return rem > 0 ? `${h}h ${rem}m` : `${h}h`;
}

// ----------------------------------------------------------------------------
// Audio Synthesizer (Web Audio API) — Zero external audio assets needed
// ----------------------------------------------------------------------------

/**
 * Plays clean synthesized audio cues for Pomodoro transitions:
 *  - 'focus': Bright ascending C-major arpeggio (C5 -> E5 -> G5)
 *  - 'break': Soft descending triangle wave (A4 -> E4)
 *  - 'set':   Sustained C-major chord + high C6 bell
 */
export function playFocusChime(kind, force = false) {
  if (typeof window === 'undefined') return;
  const settings = readSettings();
  if (!force && settings.soundEnabled === false) return;

  try {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) return;
    const ctx = new AudioContextClass();
    if (ctx.state === 'suspended') {
      ctx.resume().catch(() => {});
    }

    const voice = (freq, start, dur, peak, type = 'sine') => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.frequency.value = freq;
      osc.type = type;
      const t0 = ctx.currentTime + start;
      gain.gain.setValueAtTime(0.0001, t0);
      gain.gain.exponentialRampToValueAtTime(peak, t0 + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
      osc.connect(gain).connect(ctx.destination);
      osc.start(t0);
      osc.stop(t0 + dur + 0.02);
    };

    if (kind === 'focus') {
      voice(523.25, 0.0, 0.30, 0.20); // C5
      voice(659.25, 0.12, 0.30, 0.20); // E5
      voice(783.99, 0.24, 0.40, 0.22); // G5
    } else if (kind === 'break') {
      voice(440.00, 0.0, 0.45, 0.16, 'triangle'); // A4
      voice(329.63, 0.24, 0.55, 0.16, 'triangle'); // E4
    } else {
      // Sustained C-major chord (C5+E5+G5) with a high C6 bell on top
      voice(523.25, 0.0, 0.70, 0.18); // C5
      voice(659.25, 0.0, 0.70, 0.16); // E5
      voice(783.99, 0.0, 0.70, 0.16); // G5
      voice(1046.50, 0.06, 0.80, 0.20); // C6 bell
    }

    setTimeout(() => {
      ctx.close().catch(() => {});
    }, 2000);
  } catch (err) {
    // Audio contexts may fail without user gesture; gracefully ignore
  }
}

// ----------------------------------------------------------------------------
// Settings Storage
// ----------------------------------------------------------------------------

export function readSettings() {
  if (typeof window === 'undefined') {
    return {
      focusSeconds: DEFAULT_SECONDS.focus,
      shortBreakSeconds: DEFAULT_SECONDS.short,
      longBreakSeconds: DEFAULT_SECONDS.long,
      soundEnabled: true,
      autoStartBreaks: true,
      autoStartFocus: true
    };
  }
  try {
    const raw = localStorage.getItem(SETTINGS_STORAGE_KEY);
    if (!raw) {
      return {
        focusSeconds: DEFAULT_SECONDS.focus,
        shortBreakSeconds: DEFAULT_SECONDS.short,
        longBreakSeconds: DEFAULT_SECONDS.long,
        soundEnabled: true,
        autoStartBreaks: true,
        autoStartFocus: true
      };
    }
    const data = JSON.parse(raw);
    return {
      focusSeconds: Number(data.focusSeconds) || DEFAULT_SECONDS.focus,
      shortBreakSeconds: Number(data.shortBreakSeconds) || DEFAULT_SECONDS.short,
      longBreakSeconds: Number(data.longBreakSeconds) || DEFAULT_SECONDS.long,
      soundEnabled: data.soundEnabled !== false,
      autoStartBreaks: data.autoStartBreaks !== false,
      autoStartFocus: data.autoStartFocus !== false
    };
  } catch {
    return {
      focusSeconds: DEFAULT_SECONDS.focus,
      shortBreakSeconds: DEFAULT_SECONDS.short,
      longBreakSeconds: DEFAULT_SECONDS.long,
      soundEnabled: true,
      autoStartBreaks: true,
      autoStartFocus: true
    };
  }
}

export function saveSettings(settings) {
  if (typeof window === 'undefined') return;
  try {
    const existing = readSettings();
    const updated = { ...existing, ...settings };
    localStorage.setItem(SETTINGS_STORAGE_KEY, JSON.stringify(updated));
    broadcastStorageEvent('settings', updated);
  } catch (err) {
    console.error('Failed to save settings:', err);
  }
}

// ----------------------------------------------------------------------------
// Time Logs Storage & Tracking
// ----------------------------------------------------------------------------

export function readTimeLogs() {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(TIME_LOGS_STORAGE_KEY);
    if (!raw) return [];
    const logs = JSON.parse(raw);
    return Array.isArray(logs) ? logs : [];
  } catch {
    return [];
  }
}

export function logTime(minutes, subjectCode = 'General Study', moduleTitle = 'Self Review', mode = 'pomodoro', date = null) {
  if (typeof window === 'undefined') return null;
  const mins = Math.max(1, Math.round(minutes));
  const logDate = date || manilaDateKey();
  const entry = {
    id: 'log_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7),
    date: logDate,
    timestamp: Date.now(),
    isoTime: new Date().toISOString(),
    minutes: mins,
    subjectCode: subjectCode || 'General Study',
    moduleTitle: moduleTitle || 'Self Review',
    mode: mode // 'pomodoro' | 'quick-log' | 'quiz'
  };

  try {
    const current = readTimeLogs();
    current.unshift(entry);
    // Keep last 300 logs
    const trimmed = current.slice(0, 300);
    localStorage.setItem(TIME_LOGS_STORAGE_KEY, JSON.stringify(trimmed));
    broadcastStorageEvent('time_log', entry);
    return entry;
  } catch (err) {
    console.error('Failed to log time:', err);
    return null;
  }
}

export function getTodayTimeLogs() {
  const today = manilaDateKey();
  const logs = readTimeLogs();
  return logs.filter(l => l.date === today);
}

export function getTodayMinutes() {
  const todayLogs = getTodayTimeLogs();
  return todayLogs.reduce((acc, l) => acc + (Number(l.minutes) || 0), 0);
}

export function getSubjectStats() {
  const logs = readTimeLogs();
  const stats = {};
  for (const l of logs) {
    const subj = l.subjectCode || 'General Study';
    if (!stats[subj]) {
      stats[subj] = { subjectCode: subj, totalMinutes: 0, sessionCount: 0 };
    }
    stats[subj].totalMinutes += Number(l.minutes) || 0;
    stats[subj].sessionCount += 1;
  }
  return Object.values(stats).sort((a, b) => b.totalMinutes - a.totalMinutes);
}

export function clearTimeLogs() {
  if (typeof window === 'undefined') return;
  try {
    localStorage.removeItem(TIME_LOGS_STORAGE_KEY);
    broadcastStorageEvent('time_log', null);
  } catch {}
}

// ----------------------------------------------------------------------------
// Focus Session State & Pub/Sub
// ----------------------------------------------------------------------------

export function readFocusSnapshot() {
  if (typeof window === 'undefined') return null;
  try {
    const raw = localStorage.getItem(FOCUS_STORAGE_KEY);
    if (!raw) return null;
    const s = JSON.parse(raw);
    if (s.v !== 1) return null;
    if (s.phase !== 'focus' && s.phase !== 'short' && s.phase !== 'long') return null;
    const endsAt = typeof s.endsAt === 'number' && Number.isFinite(s.endsAt) ? s.endsAt : null;
    let secondsLeft = typeof s.secondsLeft === 'number' && Number.isFinite(s.secondsLeft)
      ? Math.max(0, Math.round(s.secondsLeft)) : 0;
    if (Boolean(s.running) && endsAt) {
      secondsLeft = Math.max(0, Math.ceil((endsAt - Date.now()) / 1000));
    }
    return {
      v: 1,
      phase: s.phase,
      running: Boolean(s.running),
      focusCount: Number(s.focusCount) || 0,
      subjectCode: typeof s.subjectCode === 'string' ? s.subjectCode : 'General Study',
      moduleTitle: typeof s.moduleTitle === 'string' ? s.moduleTitle : 'Comprehensive Review',
      secondsLeft,
      endsAt,
      updatedAt: s.updatedAt || Date.now()
    };
  } catch {
    return null;
  }
}

export function saveFocusSnapshot(snap) {
  if (typeof window === 'undefined') return;
  try {
    if (!snap) {
      localStorage.removeItem(FOCUS_STORAGE_KEY);
      publishFocus(null);
      return;
    }
    const data = {
      v: 1,
      phase: snap.phase,
      running: Boolean(snap.running),
      focusCount: Number(snap.focusCount) || 0,
      subjectCode: snap.subjectCode || 'General Study',
      moduleTitle: snap.moduleTitle || 'Comprehensive Review',
      secondsLeft: Math.max(0, Math.round(snap.secondsLeft)),
      endsAt: snap.running ? snap.endsAt : null,
      updatedAt: Date.now()
    };
    localStorage.setItem(FOCUS_STORAGE_KEY, JSON.stringify(data));
    publishFocus(data);
  } catch (err) {
    console.error('Failed to save focus snapshot:', err);
  }
}

const listeners = new Set();

export function subscribeFocus(callback) {
  listeners.add(callback);
  return () => {
    listeners.delete(callback);
  };
}

export function publishFocus(snap) {
  for (const cb of listeners) {
    try {
      cb(snap);
    } catch (e) {
      console.error(e);
    }
  }
  broadcastStorageEvent('focus_session', snap);
}

// Cross-tab synchronization via BroadcastChannel & Storage Event
let channel = null;
if (typeof window !== 'undefined' && 'BroadcastChannel' in window) {
  try {
    channel = new BroadcastChannel('reviewiii_focus_channel');
    channel.onmessage = (event) => {
      if (event.data?.type === 'focus_session') {
        const snap = event.data.payload;
        for (const cb of listeners) cb(snap);
      }
    };
  } catch {}
}

function broadcastStorageEvent(type, payload) {
  if (channel) {
    try {
      channel.postMessage({ type, payload });
    } catch {}
  }
}

export const INTERNAL_NAV_KEY = 'reviewiii_nav_internal';

export function markInternalNav() {
  if (typeof window === 'undefined') return;
  try {
    sessionStorage.setItem(INTERNAL_NAV_KEY, String(Date.now()));
  } catch {}
}

export function isInternalNav() {
  if (typeof window === 'undefined') return false;
  try {
    const t = sessionStorage.getItem(INTERNAL_NAV_KEY);
    if (t) {
      const elapsed = Date.now() - parseInt(t, 10);
      if (elapsed >= 0 && elapsed < 15000) {
        return true;
      }
    }
  } catch {}
  return false;
}

export function clearInternalNav() {
  if (typeof window === 'undefined') return;
  try {
    sessionStorage.removeItem(INTERNAL_NAV_KEY);
  } catch {}
}

export function pauseFocusOnExit() {
  if (typeof window === 'undefined') return;
  if (isInternalNav()) {
    return; // Do not pause focus during internal navigation
  }
  try {
    const raw = localStorage.getItem(FOCUS_STORAGE_KEY);
    if (!raw) return;
    const snap = JSON.parse(raw);
    if (snap && snap.running) {
      let remaining = snap.secondsLeft;
      if (typeof snap.endsAt === 'number' && snap.endsAt > 0) {
        remaining = Math.max(0, Math.round((snap.endsAt - Date.now()) / 1000));
      }
      snap.running = false;
      snap.secondsLeft = remaining;
      snap.endsAt = null;
      snap.updatedAt = Date.now();
      localStorage.setItem(FOCUS_STORAGE_KEY, JSON.stringify(snap));
    }
  } catch {}
}

if (typeof window !== 'undefined') {
  // Clear the internal nav flag shortly after landing on the page
  setTimeout(clearInternalNav, 1500);

  // Capture clicks on all internal links so internal page hops never pause focus
  document.addEventListener('click', (e) => {
    const target = e.target;
    const a = target && target.closest ? target.closest('a') : null;
    if (a && a.href) {
      try {
        const targetUrl = new URL(a.href, window.location.href);
        if (targetUrl.origin === window.location.origin) {
          markInternalNav();
        }
      } catch {}
    }
  }, true);

  window.addEventListener('storage', (e) => {
    if (e.key === FOCUS_STORAGE_KEY) {
      const snap = readFocusSnapshot();
      for (const cb of listeners) cb(snap);
    }
  });

  window.addEventListener('beforeunload', pauseFocusOnExit);
  window.addEventListener('pagehide', pauseFocusOnExit);

  // Expose on global ReviewIIIFocus if available
  const g = window;
  if (!g.ReviewIIIFocus) g.ReviewIIIFocus = {};
  Object.assign(g.ReviewIIIFocus, {
    markInternalNav,
    isInternalNav,
    clearInternalNav,
    pauseFocusOnExit,
    FOCUS_STORAGE_KEY,
    TIME_LOGS_STORAGE_KEY,
    SETTINGS_STORAGE_KEY,
    DEFAULT_SECONDS,
    PHASE_LABELS,
    PHASE_EMOJIS,
    manilaDateKey,
    formatTime,
    formatMinutes,
    playFocusChime,
    readSettings,
    saveSettings,
    readTimeLogs,
    logTime,
    getTodayTimeLogs,
    getTodayMinutes,
    getSubjectStats,
    clearTimeLogs,
    readFocusSnapshot,
    saveFocusSnapshot,
    subscribeFocus,
    publishFocus
  });
}
