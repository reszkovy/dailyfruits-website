/* ═══════════════════════════════════════════════════════════════════
   DailyFruits — smooth scroll (Lenis).
   Przejscia miedzy stronami obsluguje LEKKI fade (inline pt-out/pt-in).
   Ciezki overlay + blur(8px) + podwojna animacja wejscia zostaly usuniete
   dla plynnosci (powodowaly stutter przy przeladowaniach).
   ═══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  if (typeof Lenis === 'undefined') return;
  var lenis = new Lenis({
    lerp: 0.1,
    duration: 1.5,
    smoothWheel: true,
    autoResize: true,
    syncTouch: false,
  });
  function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
  requestAnimationFrame(raf);
})();
