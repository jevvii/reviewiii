const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const PORT = 4410;
const DOCS_DIR = path.resolve(__dirname, '../docs');

// Static HTTP server for docs/
const server = http.createServer((req, res) => {
  let reqPath = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
  if (reqPath.startsWith('/reviewiii/')) {
    reqPath = reqPath.slice('/reviewiii'.length);
  } else if (reqPath === '/reviewiii') {
    reqPath = '/';
  }
  if (reqPath === '/' || reqPath === '') reqPath = '/index.html';
  if (reqPath.endsWith('/')) reqPath += 'index.html';

  let filePath = path.join(DOCS_DIR, reqPath);
  if (!fs.existsSync(filePath) && fs.existsSync(filePath + '.html')) {
    filePath += '.html';
  }

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    const mimeTypes = {
      '.html': 'text/html; charset=utf-8',
      '.js': 'application/javascript; charset=utf-8',
      '.css': 'text/css; charset=utf-8',
      '.json': 'application/json; charset=utf-8',
      '.svg': 'image/svg+xml',
      '.pdf': 'application/pdf',
      '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    };
    res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found: ' + reqPath);
  }
});

async function runTests() {
  await new Promise((resolve) => server.listen(PORT, resolve));
  console.log(`[TEST] HTTP Server listening at http://localhost:${PORT}`);

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 }
  });
  const page = await context.newPage();

  try {
    // ------------------------------------------------------------------------
    // Test 1: Zero-Guest Policy Enforcement on Unauthenticated Home Page Visit
    // ------------------------------------------------------------------------
    console.log('[TEST 1] Testing Zero-Guest Policy on Home Page...');
    // Clear all storage to ensure fresh unauthenticated visit
    await page.goto(`http://localhost:${PORT}/index.html`);
    await page.evaluate(() => localStorage.clear());
    await page.reload();
    await page.waitForTimeout(500);

    // 1.1 Verify body is locked
    const isLocked = await page.evaluate(() => document.body.classList.contains('auth-locked'));
    console.log('  Body has auth-locked class:', isLocked);
    if (!isLocked) {
      throw new Error('Expected document.body to have class "auth-locked" when unauthenticated.');
    }

    // 1.2 Verify Auth Gate overlay is present and visible
    const gateLocator = page.locator('#reviewiii-auth-gate');
    const isGateVisible = await gateLocator.isVisible();
    console.log('  #reviewiii-auth-gate visible:', isGateVisible);
    if (!isGateVisible) {
      throw new Error('#reviewiii-auth-gate overlay is not visible on unauthenticated visit.');
    }

    // 1.3 Verify Gate contents
    const gateTitle = await gateLocator.locator('.reviewiii-gate-title').textContent();
    console.log('  Gate title:', gateTitle?.trim());
    if (!gateTitle?.includes('Sign In to ReviewIII')) {
      throw new Error(`Unexpected gate title: ${gateTitle}`);
    }

    // 1.4 Verify "Continue with GitHub" OAuth button exists
    const oauthBtn = page.locator('#reviewiii-gate-oauth-btn');
    const hasOAuthBtn = await oauthBtn.isVisible();
    console.log('  OAuth button visible:', hasOAuthBtn);
    if (!hasOAuthBtn) {
      throw new Error('Continue with GitHub OAuth button missing from Auth Gate.');
    }

    // 1.5 Verify NO "Guest" or "Continue as Guest" option exists anywhere
    const guestButtons = await page.locator('text=Guest Session').count();
    const guestModeBtns = await page.locator('#auth-guest-mode-btn').count();
    console.log('  Guest session buttons count:', guestButtons + guestModeBtns);
    if (guestButtons > 0 || guestModeBtns > 0) {
      throw new Error('Guest session option is present in DOM, violating zero-guest policy.');
    }

    console.log('  ✓ Zero-guest policy verified: Unauthenticated visitors are strictly locked out!');

    // ------------------------------------------------------------------------
    // Test 2: Standalone Quiz Auth Gate Protection
    // ------------------------------------------------------------------------
    console.log('[TEST 2] Testing Standalone Quiz Auth Gate Protection...');
    await page.goto(`http://localhost:${PORT}/quizzes/netc311/module3.html`);
    await page.waitForTimeout(500);

    const quizLocked = await page.evaluate(() => document.body.classList.contains('auth-locked'));
    const quizGateVisible = await page.locator('#reviewiii-auth-gate').isVisible();
    console.log('  Quiz body has auth-locked class:', quizLocked);
    console.log('  Quiz auth gate visible:', quizGateVisible);

    if (!quizLocked || !quizGateVisible) {
      throw new Error('Standalone quiz failed to enforce auth gate on unauthenticated access.');
    }
    console.log('  ✓ Standalone quizzes are strictly protected behind the Auth Gate!');

    // ------------------------------------------------------------------------
    // Test 3: Sign In with GitHub via Direct Form
    // ------------------------------------------------------------------------
    console.log('[TEST 3] Testing Sign In with GitHub...');
    await page.goto(`http://localhost:${PORT}/index.html`);
    await page.waitForTimeout(400);

    // Fill in username in the Auth Gate
    await page.fill('#reviewiii-gate-user', 'javvii');
    await page.click('#reviewiii-gate-submit');
    await page.waitForTimeout(800);

    // Gate should now be removed and body unlocked
    const isUnlockedAfterLogin = await page.evaluate(() => !document.body.classList.contains('auth-locked'));
    const gateGone = (await page.locator('#reviewiii-auth-gate').count()) === 0;
    console.log('  Page unlocked after sign in:', isUnlockedAfterLogin);
    console.log('  Auth Gate dissolved:', gateGone);

    if (!isUnlockedAfterLogin || !gateGone) {
      throw new Error('Auth Gate did not dissolve after successful login.');
    }

    // Verify Header Pill shows @javvii
    const pillText = await page.textContent('#auth-pill-label');
    console.log('  Header pill shows:', pillText?.trim());
    if (!pillText?.toLowerCase().includes('javvii')) {
      throw new Error(`Header pill does not show @javvii: ${pillText}`);
    }
    console.log('  ✓ Successfully signed in as @javvii and unlocked ReviewIII workspace!');

    // ------------------------------------------------------------------------
    // Test 4: Standalone Quiz Unlocked & Session Isolation
    // ------------------------------------------------------------------------
    console.log('[TEST 4] Testing Quiz Answer Storage Isolation under @javvii...');
    await page.goto(`http://localhost:${PORT}/quizzes/netc311/module3.html`);
    await page.waitForTimeout(600);

    // Verify quiz is unlocked for signed-in user
    const quizUnlockedForUser = await page.evaluate(() => !document.body.classList.contains('auth-locked'));
    console.log('  Quiz unlocked for @javvii:', quizUnlockedForUser);
    if (!quizUnlockedForUser) {
      throw new Error('Quiz remained locked for signed-in user.');
    }

    // Check storage key derivation
    const javviiStorageKey = await page.evaluate(() => {
      return window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
    });
    console.log('  Derived storage key for @javvii:', javviiStorageKey);
    if (!javviiStorageKey.includes('github_javvii')) {
      throw new Error(`Expected storage key to contain github_javvii, got: ${javviiStorageKey}`);
    }

    // Simulate answer saving for @javvii
    await page.evaluate((k) => {
      localStorage.setItem(k, JSON.stringify({
        userAnswers: { 0: 'A', 1: 'C', 2: 'B' },
        currentQuestionIndex: 2,
        sessionSeed: 12345
      }));
    }, javviiStorageKey);

    // ------------------------------------------------------------------------
    // Test 5: Switch to Second Student (@student2) & Verify Isolation
    // ------------------------------------------------------------------------
    console.log('[TEST 5] Testing Multi-User Switch & Isolation for @student2...');
    await page.evaluate(() => {
      window.ReviewIIIAuth.loginWithGitHub('student2');
    });
    await page.waitForTimeout(500);

    const student2StorageKey = await page.evaluate(() => {
      return window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
    });
    console.log('  Derived storage key for @student2:', student2StorageKey);
    if (!student2StorageKey.includes('github_student2')) {
      throw new Error(`Expected storage key to contain github_student2, got: ${student2StorageKey}`);
    }

    // Verify @student2 has NO answers from @javvii
    const student2SavedData = await page.evaluate((k) => localStorage.getItem(k), student2StorageKey);
    console.log('  @student2 saved data (should be null):', student2SavedData);
    if (student2SavedData !== null) {
      throw new Error('@student2 session is not empty, session bleeding detected!');
    }

    // Switch back to @javvii
    await page.evaluate(() => {
      window.ReviewIIIAuth.switchAccount('github:javvii');
    });
    await page.waitForTimeout(300);

    const javviiRestoredData = await page.evaluate((k) => localStorage.getItem(k), javviiStorageKey);
    const parsedJavvii = JSON.parse(javviiRestoredData);
    console.log('  @javvii restored answers count:', Object.keys(parsedJavvii.userAnswers).length);
    if (parsedJavvii.userAnswers[0] !== 'A' || parsedJavvii.userAnswers[1] !== 'C') {
      throw new Error('@javvii session data was corrupted after switching accounts.');
    }
    console.log('  ✓ Complete session isolation verified across multiple student accounts!');

    // ------------------------------------------------------------------------
    // Test 6: Sign Out & Strict Re-locking (Zero Guest)
    // ------------------------------------------------------------------------
    console.log('[TEST 6] Testing Sign Out & Mandatory Auth Gate Re-locking...');
    await page.goto(`http://localhost:${PORT}/index.html`);
    await page.waitForTimeout(500);

    // Open Header account dropdown
    await page.click('#header-auth-pill');
    await page.waitForTimeout(300);

    // Verify Sign Out button is visible and NO Guest button exists
    const hasSignOutBtn = await page.locator('#auth-signout-btn').isVisible();
    const hasGuestBtn = await page.locator('#auth-guest-mode-btn').count();
    console.log('  Sign Out button visible in dropdown:', hasSignOutBtn);
    console.log('  Guest button in dropdown (should be 0):', hasGuestBtn);

    if (!hasSignOutBtn || hasGuestBtn > 0) {
      throw new Error('Dropdown does not conform to zero-guest policy.');
    }

    // Click Sign Out via JS (element is outside viewport in headless mode)
    await page.evaluate(() => document.querySelector('#auth-signout-btn').click());
    await page.waitForTimeout(500);

    // Verify page immediately re-locks with Auth Gate
    const isRelocked = await page.evaluate(() => document.body.classList.contains('auth-locked'));
    const isGateReopened = await page.locator('#reviewiii-auth-gate').isVisible();
    console.log('  Page re-locked with auth-locked class:', isRelocked);
    console.log('  #reviewiii-auth-gate re-opened:', isGateReopened);

    if (!isRelocked || !isGateReopened) {
      throw new Error('Page was not re-locked after signing out.');
    }

    // Reload page to verify persistence of unauthenticated lock
    await page.reload();
    await page.waitForTimeout(500);
    const stillLockedAfterReload = await page.evaluate(() => document.body.classList.contains('auth-locked'));
    console.log('  Still locked after page reload:', stillLockedAfterReload);
    if (!stillLockedAfterReload) {
      throw new Error('Auth Gate did not persist across page reload after sign out.');
    }
    console.log('  ✓ Zero-guest policy verified: Logging out immediately re-engages the mandatory gate!');

    // ------------------------------------------------------------------------
    // Test 7: OAuth Redirect Endpoint & Hash Handling Verification
    // ------------------------------------------------------------------------
    console.log('[TEST 7] Testing OAuth Redirect URL Construction & Hash Handling...');
    const oauthUrl = await page.evaluate(() => {
      const url = new URL(window.ReviewIIIAuth.SUPABASE_URL + '/auth/v1/authorize');
      url.searchParams.set('provider', 'github');
      url.searchParams.set('redirect_to', window.location.href);
      return url.toString();
    });
    console.log('  Constructed OAuth URL:', oauthUrl);
    if (!oauthUrl.includes('provider=github') || !oauthUrl.includes('supabase.co')) {
      throw new Error(`Malformed OAuth URL: ${oauthUrl}`);
    }

    // Simulate OAuth callback with fake token in hash
    const fakeToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTYiLCJlbWFpbCI6Im9hdXRoX3N0dWRlbnRAZXhhbXBsZS5jb20iLCJ1c2VyX21ldGFkYXRhIjp7InVzZXJfbmFtZSI6Im9hdXRoX3N0dWRlbnQiLCJmdWxsX25hbWUiOiJPQXV0aCBTdHVkZW50In19.signature';
    await page.goto(`http://localhost:${PORT}/index.html#access_token=${fakeToken}&refresh_token=fake_refresh`);
    // Wait for the async OAuth callback to complete — the Supabase /auth/v1/user fetch
    // with the fake token will fail (network or 401), then JWT decode fallback runs.
    // Poll for up to 8 seconds.
    await page.waitForFunction(
      () => window.ReviewIIIAuth && window.ReviewIIIAuth.isAuthenticated(),
      { timeout: 8000 }
    ).catch(() => {});

    const isUnlockedAfterOAuth = await page.evaluate(() => !document.body.classList.contains('auth-locked'));
    const oauthUser = await page.evaluate(() => window.ReviewIIIAuth.getActiveAccount());
    console.log('  Page unlocked after OAuth token parsed:', isUnlockedAfterOAuth);
    console.log('  Active OAuth username:', oauthUser?.username);

    if (!isUnlockedAfterOAuth || oauthUser?.username !== 'oauth_student') {
      throw new Error('OAuth callback token processing failed to authenticate user.');
    }

    // Verify hash was cleanly removed from address bar
    const currentUrl = page.url();
    console.log('  Current URL after hash cleanup:', currentUrl);
    if (currentUrl.includes('access_token')) {
      throw new Error('URL hash was not cleaned up after authentication.');
    }
    console.log('  ✓ OAuth hash token processing, profile creation, and URL hash cleanup verified!');

    console.log('\n=======================================================');
    console.log('🎉 ALL 7 ZERO-GUEST & GITHUB OAUTH TESTS PASSED!');
    console.log(' 1. Mandatory Auth Gate on Home Page (Zero Guest)');
    console.log(' 2. Standalone Quiz Auth Gate Protection');
    console.log(' 3. Direct GitHub Sign In & Workspace Unlock');
    console.log(' 4. Answer Persistence & Isolated Storage Keys');
    console.log(' 5. Multi-User Account Switching & Zero Data Bleed');
    console.log(' 6. Sign Out & Immediate Re-Locking Enforcement');
    console.log(' 7. GitHub OAuth 2.0 URL & Hash Callback Processing');
    console.log('=======================================================\n');

  } finally {
    await browser.close();
    server.close();
    console.log('[TEST] Server closed.');
  }
}

runTests().catch((err) => {
  console.error('\n❌ TEST FAILURE:', err);
  server.close();
  process.exit(1);
});
