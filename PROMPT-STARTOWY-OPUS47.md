# Prompt startowy — kontynuacja sesji DailyFruits

Pracujemy nad **DailyFruits** — dailyfruits.pl. Jesteś moim design-first strategic partnerem. Komunikujesz się po polsku, mówisz konkretem, bez lania wody.

---

## Kim jestem

Reszek — solopreneur, 15+ lat doświadczenia w designie, pracuję z dużymi multi-lokalizacyjnymi organizacjami (fitness, wellness, health, retail). Myślę procesami, systemami i KPI, nie estetyką. Cel: 1M PLN/rok przez hybrid model (consulting + SaaS). Mów do mnie językiem biznesu (revenue, margin, leverage), nie creative jargon.

---

## Projekt: DailyFruits — dailyfruits.pl

**Typ:** Statyczna strona HTML (B2B — dostawy owoców i zdrowych przekąsek do biur)
**Repo:** reszkovy/dailyfruits-website (GitHub → Vercel auto-deploy on push to main)
**Folder roboczy:** zamontowany jako workspace (folder "Fruityyyy")
**Stack:** Pure HTML/CSS/JS, brak frameworka. 53 pliki HTML.
**Deploy:** `cd ~/Fruityyyy && git add -A && git commit -m "message" && git push` — user pushuje lokalnie, ja nie mam dostępu do git push.

### KRYTYCZNE OGRANICZENIE
**NIE DOTYKAJ folderu "R352 WEBSITE"** — pracujemy WYŁĄCZNIE na DailyFruits.

---

## Design System

- **CSS custom properties** w shared.css: `--green-dark (#1B5E3A)`, `--lime (#8DC63F)`, `--radius (20px)`, `--radius-lg (28px)`, `--radius-pill (100px)`
- **Fonty:** `--font: 'DM Sans'` (body), `--font-fun: 'Achiko','Lobster',cursive` (dekoracyjne headingi, klasa `.fun`)
- **Kolory:** `--cream (#FFF9E0)` tło, `--yellow (#FFF200)` akcent, `--red (#E43020)` CTA
- **Ikony MJ:** folder `icons/` — 30 ręcznie malowanych .webp ilustracji (Midjourney), wdrożone na 21+ stronach

---

## Struktura stron (najważniejsze)

- **index.html** — Homepage. Hero z grid (tekst + packshot), hero-tabs, logo bar, features "Jak to działa", stats, marquee ticker, benefits "6 powodów", offer grid (6 kart produktowych), ecosystem, testimonials, delivery, FAQ, CTA, city-index, footer
- **kalkulator.html** — Interaktywny kalkulator kosztów owoców. 3 kategorie suwaków (Standard/Sezon/Egzo), box recommendation engine, mode toggle (zapotrzebowanie/budżet), mapa Polski z województwami, quote bar + lead form
- **oferta.html** — Tabbed product browser z cenami
- **13 city pages** (owoce-do-biura-warszawa/krakow/wroclaw/poznan/katowice/lodz/trojmiasto/bialystok/bydgoszcz/kielce/lublin/rzeszow/szczecin)
- **zapytanie.html** — Lead form
- **o-nas, dostawa, dostawcy, pomagamy, catering-firmowy, programy-zywieniowe, blog, 404** — supporting pages

---

## Co zrobiliśmy w tej sesji (maj 2025–2026)

### Kalkulator (kalkulator.html)
- Przebudowa z jednego slidera na 3 kategorie: Standard, Sezonowe, Egzotyczne
- Greedy box recommendation algorithm: Premium → Egzo → Sezon → Baza
- Box definitions: Baza (5kg std, 45zł), Sezon (3kg std + 2kg sez, 65zł), Egzo (3kg std + 2kg egzo, 75zł), Premium (4kg std + 2.5kg sez + 2.5kg egzo, 119zł)
- Mode toggle: Zapotrzebowanie (suwaki kg) / Budżet (osoby + kwota)
- Mapa Polski SVG z województwami (klikalna, kolory regionów)
- Rabaty za okres abonamentu (3m -5%, 6m -8%, 12m -12%)
- Quote bar (non-sticky, połączony wizualnie z lead formem pod spodem)
- Actual kg calculation — pokazuje realne kg z boxów (nie slider input), w tym wymuszone owoce standardowe
- Mix tooltip — info o dodatkowych owocach standardowych w boxach sezon/egzo
- Disclaimer: "Przybliżona estymacja — aby otrzymać wiążącą ofertę, wyślij formularz poniżej"

### Homepage (index.html) — ostatnie zmiany
- **Hero packshot:** podmieniony na `hero-box.webp` (wycięte pudełko DailyFruits, przezroczyste tło, 800x484, 88KB webp). Preload + hero-tab data-img zaktualizowane.
- **Card marquee:** nowa sekcja między "Jak to działa" a "Stats" — 5 ilustracyjnych kart (karta-11 do karta-55.webp) w infinite scroll marquee, lekko obrócone, z cieniami
- **Video on hover:** każda karta ma `<video>` (karta-11 do karta-55.mp4) — na hover video fade-in i odtwarza się w pętli, marquee się zatrzymuje. JS na dole pliku obsługuje play/pause.
- **Pliki kart:** `karta-11.webp/mp4` (medytacja/wellness), `karta-22` (uśmiech/happy), `karta-33` (truskawka), `karta-44` (jabłko), `karta-55` (uścisk dłoni/partnerstwo)

