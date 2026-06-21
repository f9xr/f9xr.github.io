/* F9XR Tools Enhancements v1.0 — save/load, share, theme, shortcuts, compare, benchmarks, animations */
(function() {
  'use strict';

  var toolKey = document.body.getAttribute('data-tool-key');
  if (!toolKey) return;
  var toolName = document.body.getAttribute('data-tool-name') || document.title;
  var STORAGE_KEY = 'f9xr-' + toolKey;
  var COMPARE_KEY = STORAGE_KEY + '-compare';

  var $ = function(id) { return document.getElementById(id); };
  var qs = function(s) { return document.querySelector(s); };
  var qsa = function(s) { return document.querySelectorAll(s); };

  /* --- Helpers --- */
  function findInputs() {
    var els = [];
    qsa('[id^="ts-"]').forEach(function(el) {
      if (el.tagName === 'SELECT' || el.tagName === 'INPUT') {
        if (el.type !== 'hidden' && el.type !== 'submit' && el.type !== 'button') {
          if (el.id !== 'search-input') els.push(el);
        }
      }
    });
    return els;
  }

  function getValues() {
    var obj = {};
    findInputs().forEach(function(el) {
      if (el.type === 'checkbox') obj[el.id] = el.checked ? '1' : '0';
      else obj[el.id] = el.value;
    });
    return obj;
  }

  function setValues(obj) {
    var inputs = findInputs();
    var changed = false;
    inputs.forEach(function(el) {
      var v = obj[el.id];
      if (v === undefined) return;
      if (el.type === 'checkbox') el.checked = v === '1' || v === 'true';
      else el.value = v;
      changed = true;
    });
    /* Trigger calculate by dispatching change on first input */
    if (changed && inputs.length > 0) {
      inputs[0].dispatchEvent(new Event('change', { bubbles: true }));
    }
  }

  function getResultsCard() {
    return $('ts-results-card') || qs('[id$="-results-card"]');
  }

  function getResultsData() {
    return $('ts-results-data');
  }

  function getEmptyState() {
    return $('ts-empty-state');
  }

  function getVisibleResultsText() {
    var data = getResultsData();
    if (!data) return '';
    if (data.style.display === 'none') return '';
    var hero = qs('.hero-value');
    return hero ? hero.textContent.trim() : data.textContent.trim().slice(0, 80);
  }

  function isResultsVisible() {
    var data = getResultsData();
    if (!data) return true;
    return data.style.display !== 'none';
  }

  /* --- Toast --- */
  function toast(msg) {
    var old = qs('.f9xr-toast');
    if (old) old.remove();
    var t = document.createElement('div');
    t.className = 'f9xr-toast';
    t.textContent = msg;
    document.body.appendChild(t);
    setTimeout(function() {
      t.classList.add('f9xr-out');
      setTimeout(function() { t.remove(); }, 400);
    }, 2500);
  }

  /* --- Save / Load --- */
  function saveInputs() {
    try {
      var data = getValues();
      data._saved = Date.now();
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (e) {/* ignore */}
  }

  function loadInputs() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var data = JSON.parse(raw);
      if (!data._saved) return null;
      return data;
    } catch (e) { return null; }
  }

  function applySaved() {
    var data = loadInputs();
    if (!data) { toast('No saved inputs found.'); return; }
    setValues(data);
    toast('Saved inputs restored!');
  }

  function clearSaved() {
    try { localStorage.removeItem(STORAGE_KEY); } catch (e) {/* ignore */}
  }

  /* --- Trigger Calculate --- */
  function triggerCalc() {
    /* Dispatch change on first input to trigger tool's own listeners */
    var inputs = findInputs();
    if (inputs.length > 0) {
      inputs[0].dispatchEvent(new Event('change', { bubbles: true }));
      return;
    }
    /* Fallback: click the calc button */
    var btn = $('ts-calc-btn');
    if (btn) { btn.click(); }
  }

  /* --- Share URL --- */
  function buildShareURL() {
    var base = window.location.href.split('?')[0].split('#')[0];
    var vals = getValues();
    var parts = [];
    for (var k in vals) {
      if (vals.hasOwnProperty(k)) {
        parts.push(encodeURIComponent(k) + '=' + encodeURIComponent(vals[k]));
      }
    }
    return parts.length ? base + '?' + parts.join('&') : base;
  }

  function copyLink() {
    var url = buildShareURL();
    if (navigator.clipboard) {
      navigator.clipboard.writeText(url).then(function() {
        toast('Link copied to clipboard!');
      }).catch(function() {
        fallbackCopy(url);
      });
    } else {
      fallbackCopy(url);
    }
  }

  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); toast('Link copied!'); } catch (e) { toast('Press Ctrl+C to copy'); }
    document.body.removeChild(ta);
  }

  function handleQueryParams() {
    var q = window.location.search.substring(1);
    if (!q) return;
    var params = new URLSearchParams(q);
    var vals = {};
    var found = false;
    findInputs().forEach(function(el) {
      if (params.has(el.id)) {
        vals[el.id] = params.get(el.id);
        found = true;
      }
    });
    if (!found) return;
    setValues(vals);
  }

  function updateURL() {
    var url = buildShareURL();
    if (url !== window.location.href) {
      window.history.replaceState({}, '', url);
    }
  }

  /* --- Theme --- */
  function applyTheme(theme) {
    document.documentElement.classList.toggle('light-mode', theme === 'light');
    try { localStorage.setItem('f9xr-theme', theme); } catch (e) {/* ignore */}
    var btn = $('f9xr-theme-btn');
    if (btn) {
      btn.innerHTML = theme === 'light'
        ? '<i class="fa-solid fa-moon"></i><span>Theme</span>'
        : '<i class="fa-solid fa-sun"></i><span>Theme</span>';
    }
  }

  function toggleTheme() {
    var cur = document.documentElement.classList.contains('light-mode') ? 'light' : 'dark';
    applyTheme(cur === 'dark' ? 'light' : 'dark');
  }

  /* --- Light Mode CSS --- */
  function injectLightCSS() {
    var s = document.createElement('style');
    s.id = 'f9xr-light-css';
    s.textContent =
      'html.light-mode{--bg-p:#ffffff;--bg-s:#f3f4f6;--bg-c:#ffffff;--t-p:#1f2937;--t-s:#4b5563;--t-m:#9ca3af;--b-c:#e5e7eb}' +
      'html.light-mode body{background:#fff!important}' +
      'html.light-mode .text-bright-snow,html.light-mode .hero-value,html.light-mode h1,html.light-mode h2,html.light-mode h3,html.light-mode label{color:var(--t-p)!important}' +
      'html.light-mode .text-platinum,html.light-mode .text-white\/70,html.light-mode .text-white\/60{color:var(--t-s)!important}' +
      'html.light-mode .text-white\/50,html.light-mode .text-white\/40,html.light-mode .text-white\/30{color:var(--t-m)!important}' +
      'html.light-mode .bg-carbon-black{background:#fff!important}' +
      'html.light-mode .bg-gunmetal{background:var(--bg-s)!important}' +
      'html.light-mode .bg-gunmetal\/40,html.light-mode .bg-gunmetal\/30{background:rgba(243,244,246,.7)!important}' +
      'html.light-mode .bg-carbon-black\/60,html.light-mode .bg-carbon-black\/80{background:#f9fafb!important}' +
      'html.light-mode .border-white\/10,html.light-mode .border-white\/5,html.light-mode .border-white\/6{border-color:var(--b-c)!important}' +
      'html.light-mode .field input,html.light-mode .field select{background:#fff!important;color:var(--t-p)!important;border-color:var(--b-c)!important}' +
      'html.light-mode .field select option{background:#fff!important;color:var(--t-p)!important}' +
      'html.light-mode .breakdown-table td{color:var(--t-s)!important}' +
      'html.light-mode .breakdown-table td:last-child{color:var(--t-p)!important}' +
      'html.light-mode .breakdown-table th{color:var(--t-m)!important}' +
      'html.light-mode #ts-results-card,html.light-mode .ts-results-card{background:var(--bg-s)!important}' +
      'html.light-mode ::-webkit-scrollbar-track{background:#f1f1f1!important}' +
      'html.light-mode ::-webkit-scrollbar-thumb{background:#c1c1c1!important}' +
      'html.light-mode .glass-nav{background:rgba(255,255,255,.95)!important}' +
      'html.light-mode .faq-item,html.light-mode .bd-subtotal td{border-color:var(--b-c)!important}' +
      'html.light-mode .ts-calc-card,html.light-mode .ts-hero-card,html.light-mode .results-card-inner{background:var(--bg-c)!important}' +
      'html.light-mode .cost-scale-labels span{color:var(--t-s)!important}' +
      'html.light-mode .bg-accent-blue\/10{background:rgba(59,130,246,.06)!important}' +
      'html.light-mode .field .error-msg{color:#dc2626!important}' +
      'html.light-mode .f9xr-modal-content{background:#fff!important}';
    document.head.appendChild(s);
  }

  /* --- Print CSS --- */
  function injectPrintCSS() {
    var s = document.createElement('style');
    s.id = 'f9xr-print-css';
    s.textContent =
      '@media print{' +
        'body{background:#fff!important;color:#333!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}' +
        '#main-header,.mobile-menu,#backToTop,footer>.footer-inner,footer>.footer-bottom,.faq-section,#seo-tools-grid,#seo-tools-loading,.blog-posts,.f9xr-toolbar,.f9xr-compare-wrap,.f9xr-benchmarks,nav,#mobile-menu,#search-modal,.click-spark-area{display:none!important}' +
        'footer{background:#fff!important;padding:0!important}' +
        'main,.ts-calc-card,.ts-results-card,.breakdown-table{background:#fff!important;color:#333!important;box-shadow:none!important;border:none!important}' +
        '.hero-value,h1,h2,h3,h4{color:#1a1a1a!important}' +
        '.text-bright-snow{color:#1a1a1a!important}' +
        '*{box-shadow:none!important;text-shadow:none!important}' +
        '.field input,.field select{border-color:#ccc!important;background:#f9f9f9!important;color:#333!important}' +
        '@page{margin:1.5cm}' +
      '}';
    document.head.appendChild(s);
  }

  /* --- Comparison --- */
  var snapshots = [];

  function loadSnapshots() {
    try {
      var raw = localStorage.getItem(COMPARE_KEY);
      snapshots = raw ? JSON.parse(raw) : [];
    } catch (e) { snapshots = []; }
  }

  function saveSnapshots() {
    try { localStorage.setItem(COMPARE_KEY, JSON.stringify(snapshots)); } catch (e) {/* ignore */}
  }

  function takeSnapshot() {
    if (!isResultsVisible()) { toast('Run the calculator first!'); return; }
    if (snapshots.length >= 3) { toast('Max 3 snapshots. Remove one first.'); return; }
    snapshots.push({
      id: Date.now(),
      label: 'Snapshot ' + (snapshots.length + 1),
      text: getVisibleResultsText(),
      inputs: getValues(),
      time: new Date().toLocaleString()
    });
    saveSnapshots();
    renderSnapshots();
    showCompare();
    toast('Snapshot saved!');
  }

  function removeSnapshot(id) {
    snapshots = snapshots.filter(function(s) { return s.id !== id; });
    saveSnapshots();
    renderSnapshots();
    if (snapshots.length === 0) hideCompare();
  }

  function loadSnapshot(id) {
    var snap = null;
    for (var i = 0; i < snapshots.length; i++) {
      if (snapshots[i].id === id) { snap = snapshots[i]; break; }
    }
    if (!snap) return;
    setValues(snap.inputs);
    toast('Snapshot loaded!');
  }

  function renderSnapshots() {
    var c = $('f9xr-compare');
    if (!c) return;
    if (snapshots.length === 0) {
      c.innerHTML = '<div class="f9xr-compare-empty">No snapshots yet. Run the calculator and click <strong>Snapshot</strong> to save scenarios for comparison.</div>';
      return;
    }
    var html = '<div class="f9xr-compare-grid">';
    for (var i = 0; i < snapshots.length; i++) {
      var s = snapshots[i];
      var ctx = Object.keys(s.inputs).slice(0, 3).map(function(k) {
        return k.replace('ts-', '') + '=' + s.inputs[k];
      }).join(', ');
      html +=
        '<div class="f9xr-compare-card">' +
          '<div class="f9xr-compare-hd"><strong>' + s.label + '</strong><span class="f9xr-compare-time">' + s.time + '</span></div>' +
          '<button class="f9xr-compare-rm" onclick="(function(){var e=document.getElementById(\'f9xr-enh\');if(e)e.__rm(' + s.id + ')})()" title="Remove">&times;</button>' +
          '<div class="f9xr-compare-val">' + s.text + '</div>' +
          '<div class="f9xr-compare-ctx">' + ctx + '</div>' +
          '<button class="f9xr-compare-load" onclick="(function(){var e=document.getElementById(\'f9xr-enh\');if(e)e.__load(' + s.id + ')})()">Load</button>' +
        '</div>';
    }
    html += '</div>';
    c.innerHTML = html;
  }

  function showCompare() {
    var w = $('f9xr-compare-wrap');
    if (w) w.style.display = '';
  }

  function hideCompare() {
    var w = $('f9xr-compare-wrap');
    if (w) w.style.display = 'none';
  }

  /* --- Benchmarks --- */
  var BENCHMARKS = {
    'website-cost': {
      title: 'Website Cost Benchmarks',
      data: [
        ['Avg. SME site (India)', '₹35K – ₹80K'],
        ['E-commerce build', '₹70K – ₹1.5L'],
        ['Typical redesign', '₹40K – ₹1L'],
        ['Annual maintenance', '₹8K – ₹20K']
      ]
    },
    'freelancer-quote': {
      title: 'Freelance Rate Benchmarks (India)',
      data: [
        ['Web Dev (Mid)', '₹500 – ₹1,200/hr'],
        ['Mobile Dev', '₹800 – ₹1,500/hr'],
        ['Graphic Design', '₹400 – ₹800/hr'],
        ['Content Writing', '₹300 – ₹600/hr'],
        ['Digital Marketing', '₹500 – ₹1,000/hr']
      ]
    },
    'gbp-checker': {
      title: 'GBP Optimization Benchmarks',
      data: [
        ['Complete GBP → direction requests', '68% more'],
        ['Photos added → clicks', '42% more'],
        ['Weekly posting → site clicks', '2.5× more'],
        ['50+ reviews → conversion', '4.6× higher']
      ]
    },
    'local-seo-score': {
      title: 'Local SEO Benchmarks',
      data: [
        ['Local Pack CTR', '44% of searches'],
        ['Top 3 → clicks', '90% share'],
        ['Mobile-friendly → ranking', '53% higher'],
        ['Citations consistency boost', 'Up to 30%']
      ]
    },
    'marketing-budget': {
      title: 'Marketing Budget Benchmarks',
      data: [
        ['B2B services', '8% of revenue'],
        ['E-commerce', '12% of revenue'],
        ['Tech / SaaS', '15% of revenue'],
        ['Local business', '6% of revenue']
      ]
    },
    'redesign-calculator': {
      title: 'Redesign Cost Benchmarks (India)',
      data: [
        ['Basic (20-30 pages)', '₹35K – ₹60K'],
        ['With CMS', '₹50K – ₹1L'],
        ['E-commerce redesign', '₹80K – ₹2L'],
        ['Timeline (standard)', '3–8 weeks']
      ]
    },
    'digital-presence': {
      title: 'Digital Presence Benchmarks',
      data: [
        ['Website + Social → leads', '2.8× more'],
        ['Active social → brand recall', '64% higher'],
        ['Reviews → trust', '91% trust reviews'],
        ['Multi-channel → engagement', '300% higher']
      ]
    }
  };

  function renderBenchmarks() {
    var c = $('f9xr-benchmarks');
    if (!c) return;
    var bm = BENCHMARKS[toolKey];
    if (!bm) { c.style.display = 'none'; return; }
    c.style.display = '';
    var html = '<div class="f9xr-benchmarks-inner"><h4 class="f9xr-benchmarks-title">' + bm.title + '</h4><div class="f9xr-benchmarks-grid">';
    for (var i = 0; i < bm.data.length; i++) {
      html += '<div class="f9xr-bench-item"><span class="f9xr-bench-lbl">' + bm.data[i][0] + '</span><span class="f9xr-bench-val">' + bm.data[i][1] + '</span></div>';
    }
    html += '</div></div>';
    c.innerHTML = html;
  }

  /* --- Keyboard Shortcuts --- */
  function setupKeys() {
    document.addEventListener('keydown', function(e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        triggerCalc();
      }
      if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        saveInputs();
        toast('Inputs saved!');
      }
    });
  }

  /* --- Inject Toolbar --- */
  function injectToolbar() {
    var card = getResultsCard();
    if (!card) return;
    if ($('f9xr-toolbar')) return;

    var tb = document.createElement('div');
    tb.id = 'f9xr-toolbar';
    tb.className = 'f9xr-toolbar';
    tb.innerHTML =
      '<button class="f9xr-tb-btn" data-f9xr="save" title="Save inputs (Ctrl+S)"><i class="fa-solid fa-floppy-disk"></i><span>Save</span></button>' +
      '<button class="f9xr-tb-btn" data-f9xr="load" title="Load saved inputs"><i class="fa-solid fa-download"></i><span>Load</span></button>' +
      '<button class="f9xr-tb-btn" data-f9xr="share" title="Copy shareable link"><i class="fa-solid fa-link"></i><span>Share</span></button>' +
      '<button class="f9xr-tb-btn" data-f9xr="print" title="Save as PDF"><i class="fa-solid fa-file-pdf"></i><span>PDF</span></button>' +
      '<button class="f9xr-tb-btn" id="f9xr-theme-btn" title="Toggle dark/light mode"><i class="fa-solid fa-sun"></i><span>Theme</span></button>' +
      '<button class="f9xr-tb-btn" data-f9xr="snapshot" title="Save snapshot to compare"><i class="fa-solid fa-camera"></i><span>Snapshot</span></button>';

    card.parentNode.insertBefore(tb, card.nextSibling);

    /* Compare section */
    var cw = document.createElement('div');
    cw.id = 'f9xr-compare-wrap';
    cw.className = 'f9xr-compare-wrap';
    cw.innerHTML = '<div class="f9xr-compare-inner"><div id="f9xr-compare" class="f9xr-compare-empty">No snapshots yet.</div></div>';
    tb.parentNode.insertBefore(cw, tb.nextSibling);

    /* Benchmarks section */
    var bm = document.createElement('div');
    bm.id = 'f9xr-benchmarks';
    bm.className = 'f9xr-benchmarks';
    cw.parentNode.insertBefore(bm, cw.nextSibling);

    /* Hidden element for inline function references */
    var enh = document.createElement('div');
    enh.id = 'f9xr-enh';
    enh.style.display = 'none';
    enh.__rm = removeSnapshot;
    enh.__load = loadSnapshot;
    document.body.appendChild(enh);

    /* Delegate clicks */
    tb.addEventListener('click', function(e) {
      var btn = e.target.closest('[data-f9xr]');
      if (!btn) return;
      switch (btn.getAttribute('data-f9xr')) {
        case 'save': saveInputs(); toast('Inputs saved!'); break;
        case 'load': applySaved(); break;
        case 'share': copyLink(); break;
        case 'print': window.print(); break;
        case 'snapshot': takeSnapshot(); break;
      }
    });
  }

  /* --- Post-calc hook (called after each calculate) --- */
  function afterCalc() {
    updateURL();
    if (isResultsVisible()) {
      animateResults();
      renderSnapshots();
      if (snapshots.length > 0) showCompare();
    }
  }

  /* --- Animation --- */
  var _animating = false;

  function animateResults() {
    if (_animating) return;
    _animating = true;
    var data = getResultsData();
    if (data) {
      data.classList.remove('f9xr-animate');
      void data.offsetWidth;
      data.classList.add('f9xr-animate');
    }
    setTimeout(function() { _animating = false; }, 600);
  }

  /* --- Debounced after-calc --- */
  var _pendingCalc = false;

  function queueAfterCalc() {
    if (_pendingCalc) return;
    _pendingCalc = true;
    setTimeout(function() {
      _pendingCalc = false;
      afterCalc();
    }, 120);
  }

  /* --- Mutation Observer for auto-detecting calculates --- */
  function watchResults() {
    var data = getResultsData();

    if (data) {
      /* Tools with ts-results-data: watch display toggle and content */
      var obs = new MutationObserver(function() {
        if (data.style.display !== 'none') {
          queueAfterCalc();
        }
      });
      obs.observe(data, {
        attributes: true,
        attributeFilter: ['style'],
        childList: true,
        subtree: true
      });
    }

    /* For ALL tools: watch content changes on output elements (spans, divs with ts- ids) */
    qsa('[id^="ts-"]').forEach(function(el) {
      var tag = el.tagName;
      if (tag === 'SPAN' || tag === 'DIV' || tag === 'P' || tag === 'H1' || tag === 'H2' || tag === 'H3' || tag === 'H4') {
        if (el.id === 'ts-empty-state' || el.id === 'ts-results-data') return;
        if (el.closest('.field') || el.tagName === 'INPUT' || el.tagName === 'SELECT') return;
        var obs = new MutationObserver(function() {
          if (isResultsVisible()) queueAfterCalc();
        });
        obs.observe(el, { childList: true, characterData: true, subtree: true });
      }
    });
  }

  /* --- Auto-save on input change --- */
  function watchInputs() {
    findInputs().forEach(function(el) {
      el.addEventListener('change', function() {
        saveInputs();
      });
    });
  }

  /* --- Init --- */
  function init() {
    if (document.documentElement.getAttribute('data-f9xr-loaded') === '1') return;
    document.documentElement.setAttribute('data-f9xr-loaded', '1');

    injectLightCSS();
    injectPrintCSS();

    /* Theme */
    var savedTheme = (function() {
      try { return localStorage.getItem('f9xr-theme'); } catch (e) { return null; }
    })();
    applyTheme(savedTheme || 'dark');

    watchInputs();
    handleQueryParams();
    setupKeys();
    loadSnapshots();
    injectToolbar();
    renderBenchmarks();

    /* Watch for result changes */
    watchResults();

    /* If calculate was already called (results visible), update */
    if (isResultsVisible()) {
      afterCalc();
    }

    /* Expose globally */
    window.__f9xrCalc = triggerCalc;
    window.F9XR_TRIGGER = queueAfterCalc;
    window.F9XR_TOAST = toast;
  }

  /* Run after DOM ready */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    setTimeout(init, 50);
  }

})();
