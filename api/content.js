// CMS API — edycja tresci stron statycznych (home, oferta, podstrony) + menu.
// Wymagane env: GITHUB_TOKEN, GITHUB_REPO, CMS_PASSWORD. Opcjonalne: GITHUB_BRANCH.
//
// Model edycji tekstow: inwentarz z offsetami znakowymi.
//   GET ?action=pages            — lista edytowalnych stron
//   GET ?action=texts&page=X     — {sha, meta, items:[{id,start,end,text,tag,section,kind}]}
//   PUT ?action=texts&page=X     — {sha, edits:[{start,end,old,text}]} → commit
//   GET ?action=menu             — pozycje nawigacji (etykiety + hrefy z index.html)
//   PUT ?action=menu             — {items:[{href,label}], cta} → podmiana etykiet we
//                                  wszystkich stronach + _includes/mobile-menu.html (1 commit)
//
// Edycja przez offsety: klient odsyla stare (start,end,old) + nowy tekst; serwer
// weryfikuje sha pliku i zgodnosc wycinka, aplikuje od konca — struktura HTML
// pozostaje nietknieta. (Helpery GitHub celowo skopiowane z posts.js — funkcje
// serverless bundlowane sa osobno.)

const GITHUB_API = 'https://api.github.com';

const repo = () => process.env.GITHUB_REPO;
const branch = () => process.env.GITHUB_BRANCH || 'main';

function verifyAuth(req) {
  const auth = req.headers['x-cms-token'];
  if (!auth || !process.env.CMS_PASSWORD) return false;
  return Buffer.from(auth, 'base64').toString() === `cms:${process.env.CMS_PASSWORD}`;
}

