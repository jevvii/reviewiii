const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const PORT = 4399;
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
    // Test 1: Home Page & Bento Badges
    // ------------------------------------------------------------------------
    console.log('[TEST 1] Testing Home Page and Totals...');
    await page.goto(`http://localhost:${PORT}/index.html`);
    await page.waitForLoadState('domcontentloaded');

    const title = await page.title();
    console.log('  Page title:', title);
    if (!title.includes('ReviewIII')) {
      throw new Error(`Unexpected page title: ${title}`);
    }

    // Verify Question Bank metric shows 830
    const qbValue = await page.textContent('.bento-tile:has(.bento-label:has-text("Question Bank")) .bento-value');
    console.log('  Question Bank total:', qbValue?.trim());
    if (qbValue?.trim() !== '830') {
      throw new Error(`Expected Question Bank total 830, got: ${qbValue?.trim()}`);
    }

    // Verify Ready Modules metric shows 12
    const rmValue = await page.textContent('.bento-tile:has(.bento-label:has-text("Ready Modules")) .bento-value');
    console.log('  Ready Modules count:', rmValue?.trim());
    if (rmValue?.trim() !== '12') {
      throw new Error(`Expected Ready Modules 12, got: ${rmValue?.trim()}`);
    }

    // ------------------------------------------------------------------------
    // Test 2: NETC311 Course Hub & Module 3 Downloads
    // ------------------------------------------------------------------------
    console.log('[TEST 2] Testing NETC311 Course Hub & Module 3 Downloads...');
    await page.goto(`http://localhost:${PORT}/courses/netc311/index.html`);
    await page.waitForLoadState('domcontentloaded');

    const courseTitle = await page.textContent('h1');
    console.log('  Course Heading:', courseTitle?.trim());

    // Check Module 3 card exists
    const m3Card = page.locator('.module-card:has-text("Protocols & Models")');
    const m3Count = await m3Card.count();
    if (m3Count === 0) {
      throw new Error('Module 3 card "Protocols & Models" was not found on NETC311 page.');
    }
    console.log('  ✓ Module 3 card present on NETC311 hub!');

    const m3Badge = await m3Card.locator('.item-count-badge').textContent();
    console.log('  Module 3 Question Count badge:', m3Badge?.trim());
    if (!m3Badge?.includes('95')) {
      throw new Error(`Expected 95 questions badge, got: ${m3Badge}`);
    }

    // Verify files exist in docs/downloads/netc311/
    const m3Pdf = path.join(DOCS_DIR, 'downloads/netc311/Module 3 - Protocols and Models - Questionnaire.pdf');
    const m3Docx = path.join(DOCS_DIR, 'downloads/netc311/Module 3 - Protocols and Models - Questionnaire.docx');
    const m3Json = path.join(DOCS_DIR, 'downloads/netc311/Module_3_NotebookLM_Quiz.json');
    const m3Md = path.join(DOCS_DIR, 'downloads/netc311/Module_3_NotebookLM_Quiz.md');

    if (!fs.existsSync(m3Pdf)) throw new Error('Module 3 PDF missing from docs/downloads/netc311/');
    if (!fs.existsSync(m3Docx)) throw new Error('Module 3 DOCX missing from docs/downloads/netc311/');
    if (!fs.existsSync(m3Json)) throw new Error('Module 3 JSON missing from docs/downloads/netc311/');
    if (!fs.existsSync(m3Md)) throw new Error('Module 3 MD missing from docs/downloads/netc311/');
    console.log('  ✓ Verified PDF, DOCX, JSON, and MD questionnaires exist on disk and are ready for offline download!');

    // ------------------------------------------------------------------------
    // Test 3: Standalone Quiz Player for NETC311 Module 3
    // ------------------------------------------------------------------------
    console.log('[TEST 3] Testing NETC311 Module 3 Quiz Player & Payload...');
    await page.goto(`http://localhost:${PORT}/quizzes/netc311/module3.html`);
    await page.waitForLoadState('domcontentloaded');

    const quizTitle = await page.title();
    console.log('  Quiz Page Title:', quizTitle);
    if (!quizTitle.includes('NETC311') || !quizTitle.includes('Module 3')) {
      throw new Error(`Unexpected quiz title: ${quizTitle}`);
    }

    // Verify data-app-data payload contains 95 questions
    const appData = await page.evaluate(() => {
      const match = document.documentElement.outerHTML.match(/data-app-data="([^"]+)"/);
      if (!match) return null;
      const jsonStr = match[1].replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
      return JSON.parse(jsonStr);
    });

    if (!appData || !appData.quiz || appData.quiz.length !== 95) {
      throw new Error(`Expected 95 questions in data-app-data payload, found: ${appData?.quiz?.length}`);
    }
    console.log(`  ✓ Successfully verified 95 questions loaded in Module 3 payload!`);
    console.log(`  Sample Q1: "${appData.quiz[0].question}"`);

    // Verify ReviewIII Auth & Persistence are loaded
    const authAvailable = await page.evaluate(() => typeof window.ReviewIIIAuth !== 'undefined');
    if (!authAvailable) {
      throw new Error('window.ReviewIIIAuth was not loaded in module3.html!');
    }
    console.log('  ✓ window.ReviewIIIAuth initialized in standalone quiz!');

    // ------------------------------------------------------------------------
    // Test 4: GitHub Multi-User Authentication & Isolated Sessions
    // ------------------------------------------------------------------------
    console.log('[TEST 4] Testing GitHub Multi-User Authentication & Session Isolation...');
    await page.goto(`http://localhost:${PORT}/index.html`);
    await page.waitForLoadState('domcontentloaded');
    await page.waitForFunction(() => typeof window.ReviewIIIAuth !== 'undefined');

    // 4.1 Guest Session Testing
    await page.evaluate(() => {
      window.ReviewIIIAuth.switchAccount('guest');
      const key = window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
      localStorage.setItem(key, JSON.stringify({
        userAnswers: { "0": 2 },
        currentQuestionIndex: 1
      }));
    });

    const guestSaved = await page.evaluate(() => {
      const key = window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
      return { key, data: JSON.parse(localStorage.getItem(key) || 'null') };
    });
    console.log(`  ✓ Guest session saved at key: ${guestSaved.key}`);
    if (guestSaved.key !== 'reviewiii_quiz_NETC311_3') {
      throw new Error(`Guest key should be base key 'reviewiii_quiz_NETC311_3', got: ${guestSaved.key}`);
    }
    if (guestSaved.data.userAnswers["0"] !== 2) {
      throw new Error('Guest answer was not saved properly!');
    }

    // 4.2 Connect GitHub User 1: 'javvii'
    console.log('  Logging in as GitHub User 1 (@javvii)...');
    await page.evaluate(async () => {
      await window.ReviewIIIAuth.loginWithGitHub('javvii');
      const key = window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
      localStorage.setItem(key, JSON.stringify({
        userAnswers: { "0": 1, "1": 3 },
        currentQuestionIndex: 2
      }));
    });

    const user1Saved = await page.evaluate(() => {
      const key = window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
      return { key, data: JSON.parse(localStorage.getItem(key) || 'null') };
    });
    console.log(`  ✓ User 1 session saved at: ${user1Saved.key}`);
    if (!user1Saved.key.includes('github_javvii')) {
      throw new Error(`Expected User 1 key to contain 'github_javvii', got: ${user1Saved.key}`);
    }
    if (Object.keys(user1Saved.data.userAnswers).length !== 2) {
      throw new Error('User 1 should have 2 answers saved!');
    }

    // 4.3 Connect GitHub User 2: 'student2'
    console.log('  Logging in as GitHub User 2 (@student2)...');
    await page.evaluate(async () => {
      await window.ReviewIIIAuth.loginWithGitHub('student2');
    });

    const user2Saved = await page.evaluate(() => {
      const key = window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
      return { key, data: JSON.parse(localStorage.getItem(key) || 'null') };
    });
    console.log(`  ✓ User 2 session at: ${user2Saved.key}`);
    if (user2Saved.data !== null) {
      throw new Error('User 2 should have clean isolated session (null)!');
    }

    // 4.4 Switch back to User 1 (@javvii) and verify answers are restored
    console.log('  Switching back to @javvii...');
    await page.evaluate(() => {
      window.ReviewIIIAuth.switchAccount('github:javvii');
    });
    const user1Restored = await page.evaluate(() => {
      const key = window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
      return JSON.parse(localStorage.getItem(key) || 'null');
    });
    if (!user1Restored || Object.keys(user1Restored.userAnswers).length !== 2) {
      throw new Error('User 1 answers were lost when switching accounts!');
    }
    console.log('  ✓ User 1 answers completely intact after switching back!');

    // 4.5 Switch to Guest and verify guest's answers are restored
    console.log('  Switching back to Guest mode...');
    await page.evaluate(() => {
      window.ReviewIIIAuth.switchAccount('guest');
    });
    const guestRestored = await page.evaluate(() => {
      const key = window.ReviewIIIAuth.getStorageKey('reviewiii_quiz_NETC311_3');
      return JSON.parse(localStorage.getItem(key) || 'null');
    });
    if (!guestRestored || guestRestored.userAnswers["0"] !== 2) {
      throw new Error('Guest answers were lost when switching accounts!');
    }
    console.log('  ✓ Guest session answers completely intact!');

    // ------------------------------------------------------------------------
    // Test 5: UI Interaction with Account Switcher in Header
    // ------------------------------------------------------------------------
    console.log('[TEST 5] Testing UI Header Account Manager...');
    await page.goto(`http://localhost:${PORT}/index.html`);
    await page.waitForLoadState('domcontentloaded');
    await page.waitForFunction(() => typeof window.ReviewIIIAuth !== 'undefined');

    // Click auth pill to toggle dropdown
    await page.click('#header-auth-pill');
    await page.waitForSelector('#auth-dropdown:not([style*="display: none"])');
    console.log('  ✓ Dropdown opened');

    // Verify account items are rendered in dropdown
    const accountItems = await page.locator('.auth-account-item').allTextContents();
    console.log('  Rendered Accounts in Menu:', accountItems.map(a => a.trim().replace(/\s+/g, ' ')));

    // Switch to javvii via UI click
    const javviiRow = page.locator('.auth-account-item').filter({ hasText: 'Javvii' });
    await javviiRow.click();
    console.log('  ✓ Clicked @javvii account row');

    // Verify header pill now shows @javvii
    await page.waitForFunction(() => {
      const pill = document.getElementById('auth-pill-label');
      return pill && pill.textContent && pill.textContent.toLowerCase().includes('javvii');
    });
    const updatedLabel = await page.textContent('#auth-pill-label');
    console.log(`  ✓ Header pill updated to: ${updatedLabel?.trim()}`);

    console.log('\n=======================================================');
    console.log('🎉 ALL 5 E2E INTEGRATION TESTS PASSED!');
    console.log(' 1. Home Page & Updated Question Bank (830 items, 12 modules)');
    console.log(' 2. NETC311 Hub & Module 3 Downloads (DOCX, PDF, JSON, MD)');
    console.log(' 3. Standalone Interactive Quiz Player (95 questions loaded)');
    console.log(' 4. GitHub Multi-User Authentication & Storage Isolation');
    console.log(' 5. Interactive UI Header Account Switcher');
    console.log('=======================================================\n');

  } finally {
    await browser.close();
    await new Promise((resolve) => server.close(resolve));
    console.log('[TEST] Test server closed cleanly.');
  }
}

runTests().catch((err) => {
  console.error('\n❌ TEST FAILED:', err);
  process.exit(1);
});
