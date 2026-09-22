const U="https://uenxceusckmokmqhrkby.supabase.co",J="sb_publishable_OCUPoA1pEFODxzOUoTD8aA_HevquQfY",b="reviewiii_accounts:v1",g="reviewiii_active_user:v1",ie="reviewiii_auth_channel",N=new Set;let I=null;if(typeof window<"u"&&"BroadcastChannel"in window)try{I=new BroadcastChannel(ie),I.onmessage=t=>{t.data&&t.data.type==="auth_changed"&&(G(t.data.activeUser),f())}}catch{}typeof window<"u"&&window.addEventListener("storage",t=>{(t.key===g||t.key===b)&&(G(x()),f())});function G(t){const e=t||x();N.forEach(i=>{try{i(e)}catch(n){console.error("Error in auth listener:",n)}}),typeof window<"u"&&window.dispatchEvent(new CustomEvent("reviewiii:auth_changed",{detail:{user:e}}))}function h(t){if(I)try{I.postMessage({type:"auth_changed",activeUser:t})}catch{}G(t)}function y(){if(typeof window>"u")return[];try{const t=localStorage.getItem(b);if(!t)return[];const e=JSON.parse(t);return Array.isArray(e)?e.filter(i=>i&&i.id&&i.id!=="guest"):[]}catch{return[]}}function M(){if(typeof window>"u")return null;try{const t=localStorage.getItem(g);return!t||t==="guest"?(t==="guest"&&localStorage.removeItem(g),null):y().some(n=>n.id===t)?t:(localStorage.removeItem(g),null)}catch{return null}}function x(){const t=M();return t&&y().find(n=>n.id===t)||null}function Y(){return!!x()}function E(t){const e=x();return!e||!e.id?`reviewiii_u_unauth_${t}`:`reviewiii_u_${e.id.toLowerCase().replace(/[^a-z0-9_-]/g,"_")}_${t}`}function K(t){if(typeof window>"u")return;const e=t||window.location.href.split("#")[0];try{localStorage.setItem("reviewiii_oauth_return",e)}catch{}const i=`${U}/auth/v1/authorize?provider=github&redirect_to=${encodeURIComponent(e)}`;window.location.href=i}async function R(){if(typeof window>"u")return null;const t=window.location.hash;if(!t||!t.includes("access_token="))return null;try{const e=new URLSearchParams(t.replace(/^#/,"")),i=e.get("access_token"),n=e.get("refresh_token");if(!i)return null;m("Verifying GitHub OAuth credentials...",!1);let r=null;try{const s=await fetch(`${U}/auth/v1/user`,{headers:{Authorization:`Bearer ${i}`,apikey:J}});if(s.ok){const c=await s.json(),o=c.user_metadata||{},u=o.user_name||o.preferred_username||(c.email?c.email.split("@")[0]:"github_student"),p=o.full_name||o.name||u,d=o.avatar_url||`https://github.com/${u}.png`;r={id:`github:${u.toLowerCase()}`,username:u,displayName:p,avatarUrl:d,bio:o.bio||"Verified GitHub Student",profileUrl:`https://github.com/${u}`,authType:"oauth",token:i,refreshToken:n||null,connectedAt:Date.now(),lastActiveAt:Date.now()}}}catch(s){console.warn("Could not fetch /auth/v1/user, decoding JWT payload fallback:",s)}if(!r)try{const s=i.split(".")[1],c=JSON.parse(atob(s.replace(/-/g,"+").replace(/_/g,"/"))),o=c.user_metadata||{},u=o.user_name||o.preferred_username||(c.email?c.email.split("@")[0]:"github_student");r={id:`github:${u.toLowerCase()}`,username:u,displayName:o.full_name||o.name||u,avatarUrl:o.avatar_url||`https://github.com/${u}.png`,bio:o.bio||"Verified GitHub Student",profileUrl:`https://github.com/${u}`,authType:"oauth",token:i,refreshToken:n||null,connectedAt:Date.now(),lastActiveAt:Date.now()}}catch(s){console.error("Failed to parse access token:",s)}if(!r)throw new Error("Unable to extract GitHub profile from OAuth token.");q(r);try{window.history&&window.history.replaceState&&window.history.replaceState(null,"",window.location.pathname+window.location.search)}catch{}const a=localStorage.getItem("reviewiii_oauth_return");return a&&(localStorage.removeItem("reviewiii_oauth_return"),a!==window.location.href&&a.startsWith(window.location.origin))?(window.location.href=a,r):(h(r),f(),r)}catch(e){return console.error("OAuth Callback Exception:",e),m(e.message||"GitHub OAuth failed.",!0),null}}async function V(t,e=""){if(typeof window>"u")return null;const i=(t||"").trim(),n=(e||"").trim();if(!i&&!n)throw new Error("Please provide a GitHub username or Personal Access Token.");let r=null;try{const a={Accept:"application/vnd.github.v3+json"};n&&(a.Authorization=`token ${n}`);const s=n&&!i?"https://api.github.com/user":`https://api.github.com/users/${encodeURIComponent(i)}`,c=await fetch(s,{headers:a});if(c.status===404)throw new Error(`GitHub user "${i}" was not found.`);if(c.status===401)throw new Error("Invalid GitHub Personal Access Token.");if(c.ok){const o=await c.json();r={id:`github:${o.login.toLowerCase()}`,username:o.login,displayName:o.name||o.login,avatarUrl:o.avatar_url,bio:o.bio||"",profileUrl:o.html_url||`https://github.com/${o.login}`,publicRepos:typeof o.public_repos=="number"?o.public_repos:0,token:n||null,authType:"api",connectedAt:Date.now(),lastActiveAt:Date.now()}}else r=H(i,n)}catch(a){if(a.message&&(a.message.includes("not found")||a.message.includes("Invalid GitHub")))throw a;r=H(i,n)}return q(r),h(r),f(),r}function H(t,e){const i=t||"User";return{id:`github:${i.toLowerCase()}`,username:i,displayName:i,avatarUrl:`https://github.com/${i}.png`,bio:"GitHub Connected Student",profileUrl:`https://github.com/${i}`,publicRepos:0,token:e||null,authType:"fallback",connectedAt:Date.now(),lastActiveAt:Date.now()}}function q(t){const e=y(),i=e.findIndex(n=>n.id===t.id);i>=0?e[i]={...e[i],...t}:e.push(t);try{localStorage.setItem(b,JSON.stringify(e)),localStorage.setItem(g,t.id)}catch(n){console.error("Failed to save account:",n)}}function W(t){if(typeof window>"u"||!t||t==="guest")return;const e=y(),i=e.find(n=>n.id===t);if(i){i.lastActiveAt=Date.now();try{localStorage.setItem(b,JSON.stringify(e)),localStorage.setItem(g,i.id)}catch{}h(i),f()}}function ne(t){if(typeof window>"u")return;let e=y();e=e.filter(i=>i.id!==t);try{localStorage.setItem(b,JSON.stringify(e))}catch{}if(M()===t)if(e.length>0)W(e[0].id);else{try{localStorage.removeItem(g)}catch{}h(null),f()}else h(x())}function oe(){if(!(typeof window>"u")){try{localStorage.removeItem(g)}catch{}h(null),f()}}function re(t){return N.add(t),()=>N.delete(t)}function ae(){if(typeof document>"u"||document.getElementById("reviewiii-auth-styles"))return;const t=document.createElement("style");t.id="reviewiii-auth-styles",t.textContent=`
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
  `,document.head.appendChild(t)}function m(t,e=!1){const i=document.getElementById("reviewiii-gate-status");if(i){if(!t){i.style.display="none",i.textContent="";return}i.textContent=t,i.className=`reviewiii-gate-status ${e?"error":""}`,i.style.display="block"}}function f(){if(typeof document>"u")return;ae();const t=Y();let e=document.getElementById("reviewiii-auth-gate");if(t){document.body.classList.remove("auth-locked"),e&&e.remove();return}if(document.body.classList.add("auth-locked"),e){e.style.display="flex";return}e=document.createElement("div"),e.id="reviewiii-auth-gate",e.innerHTML=`
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
  `,document.body.appendChild(e),document.getElementById("reviewiii-gate-oauth-btn")?.addEventListener("click",()=>{m("Redirecting to GitHub OAuth...",!1),K()});const n=document.getElementById("reviewiii-gate-pat-toggle"),r=document.getElementById("reviewiii-gate-pat-wrap");n?.addEventListener("click",()=>{if(!r)return;const u=r.style.display==="none";r.style.display=u?"block":"none",n.textContent=u?"Hide PAT Field":"Use PAT Token"});const a=document.getElementById("reviewiii-gate-form"),s=document.getElementById("reviewiii-gate-user"),c=document.getElementById("reviewiii-gate-pat"),o=document.getElementById("reviewiii-gate-submit");a?.addEventListener("submit",async u=>{u.preventDefault();const p=s?s.value.trim():"",d=c?c.value.trim():"";if(!(!p&&!d)){o&&(o.setAttribute("disabled","true"),o.textContent="Verifying..."),m("Verifying GitHub account...",!1);try{await V(p,d),m("Authenticated! Loading workspace...",!1)}catch(w){m(w.message||"Failed to authenticate.",!0),o&&(o.removeAttribute("disabled"),o.textContent="Sign In →")}}})}if(typeof window<"u"){const t=window;t.ReviewIIIAuth={SUPABASE_URL:U,SUPABASE_ANON_KEY:J,ACCOUNTS_STORAGE_KEY:b,ACTIVE_USER_STORAGE_KEY:g,getActiveUserId:M,getActiveAccount:x,getAccounts:y,getStorageKey:E,isAuthenticated:Y,startGitHubOAuth:K,handleOAuthCallback:R,loginWithGitHub:V,switchAccount:W,removeAccount:ne,logout:oe,subscribeAuth:re,ensureAuthGate:f},window.location.hash&&window.location.hash.includes("access_token=")?R():document.readyState==="loading"?document.addEventListener("DOMContentLoaded",()=>{f()}):f()}const O="reviewiii_focus:v1",Z="reviewiii_timelogs:v1",Q="reviewiii_settings:v1";function v(){return E(O)}function $(){return E(Z)}function X(){return E(Q)}const l={focus:1500,short:300,long:900},se={focus:"Focus",short:"Short Break",long:"Long Break"},ce={focus:"🎯",short:"☕",long:"☕"},ue="Asia/Manila";function F(t=new Date){try{return new Intl.DateTimeFormat("en-CA",{timeZone:ue,year:"numeric",month:"2-digit",day:"2-digit"}).format(t)}catch{return t.toISOString().slice(0,10)}}function le(t){const e=Math.max(0,Math.floor(t)),i=Math.floor(e/3600),n=Math.floor(e%3600/60),r=e%60,a=s=>s<10?`0${s}`:`${s}`;return i>0?`${i}:${a(n)}:${a(r)}`:`${a(n)}:${a(r)}`}function de(t){const e=Math.max(0,Math.round(t));if(e<60)return`${e}m`;const i=Math.floor(e/60),n=e%60;return n>0?`${i}h ${n}m`:`${i}h`}function fe(t,e=!1){if(typeof window>"u")return;const i=D();if(!(!e&&i.soundEnabled===!1))try{const n=window.AudioContext||window.webkitAudioContext;if(!n)return;const r=new n;r.state==="suspended"&&r.resume().catch(()=>{});const a=(s,c,o,u,p="sine")=>{const d=r.createOscillator(),w=r.createGain();d.frequency.value=s,d.type=p;const S=r.currentTime+c;w.gain.setValueAtTime(1e-4,S),w.gain.exponentialRampToValueAtTime(u,S+.02),w.gain.exponentialRampToValueAtTime(1e-4,S+o),d.connect(w).connect(r.destination),d.start(S),d.stop(S+o+.02)};t==="focus"?(a(523.25,0,.3,.2),a(659.25,.12,.3,.2),a(783.99,.24,.4,.22)):t==="break"?(a(440,0,.45,.16,"triangle"),a(329.63,.24,.55,.16,"triangle")):(a(523.25,0,.7,.18),a(659.25,0,.7,.16),a(783.99,0,.7,.16),a(1046.5,.06,.8,.2)),setTimeout(()=>{r.close().catch(()=>{})},2e3)}catch{}}function D(){if(typeof window>"u")return{focusSeconds:l.focus,shortBreakSeconds:l.short,longBreakSeconds:l.long,soundEnabled:!0,autoStartBreaks:!0,autoStartFocus:!0};try{const t=localStorage.getItem(X());if(!t)return{focusSeconds:l.focus,shortBreakSeconds:l.short,longBreakSeconds:l.long,soundEnabled:!0,autoStartBreaks:!0,autoStartFocus:!0};const e=JSON.parse(t);return{focusSeconds:Number(e.focusSeconds)||l.focus,shortBreakSeconds:Number(e.shortBreakSeconds)||l.short,longBreakSeconds:Number(e.longBreakSeconds)||l.long,soundEnabled:e.soundEnabled!==!1,autoStartBreaks:e.autoStartBreaks!==!1,autoStartFocus:e.autoStartFocus!==!1}}catch{return{focusSeconds:l.focus,shortBreakSeconds:l.short,longBreakSeconds:l.long,soundEnabled:!0,autoStartBreaks:!0,autoStartFocus:!0}}}function ge(t){if(!(typeof window>"u"))try{const i={...D(),...t};localStorage.setItem(X(),JSON.stringify(i)),T("settings",i)}catch(e){console.error("Failed to save settings:",e)}}function C(){if(typeof window>"u")return[];try{const t=localStorage.getItem($());if(!t)return[];const e=JSON.parse(t);return Array.isArray(e)?e:[]}catch{return[]}}function pe(t,e="General Study",i="Self Review",n="pomodoro",r=null){if(typeof window>"u")return null;const a=Math.max(1,Math.round(t)),s=r||F(),c={id:"log_"+Date.now()+"_"+Math.random().toString(36).substring(2,7),date:s,timestamp:Date.now(),isoTime:new Date().toISOString(),minutes:a,subjectCode:e||"General Study",moduleTitle:i||"Self Review",mode:n};try{const o=C();o.unshift(c);const u=o.slice(0,300);return localStorage.setItem($(),JSON.stringify(u)),T("time_log",c),c}catch(o){return console.error("Failed to log time:",o),null}}function ee(){const t=F();return C().filter(i=>i.date===t)}function we(){return ee().reduce((e,i)=>e+(Number(i.minutes)||0),0)}function me(){const t=C(),e={};for(const i of t){const n=i.subjectCode||"General Study";e[n]||(e[n]={subjectCode:n,totalMinutes:0,sessionCount:0}),e[n].totalMinutes+=Number(i.minutes)||0,e[n].sessionCount+=1}return Object.values(e).sort((i,n)=>n.totalMinutes-i.totalMinutes)}function he(){if(!(typeof window>"u"))try{localStorage.removeItem($()),T("time_log",null)}catch{}}function L(){if(typeof window>"u")return null;try{const t=localStorage.getItem(v());if(!t)return null;const e=JSON.parse(t);if(e.v!==1||e.phase!=="focus"&&e.phase!=="short"&&e.phase!=="long")return null;const i=typeof e.endsAt=="number"&&Number.isFinite(e.endsAt)?e.endsAt:null;let n=typeof e.secondsLeft=="number"&&Number.isFinite(e.secondsLeft)?Math.max(0,Math.round(e.secondsLeft)):0;return e.running&&i&&(n=Math.max(0,Math.ceil((i-Date.now())/1e3))),{v:1,phase:e.phase,running:!!e.running,focusCount:Number(e.focusCount)||0,subjectCode:typeof e.subjectCode=="string"?e.subjectCode:"General Study",moduleTitle:typeof e.moduleTitle=="string"?e.moduleTitle:"Comprehensive Review",secondsLeft:n,endsAt:i,updatedAt:e.updatedAt||Date.now()}}catch{return null}}function ve(t){if(!(typeof window>"u"))try{if(!t){localStorage.removeItem(v()),k(null);return}const e={v:1,phase:t.phase,running:!!t.running,focusCount:Number(t.focusCount)||0,subjectCode:t.subjectCode||"General Study",moduleTitle:t.moduleTitle||"Comprehensive Review",secondsLeft:Math.max(0,Math.round(t.secondsLeft)),endsAt:t.running?t.endsAt:null,updatedAt:Date.now()};localStorage.setItem(v(),JSON.stringify(e)),k(e)}catch(e){console.error("Failed to save focus snapshot:",e)}}const A=new Set;function be(t){return A.add(t),()=>{A.delete(t)}}function k(t){for(const e of A)try{e(t)}catch(i){console.error(i)}T("focus_session",t)}let _=null;if(typeof window<"u"&&"BroadcastChannel"in window)try{_=new BroadcastChannel("reviewiii_focus_channel"),_.onmessage=t=>{if(t.data?.type==="focus_session"){const e=t.data.payload;for(const i of A)i(e)}}}catch{}function T(t,e){if(_)try{_.postMessage({type:t,payload:e})}catch{}}const z="reviewiii_nav_internal";function j(){if(!(typeof window>"u"))try{sessionStorage.setItem(z,String(Date.now()))}catch{}}function te(){if(typeof window>"u")return!1;try{const t=sessionStorage.getItem(z);if(t){const e=Date.now()-parseInt(t,10);if(e>=0&&e<15e3)return!0}}catch{}return!1}function P(){if(!(typeof window>"u"))try{sessionStorage.removeItem(z)}catch{}}function B(){if(!(typeof window>"u")&&!te())try{const t=localStorage.getItem(v());if(!t)return;const e=JSON.parse(t);if(e&&e.running){let i=e.secondsLeft;typeof e.endsAt=="number"&&e.endsAt>0&&(i=Math.max(0,Math.round((e.endsAt-Date.now())/1e3))),e.running=!1,e.secondsLeft=i,e.endsAt=null,e.updatedAt=Date.now(),localStorage.setItem(v(),JSON.stringify(e))}}catch{}}if(typeof window<"u"){setTimeout(P,1500),document.addEventListener("click",e=>{const i=e.target,n=i&&i.closest?i.closest("a"):null;if(n&&n.href)try{new URL(n.href,window.location.href).origin===window.location.origin&&j()}catch{}},!0),window.addEventListener("storage",e=>{if(e.key===v()||e.key&&e.key.indexOf(O)!==-1){const i=L();for(const n of A)n(i)}}),window.addEventListener("reviewiii:auth_changed",()=>{k(L())}),window.addEventListener("beforeunload",B),window.addEventListener("pagehide",B);const t=window;t.ReviewIIIFocus||(t.ReviewIIIFocus={}),Object.assign(t.ReviewIIIFocus,{markInternalNav:j,isInternalNav:te,clearInternalNav:P,pauseFocusOnExit:B,FOCUS_STORAGE_KEY:O,TIME_LOGS_STORAGE_KEY:Z,SETTINGS_STORAGE_KEY:Q,DEFAULT_SECONDS:l,PHASE_LABELS:se,PHASE_EMOJIS:ce,manilaDateKey:F,formatTime:le,formatMinutes:de,playFocusChime:fe,readSettings:D,saveSettings:ge,readTimeLogs:C,logTime:pe,getTodayTimeLogs:ee,getTodayMinutes:we,getSubjectStats:me,clearTimeLogs:he,readFocusSnapshot:L,saveFocusSnapshot:ve,subscribeFocus:be,publishFocus:k})}export{l as D,ce as P,L as a,ve as b,he as c,be as d,se as e,le as f,ee as g,we as h,de as i,me as j,K as k,pe as l,j as m,V as n,oe as o,fe as p,re as q,D as r,ge as s,x as t,f as u,y as v,W as w,ne as x};
