/* F9XR Skeleton Loader v1.0 */
(function () {
  'use strict';

  var overlay = document.getElementById('skel-overlay');
  if (!overlay) return;

  var minDisplay = 800;
  var startTime = Date.now();

  function hideSkeleton() {
    var elapsed = Date.now() - startTime;
    var remaining = Math.max(0, minDisplay - elapsed);

    setTimeout(function () {
      overlay.classList.add('skel-hidden');
      setTimeout(function () {
        if (overlay && overlay.parentNode) {
          overlay.parentNode.removeChild(overlay);
        }
      }, 500);
    }, remaining);
  }

  if (document.readyState === 'complete') {
    hideSkeleton();
  } else {
    window.addEventListener('load', hideSkeleton);
  }

  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'visible' && overlay && !overlay.classList.contains('skel-hidden')) {
      var elapsed = Date.now() - startTime;
      if (elapsed > minDisplay + 2000) {
        hideSkeleton();
      }
    }
  });
})();
