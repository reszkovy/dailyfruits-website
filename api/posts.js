// Blog CMS API — CRUD wpisow blogowych przez GitHub API.
// Wymagane env: GITHUB_TOKEN (contents:write), GITHUB_REPO ("owner/repo"), CMS_PASSWORD.
// Opcjonalne env: GITHUB_BRANCH (domyslnie "main").
//
// Akcje:
//   GET    ?action=list                 — lista wpisow (zrodlo: karty w blog.html)
//   GET    ?action=get&slug=X           — pola wpisu + rawHtml
//   PUT    ?action=update&slug=X        — zapis pol (fields) LUB surowego html (legacy)
//   POST   ?action=create               — nowy wpis (klon najnowszego jako szkielet)
//   DELETE ?action=delete&slug=X        — usuniecie wpisu + karty + sitemap
//   POST   ?action=upload               — upload obrazka (base64) do repo
//
// Zapisy wielu plikow ida JEDNYM commitem (Git Data API) => jeden deploy Vercela.

import crypto from 'node:crypto';
import { SITE_URL, BLOG, UPLOAD } from './_config.js';

const GITHUB_API = 'https://api.github.com';

const repo = () => process.env.GITHUB_REPO;
const branch = () => process.env.GITHUB_BRANCH || 'main';

function verifyAuth(req) {
  const auth = req.headers['x-cms-token'];
  if (!auth || !process.env.CMS_PASSWORD) return false;
  const expected = crypto.createHmac('sha256', process.env.CMS_PASSWORD).update('df-cms-session-v1').digest('hex');
  return Buffer.from(auth, 'base64').toString() === `cms:${expected}`;
}

