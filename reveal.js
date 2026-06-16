// ─── Reveal on scroll (shared) ───
// shared.css ma .reveal{opacity:0} i .reveal.vis{opacity:1}.
// Ten skrypt dodaje .vis: od razu dla elementów w widoku, na scroll dla reszty.
// Bez niego elementy .reveal zostają niewidoczne = puste przerwy.
(function () {
  function run() {
    var els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (e) { e.classList.add('vis'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('vis'); io.unobserve(en.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -5% 0px' });
    els.forEach(function (e) { io.observe(e); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
})();
