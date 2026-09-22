import{d as q,a as H,m as x,k as F,n as C,o as V,P as j,f as z,q as R,t as W,u as _}from"./focus-system.V9C6BpdX.js";(function(){const d=document.getElementById("header-focus-pill"),f=document.getElementById("pill-ping-indicator"),g=document.getElementById("pill-phase-icon"),p=document.getElementById("pill-display-text"),b=document.getElementById("header-search-trigger"),P=document.querySelectorAll(".header-nav-btn");function E(t){if(!d)return;if(!t||!t.running){d.className="header-focus-pill idle",f&&(f.style.display="none"),g&&(g.textContent="⏱️"),p&&(p.textContent="Focus");return}const e=Date.now(),i=t.endsAt?Math.max(0,Math.ceil((t.endsAt-e)/1e3)):t.secondsLeft,a=t.phase==="focus";d.className=`header-focus-pill ${a?"running-focus":"running-break"}`,f&&(f.style.display="inline-flex"),g&&(g.textContent=j[t.phase]||(a?"🎯":"☕")),p&&(p.textContent=`${z(i)}`)}d&&(q(E),E(H()),setInterval(()=>{const t=H();t&&t.running&&E(t)},1e3));const I=document.getElementById("site-header")?.getAttribute("data-base-url")||"/reviewiii/";d?.addEventListener("click",()=>{const t=document.querySelector('[data-view-tab="focus"]');if(t){t.click();const e=document.getElementById("view-focus");e&&e.scrollIntoView({behavior:"smooth"})}else x(),window.location.href=`${I}#focus-timer`}),P.forEach(t=>{t.addEventListener("click",()=>{const e=t.getAttribute("data-view"),i=document.querySelector(`[data-view-tab="${e}"]`);if(i){i.click();const a=document.getElementById(`view-${e}`);a&&a.scrollIntoView({behavior:"smooth"})}else x(),window.location.href=`${I}#${e}`})}),b&&b.addEventListener("click",()=>{const t=document.querySelector('[data-view-tab="reviewers"]');if(t){t.click();const e=document.getElementById("subject-search");e&&(e.focus(),e.scrollIntoView({behavior:"smooth",block:"center"}))}else x(),window.location.href=`${I}?search=true#subjects`}),window.addEventListener("keydown",t=>{t.key==="/"&&document.activeElement?.tagName!=="INPUT"&&document.activeElement?.tagName!=="TEXTAREA"&&(t.preventDefault(),b?.click())});const l=document.getElementById("header-auth-pill"),o=document.getElementById("auth-dropdown"),w=document.getElementById("auth-pill-label"),k=document.getElementById("auth-pill-avatar-wrap"),v=document.getElementById("auth-status-dot"),A=document.getElementById("auth-dropdown-header"),y=document.getElementById("auth-accounts-list"),M=document.getElementById("auth-add-toggle-btn"),s=document.getElementById("auth-login-form"),T=document.getElementById("auth-github-username"),G=document.getElementById("auth-github-token"),B=document.getElementById("auth-token-group"),S=document.getElementById("auth-pat-toggle-link"),c=document.getElementById("auth-error-msg"),r=document.getElementById("auth-submit-btn"),D=document.getElementById("auth-guest-mode-btn");function $(t=_()){if(!l||!w||!k)return;const e=!t||t.isGuest;if(e?(l.className="header-auth-pill",w.textContent="Sign in",v&&(v.style.display="none"),k.innerHTML=`
          <svg class="github-icon-svg" viewBox="0 0 24 24" width="14" height="14" fill="currentColor">
            <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
          </svg>
        `):(l.className="header-auth-pill logged-in",w.textContent=`@${t.username}`,v&&(v.style.display="inline-block"),k.innerHTML=`
          <img src="${t.avatarUrl}" alt="${t.username}" class="auth-pill-avatar" />
        `),A&&(e?A.innerHTML=`
            <div class="auth-profile-card">
              <div class="auth-profile-avatar" style="display:flex;align-items:center;justify-content:center;font-size:1.2rem;">
                👤
              </div>
              <div class="auth-profile-info">
                <div class="auth-profile-name">Guest Student</div>
                <div class="auth-profile-sub">Anonymous Session</div>
                <span class="auth-badge-guest">⚡ Local Browser Storage</span>
              </div>
            </div>
          `:A.innerHTML=`
            <div class="auth-profile-card">
              <img src="${t.avatarUrl}" alt="${t.username}" class="auth-profile-avatar" />
              <div class="auth-profile-info">
                <div class="auth-profile-name">${t.displayName||t.username}</div>
                <div class="auth-profile-sub">
                  <a href="${t.profileUrl}" target="_blank" rel="noopener noreferrer">@${t.username} &nearr;</a>
                </div>
                <span class="auth-badge-active">● Active GitHub Session</span>
              </div>
            </div>
          `),y){const i=R();let a="";i.forEach(n=>{const u=!e&&n.id===t.id;a+=`
            <div class="auth-account-item ${u?"active":""}" data-user-id="${n.id}">
              <div class="auth-account-item-left">
                <img src="${n.avatarUrl}" alt="${n.username}" class="auth-account-item-avatar" />
                <span class="auth-account-item-name">@${n.username}</span>
              </div>
              <div class="auth-account-item-right">
                ${u?'<span class="auth-active-check">Active ✓</span>':""}
                <button type="button" class="auth-account-remove-btn" data-remove-id="${n.id}" title="Remove account from device">✕</button>
              </div>
            </div>
          `}),a+=`
          <div class="auth-account-item ${e?"active":""}" data-user-id="guest">
            <div class="auth-account-item-left">
              <span style="font-size: 1.1rem; width: 24px; text-align: center;">👤</span>
              <span class="auth-account-item-name">Guest Session</span>
            </div>
            <div class="auth-account-item-right">
              ${e?'<span class="auth-active-check">Active ✓</span>':""}
            </div>
          </div>
        `,y.innerHTML=a,y.querySelectorAll(".auth-account-item").forEach(n=>{n.addEventListener("click",u=>{const h=u.target;if(h&&h.classList.contains("auth-account-remove-btn"))return;const L=n.getAttribute("data-user-id");L&&L!==t.id&&(C(L),m())})}),y.querySelectorAll(".auth-account-remove-btn").forEach(n=>{n.addEventListener("click",u=>{u.stopPropagation();const h=n.getAttribute("data-remove-id");h&&confirm("Disconnect this GitHub account from ReviewIII on this device?")&&W(h)})})}}function N(){if(!o)return;o.style.display!=="none"?m():($(),o.style.display="block",l?.setAttribute("aria-expanded","true"))}function m(){o&&(o.style.display="none",l?.setAttribute("aria-expanded","false"),s&&(s.style.display="none"),c&&(c.style.display="none"))}l?.addEventListener("click",t=>{t.stopPropagation(),N()}),document.addEventListener("click",t=>{if(!o||o.style.display==="none")return;t.target.closest("#header-auth-wrapper")||m()}),M?.addEventListener("click",t=>{if(t.stopPropagation(),!s)return;const e=s.style.display==="none";s.style.display=e?"block":"none",e&&T?.focus()}),S?.addEventListener("click",t=>{if(t.stopPropagation(),!B)return;const e=B.style.display==="none";B.style.display=e?"block":"none",S.textContent=e?"Hide PAT field":"Use PAT Token"}),s?.addEventListener("submit",async t=>{t.preventDefault();const e=T?.value.trim(),i=G?.value.trim();if(!(!e&&!i)){r&&(r.setAttribute("disabled","true"),r.textContent="Connecting..."),c&&(c.style.display="none");try{await F(e,i),s.reset(),s.style.display="none",m()}catch(a){c&&(c.textContent=a?.message||"Failed to authenticate with GitHub.",c.style.display="block")}finally{r&&(r.removeAttribute("disabled"),r.textContent="Connect & Switch")}}}),D?.addEventListener("click",()=>{C("guest"),m()}),V(t=>{$(t)}),$()})();
