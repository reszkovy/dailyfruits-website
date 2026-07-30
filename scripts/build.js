#!/usr/bin/env node
/*
 * DailyFruits — lekki build includes (bez frameworka).
 * Wstrzykuje partiale z _includes/ w bloki oznaczone:
 *   <!--#include:NAZWA-->  ...zawartosc...  <!--#endinclude:NAZWA-->
 * Idempotentny: nadpisuje tylko zawartosc miedzy znacznikami z _includes/NAZWA.html.
 * Edycja nav/footer/GTM = edycja JEDNEGO pliku w _includes/ + `node scripts/build.js`.
 *
 * Uzycie: node scripts/build.js          (przebuduj wszystkie .html w roocie + oferta/)
 *         node scripts/build.js --check  (nie zapisuj; faili jesli cos by sie zmienilo)
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const INC = path.join(ROOT, '_includes');
const CHECK = process.argv.includes('--check');

function listHtml() {
  const out = [];
  for (const e of fs.readdirSync(ROOT)) if (e.endsWith('.html')) out.push(path.join(ROOT, e));
  for (const sub of ['oferta', 'blog']) {
  const od = path.join(ROOT, sub);
  if (fs.existsSync(od)) {
    const walk = d => {
      for (const e of fs.readdirSync(d, { withFileTypes: true })) {
        const p = path.join(d, e.name);
        if (e.isDirectory()) walk(p);
        else if (e.name.endsWith('.html')) out.push(p);
      }
    };
    walk(od);
  }
  }
  return out;
}

const cache = {};
function partial(name) {
  if (!(name in cache)) {
    const p = path.join(INC, name + '.html');
    cache[name] = fs.existsSync(p) ? fs.readFileSync(p, 'utf8').replace(/\n+$/, '') : null;
  }
  return cache[name];
}

let changed = 0, injected = 0, missing = new Set();
for (const file of listHtml()) {
  const src = fs.readFileSync(file, 'utf8');
  const out = src.replace(
    /(<!--#include:([\w-]+)-->)([\s\S]*?)(<!--#endinclude:\2-->)/g,
    (m, open, name, _body, close) => {
      const c = partial(name);
      if (c === null) { missing.add(name); return m; }
      injected++;
      return `${open}\n${c}\n${close}`;
    }
  );
  if (out !== src) {
    changed++;
    if (!CHECK) fs.writeFileSync(file, out);
  }
}

if (missing.size) {
  console.error('BRAK partiali w _includes/: ' + [...missing].join(', '));
  process.exit(2);
}
console.log(`Wstrzyknieto blokow: ${injected} | plikow ${CHECK ? 'do zmiany' : 'zmienionych'}: ${changed}`);
if (CHECK && changed > 0) {
  console.error('FAIL: pliki nie sa zgodne z _includes/ — uruchom `node scripts/build.js`');
  process.exit(1);
}
