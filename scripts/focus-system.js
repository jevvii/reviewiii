// ============================================================================
// ReviewIII Focus System & Automatic Time Tracking (Browser Bundle)
// Digital Sobriety & Pitch-Black OLED compatible
// Attaches to window.ReviewIIIFocus
// ============================================================================
(function (global) {
  'use strict';

  var FOCUS_STORAGE_KEY = 'reviewiii_focus:v1';
  var TIME_LOGS_STORAGE_KEY = 'reviewiii_timelogs:v1';
  var SETTINGS_STORAGE_KEY = 'reviewiii_settings:v1';

  var DEFAULT_SECONDS = {
    focus: 1500, // 25 minutes
    short: 300,  // 5 minutes
    long: 900    // 15 minutes
  };

  var PHASE_LABELS = {
    focus: 'Focus',
    short: 'Short Break',
    long: 'Long Break'
  };

  var PHASE_EMOJIS = {
    focus: '🎯',
    short: '☕',
    long: '☕'
  };

  var MANILA_TZ = 'Asia/Manila';

  function manilaDateKey(d) {
    d = d || new Date();
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

  function formatTime(seconds) {
    var s = Math.max(0, Math.floor(seconds));
    var hrs = Math.floor(s / 3600);
    var mins = Math.floor((s % 3600) / 60);
    var secs = s % 60;
    var pad = function (n) { return (n < 10 ? '0' + n : '' + n); };
    if (hrs > 0) {
      return hrs + ':' + pad(mins) + ':' + pad(secs);
    }
    return pad(mins) + ':' + pad(secs);
  }

  function formatMinutes(mins) {
    var m = Math.max(0, Math.round(mins));
    if (m < 60) return m + 'm';
    var h = Math.floor(m / 60);
    var rem = m % 60;
    return rem > 0 ? h + 'h ' + rem + 'm' : h + 'h';
  }

  function readSettings() {
    try {
      var raw = localStorage.getItem(SETTINGS_STORAGE_KEY);
      if (!raw) return getDefaultSettings();
      var data = JSON.parse(raw);
      return {
        focusSeconds: Number(data.focusSeconds) || DEFAULT_SECONDS.focus,
        shortBreakSeconds: Number(data.shortBreakSeconds) || DEFAULT_SECONDS.short,
        longBreakSeconds: Number(data.longBreakSeconds) || DEFAULT_SECONDS.long,
        soundEnabled: data.soundEnabled !== false,
        autoStartBreaks: data.autoStartBreaks !== false,
        autoStartFocus: data.autoStartFocus !== false
      };
    } catch (e) {
      return getDefaultSettings();
    }
  }

  function getDefaultSettings() {
    return {
      focusSeconds: DEFAULT_SECONDS.focus,
      shortBreakSeconds: DEFAULT_SECONDS.short,
      longBreakSeconds: DEFAULT_SECONDS.long,
      soundEnabled: true,
      autoStartBreaks: true,
      autoStartFocus: true
    };
  }

  function saveSettings(settings) {
    try {
      var existing = readSettings();
      var updated = Object.assign({}, existing, settings);
      localStorage.setItem(SETTINGS_STORAGE_KEY, JSON.stringify(updated));
      broadcastStorageEvent('settings', updated);
    } catch (err) {
      console.error('Failed to save settings:', err);
    }
  }

  function playFocusChime(kind, force) {
    var settings = readSettings();
    if (!force && settings.soundEnabled === false) return;

    try {
      var AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (!AudioContextClass) return;
      var ctx = new AudioContextClass();
      if (ctx.state === 'suspended') {
        ctx.resume().catch(function () {});
      }

      var voice = function (freq, start, dur, peak, type) {
        type = type || 'sine';
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();
        osc.frequency.value = freq;
        osc.type = type;
        var t0 = ctx.currentTime + start;
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
        // 'set'
        voice(523.25, 0.0, 0.70, 0.18); // C5
        voice(659.25, 0.0, 0.70, 0.16); // E5
        voice(783.99, 0.0, 0.70, 0.16); // G5
        voice(1046.50, 0.06, 0.80, 0.20); // C6 bell
      }

      setTimeout(function () {
        ctx.close().catch(function () {});
      }, 2000);
    } catch (err) {}
  }

  function readTimeLogs() {
    try {
      var raw = localStorage.getItem(TIME_LOGS_STORAGE_KEY);
      if (!raw) return [];
      var logs = JSON.parse(raw);
      return Array.isArray(logs) ? logs : [];
    } catch (e) {
      return [];
    }
  }

  function logTime(minutes, subjectCode, moduleTitle, mode, date) {
    var mins = Math.max(1, Math.round(minutes));
    var logDate = date || manilaDateKey();
    var entry = {
      id: 'log_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7),
      date: logDate,
      timestamp: Date.now(),
      isoTime: new Date().toISOString(),
      minutes: mins,
      subjectCode: subjectCode || 'General Study',
      moduleTitle: moduleTitle || 'Self Review',
      mode: mode || 'pomodoro'
    };

    try {
      var current = readTimeLogs();
      current.unshift(entry);
      var trimmed = current.slice(0, 300);
      localStorage.setItem(TIME_LOGS_STORAGE_KEY, JSON.stringify(trimmed));
      broadcastStorageEvent('time_log', entry);
      return entry;
    } catch (err) {
      console.error('Failed to log time:', err);
      return null;
    }
  }

  function getTodayTimeLogs() {
    var today = manilaDateKey();
    var logs = readTimeLogs();
    return logs.filter(function (l) { return l.date === today; });
  }

  function getTodayMinutes() {
    var logs = getTodayTimeLogs();
    return logs.reduce(function (acc, l) { return acc + (Number(l.minutes) || 0); }, 0);
  }

  function getSubjectStats() {
    var logs = readTimeLogs();
    var stats = {};
    for (var i = 0; i < logs.length; i++) {
      var l = logs[i];
      var subj = l.subjectCode || 'General Study';
      if (!stats[subj]) {
        stats[subj] = { subjectCode: subj, totalMinutes: 0, sessionCount: 0 };
      }
      stats[subj].totalMinutes += Number(l.minutes) || 0;
      stats[subj].sessionCount += 1;
    }
    return Object.values(stats).sort(function (a, b) { return b.totalMinutes - a.totalMinutes; });
  }

  function clearTimeLogs() {
    try {
      localStorage.removeItem(TIME_LOGS_STORAGE_KEY);
      broadcastStorageEvent('time_log', null);
    } catch (e) {}
  }

  function readFocusSnapshot() {
    try {
      var raw = localStorage.getItem(FOCUS_STORAGE_KEY);
      if (!raw) return null;
      var s = JSON.parse(raw);
      if (s.v !== 1) return null;
      if (s.phase !== 'focus' && s.phase !== 'short' && s.phase !== 'long') return null;
      var endsAt = typeof s.endsAt === 'number' && Number.isFinite(s.endsAt) ? s.endsAt : null;
      var secondsLeft = typeof s.secondsLeft === 'number' && Number.isFinite(s.secondsLeft)
        ? Math.max(0, Math.round(s.secondsLeft)) : 0;
      return {
        v: 1,
        phase: s.phase,
        running: Boolean(s.running),
        focusCount: Number(s.focusCount) || 0,
        subjectCode: typeof s.subjectCode === 'string' ? s.subjectCode : 'General Study',
        moduleTitle: typeof s.moduleTitle === 'string' ? s.moduleTitle : 'Comprehensive Review',
        secondsLeft: secondsLeft,
        endsAt: endsAt,
        updatedAt: s.updatedAt || Date.now()
      };
    } catch (e) {
      return null;
    }
  }

  function saveFocusSnapshot(snap) {
    try {
      if (!snap) {
        localStorage.removeItem(FOCUS_STORAGE_KEY);
        publishFocus(null);
        return;
      }
      var data = {
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

  var listeners = new Set();

  function subscribeFocus(callback) {
    listeners.add(callback);
    return function () { listeners.delete(callback); };
  }

  function publishFocus(snap) {
    listeners.forEach(function (cb) {
      try { cb(snap); } catch (e) {}
    });
    broadcastStorageEvent('focus_session', snap);
  }

  var channel = null;
  if ('BroadcastChannel' in window) {
    try {
      channel = new BroadcastChannel('reviewiii_focus_channel');
      channel.onmessage = function (event) {
        if (event.data && event.data.type === 'focus_session') {
          var snap = event.data.payload;
          listeners.forEach(function (cb) {
            try { cb(snap); } catch (e) {}
          });
        }
      };
    } catch (e) {}
  }

  function broadcastStorageEvent(type, payload) {
    if (channel) {
      try { channel.postMessage({ type: type, payload: payload }); } catch (e) {}
    }
  }

  window.addEventListener('storage', function (e) {
    if (e.key === FOCUS_STORAGE_KEY) {
      var snap = readFocusSnapshot();
      listeners.forEach(function (cb) {
        try { cb(snap); } catch (err) {}
      });
    }
  });

  // Export to global object
  global.ReviewIIIFocus = {
    FOCUS_STORAGE_KEY: FOCUS_STORAGE_KEY,
    TIME_LOGS_STORAGE_KEY: TIME_LOGS_STORAGE_KEY,
    SETTINGS_STORAGE_KEY: SETTINGS_STORAGE_KEY,
    DEFAULT_SECONDS: DEFAULT_SECONDS,
    PHASE_LABELS: PHASE_LABELS,
    PHASE_EMOJIS: PHASE_EMOJIS,
    manilaDateKey: manilaDateKey,
    formatTime: formatTime,
    formatMinutes: formatMinutes,
    playFocusChime: playFocusChime,
    readSettings: readSettings,
    saveSettings: saveSettings,
    readTimeLogs: readTimeLogs,
    logTime: logTime,
    getTodayTimeLogs: getTodayTimeLogs,
    getTodayMinutes: getTodayMinutes,
    getSubjectStats: getSubjectStats,
    clearTimeLogs: clearTimeLogs,
    readFocusSnapshot: readFocusSnapshot,
    saveFocusSnapshot: saveFocusSnapshot,
    subscribeFocus: subscribeFocus,
    publishFocus: publishFocus
  };
})(typeof window !== 'undefined' ? window : this);
