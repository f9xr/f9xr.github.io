/* Page Transition — Fade (internal links only) */
(function () {
    'use strict';

    var DURATION = 280;

    document.addEventListener('DOMContentLoaded', function () {
        document.body.classList.add('page-enter');
        document.body.addEventListener('animationend', function handler(e) {
            if (e.animationName === 'pageFadeIn') {
                document.body.classList.remove('page-enter');
                document.body.removeEventListener('animationend', handler);
            }
        });
    });

    document.addEventListener('click', function (e) {
        var link = e.target.closest('a');
        if (!link) return;

        if (link.hasAttribute('data-no-transition')) return;
        if (link.target === '_blank') return;
        if (link.hostname && link.hostname !== location.hostname) return;
        if (link.hash && link.pathname === location.pathname) return;
        if (link.href.indexOf('mailto:') === 0) return;
        if (link.href.indexOf('tel:') === 0) return;

        var url;
        try { url = new URL(link.href); } catch (_) { return; }
        if (url.pathname === location.pathname && url.search === location.search) return;

        e.preventDefault();
        document.body.classList.add('page-exit', 'page-transitioning');

        setTimeout(function () {
            location.href = link.href;
        }, DURATION);
    });
})();