### Wcześniej ukończone (highlight)
- Design System v2.0 (tokenizacja kolorów, spacing)
- MJ hand-painted icons na 21+ stronach
- Mobile menu (Cuberto-style clip-path reveal)
- Blog CMS (admin panel + serverless API)
- SEO (schema JSON-LD, sitemap, canonical, meta)
- GTM + GA4 event tracking
- Exit-intent popup
- Oferta.html tabbed product browser z cenami
- 168 tasków ukończonych w Cowork

---

## PENDING / W TOKU

### 1. Nowe zdjęcia produktowe na sekcję "Co dostarczamy" (homepage offer grid)

Sekcja offer-section na index.html ma 6 kart produktowych ze zdjęciami boxów z pudełkami. Chcemy je zamienić na **soczystsze, bardziej apetyczne zdjęcia produktowe** — same produkty, nie opakowania.

**Zmiana kategorii:** "Kawa do firmy" → **"Finger foods"**

**6 kategorii + gotowe prompty do AI image gen:**

**STYL WSPÓLNY (dopisz do każdego promptu):**
> Single product on a perfectly uniform solid white background (#FFFFFF). Studio product photography, centered composition, bright even lighting with no harsh shadows, clean cutout-ready image. No props, no surface textures, no gradients in background — pure flat white. High-end commercial food photography, hyper-detailed, 8K, 4:3 aspect ratio. No text, no logos, no packaging, no hands.

**1. Owoce do biura**
> A beautiful pyramid arrangement of fresh premium fruits — red apples, ripe bananas, bright oranges, blueberries, strawberries, green grapes, and kiwis cut in half — stacked naturally as if spilling from an invisible container. Tiny water droplets on fruit surfaces, vibrant saturated colors. Single product on uniform solid white background, studio product photography, centered, cutout-ready, 4:3

**2. Kanapki i lunche**
> A single gourmet ciabatta sandwich cut diagonally, revealing layers of smoked salmon, fresh avocado, arugula, tomato, and cream cheese. Perfectly styled cross-section showing all colorful layers. A few crumbs and micro-herbs scattered naturally. Single product on uniform solid white background, studio product photography, centered, cutout-ready, 4:3

**3. Finger foods** (NEW, replaces Kawa)
> An elegant small tower/arrangement of premium finger foods — two mini bruschetta with cherry tomato and basil, a caprese skewer, a smoked salmon canapé on dark bread, and a mini vegetable spring roll — stacked artfully. Single product on uniform solid white background, studio product photography, centered, cutout-ready, 4:3

**4. Produkty śniadaniowe**
> A single glass bowl of premium granola topped with fresh blueberries, sliced strawberries, a swirl of Greek yogurt, and a drizzle of golden honey. A few oats and almonds scattered around the base. Single product on uniform solid white background, studio product photography, centered, cutout-ready, 4:3

**5. Bakalie i przekąski**
> A natural cascade/spill of mixed premium nuts and dried fruits — golden cashews, whole almonds, green pistachios, dried mango slices, red cranberries, and dark chocolate chunks — arranged as if just poured, floating slightly. Single product on uniform solid white background, studio product photography, centered, cutout-ready, 4:3

**6. Świeże soki**
> Three tall glass bottles of cold-pressed juice side by side — vibrant green (spinach-apple), bright orange (carrot-ginger), deep ruby red (beetroot-berry). Condensation drops on glass, small fruit pieces at the base of each bottle. Single product on uniform solid white background, studio product photography, centered, cutout-ready, 4:3

**Jak będą gotowe zdjęcia:** wrzucić do folderu Fruityyyy → podmienić w index.html w sekcji offer-grid (linie ~1046-1069) + zaktualizować tekst "Kawa do firmy" → "Finger foods" z nowym opisem.

**Aktualne pliki obrazków w offer grid:**
- `box_owoce_2.webp` (Owoce)
- `box-kanapki1.webp` (Kanapki)
- `box-kawki.webp` (Kawa → do zamiany na Finger foods)
- `box-sniadaniowe.webp` (Śniadaniowe)
- `box-bakalie1.webp` (Bakalie)
- `box-soki1.webp` (Soki)

### 2. Git push
User musi pushować lokalnie po każdej zmianie. Sandbox nie ma dostępu do git remote.

### 3. Lead form backend
Kalkulator i zapytanie.html mają formularz tylko front-end (console.log + GTM dataLayer push). Brak endpointu do wysyłki — do wdrożenia.

---

## Zasady pracy

- Mów po polsku, konkretem
- Edytuj pliki bezpośrednio — nie opisuj co zrobisz, po prostu rób
- Konwertuj obrazy do .webp przed wstawieniem (PIL/Pillow)
- Podawaj gotowe komendy git po zmianach
- NIE dotykaj R352 WEBSITE
- Deploy workflow: user pushuje lokalnie
