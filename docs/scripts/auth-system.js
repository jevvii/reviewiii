// ============================================================================
// ReviewIII Multi-User GitHub Authentication & Strict Zero-Guest Gate
// Client-side Browser Script (attaches to window.ReviewIIIAuth)
// ============================================================================
(function (global) {
  'use strict';

  var SUPABASE_URL = 'https://uenxceusckmokmqhrkby.supabase.co';
  // Supabase anon key (public by design — safe for client-side use)
  var SUPABASE_ANON_KEY = 'sb_publishable_OCUPoA1pEFODxzOUoTD8aA_HevquQfY';
  var ACCOUNTS_STORAGE_KEY = 'reviewiii_accounts:v1';
  var ACTIVE_USER_STORAGE_KEY = 'reviewiii_active_user:v1';
  var AUTH_CHANNEL_NAME = 'reviewiii_auth_channel';

  var listeners = new Set();
  var authChannel = null;

  if (typeof window !== 'undefined' && 'BroadcastChannel' in window) {
    try {
      authChannel = new BroadcastChannel(AUTH_CHANNEL_NAME);
      authChannel.onmessage = function (event) {
        if (event.data && event.data.type === 'auth_changed') {
          notifyListeners(event.data.activeUser);
          ensureAuthGate();
        }
      };
    } catch (e) {}
  }

  if (typeof window !== 'undefined') {
    window.addEventListener('storage', function (e) {
      if (e.key === ACTIVE_USER_STORAGE_KEY || e.key === ACCOUNTS_STORAGE_KEY) {
        notifyListeners(getActiveAccount());
        ensureAuthGate();
      }
    });
  }

  function notifyListeners(user) {
    var current = user || getActiveAccount();
    listeners.forEach(function (cb) {
      try {
        cb(current);
      } catch (err) {
        console.error('Error in auth listener:', err);
      }
    });
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('reviewiii:auth_changed', {
        detail: { user: current }
      }));
    }
  }

  function broadcastAuthChange(user) {
    if (authChannel) {
      try {
        authChannel.postMessage({ type: 'auth_changed', activeUser: user });
      } catch (e) {}
    }
    notifyListeners(user);
  }

  function getAccounts() {
    if (typeof window === 'undefined') return [];
    try {
      var raw = localStorage.getItem(ACCOUNTS_STORAGE_KEY);
      if (!raw) return [];
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed.filter(function (a) { return a && a.id && a.id !== 'guest'; }) : [];
    } catch (e) {
      return [];
    }
  }

  function getActiveUserId() {
    if (typeof window === 'undefined') return null;
    try {
      var id = localStorage.getItem(ACTIVE_USER_STORAGE_KEY);
      if (!id || id === 'guest') {
        if (id === 'guest') {
          localStorage.removeItem(ACTIVE_USER_STORAGE_KEY);
        }
        return null;
      }
      var accounts = getAccounts();
      var exists = accounts.some(function (acc) { return acc.id === id; });
      if (!exists) {
        localStorage.removeItem(ACTIVE_USER_STORAGE_KEY);
        return null;
      }
      return id;
    } catch (e) {
      return null;
    }
  }

  function getActiveAccount() {
    var activeId = getActiveUserId();
    if (!activeId) return null;
    var accounts = getAccounts();
    var found = accounts.find(function (acc) { return acc.id === activeId; });
    return found || null;
  }

  function isAuthenticated() {
    return Boolean(getActiveAccount());
  }

  function getStorageKey(baseKey) {
    var activeUser = getActiveAccount();
    if (!activeUser || !activeUser.id) {
      return 'reviewiii_u_unauth_' + baseKey;
    }
    var safeId = activeUser.id.toLowerCase().replace(/[^a-z0-9_-]/g, '_');
    return 'reviewiii_u_' + safeId + '_' + baseKey;
  }

  function startGitHubOAuth(returnUrl) {
    if (typeof window === 'undefined') return;
    var current = returnUrl || window.location.href.split('#')[0];
    try {
      localStorage.setItem('reviewiii_oauth_return', current);
    } catch (e) {}

    var authUrl = SUPABASE_URL + '/auth/v1/authorize?provider=github&redirect_to=' + encodeURIComponent(current);
    window.location.href = authUrl;
  }

  async function handleOAuthCallback() {
    if (typeof window === 'undefined') return null;
    var hash = window.location.hash;
    if (!hash || !hash.includes('access_token=')) return null;

    try {
      var params = new URLSearchParams(hash.replace(/^#/, ''));
      var accessToken = params.get('access_token');
      var refreshToken = params.get('refresh_token');

      if (!accessToken) return null;

      updateGateStatus('Verifying GitHub OAuth credentials...', false);

      var profileData = null;

      try {
        var res = await fetch(SUPABASE_URL + '/auth/v1/user', {
          headers: {
            'Authorization': 'Bearer ' + accessToken,
            'apikey': SUPABASE_ANON_KEY
          }
        });

        if (res.ok) {
          var userData = await res.json();
          var meta = userData.user_metadata || {};
          var username = meta.user_name || meta.preferred_username || (userData.email ? userData.email.split('@')[0] : 'github_student');
          var displayName = meta.full_name || meta.name || username;
          var avatarUrl = meta.avatar_url || ('https://github.com/' + username + '.png');

          profileData = {
            id: 'github:' + username.toLowerCase(),
            username: username,
            displayName: displayName,
            avatarUrl: avatarUrl,
            bio: meta.bio || 'Verified GitHub Student',
            profileUrl: 'https://github.com/' + username,
            authType: 'oauth',
            token: accessToken,
            refreshToken: refreshToken || null,
            connectedAt: Date.now(),
            lastActiveAt: Date.now()
          };
        }
      } catch (fetchErr) {
        console.warn('Could not fetch /auth/v1/user, decoding JWT payload fallback:', fetchErr);
      }

      if (!profileData) {
        try {
          var payloadBase64 = accessToken.split('.')[1];
          var payloadJson = JSON.parse(atob(payloadBase64.replace(/-/g, '+').replace(/_/g, '/')));
          var meta2 = payloadJson.user_metadata || {};
          var username2 = meta2.user_name || meta2.preferred_username || (payloadJson.email ? payloadJson.email.split('@')[0] : 'github_student');

          profileData = {
            id: 'github:' + username2.toLowerCase(),
            username: username2,
            displayName: meta2.full_name || meta2.name || username2,
            avatarUrl: meta2.avatar_url || ('https://github.com/' + username2 + '.png'),
            bio: meta2.bio || 'Verified GitHub Student',
            profileUrl: 'https://github.com/' + username2,
            authType: 'oauth',
            token: accessToken,
            refreshToken: refreshToken || null,
            connectedAt: Date.now(),
            lastActiveAt: Date.now()
          };
        } catch (jwtErr) {
          console.error('Failed to parse access token:', jwtErr);
        }
      }

      if (!profileData) {
        throw new Error('Unable to extract GitHub profile from OAuth token.');
      }

      saveAccountProfile(profileData);

      try {
        if (window.history && window.history.replaceState) {
          window.history.replaceState(null, '', window.location.pathname + window.location.search);
        }
      } catch (e) {}

      var savedReturn = localStorage.getItem('reviewiii_oauth_return');
      if (savedReturn) {
        localStorage.removeItem('reviewiii_oauth_return');
        if (savedReturn !== window.location.href && savedReturn.startsWith(window.location.origin)) {
          window.location.href = savedReturn;
          return profileData;
        }
      }

      broadcastAuthChange(profileData);
      ensureAuthGate();
      return profileData;
    } catch (err) {
      console.error('OAuth Callback Exception:', err);
      updateGateStatus(err.message || 'GitHub OAuth failed.', true);
      return null;
    }
  }

  async function loginWithGitHub(usernameInput, tokenInput) {
    if (typeof window === 'undefined') return null;

    var username = (usernameInput || '').trim();
    var token = (tokenInput || '').trim();

    if (!username && !token) {
      throw new Error('Please provide a GitHub username or Personal Access Token.');
    }

    var profileData = null;

    try {
      var headers = {
        'Accept': 'application/vnd.github.v3+json'
      };
      if (token) {
        headers['Authorization'] = 'token ' + token;
      }

      var apiUrl = token && !username
        ? 'https://api.github.com/user'
        : 'https://api.github.com/users/' + encodeURIComponent(username);

      var res = await fetch(apiUrl, { headers: headers });

      if (res.status === 404) {
        throw new Error('GitHub user "' + username + '" was not found.');
      }

      if (res.status === 401) {
        throw new Error('Invalid GitHub Personal Access Token.');
      }

      if (res.ok) {
        var data = await res.json();
        profileData = {
          id: 'github:' + data.login.toLowerCase(),
          username: data.login,
          displayName: data.name || data.login,
          avatarUrl: data.avatar_url,
          bio: data.bio || '',
          profileUrl: data.html_url || ('https://github.com/' + data.login),
          publicRepos: typeof data.public_repos === 'number' ? data.public_repos : 0,
          token: token || null,
          authType: 'api',
          connectedAt: Date.now(),
          lastActiveAt: Date.now()
        };
      } else {
        profileData = createFallbackProfile(username, token);
      }
    } catch (err) {
      if (err.message && (err.message.includes('not found') || err.message.includes('Invalid GitHub'))) {
        throw err;
      }
      profileData = createFallbackProfile(username, token);
    }

    saveAccountProfile(profileData);
    broadcastAuthChange(profileData);
    ensureAuthGate();
    return profileData;
  }

  function createFallbackProfile(username, token) {
    var safeName = username || 'User';
    return {
      id: 'github:' + safeName.toLowerCase(),
      username: safeName,
      displayName: safeName,
      avatarUrl: 'https://github.com/' + safeName + '.png',
      bio: 'GitHub Connected Student',
      profileUrl: 'https://github.com/' + safeName,
      publicRepos: 0,
      token: token || null,
      authType: 'fallback',
      connectedAt: Date.now(),
      lastActiveAt: Date.now()
    };
  }

  function saveAccountProfile(profileData) {
    var currentAccounts = getAccounts();
    var existingIdx = currentAccounts.findIndex(function (a) { return a.id === profileData.id; });
    if (existingIdx >= 0) {
      currentAccounts[existingIdx] = Object.assign({}, currentAccounts[existingIdx], profileData);
    } else {
      currentAccounts.push(profileData);
    }

    try {
      localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(currentAccounts));
      localStorage.setItem(ACTIVE_USER_STORAGE_KEY, profileData.id);
    } catch (err) {
      console.error('Failed to save account:', err);
    }
  }

  function switchAccount(userId) {
    if (typeof window === 'undefined') return;
    if (!userId || userId === 'guest') return;

    var accounts = getAccounts();
    var target = accounts.find(function (a) { return a.id === userId; });
    if (target) {
      target.lastActiveAt = Date.now();
      try {
        localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(accounts));
        localStorage.setItem(ACTIVE_USER_STORAGE_KEY, target.id);
      } catch (e) {}
      broadcastAuthChange(target);
      ensureAuthGate();
    }
  }

  function removeAccount(userId) {
    if (typeof window === 'undefined') return;

    var accounts = getAccounts();
    accounts = accounts.filter(function (a) { return a.id !== userId; });

    try {
      localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(accounts));
    } catch (e) {}

    if (getActiveUserId() === userId) {
      if (accounts.length > 0) {
        switchAccount(accounts[0].id);
      } else {
        try {
          localStorage.removeItem(ACTIVE_USER_STORAGE_KEY);
        } catch (e) {}
        broadcastAuthChange(null);
        ensureAuthGate();
      }
    } else {
      broadcastAuthChange(getActiveAccount());
    }
  }

  function logout() {
    if (typeof window === 'undefined') return;
    try {
      localStorage.removeItem(ACTIVE_USER_STORAGE_KEY);
    } catch (e) {}
    broadcastAuthChange(null);
    ensureAuthGate();
  }

  function subscribeAuth(callback) {
    listeners.add(callback);
    return function () { listeners.delete(callback); };
  }

  function injectGateStyles() {
    if (typeof document === 'undefined') return;
    if (document.getElementById('reviewiii-auth-styles')) return;

    var style = document.createElement('style');
    style.id = 'reviewiii-auth-styles';
    style.textContent = `
      body.auth-locked > :not(#reviewiii-auth-gate) {
        filter: blur(16px) grayscale(0.6) !important;
        pointer-events: none !important;
        user-select: none !important;
        opacity: 0.1 !important;
        transition: filter 0.3s ease, opacity 0.3s ease !important;
      }

      #reviewiii-auth-gate {
        position: fixed;
        inset: 0;
        z-index: 999999;
        background: rgba(0, 0, 0, 0.94);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 16px;
        box-sizing: border-box;
        animation: reviewiiiFadeIn 0.25s ease-out;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }

      @keyframes reviewiiiFadeIn {
        from { opacity: 0; transform: scale(0.98); }
        to { opacity: 1; transform: scale(1); }
      }

      .reviewiii-gate-card {
        max-width: 440px;
        width: 100%;
        background: #080808;
        border: 1px solid rgba(255, 255, 255, 0.14);
        border-radius: 16px;
        padding: 32px 28px;
        box-shadow: 0 32px 80px rgba(0, 0, 0, 0.9), 0 0 0 1px rgba(138, 154, 134, 0.15);
        color: #f0f0f0;
        box-sizing: border-box;
        position: relative;
      }

      .reviewiii-gate-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 10.5px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #8a9a86;
        background: rgba(138, 154, 134, 0.1);
        border: 1px solid rgba(138, 154, 134, 0.25);
        border-radius: 999px;
        padding: 4px 10px;
        margin-bottom: 16px;
      }

      .reviewiii-gate-title {
        font-size: 22px;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #ffffff;
        margin: 0 0 8px 0;
      }

      .reviewiii-gate-sub {
        font-size: 13px;
        line-height: 1.55;
        color: #888888;
        margin: 0 0 24px 0;
      }

      .reviewiii-oauth-btn {
        width: 100%;
        height: 48px;
        background: #f0f0f0;
        color: #000000;
        font-size: 14px;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        transition: all 0.15s ease;
        text-decoration: none;
        box-sizing: border-box;
      }

      .reviewiii-oauth-btn:hover {
        background: #ffffff;
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(255, 255, 255, 0.18);
      }

      .reviewiii-oauth-btn:active {
        transform: translateY(0);
      }

      .reviewiii-oauth-pill {
        font-size: 10px;
        font-weight: 700;
        background: #000000;
        color: #ffffff;
        padding: 2px 7px;
        border-radius: 999px;
        letter-spacing: 0.05em;
      }

      .reviewiii-gate-divider {
        display: flex;
        align-items: center;
        text-align: center;
        margin: 22px 0 18px 0;
        color: #444444;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
      }

      .reviewiii-gate-divider::before,
      .reviewiii-gate-divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      }

      .reviewiii-gate-divider span {
        padding: 0 12px;
      }

      .reviewiii-gate-field {
        margin-bottom: 12px;
        text-align: left;
      }

      .reviewiii-gate-field label {
        display: block;
        font-size: 11px;
        font-weight: 500;
        color: #888888;
        margin-bottom: 5px;
      }

      .reviewiii-gate-input-wrap {
        position: relative;
        display: flex;
        align-items: center;
      }

      .reviewiii-gate-prefix {
        position: absolute;
        left: 12px;
        color: #666666;
        font-size: 14px;
        font-family: monospace;
        pointer-events: none;
      }

      .reviewiii-gate-field input {
        width: 100%;
        height: 42px;
        background: #111111;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 8px;
        color: #ffffff;
        font-size: 13px;
        padding: 0 12px 0 32px;
        box-sizing: border-box;
        outline: none;
        transition: border-color 0.15s ease;
        font-family: inherit;
      }

      .reviewiii-gate-field input:focus {
        border-color: #8a9a86;
        background: #141414;
      }

      .reviewiii-gate-form-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
        margin-top: 14px;
      }

      .reviewiii-pat-link {
        background: none;
        border: none;
        color: #777777;
        font-size: 11.5px;
        cursor: pointer;
        text-decoration: underline;
        padding: 0;
      }

      .reviewiii-pat-link:hover {
        color: #aaaaaa;
      }

      .reviewiii-gate-submit-btn {
        height: 40px;
        padding: 0 20px;
        background: #181818;
        border: 1px solid rgba(255, 255, 255, 0.18);
        color: #f0f0f0;
        font-size: 13px;
        font-weight: 600;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.15s ease;
      }

      .reviewiii-gate-submit-btn:hover {
        background: #222222;
        border-color: #8a9a86;
        color: #ffffff;
      }

      .reviewiii-gate-status {
        min-height: 20px;
        font-size: 12px;
        margin-top: 14px;
        text-align: center;
        color: #8a9a86;
        display: none;
      }

      .reviewiii-gate-status.error {
        color: #f87171;
      }

      .reviewiii-gate-policy {
        margin-top: 22px;
        padding-top: 16px;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        font-size: 11px;
        line-height: 1.5;
        color: #666666;
        text-align: left;
        display: flex;
        gap: 8px;
        align-items: flex-start;
      }

      .reviewiii-gate-policy .policy-icon {
        font-size: 12px;
        margin-top: 1px;
      }

      .reviewiii-gate-policy strong {
        color: #999999;
      }
    `;
    document.head.appendChild(style);
  }

  function updateGateStatus(msg, isError) {
    var el = document.getElementById('reviewiii-gate-status');
    if (!el) return;
    if (!msg) {
      el.style.display = 'none';
      el.textContent = '';
      return;
    }
    el.textContent = msg;
    el.className = 'reviewiii-gate-status' + (isError ? ' error' : '');
    el.style.display = 'block';
  }

  function ensureAuthGate() {
    if (typeof document === 'undefined') return;
    injectGateStyles();

    var authenticated = isAuthenticated();
    var gateEl = document.getElementById('reviewiii-auth-gate');

    if (authenticated) {
      if (document.body) document.body.classList.remove('auth-locked');
      if (gateEl) {
        gateEl.remove();
      }
      return;
    }

    if (document.body) document.body.classList.add('auth-locked');

    if (gateEl) {
      gateEl.style.display = 'flex';
      return;
    }

    gateEl = document.createElement('div');
    gateEl.id = 'reviewiii-auth-gate';
    gateEl.innerHTML = `
      <div class="reviewiii-gate-card">
        <div class="reviewiii-gate-badge">
          <span>✦</span>
          <span>ReviewIII Workstation</span>
        </div>
        <h2 class="reviewiii-gate-title">Sign In to ReviewIII</h2>
        <p class="reviewiii-gate-sub">
          Authorized academic portal for Year III Computer Science. All students are required to authenticate with GitHub before accessing question banks, interactive quizzes, offline vaults, and personal Pomodoro study logs.
        </p>

        <button type="button" id="reviewiii-gate-oauth-btn" class="reviewiii-oauth-btn">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
            <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
          </svg>
          <span>Continue with GitHub</span>
          <span class="reviewiii-oauth-pill">OAuth</span>
        </button>

        <div class="reviewiii-gate-divider">
          <span>or sign in with username</span>
        </div>

        <form id="reviewiii-gate-form" class="reviewiii-gate-form">
          <div class="reviewiii-gate-field">
            <label for="reviewiii-gate-user">GitHub Username</label>
            <div class="reviewiii-gate-input-wrap">
              <span class="reviewiii-gate-prefix">@</span>
              <input type="text" id="reviewiii-gate-user" placeholder="e.g. jevvii, student-name" autocomplete="username" required />
            </div>
          </div>

          <div id="reviewiii-gate-pat-wrap" class="reviewiii-gate-field" style="display: none;">
            <label for="reviewiii-gate-pat">Personal Access Token (optional)</label>
            <input type="password" id="reviewiii-gate-pat" placeholder="ghp_xxxxxxxxxxxx" autocomplete="current-password" />
          </div>

          <div class="reviewiii-gate-form-row">
            <button type="button" id="reviewiii-gate-pat-toggle" class="reviewiii-pat-link">Use PAT Token</button>
            <button type="submit" id="reviewiii-gate-submit" class="reviewiii-gate-submit-btn">Sign In &rarr;</button>
          </div>
        </form>

        <div id="reviewiii-gate-status" class="reviewiii-gate-status"></div>

        <div class="reviewiii-gate-policy">
          <span class="policy-icon">🔒</span>
          <span><strong>Zero-Guest Policy Enforced</strong>: Guest accounts are strictly disabled. Your quiz state, answers, and study logs are isolated to your personal GitHub account.</span>
        </div>
      </div>
    `;

    if (document.body) {
      document.body.appendChild(gateEl);
    } else {
      document.addEventListener('DOMContentLoaded', function () {
        document.body.appendChild(gateEl);
      });
    }

    var oauthBtn = document.getElementById('reviewiii-gate-oauth-btn');
    if (oauthBtn) {
      oauthBtn.addEventListener('click', function () {
        updateGateStatus('Redirecting to GitHub OAuth...', false);
        startGitHubOAuth();
      });
    }

    var patToggle = document.getElementById('reviewiii-gate-pat-toggle');
    var patWrap = document.getElementById('reviewiii-gate-pat-wrap');
    if (patToggle) {
      patToggle.addEventListener('click', function () {
        if (!patWrap) return;
        var isHidden = patWrap.style.display === 'none';
        patWrap.style.display = isHidden ? 'block' : 'none';
        patToggle.textContent = isHidden ? 'Hide PAT Field' : 'Use PAT Token';
      });
    }

    var form = document.getElementById('reviewiii-gate-form');
    var userInput = document.getElementById('reviewiii-gate-user');
    var patInput = document.getElementById('reviewiii-gate-pat');
    var submitBtn = document.getElementById('reviewiii-gate-submit');

    if (form) {
      form.addEventListener('submit', async function (e) {
        e.preventDefault();
        var u = userInput ? userInput.value.trim() : '';
        var p = patInput ? patInput.value.trim() : '';

        if (!u && !p) return;

        if (submitBtn) {
          submitBtn.setAttribute('disabled', 'true');
          submitBtn.textContent = 'Verifying...';
        }
        updateGateStatus('Verifying GitHub account...', false);

        try {
          await loginWithGitHub(u, p);
          updateGateStatus('Authenticated! Loading workspace...', false);
        } catch (err) {
          updateGateStatus(err.message || 'Failed to authenticate.', true);
          if (submitBtn) {
            submitBtn.removeAttribute('disabled');
            submitBtn.textContent = 'Sign In →';
          }
        }
      });
    }
  }

  // Attach ReviewIIIAuth to global
  global.ReviewIIIAuth = {
    SUPABASE_URL: SUPABASE_URL,
    SUPABASE_ANON_KEY: SUPABASE_ANON_KEY,
    ACCOUNTS_STORAGE_KEY: ACCOUNTS_STORAGE_KEY,
    ACTIVE_USER_STORAGE_KEY: ACTIVE_USER_STORAGE_KEY,
    getActiveUserId: getActiveUserId,
    getActiveAccount: getActiveAccount,
    getAccounts: getAccounts,
    getStorageKey: getStorageKey,
    isAuthenticated: isAuthenticated,
    startGitHubOAuth: startGitHubOAuth,
    handleOAuthCallback: handleOAuthCallback,
    loginWithGitHub: loginWithGitHub,
    switchAccount: switchAccount,
    removeAccount: removeAccount,
    logout: logout,
    subscribeAuth: subscribeAuth,
    ensureAuthGate: ensureAuthGate
  };

  // Immediate execution on script load
  if (typeof window !== 'undefined') {
    if (window.location.hash && window.location.hash.includes('access_token=')) {
      handleOAuthCallback();
    } else {
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () {
          ensureAuthGate();
        });
      } else {
        ensureAuthGate();
      }
    }
  }
})(typeof window !== 'undefined' ? window : this);
