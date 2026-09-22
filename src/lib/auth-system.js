// ============================================================================
// ReviewIII Multi-User GitHub Authentication & Session Isolation Manager
// Enables multiple users to log in via GitHub, switch accounts, and isolate
// study sessions, quiz progress, pomodoro timers, and logs per user.
// ============================================================================

export const ACCOUNTS_STORAGE_KEY = 'reviewiii_accounts:v1';
export const ACTIVE_USER_STORAGE_KEY = 'reviewiii_active_user:v1';
export const AUTH_CHANNEL_NAME = 'reviewiii_auth_channel';

export const GUEST_USER = {
  id: 'guest',
  username: 'Guest',
  displayName: 'Guest Student',
  avatarUrl: '',
  bio: 'Local anonymous session',
  profileUrl: '',
  isGuest: true
};

const listeners = new Set();
let authChannel = null;

if (typeof window !== 'undefined' && 'BroadcastChannel' in window) {
  try {
    authChannel = new BroadcastChannel(AUTH_CHANNEL_NAME);
    authChannel.onmessage = (event) => {
      if (event.data && event.data.type === 'auth_changed') {
        notifyListeners(event.data.activeUser);
      }
    };
  } catch (e) {}
}

if (typeof window !== 'undefined') {
  window.addEventListener('storage', (e) => {
    if (e.key === ACTIVE_USER_STORAGE_KEY || e.key === ACCOUNTS_STORAGE_KEY) {
      notifyListeners(getActiveAccount());
    }
  });
}

function notifyListeners(user) {
  listeners.forEach((cb) => {
    try {
      cb(user || getActiveAccount());
    } catch (err) {
      console.error('Error in auth listener:', err);
    }
  });
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('reviewiii:auth_changed', {
      detail: { user: user || getActiveAccount() }
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

export function getActiveUserId() {
  if (typeof window === 'undefined') return 'guest';
  try {
    const id = localStorage.getItem(ACTIVE_USER_STORAGE_KEY);
    return id && typeof id === 'string' ? id : 'guest';
  } catch (e) {
    return 'guest';
  }
}

export function getAccounts() {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(ACCOUNTS_STORAGE_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch (e) {
    return [];
  }
}

export function getActiveAccount() {
  const activeId = getActiveUserId();
  if (!activeId || activeId === 'guest') {
    return { ...GUEST_USER };
  }
  const accounts = getAccounts();
  const found = accounts.find((acc) => acc.id === activeId);
  if (found) {
    return { ...found, isGuest: false };
  }
  // Fallback to guest if account not found
  return { ...GUEST_USER };
}

/**
 * Returns a storage key namespaced by the active user.
 * If active user is 'guest', returns the baseKey directly to preserve
 * 100% backward compatibility with existing guest sessions.
 */
export function getStorageKey(baseKey) {
  const activeId = getActiveUserId();
  if (!activeId || activeId === 'guest') {
    return baseKey;
  }
  const safeId = activeId.toLowerCase().replace(/[^a-z0-9_-]/g, '_');
  return `reviewiii_u_${safeId}_${baseKey}`;
}

/**
 * Log in / connect via GitHub username or Personal Access Token
 */
export async function loginWithGitHub(usernameInput, tokenInput = '') {
  if (typeof window === 'undefined') return null;

  const username = (usernameInput || '').trim();
  const token = (tokenInput || '').trim();

  if (!username && !token) {
    throw new Error('Please provide a GitHub username or Personal Access Token.');
  }

  let profileData = null;

  // 1. Fetch from GitHub API
  try {
    const headers = {
      'Accept': 'application/vnd.github.v3+json'
    };
    if (token) {
      headers['Authorization'] = `token ${token}`;
    }

    const apiUrl = token && !username
      ? 'https://api.github.com/user'
      : `https://api.github.com/users/${encodeURIComponent(username)}`;

    const res = await fetch(apiUrl, { headers });

    if (res.status === 404) {
      throw new Error(`GitHub user "${username}" was not found.`);
    }

    if (res.status === 401) {
      throw new Error('Invalid GitHub Personal Access Token.');
    }

    if (res.ok) {
      const data = await res.json();
      profileData = {
        id: `github:${data.login.toLowerCase()}`,
        username: data.login,
        displayName: data.name || data.login,
        avatarUrl: data.avatar_url,
        bio: data.bio || '',
        profileUrl: data.html_url || `https://github.com/${data.login}`,
        publicRepos: typeof data.public_repos === 'number' ? data.public_repos : 0,
        token: token || null,
        connectedAt: Date.now(),
        lastActiveAt: Date.now()
      };
    } else {
      // If rate limited or other non-fatal error, build offline fallback profile
      profileData = createFallbackProfile(username, token);
    }
  } catch (err) {
    if (err.message && (err.message.includes('not found') || err.message.includes('Invalid GitHub'))) {
      throw err;
    }
    // Network / offline fallback
    profileData = createFallbackProfile(username, token);
  }

  // 2. Persist to accounts list
  const currentAccounts = getAccounts();
  const existingIdx = currentAccounts.findIndex((a) => a.id === profileData.id);
  if (existingIdx >= 0) {
    currentAccounts[existingIdx] = { ...currentAccounts[existingIdx], ...profileData };
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
}

function createFallbackProfile(username, token) {
  const safeName = username || 'User';
  return {
    id: `github:${safeName.toLowerCase()}`,
    username: safeName,
    displayName: safeName,
    avatarUrl: `https://github.com/${safeName}.png`,
    bio: 'GitHub Connected Student',
    profileUrl: `https://github.com/${safeName}`,
    publicRepos: 0,
    token: token || null,
    connectedAt: Date.now(),
    lastActiveAt: Date.now()
  };
}

export function switchAccount(userId) {
  if (typeof window === 'undefined') return;

  if (userId === 'guest') {
    try {
      localStorage.setItem(ACTIVE_USER_STORAGE_KEY, 'guest');
    } catch (e) {}
    broadcastAuthChange(GUEST_USER);
    return;
  }

  const accounts = getAccounts();
  const target = accounts.find((a) => a.id === userId);
  if (target) {
    target.lastActiveAt = Date.now();
    try {
      localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(accounts));
      localStorage.setItem(ACTIVE_USER_STORAGE_KEY, target.id);
    } catch (e) {}
    broadcastAuthChange(target);
  }
}

export function removeAccount(userId) {
  if (typeof window === 'undefined') return;

  let accounts = getAccounts();
  accounts = accounts.filter((a) => a.id !== userId);

  try {
    localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(accounts));
  } catch (e) {}

  if (getActiveUserId() === userId) {
    switchAccount('guest');
  } else {
    broadcastAuthChange(getActiveAccount());
  }
}

export function subscribeAuth(callback) {
  listeners.add(callback);
  return () => listeners.delete(callback);
}

// Global attachment for browser scripts
if (typeof window !== 'undefined') {
  const g = window;
  g.ReviewIIIAuth = {
    ACCOUNTS_STORAGE_KEY,
    ACTIVE_USER_STORAGE_KEY,
    GUEST_USER,
    getActiveUserId,
    getActiveAccount,
    getAccounts,
    getStorageKey,
    loginWithGitHub,
    switchAccount,
    removeAccount,
    subscribeAuth
  };
}
