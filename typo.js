// ─── Polska typografia: wiszące spójniki, myślniki i sieroty (widows) ───
// Wstawia twardą spację ( ) po jednoliterowych spójnikach/przyimkach (a, i, o, u, w, z…),
// przykleja myślnik do poprzedzającego słowa i zapobiega samotnemu ostatniemu słowu w bloku.
// Działa po stronie klienta, na treści (pomija nav/script/style/code).
(function () {
  if (window.__dfTypo) return;
  window.__dfTypo = true;
  var NBSP = ' ';
  // jednoliterowe wyrazy (PL) + popularne dwuliterowe przyimki/spójniki
  var ONE = /(^|[\s( „"»])([aiouwzAIOUWZ])[ \t]+/g;
  var TWO = /(^|[\s( „"»])(do|we|ze|za|na|od|po|to|że|by|si|np|tj|nr)[ \t]+/gi;

  function glue(t) {
    var s = t;
    for (var i = 0; i < 2; i++) {                  // 2x dla ciągów typu "i o tym"
      s = s.replace(ONE, function (m, p, w) { return p + w + NBSP; });
    }
    s = s.replace(TWO, function (m, p, w) { return p + w + NBSP; });
    // myślnik/dywiz jako pauza: NIE może kończyć wiersza - przyklej go do słowa następnego
    // (spacja przed myślnikiem łamliwa, twarda spacja po myślniku => "- słowo" schodzą razem)
    s = s.replace(/[ \t]+([-–—])[ \t]+/g, ' $1' + NBSP);
    return s;
  }

  function walk(node) {
    for (var n = node.firstChild; n; n = n.nextSibling) {
      if (n.nodeType === 3) {
        var v = glue(n.nodeValue);
        if (v !== n.nodeValue) n.nodeValue = v;
      } else if (n.nodeType === 1 && !/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(n.tagName)) {
        walk(n);
      }
    }
  }

  function widow(el) {
    var last = null;
    (function find(node) {
      for (var c = node.firstChild; c; c = c.nextSibling) {
        if (c.nodeType === 3 && c.nodeValue.trim()) last = c;
        else if (c.nodeType === 1 && !/^(SCRIPT|STYLE)$/.test(c.tagName)) find(c);
      }
    })(el);
    if (last && /\s\S+\s*$/.test(last.nodeValue)) {
      last.nodeValue = last.nodeValue.replace(/[ \t]+(\S+)([ \t]*)$/, NBSP + '$1$2');
    }
  }

  function run() {
    if (!document.body) return;
    walk(document.body);
    document.querySelectorAll('h1,h2,h3,h4,p,li,figcaption,blockquote,.tagline,summary').forEach(widow);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
})();
