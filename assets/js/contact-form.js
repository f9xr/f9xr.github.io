/* F9XR Contact Form Cooldown v1.0 */
(function () {
  'use strict';

  var COOLDOWN_SECONDS = 45;
  var STORE_KEY = 'f9xr_last_form_submit';

  function getRemaining() {
    try {
      var last = parseInt(window.localStorage.getItem(STORE_KEY), 10);
      if (!last) return 0;
      var elapsed = Math.floor((Date.now() - last) / 1000);
      return elapsed < COOLDOWN_SECONDS ? COOLDOWN_SECONDS - elapsed : 0;
    } catch (e) {
      return 0;
    }
  }

  function markSubmitted() {
    try {
      window.localStorage.setItem(STORE_KEY, String(Date.now()));
    } catch (e) {
      /* storage unavailable (private mode / disabled) - fail open */
    }
  }

  window.F9XRCooldown = {
    seconds: COOLDOWN_SECONDS,
    getRemaining: getRemaining,
    markSubmitted: markSubmitted
  };
})();
