// ─── GA4 Event Tracking via dataLayer (shared, site-wide) ───
// Spójne eventy konwersji: cta_click, phone_click, email_click, scroll_depth, faq_click.
// Zabezpieczone przed podwójną inicjalizacją (gdyby strona miała też tracking inline).
(function () {
  if (window.__dfTrackInit) return;
  window.__dfTrackInit = true;
  window.dataLayer = window.dataLayer || [];

  function init() {
    // CTA — kliknięcia w zapytanie/wycenę i główne przyciski
    document.querySelectorAll('a[href*="zapytanie"], a[href^="#formularz"], .btn-red-solid, .btn-green, .btn-feed, .cta-primary').forEach(function (el) {
      el.addEventListener('click', function () {
        dataLayer.push({ event: 'cta_click', cta_text: this.textContent.trim().slice(0, 50), cta_url: this.href, page: location.pathname });
      });
    });
    // Telefon
    document.querySelectorAll('a[href^="tel:"]').forEach(function (el) {
      el.addEventListener('click', function () {
        dataLayer.push({ event: 'phone_click', page: location.pathname });
      });
    });
    // E-mail
    document.querySelectorAll('a[href^="mailto:"]').forEach(function (el) {
      el.addEventListener('click', function () {
        dataLayer.push({ event: 'email_click', page: location.pathname });
      });
    });
    // Głębokość scrolla
    var marks = [25, 50, 75, 100], fired = {};
    window.addEventListener('scroll', function () {
      var pct = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
      marks.forEach(function (m) { if (pct >= m && !fired[m]) { fired[m] = true; dataLayer.push({ event: 'scroll_depth', depth: m, page: location.pathname }); } });
    }, { passive: true });
    // Otwarcie FAQ
    document.querySelectorAll('.faq-q, details summary').forEach(function (el) {
      el.addEventListener('click', function () {
        dataLayer.push({ event: 'faq_click', question: this.textContent.trim().slice(0, 80), page: location.pathname });
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
