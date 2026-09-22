// ============================================================================
// ReviewIII Multi-User GitHub Authentication & Session Isolation (Browser Bundle)
// Attaches to window.ReviewIIIAuth
// ============================================================================
(function (global) {
  'use strict';

  var ACCOUNTS_STORAGE_KEY = 'reviewiii_accounts:v1';
  var ACTIVE_USER_STORAGE_KEY = 'reviewiii_active_user:v1';
  var AUTH_CHANNEL_NAME = 'reviewiii_auth_channel';

  var GUEST_USER = {
    id: 'guest',
    username: 'Guest',
    displayName: 'Guest Student',
    avatarUrl: '',
    bio: 'Local anonymous session',
    profileUrl: '',
    isGuest: true
  };

  var listeners = new Set();
  var authChannel = null;

  if (typeof window !== 'undefined' && 'BroadcastChannel' in window) {
    try {
      authChannel = new BroadcastChannel(AUTH_CHANNEL_NAME);
      authChannel.onmessage = function (event) {
        if (event.data && event.data.type === 'auth_changed') {
          notifyListeners(event.data.activeUser);
        }
      };
    } catch (e) {}
  }

  function notifyListeners(user) {
    var resolvedUser = user || getActiveAccount();
    listeners.forEach(function (cb) {
      try {
        cb(resolvedUser);
      } catch (err) {
        console.error('Error in auth listener:', err);
      }
    });
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('reviewiii:auth_changed', {
        detail: { user: resolvedUser }
      }));
    }
  }

  if (typeof window !== 'undefined') {
    window.addEventListener('storage', function (e) {
      if (e.key === ACTIVE_USER_STORAGE_KEY || e.key === ACCOUNTS_STORAGE_KEY) {
        notifyListeners(getActiveAccount());
      }
    });
  }

  function broadcastAuthChange(user) {
    if (authChannel) {
      try {
        authChannel.postMessage({ type: 'auth_changed', activeUser: user });
      } catch (e) {}
    }
    notifyListeners(user);
  }

  function getActiveUserId() {
    if (typeof window === 'undefined') return 'guest';
    try {
      var id = localStorage.getItem(ACTIVE_USER_STORAGE_KEY);
      return id && typeof id === 'string' ? id : 'guest';
    } catch (e) {
      return 'guest';
    }
  }

  function getAccounts() {
    if (typeof window === 'undefined') return [];
    try {
      var raw = localStorage.getItem(ACCOUNTS_STORAGE_KEY);
      if (!raw) return [];
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  }

  function getActiveAccount() {
    var activeId = getActiveUserId();
    if (!activeId || activeId === 'guest') {
      return Object.assign({}, GUEST_USER);
    }
    var accounts = getAccounts();
    for (var i = 0; i < accounts.length; i++) {
      if (accounts[i].id === activeId) {
        return Object.assign({}, accounts[i], { isGuest: false });
      }
    }
    return Object.assign({}, GUEST_USER);
  }

  function getStorageKey(baseKey) {
    var activeId = getActiveUserId();
    if (!activeId || activeId === 'guest') {
      return baseKey;
    }
    var safeId = activeId.toLowerCase().replace(/[^a-z0-9_-]/g, '_');
    return 'reviewiii_u_' + safeId + '_' + baseKey;
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
      connectedAt: Date.now(),
      lastActiveAt: Date.now()
    };
  }

  function loginWithGitHub(usernameInput, tokenInput) {
    if (typeof window === 'undefined') return Promise.resolve(null);

    var username = (usernameInput || '').trim();
    var token = (tokenInput || '').trim();

    if (!username && !token) {
      return Promise.reject(new Error('Please provide a GitHub username or Personal Access Token.'));
    }

    var headers = {
      'Accept': 'application/vnd.github.v3+json'
    };
    if (token) {
      headers['Authorization'] = 'token ' + token;
    }

    var apiUrl = token && !username
      ? 'https://api.github.com/user'
      : 'https://api.github.com/users/' + encodeURIComponent(username);

    return fetch(apiUrl, { headers: headers })
      .then(function (res) {
        if (res.status === 404) {
          throw new Error('GitHub user "' + username + '" was not found.');
        }
        if (res.status === 401) {
          throw new Error('Invalid GitHub Personal Access Token.');
        }
        if (res.ok) {
          return res.json().then(function (data) {
            return {
              id: 'github:' + data.login.toLowerCase(),
              username: data.login,
              displayName: data.name || data.login,
              avatarUrl: data.avatar_url,
              bio: data.bio || '',
              profileUrl: data.html_url || ('https://github.com/' + data.login),
              publicRepos: typeof data.public_repos === 'number' ? data.public_repos : 0,
              token: token || null,
              connectedAt: Date.now(),
              lastActiveAt: Date.now()
            };
          });
        }
        return createFallbackProfile(username, token);
      })
      .catch(function (err) {
        if (err.message && (err.message.indexOf('not found') !== -1 || err.message.indexOf('Invalid GitHub') !== -1)) {
          throw err;
        }
        return createFallbackProfile(username, token);
      })
      .then(function (profileData) {
        var currentAccounts = getAccounts();
        var existingIdx = -1;
        for (var i = 0; i < currentAccounts.length; i++) {
          if (currentAccounts[i].id === profileData.id) {
            existingIdx = i;
            break;
          }
        }
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

        broadcastAuthChange(profileData);
        return profileData;
      });
  }

  function switchAccount(userId) {
    if (typeof window === 'undefined') return;

    if (userId === 'guest') {
      try {
        localStorage.setItem(ACTIVE_USER_STORAGE_KEY, 'guest');
      } catch (e) {}
      broadcastAuthChange(GUEST_USER);
      return;
    }

    var accounts = getAccounts();
    var target = null;
    for (var i = 0; i < accounts.length; i++) {
      if (accounts[i].id === userId) {
        target = accounts[i];
        break;
      }
    }
    if (target) {
      target.lastActiveAt = Date.now();
      try {
        localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(accounts));
        localStorage.setItem(ACTIVE_USER_STORAGE_KEY, target.id);
      } catch (e) {}
      broadcastAuthChange(target);
    }
  }

  function removeAccount(userId) {
    if (typeof window === 'undefined') return;

    var accounts = getAccounts().filter(function (a) { return a.id !== userId; });
    try {
      localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(accounts));
    } catch (e) {}

    if (getActiveUserId() === userId) {
      switchAccount('guest');
    } else {
      broadcastAuthChange(getActiveAccount());
    }
  }

  function subscribeAuth(callback) {
    listeners.add(callback);
    return function () { listeners.delete(callback); };
  }

  global.ReviewIIIAuth = {
    ACCOUNTS_STORAGE_KEY: ACCOUNTS_STORAGE_KEY,
    ACTIVE_USER_STORAGE_KEY: ACTIVE_USER_STORAGE_KEY,
    GUEST_USER: GUEST_USER,
    getActiveUserId: getActiveUserId,
    getActiveAccount: getActiveAccount,
    getAccounts: getAccounts,
    getStorageKey: getStorageKey,
    loginWithGitHub: loginWithGitHub,
    switchAccount: switchAccount,
    removeAccount: removeAccount,
    subscribeAuth: subscribeAuth
  };
})(typeof window !== 'undefined' ? window : this);