async function gh(path, options = {}) {
  const res = await fetch(`${GITHUB_API}${path}`, {
    ...options,
    headers: {
      'Authorization': `Bearer ${process.env.GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json',
      ...(options.headers || {})
    }
  });
  return res;
}

async function readFile(path, ref) {
  const res = await gh(`/repos/${repo()}/contents/${encodeURIComponent(path)}?ref=${ref || branch()}`);
  if (!res.ok) return null;
  const data = await res.json();
  return { content: Buffer.from(data.content, 'base64').toString('utf-8'), sha: data.sha };
}

// Atomowy commit wielu plikow. files: [{path, content}|{path, contentBase64}|{path, delete:true}]
async function commitFiles(files, message) {
  const refRes = await gh(`/repos/${repo()}/git/ref/heads/${branch()}`);
  if (!refRes.ok) throw new Error('Nie mozna odczytac galezi ' + branch());
  const baseSha = (await refRes.json()).object.sha;

  const baseCommitRes = await gh(`/repos/${repo()}/git/commits/${baseSha}`);
  const baseTree = (await baseCommitRes.json()).tree.sha;

  const tree = [];
  for (const f of files) {
    if (f.delete) {
      tree.push({ path: f.path, mode: '100644', type: 'blob', sha: null });
    } else if (f.contentBase64) {
      const blobRes = await gh(`/repos/${repo()}/git/blobs`, {
        method: 'POST',
        body: JSON.stringify({ content: f.contentBase64, encoding: 'base64' })
      });
      if (!blobRes.ok) throw new Error('Blad tworzenia blobu: ' + f.path);
      tree.push({ path: f.path, mode: '100644', type: 'blob', sha: (await blobRes.json()).sha });
    } else {
      tree.push({ path: f.path, mode: '100644', type: 'blob', content: f.content });
    }
  }

  const treeRes = await gh(`/repos/${repo()}/git/trees`, {
    method: 'POST',
    body: JSON.stringify({ base_tree: baseTree, tree })
  });
  if (!treeRes.ok) throw new Error('Blad tworzenia drzewa: ' + (await treeRes.text()).slice(0, 200));
  const treeSha = (await treeRes.json()).sha;

  const commitRes = await gh(`/repos/${repo()}/git/commits`, {
    method: 'POST',
    body: JSON.stringify({ message, tree: treeSha, parents: [baseSha] })
  });
  if (!commitRes.ok) throw new Error('Blad tworzenia commita');
  const commitSha = (await commitRes.json()).sha;

  const updateRes = await gh(`/repos/${repo()}/git/refs/heads/${branch()}`, {
    method: 'PATCH',
    body: JSON.stringify({ sha: commitSha, force: false })
  });
  if (!updateRes.ok) throw new Error('Konflikt zapisu (ktos wlasnie commitowal) — sprobuj ponownie');
  return commitSha;
}

// ─── PARSOWANIE WPISU (aktualna struktura; fallback na starsza) ───

function esc(s) { return String(s).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }
function escAttr(s) { return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
function stripTags(s) {
  return String(s).replace(/<[^>]*>/g, '').replace(/&nbsp;/g, ' ')
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#0?39;/g, "'").replace(/&amp;/g, '&')
    .trim();
}
// Escapuje "$" w tekstach wstawianych jako replacement do String.replace
// (inaczej "$&", "$1" itp. w tresci artykulu psulyby zapis).
function R(s) { return String(s).replace(/\$/g, '$$$$'); }

function extractPost(html, slug) {
  const get = (re) => (html.match(re) || [])[1] || '';
  const title = stripTags(get(/<title>([\s\S]*?)<\/title>/).replace(/\s*[-–]\s*(DailyFruits\s*)?Blog\s*$/i, ''));
  const description = get(/<meta name="description" content="([^"]*)"/);
  const h1 = get(/<section id="main" class="page-hero">[\s\S]*?<h1>([\s\S]*?)<\/h1>/) || get(/<h1[^>]*>([\s\S]*?)<\/h1>/);
  const dateDisplay = get(/<span class="article-date">([^<]*)<\/span>/) || get(/<time[^>]*>([^<]*)<\/time>/);
  const category = get(/<span class="article-tag"[^>]*>([^<]*)<\/span>/);
  const heroImage = get(/<div class="container" style="max-width:880px[^"]*">\s*<img src="([^"]*)"/);
  const ogImage = get(/<meta property="og:image" content="([^"]*)"/);

  let body = '';
  let structure = 'none';
  let m = html.match(/<div class="article-meta">[\s\S]*?<\/div>([\s\S]*?)<a href="blog" class="article-back">/);
  if (m) { body = m[1].trim(); structure = 'current'; }
  else {
    m = html.match(/<div class="article-body">([\s\S]*?)<\/div>\s*<\/article>/);
    if (m) { body = m[1].trim(); structure = 'legacy'; }
  }
  return { slug, title, h1, description, dateDisplay, category, heroImage, ogImage, body, structure };
}

// Wstrzykuje pola do istniejacego HTML wpisu. Zwraca {html, warnings[]}.
function splicePost(html, f) {
  const warnings = [];
  const rep = (re, replacement, label) => {
    if (re.test(html)) { html = html.replace(re, replacement); }
    else warnings.push('Nie znaleziono: ' + label);
  };

  const fullTitle = `${stripTags(f.title)} - Blog`;
  rep(/<title>[\s\S]*?<\/title>/, `<title>${R(escAttr(fullTitle))}</title>`, 'title');
  rep(/(<meta name="description" content=")[^"]*(")/, `$1${R(escAttr(f.description || ''))}$2`, 'meta description');
  rep(/(<meta property="og:title" content=")[^"]*(")/, `$1${R(escAttr(fullTitle))}$2`, 'og:title');
  rep(/(<meta property="og:description" content=")[^"]*(")/, `$1${R(escAttr(f.description || ''))}$2`, 'og:description');
  if (f.slug) rep(/(<meta property="og:url" content=")[^"]*(")/, `$1${SITE_URL}/${BLOG.postPrefix}${f.slug}$2`, 'og:url');
  if (f.heroImage) {
    const abs = /^https?:/.test(f.heroImage) ? f.heroImage : `${SITE_URL}/${f.heroImage}`;
    rep(/(<meta property="og:image" content=")[^"]*(")/, `$1${R(escAttr(abs))}$2`, 'og:image');
    html = html.replace(/(<meta name="twitter:image" content=")[^"]*(")/, `$1${R(escAttr(abs))}$2`);
  }
  html = html.replace(/(<meta name="twitter:title" content=")[^"]*(")/, `$1${R(escAttr(fullTitle))}$2`);
  html = html.replace(/(<meta name="twitter:description" content=")[^"]*(")/, `$1${R(escAttr(f.description || ''))}$2`);

  rep(/(<section id="main" class="page-hero">[\s\S]*?<h1>)[\s\S]*?(<\/h1>)/, `$1${R(f.title)}$2`, 'h1');
  rep(/(<span class="article-date">)[^<]*(<\/span>)/, `$1${R(f.dateDisplay)}$2`, 'data (article-date)');
  rep(/(<span class="article-tag"[^>]*>)[^<]*(<\/span>)/, `$1${R(escAttr(f.category))}$2`, 'kategoria (article-tag)');

  if (f.heroImage && !/^https?:/.test(f.heroImage)) {
    rep(/(<div class="container" style="max-width:880px[^"]*">\s*<img src=")[^"]*(" alt=")[^"]*(")/,
      `$1${R(escAttr(f.heroImage))}$2${R(escAttr(stripTags(f.title)))}$3`, 'obrazek hero');
  }

  if (typeof f.body === 'string') {
    const cur = /(<div class="article-meta">[\s\S]*?<\/div>)[\s\S]*?(<a href="blog" class="article-back">)/;
    const legacy = /(<div class="article-body">)[\s\S]*?(<\/div>\s*<\/article>)/;
    if (cur.test(html)) html = html.replace(cur, `$1\n\n${R(f.body)}\n\n            $2`);
    else if (legacy.test(html)) html = html.replace(legacy, `$1\n${R(f.body)}\n$2`);
    else warnings.push('Nie znaleziono kontenera tresci — tresc nie zostala zapisana');
  }
  return { html, warnings };
}

// ─── BLOG.HTML: karty + filtry ───

// MARKUP: szablon karty wpisu — dostosuj przy przenoszeniu na inna strone (README-CMS)
function cardHtml(f) {
  return `            <a href="wpis-${f.slug}" class="blog-card reveal" data-category="${escAttr(f.category)}">
                <img src="${escAttr(f.heroImage || BLOG.fallbackHero)}" alt="${escAttr(stripTags(f.title))}" class="blog-card-img" loading="lazy" width="400" height="300">
                <div class="blog-card-body">
                    <span class="blog-card-date">${f.dateDisplay}</span>
                    <span class="blog-card-tag">${escAttr(f.category)}</span>
                    <h3>${f.title}</h3>
                    <p>${f.excerpt || ''}</p>
                    <span class="blog-card-link">Czytaj dalej →</span>
                </div>
            </a>`;
}

// MARKUP: selektory kart/list bloga — dostosuj przy przenoszeniu
function cardRegex(slug) {
  return new RegExp(`[ \\t]*<a href="wpis-${esc(slug)}"[^>]*class="blog-card[\\s\\S]*?<\\/a>\\n?`);
}

function upsertCard(blogHtml, f, { insert }) {
  const re = cardRegex(f.slug);
  if (re.test(blogHtml)) {
    return blogHtml.replace(re, R(cardHtml(f)) + '\n');
  }
  if (!insert) return blogHtml;
  return blogHtml.replace(/(<div class="blog-grid">\n?)/, `$1${R(cardHtml(f))}\n\n`);
}

function removeCard(blogHtml, slug) {
  blogHtml = blogHtml.replace(cardRegex(slug), '');
  blogHtml = blogHtml.replace(new RegExp(`[ \\t]*<a href="wpis-${esc(slug)}"[^>]*class="featured-card[\\s\\S]*?<\\/a>\\n?`), '');
  return blogHtml;
}

function syncFeaturedCard(blogHtml, f) {
  const re = new RegExp(`(<a href="wpis-${esc(f.slug)}"[^>]*class="featured-card[\\s\\S]*?<\\/a>)`);
  const m = blogHtml.match(re);
  if (!m) return blogHtml;
  let card = m[1];
  card = card.replace(/(<span class="featured-card-tag">)[^<]*(<\/span>)/, `$1${R(escAttr(f.category))}$2`);
  card = card.replace(/(featured-card-tag">[^<]*<\/span><span>)[^<]*(<\/span>)/, `$1${R(f.dateDisplay)}$2`);
  card = card.replace(/(<h3>)[\s\S]*?(<\/h3>)/, `$1${R(f.title)}$2`);
  card = card.replace(/(data-category=")[^"]*(")/, `$1${R(escAttr(f.category))}$2`);
  return blogHtml.replace(re, R(card));
}

function rebuildFilters(blogHtml) {
  const cats = {};
  let total = 0;
  const cardRe = /class="blog-card[^"]*" data-category="([^"]*)"/g;
  let m;
  while ((m = cardRe.exec(blogHtml)) !== null) { total++; if (m[1]) cats[m[1]] = (cats[m[1]] || 0) + 1; }
  if (!total) return blogHtml;
  const sorted = Object.entries(cats).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], 'pl'));
  const buttons = [
    `            <button class="filter-btn active" data-filter="all">Wszystkie <span class="count">${total}</span></button>`,
    ...sorted.map(([c, n]) => `            <button class="filter-btn" data-filter="${escAttr(c)}">${escAttr(c)} <span class="count">${n}</span></button>`)
  ].join('\n');
  return blogHtml.replace(/(<div class="blog-filters">\n)[\s\S]*?(\n\s*<\/div>)/, `$1${R(buttons)}$2`);
}

// ─── SITEMAP ───

function sitemapUpsert(xml, slug, isoDate) {
  const line = `  <url><loc>${SITE_URL}/${BLOG.postPrefix}${slug}</loc><lastmod>${isoDate}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>`;
  const re = new RegExp(`[ \\t]*<url><loc>${esc(SITE_URL)}/${esc(BLOG.postPrefix)}${esc(slug)}</loc>[^\\n]*\\n?`);
  if (re.test(xml)) return xml.replace(re, line + '\n');
  return xml.replace(/(<\/urlset>)/, `${line}\n$1`);
}

function sitemapRemove(xml, slug) {
  return xml.replace(new RegExp(`[ \\t]*<url><loc>${esc(SITE_URL)}/${esc(BLOG.postPrefix)}${esc(slug)}</loc>[^\\n]*\\n?`), '');
}

// ─── WALIDACJA POL ───

function validateFields(f, { forCreate } = {}) {
  const errors = [];
  if (!f.title || !stripTags(f.title)) errors.push('Tytul jest wymagany');
  if (!f.category) errors.push('Kategoria jest wymagana');
  if (!f.dateDisplay) errors.push('Data jest wymagana');
  if (forCreate) {
    if (!f.slug || !/^[a-z0-9-]{2,80}$/.test(f.slug)) errors.push('Slug: tylko male litery, cyfry i myslniki (2-80 znakow)');
  }
  if (f.heroImage && /[<>"']/.test(f.heroImage)) errors.push('Nieprawidlowa sciezka obrazka');
  return errors;
}

const todayISO = () => new Date().toISOString().slice(0, 10);

// ─── HANDLER ───

export default async function handler(req, res) {
  if (!verifyAuth(req)) return res.status(401).json({ error: 'Unauthorized' });

  const { method } = req;
  const { action, slug } = req.query;
  const safeSlug = slug && /^[a-z0-9-]{2,80}$/.test(slug) ? slug : null;

  try {
    if (method === 'GET' && action === 'list') {
      const blog = await readFile(BLOG.listPage);
      if (!blog) return res.status(500).json({ error: 'Nie mozna pobrac blog.html' });

      const posts = [];
      const re = /<a href="wpis-([a-z0-9-]+)"[^>]*class="blog-card[^"]*" data-category="([^"]*)">[\s\S]*?<img src="([^"]*)"[\s\S]*?<span class="blog-card-date">([^<]*)<\/span>[\s\S]*?<h3>([\s\S]*?)<\/h3>[\s\S]*?<p>([\s\S]*?)<\/p>/g;
      let m;
      while ((m = re.exec(blog.content)) !== null) {
        posts.push({ slug: m[1], category: m[2], image: m[3], date: m[4], title: stripTags(m[5]), excerpt: stripTags(m[6]) });
      }
      const categories = [...new Set(posts.map(p => p.category).filter(Boolean))].sort((a, b) => a.localeCompare(b, 'pl'));
      return res.status(200).json({ posts, categories });
    }

    if (method === 'GET' && action === 'get' && safeSlug) {
      const file = await readFile(`${BLOG.postPrefix}${safeSlug}.html`);
      if (!file) return res.status(404).json({ error: 'Nie znaleziono wpisu' });
      const post = extractPost(file.content, safeSlug);
      post.sha = file.sha;
      post.rawHtml = file.content;

      const blog = await readFile(BLOG.listPage);
      if (blog) {
        const cm = blog.content.match(cardRegex(safeSlug));
        if (cm) {
          post.excerpt = stripTags((cm[0].match(/<p>([\s\S]*?)<\/p>/) || [])[1] || '');
          post.cardImage = (cm[0].match(/<img src="([^"]*)"/) || [])[1] || '';
        }
      }
      return res.status(200).json({ post });
    }

    if (method === 'PUT' && action === 'update' && safeSlug) {
      const { fields, html: rawHtml, sha, commitMessage } = req.body || {};

      // Legacy: surowy HTML (stary panel / edycja zrodla)
      if (rawHtml && !fields) {
        const response = await gh(`/repos/${repo()}/contents/wpis-${safeSlug}.html`, {
          method: 'PUT',
          body: JSON.stringify({
            message: commitMessage || `CMS: update wpis-${safeSlug}.html`,
            content: Buffer.from(rawHtml).toString('base64'),
            sha, branch: branch()
          })
        });
        if (!response.ok) return res.status(response.status).json({ error: (await response.json()).message });
        return res.status(200).json({ ok: true, sha: (await response.json()).content.sha });
      }

      if (!fields) return res.status(400).json({ error: 'Brak pol (fields)' });
      fields.slug = safeSlug;
      const errors = validateFields(fields);
      if (errors.length) return res.status(400).json({ error: errors.join('; ') });

      const file = await readFile(`${BLOG.postPrefix}${safeSlug}.html`);
      if (!file) return res.status(404).json({ error: 'Nie znaleziono wpisu' });

      const { html: newHtml, warnings } = splicePost(file.content, fields);

      const files = [{ path: `${BLOG.postPrefix}${safeSlug}.html`, content: newHtml }];
      const blog = await readFile(BLOG.listPage);
      if (blog) {
        let b = upsertCard(blog.content, fields, { insert: false });
        b = syncFeaturedCard(b, fields);
        b = rebuildFilters(b);
        if (b !== blog.content) files.push({ path: BLOG.listPage, content: b });
      }
      const sitemap = await readFile('sitemap.xml');
      if (sitemap) {
        const s = sitemapUpsert(sitemap.content, safeSlug, fields.dateISO || todayISO());
        if (s !== sitemap.content) files.push({ path: 'sitemap.xml', content: s });
      }

      const commit = await commitFiles(files, `CMS: aktualizacja wpisu "${stripTags(fields.title)}"`);
      return res.status(200).json({ ok: true, commit, warnings });
    }

    if (method === 'POST' && action === 'create') {
      const { fields } = req.body || {};
      if (!fields) return res.status(400).json({ error: 'Brak pol (fields)' });
      const errors = validateFields(fields, { forCreate: true });
      if (errors.length) return res.status(400).json({ error: errors.join('; ') });

      const exists = await readFile(`${BLOG.postPrefix}${fields.slug}.html`);
      if (exists) return res.status(409).json({ error: `Wpis wpis-${fields.slug} juz istnieje` });

      // Szkielet = najnowszy istniejacy wpis (pierwsza karta w blog.html)
      const blog = await readFile(BLOG.listPage);
      if (!blog) return res.status(500).json({ error: 'Nie mozna pobrac blog.html' });
      const first = blog.content.match(/<a href="wpis-([a-z0-9-]+)"[^>]*class="blog-card/);
      if (!first) return res.status(500).json({ error: 'Brak wpisu-szkieletu w blog.html' });
      const ref = await readFile(`${BLOG.postPrefix}${first[1]}.html`);
      if (!ref) return res.status(500).json({ error: 'Nie mozna pobrac wpisu-szkieletu' });

      const { html: newHtml, warnings } = splicePost(ref.content, fields);

      let b = upsertCard(blog.content, fields, { insert: true });
      b = rebuildFilters(b);

      const files = [
        { path: `${BLOG.postPrefix}${fields.slug}.html`, content: newHtml },
        { path: BLOG.listPage, content: b }
      ];
      const sitemap = await readFile('sitemap.xml');
      if (sitemap) files.push({ path: 'sitemap.xml', content: sitemapUpsert(sitemap.content, fields.slug, fields.dateISO || todayISO()) });

      const commit = await commitFiles(files, `CMS: nowy wpis "${stripTags(fields.title)}"`);
      return res.status(200).json({ ok: true, commit, warnings, slug: fields.slug });
    }

    if (method === 'DELETE' && action === 'delete' && safeSlug) {
      const file = await readFile(`${BLOG.postPrefix}${safeSlug}.html`);
      if (!file) return res.status(404).json({ error: 'Nie znaleziono wpisu' });

      const files = [{ path: `${BLOG.postPrefix}${safeSlug}.html`, delete: true }];
      const blog = await readFile(BLOG.listPage);
      if (blog) {
        let b = removeCard(blog.content, safeSlug);
        b = rebuildFilters(b);
        files.push({ path: BLOG.listPage, content: b });
      }
      const sitemap = await readFile('sitemap.xml');
      if (sitemap) {
        const s = sitemapRemove(sitemap.content, safeSlug);
        if (s !== sitemap.content) files.push({ path: 'sitemap.xml', content: s });
      }

      const commit = await commitFiles(files, `CMS: usuniecie wpisu wpis-${safeSlug}`);
      return res.status(200).json({ ok: true, commit });
    }

    // KOSZ: lista usunietych wpisow (z historii commitow CMS)
    if (method === 'GET' && action === 'trash') {
      const cRes = await gh(`/repos/${repo()}/commits?sha=${branch()}&per_page=100`);
      if (!cRes.ok) return res.status(500).json({ error: 'Nie mozna pobrac historii' });
      const commits = await cRes.json();
      const blog = await readFile(BLOG.listPage);
      const existing = new Set();
      if (blog) {
        let em;
        const exRe = /<a href="wpis-([a-z0-9-]+)"/g;
        while ((em = exRe.exec(blog.content)) !== null) existing.add(em[1]);
      }
      const seen = new Set();
      const items = [];
      for (const c of commits) {
        const m = c.commit.message.match(/^CMS: usuniecie wpisu wpis-([a-z0-9-]+)/);
        if (m && !seen.has(m[1])) {
          seen.add(m[1]);
          if (!existing.has(m[1])) items.push({ slug: m[1], commit: c.sha, date: c.commit.author.date });
        }
      }
      return res.status(200).json({ items });
    }

    // KOSZ: przywrocenie wpisu (plik + karta + sitemap z commita sprzed usuniecia)
    if (method === 'POST' && action === 'restore') {
      const { commit } = req.body || {};
      if (!commit || !/^[0-9a-f]{7,40}$/.test(commit)) return res.status(400).json({ error: 'commit wymagany' });

      const cRes = await gh(`/repos/${repo()}/commits/${commit}`);
      if (!cRes.ok) return res.status(404).json({ error: 'Nie znaleziono commita' });
      const cData = await cRes.json();
      const m = cData.commit.message.match(/^CMS: usuniecie wpisu wpis-([a-z0-9-]+)/);
      if (!m || !cData.parents.length) return res.status(400).json({ error: 'To nie jest commit usuniecia wpisu' });
      const slug = m[1];
      const parentSha = cData.parents[0].sha;

      const exists = await readFile(`${BLOG.postPrefix}${slug}.html`);
      if (exists) return res.status(409).json({ error: `Wpis wpis-${slug} juz istnieje — nie ma czego przywracac` });

      const old = await readFile(`${BLOG.postPrefix}${slug}.html`, parentSha);
      if (!old) return res.status(404).json({ error: 'Nie znaleziono pliku wpisu w historii' });

      const fields = extractPost(old.content, slug);
      fields.slug = slug;
      const oldBlog = await readFile(BLOG.listPage, parentSha);
      if (oldBlog) {
        const cm = oldBlog.content.match(cardRegex(slug));
        if (cm) {
          fields.excerpt = stripTags((cm[0].match(/<p>([\s\S]*?)<\/p>/) || [])[1] || '');
          fields.heroImage = (cm[0].match(/<img src="([^"]*)"/) || [])[1] || fields.heroImage;
        }
      }
      fields.title = fields.h1 || fields.title;

      const files = [{ path: `${BLOG.postPrefix}${slug}.html`, content: old.content }];
      const blog = await readFile(BLOG.listPage);
      if (blog) {
        let b = upsertCard(blog.content, fields, { insert: true });
        b = rebuildFilters(b);
        files.push({ path: BLOG.listPage, content: b });
      }
      const sitemap = await readFile('sitemap.xml');
      if (sitemap) files.push({ path: 'sitemap.xml', content: sitemapUpsert(sitemap.content, slug, todayISO()) });

      const sha = await commitFiles(files, `CMS: przywrocenie wpisu wpis-${slug}`);
      return res.status(200).json({ ok: true, commit: sha, slug });
    }

    if (method === 'POST' && action === 'upload') {
      const { filename, contentBase64 } = req.body || {};
      if (!filename || !contentBase64) return res.status(400).json({ error: 'filename i contentBase64 wymagane' });
      if (contentBase64.length > UPLOAD.maxBase64Bytes) return res.status(413).json({ error: 'Plik za duzy (max ~4 MB)' });

      const map = { 'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z' };
      const clean = filename.toLowerCase()
        .replace(/[ąćęłńóśźż]/g, c => map[c])
        .replace(/[^a-z0-9.-]/g, '-').replace(/-+/g, '-');
      if (!UPLOAD.allowedExt.test(clean)) return res.status(400).json({ error: 'Dozwolone: webp, jpg, png, svg, avif, pdf' });

      const existing = await readFile(clean);
      const path = existing ? clean.replace(/(\.[a-z]+)$/, `-${Date.now().toString(36)}$1`) : clean;

      await commitFiles([{ path, contentBase64 }], `CMS: upload pliku ${path}`);
      return res.status(200).json({ ok: true, path });
    }

    return res.status(400).json({ error: 'Nieznana akcja. Dostepne: list, get, update, create, delete, upload' });
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}
