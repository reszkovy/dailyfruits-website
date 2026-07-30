// Konfiguracja CMS — JEDYNY plik do edycji przy przenoszeniu CMS na inna strone.
// Pliki w api/ zaczynajace sie od "_" nie sa wystawiane jako endpointy Vercela.
//
// Wymagane env vary (Vercel → Settings → Environment Variables):
//   GITHUB_TOKEN  — token z uprawnieniem contents:write do repo strony
//   GITHUB_REPO   — "owner/nazwa-repo"
//   CMS_PASSWORD  — haslo logowania do panelu /admin
// Opcjonalnie: GITHUB_BRANCH (domyslnie "main")

export const SITE_URL = 'https://dailyfruits.pl';

// ── Blog ──
export const BLOG = {
  postPrefix: 'wpis-',        // pliki wpisow: wpis-<slug>.html
  listPage: 'blog.html',      // strona z lista wpisow (karty)
  cardClass: 'blog-card',     // klasa karty wpisu na liscie
  featuredClass: 'featured-card',
  gridMarker: '<div class="blog-grid">',   // nowe karty wstawiane zaraz za tym
  filtersMarker: '<div class="blog-filters">', // pasek filtrow kategorii (przebudowywany)
  fallbackHero: 'blog-fakty-mity-hero.webp',
};

// ── Edytor tresci stron ──
export const PAGES = {
  // katalogi z podstronami (poza rootem)
  extraDirs: ['oferta'],
  // strony wykluczone z edycji niezaleznie od .vercelignore
  excludePattern: /^(admin|404|wpis-.*)\.html$/,
  // zrodlo prawdy o stronach niepublicznych
  ignoreFile: '.vercelignore',
};

// ── Produkty (opcjonalne — usun/zostaw pusty selektor, jesli strona nie ma produktow) ──
export const PRODUCTS = {
  page: 'oferta.html',
  panelRegex: /<div class="cat-panel[^"]*" data-cat="([a-z0-9-]+)"[^>]*>/g,
  cardOpenRegex: /<div class="product-card"[^>]*>/g,
  gridMarker: '<div class="products-grid">',
  fallbackImage: 'hero-box.webp',
};

// ── Menu ──
export const MENU = {
  navRegex: /<ul class="nav-links">([\s\S]*?)<\/ul>/,
  itemRegex: /<li><a href="(\/?[a-z0-9-]*)"[^>]*>([^<]*)<\/a><\/li>/g,
  mobileLinkClass: 'mn-link',
  mobileCtaClass: 'mn-cta',
  desktopCtaClass: 'btn btn-nav-cta',
  includesFile: '_includes/mobile-menu.html',
};

// ── Upload ──
export const UPLOAD = {
  allowedExt: /\.(webp|jpg|jpeg|png|svg|avif|pdf)$/,
  maxBase64Bytes: 6 * 1024 * 1024, // ~4 MB pliku
};