async function gh(path, options = {}) {
  return fetch(`${GITHUB_API}${path}`, {
    ...options,
    headers: {
      'Authorization': `Bearer ${process.env.GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json',
      ...(options.headers || {})
    }
  });
}

async function readFile(path) {
  const res = await gh(`/repos/${repo()}/contents/${encodeURIComponent(path)}?ref=${branch()}`);
  if (!res.ok) return null;
  const data = await res.json();
  return { content: Buffer.from(data.content, 'base64').toString('utf-8'), sha: data.sha };
}

async function listDir(path) {
  const res = await gh(`/repos/${repo()}/contents/${encodeURIComponent(path)}?ref=${branch()}`);
  if (!res.ok) return [];
  return res.json();
}

async function commitFiles(files, message) {
  const refRes = await gh(`/repos/${repo()}/git/ref/heads/${branch()}`);
  if (!refRes.ok) throw new Error('Nie mozna odczytac galezi ' + branch());
  const baseSha = (await refRes.json()).object.sha;
  const baseCommitRes = await gh(`/repos/${repo()}/git/commits/${baseSha}`);
  const baseTree = (await baseCommitRes.json()).tree.sha;
  const tree = files.map(f => ({ path: f.path, mode: '100644', type: 'blob', content: f.content }));
  const treeRes = await gh(`/repos/${repo()}/git/trees`, { method: 'POST', body: JSON.stringify({ base_tree: baseTree, tree }) });
  if (!treeRes.ok) throw new Error('Blad tworzenia drzewa: ' + (await treeRes.text()).slice(0, 200));
  const treeSha = (await treeRes.json()).sha;
  const commitRes = await gh(`/repos/${repo()}/git/commits`, { method: 'POST', body: JSON.stringify({ message, tree: treeSha, parents: [baseSha] }) });
  if (!commitRes.ok) throw new Error('Blad tworzenia commita');
  const commitSha = (await commitRes.json()).sha;
  const updateRes = await gh(`/repos/${repo()}/git/refs/heads/${branch()}`, { method: 'PATCH', body: JSON.stringify({ sha: commitSha, force: false }) });
  if (!updateRes.ok) throw new Error('Konflikt zapisu (ktos wlasnie commitowal) — sprobuj ponownie');
  return commitSha;
}

// ─── INWENTARZ TEKSTOW ───

const VOID_TAGS = new Set(['img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'area', 'base', 'col', 'embed', 'track', 'wbr']);
const SKIP_CONTENT = new Set(['script', 'style', 'svg', 'noscript', 'head']);

function decode(s) {
  return s.replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#0?39;/g, "'").replace(/&amp;/g, '&');
}
function encodeNode(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
function encodeAttr(s) { return s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

function extractTexts(html) {
  const items = [];
  let id = 0;

  // <title>
  const t = html.match(/<title>([\s\S]*?)<\/title>/);
  if (t) items.push({ id: id++, start: t.index + 7, end: t.index + 7 + t[1].length, text: decode(t[1]), tag: 'title', section: 'SEO strony', kind: 'node' });

  // meta description + og:description
  for (const re of [/<meta name="description" content="/g, /<meta property="og:description" content="/g]) {
    let m;
    while ((m = re.exec(html)) !== null) {
      const start = m.index + m[0].length;
      const end = html.indexOf('"', start);
      if (end > start) items.push({ id: id++, start, end, text: decode(html.slice(start, end)), tag: 'meta', section: 'SEO strony', kind: 'attr' });
    }
  }

  // Tokenizacja body: teksty miedzy tagami + alty obrazkow
  const bodyStart = html.search(/<body[^>]*>/);
  if (bodyStart < 0) return items;

  const tagRe = /<!--[\s\S]*?-->|<[^>]+>/g;
  tagRe.lastIndex = bodyStart;
  const stack = [];
  let skipDepthTag = null;
  let lastSection = 'Poczatek strony';
  let lastIndex = tagRe.lastIndex;
  let m;
  let headingCapture = null; // {tag, buf:[]}

  while ((m = tagRe.exec(html)) !== null) {
    const between = html.slice(lastIndex, m.index);
    if (between.trim() && !skipDepthTag) {
      const raw = between;
      const trimmedStart = raw.length - raw.replace(/^\s+/, '').length;
      const trimmedEnd = raw.length - raw.replace(/\s+$/, '').length;
      const start = lastIndex + trimmedStart;
      const end = m.index - trimmedEnd;
      const text = decode(raw.trim());
      const tag = stack.length ? stack[stack.length - 1] : 'body';
      if (text.length >= 2 && !/^[\d\s.,:;|→←•-]+$/.test(text)) {
        items.push({ id: id++, start, end, text, tag, section: lastSection, kind: 'node' });
      }
      if (headingCapture) headingCapture.buf.push(text);
    }
    lastIndex = tagRe.lastIndex;

    const token = m[0];
    if (token.startsWith('<!--')) continue;
    const isClose = token.startsWith('</');
    const nameM = token.match(/^<\/?\s*([a-zA-Z0-9-]+)/);
    if (!nameM) continue;
    const name = nameM[1].toLowerCase();

    if (!isClose && name === 'img') {
      const altM = token.match(/\balt="([^"]*)"/);
      if (altM && altM[1].trim().length >= 2 && !skipDepthTag) {
        const altStart = m.index + token.indexOf(altM[0]) + 5;
        items.push({ id: id++, start: altStart, end: altStart + altM[1].length, text: decode(altM[1]), tag: 'img-alt', section: lastSection, kind: 'attr' });
      }
    }
    if (VOID_TAGS.has(name)) continue;
    const selfClosed = token.endsWith('/>');
    if (selfClosed) continue;

    if (isClose) {
      const idx = stack.lastIndexOf(name);
      if (idx >= 0) stack.length = idx;
      if (skipDepthTag === name) skipDepthTag = null;
      if (headingCapture && headingCapture.tag === name) {
        const txt = headingCapture.buf.join(' ').trim();
        if (txt) lastSection = txt.slice(0, 60);
        headingCapture = null;
      }
    } else {
      stack.push(name);
      if (SKIP_CONTENT.has(name) && !skipDepthTag) skipDepthTag = name;
      if (/^h[1-3]$/.test(name) && !headingCapture) headingCapture = { tag: name, buf: [] };
    }
  }
  return items;
}

function applyEdits(html, edits) {
  const sorted = [...edits].sort((a, b) => b.start - a.start);
  for (const e of sorted) {
    if (typeof e.start !== 'number' || typeof e.end !== 'number' || e.end < e.start) throw new Error('Nieprawidlowy zakres edycji');
    const current = html.slice(e.start, e.end);
    if (decode(current.trim()) !== decode(String(e.old).trim())) {
      throw new Error(`Tekst zmienil sie w miedzyczasie ("${String(e.old).slice(0, 40)}..."). Odswiez strone i sprobuj ponownie.`);
    }
    const enc = e.kind === 'attr' ? encodeAttr(String(e.text)) : encodeNode(String(e.text));
    html = html.slice(0, e.start) + enc + html.slice(e.end);
  }
  return html;
}

// ─── STRONY ───

const PAGE_EXCLUDE = /^(admin|404|wpis-.*)\.html$/;

async function listPages() {
  const [root, oferta] = await Promise.all([listDir(''), listDir('oferta')]);
  const pages = [];
  for (const f of root) {
    if (f.type === 'file' && f.name.endsWith('.html') && !PAGE_EXCLUDE.test(f.name)) {
      pages.push({ path: f.name, group: f.name === 'index.html' ? 'Glowne' : 'Strony' });
    }
  }
  for (const f of (Array.isArray(oferta) ? oferta : [])) {
    if (f.type === 'file' && f.name.endsWith('.html')) pages.push({ path: 'oferta/' + f.name, group: 'Oferta' });
  }
  const KEY = ['index.html', 'oferta.html', 'dostawa.html', 'o-nas.html', 'kontakt.html', 'zapytanie.html', 'blog.html'];
  pages.sort((a, b) => {
    const ka = KEY.indexOf(a.path), kb = KEY.indexOf(b.path);
    if (ka >= 0 || kb >= 0) return (ka < 0 ? 99 : ka) - (kb < 0 ? 99 : kb);
    return a.path.localeCompare(b.path, 'pl');
  });
  if (KEY.slice(0, 7).some(k => pages.find(p => p.path === k))) {
    for (const p of pages) if (KEY.includes(p.path)) p.group = 'Glowne';
  }
  return pages;
}

function safePage(page) {
  return typeof page === 'string' && /^(oferta\/)?[a-z0-9-]+\.html$/.test(page) && !PAGE_EXCLUDE.test(page.replace('oferta/', ''));
}

// ─── MENU ───

function parseMenu(html) {
  const navM = html.match(/<ul class="nav-links">([\s\S]*?)<\/ul>/);
  const items = [];
  if (navM) {
    const liRe = /<li><a href="(\/?[a-z0-9-]*)"[^>]*>([^<]*)<\/a><\/li>/g;
    let m;
    while ((m = liRe.exec(navM[1])) !== null) items.push({ href: m[1].replace(/^\//, ''), label: decode(m[2]) });
  }
  const ctaM = html.match(/class="btn btn-nav-cta"[^>]*>([^<]*)</);
  return { items, cta: ctaM ? decode(ctaM[1]) : 'Zapytanie' };
}

function replaceMenuLabels(html, items, cta) {
  for (const it of items) {
    const label = encodeNode(it.label).replace(/\$/g, '$$$$');
    // desktop nav: href z "/" lub bez
    html = html.replace(new RegExp(`(<li><a href="/?${it.href}"[^>]*>)[^<]*(</a></li>)`, 'g'), `$1${label}$2`);
    // mobile menu
    html = html.replace(new RegExp(`(<a href="/${it.href}" class="mn-link"[^>]*>)[^<]*(</a>)`, 'g'), `$1${label}$2`);
  }
  if (cta) {
    const c = encodeNode(cta).replace(/\$/g, '$$$$');
    html = html.replace(/(class="btn btn-nav-cta"[^>]*>)[^<]*(<)/g, `$1${c}$2`);
    html = html.replace(/(class="mn-cta"[^>]*>)[^<]*(<)/g, `$1${c} →$2`);
  }
  return html;
}

// ─── HANDLER ───

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, PUT, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-CMS-Token');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (!verifyAuth(req)) return res.status(401).json({ error: 'Unauthorized' });

  const { method } = req;
  const { action, page } = req.query;

  try {
    if (method === 'GET' && action === 'pages') {
      return res.status(200).json({ pages: await listPages() });
    }

    if (method === 'GET' && action === 'texts') {
      if (!safePage(page)) return res.status(400).json({ error: 'Nieprawidlowa strona' });
      const file = await readFile(page);
      if (!file) return res.status(404).json({ error: 'Nie znaleziono strony' });
      return res.status(200).json({ sha: file.sha, items: extractTexts(file.content) });
    }

    if (method === 'PUT' && action === 'texts') {
      if (!safePage(page)) return res.status(400).json({ error: 'Nieprawidlowa strona' });
      const { sha, edits } = req.body || {};
      if (!sha || !Array.isArray(edits) || !edits.length) return res.status(400).json({ error: 'sha i edits wymagane' });
      if (edits.length > 300) return res.status(400).json({ error: 'Za duzo edycji naraz' });
      const file = await readFile(page);
      if (!file) return res.status(404).json({ error: 'Nie znaleziono strony' });
      if (file.sha !== sha) return res.status(409).json({ error: 'Strona zmienila sie w miedzyczasie — odswiez i sprobuj ponownie' });
      const newHtml = applyEdits(file.content, edits);
      const commit = await commitFiles([{ path: page, content: newHtml }], `CMS: edycja tresci ${page} (${edits.length} zmian)`);
      return res.status(200).json({ ok: true, commit });
    }

    if (method === 'GET' && action === 'menu') {
      const file = await readFile('index.html');
      if (!file) return res.status(500).json({ error: 'Nie mozna pobrac index.html' });
      return res.status(200).json(parseMenu(file.content));
    }

    if (method === 'PUT' && action === 'menu') {
      const { items, cta } = req.body || {};
      if (!Array.isArray(items) || !items.length) return res.status(400).json({ error: 'items wymagane' });
      for (const it of items) {
        if (!/^[a-z0-9-]{1,40}$/.test(it.href || '') || typeof it.label !== 'string' || !it.label.trim() || it.label.length > 40) {
          return res.status(400).json({ error: 'Nieprawidlowa pozycja menu' });
        }
      }

      const [root, oferta] = await Promise.all([listDir(''), listDir('oferta')]);
      const paths = [
        ...root.filter(f => f.type === 'file' && f.name.endsWith('.html')).map(f => f.name),
        ...(Array.isArray(oferta) ? oferta : []).filter(f => f.type === 'file' && f.name.endsWith('.html')).map(f => 'oferta/' + f.name),
        '_includes/mobile-menu.html'
      ];

      const files = [];
      for (const p of paths) {
        const file = await readFile(p);
        if (!file) continue;
        const updated = replaceMenuLabels(file.content, items, cta);
        if (updated !== file.content) files.push({ path: p, content: updated });
      }
      if (!files.length) return res.status(200).json({ ok: true, commit: null, changed: 0 });
      const commit = await commitFiles(files, `CMS: aktualizacja etykiet menu (${files.length} plikow)`);
      return res.status(200).json({ ok: true, commit, changed: files.length });
    }

    return res.status(400).json({ error: 'Nieznana akcja. Dostepne: pages, texts, menu' });
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}
