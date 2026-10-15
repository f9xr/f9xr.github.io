(function () {
  'use strict';

  var KEY = 'f9xr-consent';
  var GA_ID = 'G-134PMTPP82';
  var CLARITY_ID = 'xgqzx0h42p';
  var loaded = false;
  var banner = null;

  function storage() {
    try { return window.localStorage; } catch (e) { return null; }
  }

  function getStored() {
    var s = storage();
    return s ? s.getItem(KEY) : null;
  }

  function setStored(v) {
    var s = storage();
    if (s) s.setItem(KEY, v);
  }

  function isOptedOut() {
    return navigator.globalPrivacyControl === true ||
      navigator.doNotTrack === '1' ||
      window.doNotTrack === '1';
  }

  function gtag() {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(arguments);
  }

  function loadAnalytics() {
    if (loaded) return;
    loaded = true;

    window.gtag = window.gtag || gtag;
    gtag('consent', 'default', {
      ad_storage: 'granted',
      ad_user_data: 'granted',
      ad_personalization: 'granted',
      analytics_storage: 'granted'
    });
    gtag('js', new Date());
    gtag('config', GA_ID);

    var ga = document.createElement('script');
    ga.async = true;
    ga.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(ga);

    (function (c, l, a, r, i) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      var t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i + '?ref=bwt';
      var y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', CLARITY_ID);
  }

  function removeBanner() {
    if (banner && banner.parentNode) banner.parentNode.removeChild(banner);
    banner = null;
  }

  function decide(choice) {
    setStored(choice);
    removeBanner();
    if (choice === 'granted') loadAnalytics();
  }

  function showBanner() {
    if (banner || document.getElementById('f9xr-consent')) return;

    banner = document.createElement('div');
    banner.id = 'f9xr-consent';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.style.cssText = 'position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;' +
      'max-width:560px;margin:0 auto;background:#0f172a;color:#e2e8f0;border:1px solid rgba(148,163,184,.25);' +
      'border-radius:16px;padding:16px 20px;font-size:14px;line-height:1.5;' +
      'box-shadow:0 12px 40px rgba(0,0,0,.45);display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;';

    var text = document.createElement('p');
    text.style.cssText = 'margin:0;flex:1 1 240px;font-size:13px;color:#cbd5e1;';
    text.innerHTML = 'We use cookies for analytics (Google Analytics, Microsoft Clarity) to improve the site. ' +
      'See our <a href="/legals/privacy.html" style="color:#60a5fa;text-decoration:underline;">Privacy Policy</a>.';

    var actions = document.createElement('div');
    actions.style.cssText = 'display:flex;gap:8px;flex:0 0 auto;';

    function btn(label, bg, fg, border) {
      var b = document.createElement('button');
      b.type = 'button';
      b.textContent = label;
      b.style.cssText = 'cursor:pointer;border-radius:9999px;padding:8px 18px;font-size:13px;font-weight:700;' +
        'letter-spacing:.02em;border:1px solid ' + border + ';background:' + bg + ';color:' + fg + ';';
      return b;
    }

    var reject = btn('Reject', 'transparent', '#cbd5e1', 'rgba(148,163,184,.4)');
    reject.addEventListener('click', function () { decide('denied'); });
    reject.onmouseover = function () { reject.style.background = 'rgba(148,163,184,.15)'; };
    reject.onmouseout = function () { reject.style.background = 'transparent'; };

    var accept = btn('Accept', '#3b82f6', '#ffffff', '#3b82f6');
    accept.addEventListener('click', function () { decide('granted'); });
    accept.onmouseover = function () { accept.style.background = '#2563eb'; };
    accept.onmouseout = function () { accept.style.background = '#3b82f6'; };

    actions.appendChild(reject);
    actions.appendChild(accept);
    banner.appendChild(text);
    banner.appendChild(actions);
    document.body.appendChild(banner);
  }

  window.f9xrSetConsent = decide;
  window.f9xrResetConsent = function () {
    setStored(null);
    try { storage().removeItem(KEY); } catch (e) {}
    loaded = false;
    showBanner();
  };

  function init() {
    var stored = getStored();
    if (stored === 'granted') { loadAnalytics(); return; }
    if (stored === 'denied') return;
    if (isOptedOut()) { setStored('denied'); return; }
    if (document.body) showBanner();
    else document.addEventListener('DOMContentLoaded', showBanner);
  }

  init();
})();
