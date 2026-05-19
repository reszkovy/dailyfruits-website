/* ═══════════════════════════════════════════════════════════════════
   DailyFruits Page Transition — soft motion + blur per element
   Nav stays visible throughout (preserved across page swap).
   Exit:  content sections drift down + blur out, soft cascade
   Enter: content sections float up from blur, soft cascade
   Nav: never animated, always on top.
   ═══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var transitioning = false;
  var EASE_OUT = 'cubic-bezier(.25,.46,.45,.94)';
  var EASE_IN  = 'cubic-bezier(.22,1,.36,1)';

  // ─── Cream overlay — sits BELOW nav (z-index 99) but above content ───
  var overlay = document.createElement('div');
  overlay.id = 'dfOverlay';
  overlay.setAttribute('aria-hidden', 'true');
  overlay.style.cssText = 'position:fixed;inset:0;z-index:99;pointer-events:none;'
    + 'background:var(--cream,#FFF9E0);opacity:0;transition:opacity .35s ease;';
  document.body.appendChild(overlay);

  // ─── Bump nav above overlay permanently ───
  var navHeader = document.querySelector('body > header');
  if (navHeader) navHeader.style.zIndex = '200';

  // ─── Gather content elements (NOT nav, NOT mobile overlay) ───
  function getElements() {
    return Array.prototype.slice.call(
      document.querySelectorAll('body > section, body > main, body > footer, body > .wave-divider, body > .marquee-section, body > .photo-break, body > #scrollFrameWrap')
    ).filter(function (el) {
      return el.id !== 'dfOverlay' && el.offsetParent !== null;
    });
  }

  // ─── EXIT ───
  function runExit(href) {
    if (prefersReduced) {
      getElements().forEach(function (el) {
        el.style.transition = 'opacity 150ms ease';
        el.style.opacity = '0';
      });
      setTimeout(function () { window.location.href = href; }, 160);
      return;
    }

    var els = getElements();
    // Overlay fades in behind nav, covering content area
    overlay.style.opacity = '1';

    els.forEach(function (el, i) {
      var delay = i * 25;
      el.style.transition = 'opacity .35s ' + EASE_OUT + ' ' + delay + 'ms, '
        + 'transform .4s ' + EASE_OUT + ' ' + delay + 'ms, '
        + 'filter .35s ' + EASE_OUT + ' ' + delay + 'ms';
      el.style.opacity = '0';
      el.style.transform = 'translateY(14px) scale(0.98)';
      el.style.filter = 'blur(8px)';
    });

    var totalTime = 400 + Math.min(els.length * 25, 150);
    setTimeout(function () { window.location.href = href; }, totalTime);
  }

  // ─── ENTER ───
  function runEnter() {
    // Nav: immediately visible, no animation
    var hdr = document.querySelector('body > header');
    if (hdr) hdr.style.zIndex = '200';

    var els = getElements();

    if (prefersReduced) {
      els.forEach(function (el) {
        el.style.opacity = '0';
        el.style.transition = 'opacity 150ms ease';
        requestAnimationFrame(function () { el.style.opacity = '1'; });
      });
      setTimeout(cleanup, 200);
      return;
    }

    // Start state: below, blurred, invisible
    els.forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px) scale(0.98)';
      el.style.filter = 'blur(8px)';
      el.style.transition = 'none';
    });

    // Overlay visible behind nav, will fade
    overlay.style.transition = 'none';
    overlay.style.opacity = '1';

    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        els.forEach(function (el, i) {
          var delay = i * 35;
          el.style.transition = 'opacity .45s ' + EASE_IN + ' ' + delay + 'ms, '
            + 'transform .5s ' + EASE_IN + ' ' + delay + 'ms, '
            + 'filter .45s ' + EASE_IN + ' ' + delay + 'ms';
          el.style.opacity = '1';
          el.style.transform = 'translateY(0) scale(1)';
          el.style.filter = 'blur(0px)';
        });

        overlay.style.transition = 'opacity .4s ' + EASE_IN;
        overlay.style.opacity = '0';
      });
    });

    var totalTime = 500 + Math.min(els.length * 35, 200);
    setTimeout(cleanup, totalTime + 100);
  }

  function cleanup() {
    getElements().forEach(function (el) {
      el.style.transition = '';
      el.style.opacity = '';
      el.style.transform = '';
      el.style.filter = '';
    });
    overlay.style.opacity = '0';
    transitioning = false;
  }

  // ─── ENTER: if arrived via transition ───
  if (sessionStorage.getItem('df-transition')) {
    sessionStorage.removeItem('df-transition');
    runEnter();
  }

  // ─── EXIT: intercept internal links ───
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a');
    if (!link) return;
    var href = link.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel') || link.target === '_blank') return;

    e.preventDefault();
    if (transitioning) return;
    transitioning = true;

    sessionStorage.setItem('df-transition', '1');
    runExit(href);
  });

  // ─── LENIS SMOOTH SCROLL ───
  if (typeof Lenis !== 'undefined') {
    var lenis = new Lenis({
      lerp: 0.1,
      duration: 1.5,
      smoothWheel: true,
      autoResize: true,
      syncTouch: false,
    });
    function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
  }
})();
