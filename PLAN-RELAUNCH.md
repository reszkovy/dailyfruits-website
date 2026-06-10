# DailyFruits — Plan relaunchu (nowa strona zastępuje dailyfruits.pl)

**Cel:** uruchomić nową stronę na domenie dailyfruits.pl tak, by była **wyraźnie lepsza** od obecnej, **bez utraty ruchu organicznego**.
**Założenie:** oferta zostaje w wersji pierwszej (`oferta.html` — układ z tabami). `oferta-v2` parkujemy jako prywatne narzędzie handlowe (noindex).
**Data:** czerwiec 2026 · **Stan wyjścia:** audyt 7650/10000, 66 stron publicznych, webp wdrożone, mapa serwisu gotowa.

---

## 1. Dlaczego nowa bije live (teza relaunchu)

Z porównania `dailyfruits.pl` (WordPress 2010–2024) vs nowa:

| Wymiar | Przewaga nowej |
|---|---|
| Design i hierarchia | Skok generacyjny — czysty, nowoczesny, brandowany |
| Copy hero | Outcome-driven („owoce w kuchni, zanim zespół dotrze") vs opisowe |
| Lejek | Jawny: 9-etapowa home + 4 punkty CTA + exit-popup |
| Social proof | Logotypy liderów + 4.9/5, vs same cytaty |
| AEO / FAQ | 15+ pytań z ROI i porównaniem benefitów — gotowe pod AI-search |
| Lokalne SEO | 14 landingów miastowych z unikalnym contentem |
| Performance | webp na całym serwisie, lazy, wymiary (CLS) |
| Spójność | Stokenizowany design system, ujednolicona stopka/nawigacja |

**Wniosek:** produkt jest lepszy. Ryzyko nie leży w jakości nowej strony — leży w **bezpiecznej migracji** (żeby nie stracić pozycji Google) i w **parytecie treści** (żeby nie zgubić tego, co live ma, a my nie).

---

## 2. Stan obecny (z mapy serwisu)

- **Warstwa SEO (44 strony):** 30 wpisów blog + 14 miast. Magnes na ruch.
- **Rdzeń serwisu / lejek (22 strony):** home, oferta, kalkulator, zapytanie, kontakt, firmowe.
- **Lejek konwersji:** wszystko zbiega do `zapytanie` (najwyżej podlinkowana strona).
- **5 ścieżek wejścia:** SEO-blog, lokalny, brand/bezpośredni, HR-benefity, handlowy (prywatny).
- **Redirecty 301:** 55 już w `vercel.json` — solidna baza, wymaga audytu kompletności.

---

## FAZA 0 — Decyzje (zanim ruszymy) · ~1h

| # | Decyzja | Dlaczego krytyczna |
|---|---|---|
| 0.1 | **Logotypy klientów** (Google, Microsoft, JPMorgan, ING) — czy są zgodne z umowami? | Bez zgód = ryzyko prawne. Jeśli nie — zdjąć przed go-live, wrócić do nazwanych cytatów. |
| 0.2 | **Cross-sell kawy** (malapalarnia.pl) — zostaje w ofercie czy nie? | Live ma, nowa nie. Decyzja biznesowa. |
| 0.3 | **Strona UE / dofinansowania** (`otwarte-innowacje`) — odtwarzamy? | Wymóg formalny przy dotacjach UE — często obowiązkowy. |
| 0.4 | **Termin cutoveru** + okno (najlepiej wt.–czw. rano, nie pt./weekend) | Migracja w ciszy ruchowej, czas na monitoring. |

---

## FAZA 1 — Parytet treści i zaufania · ~4–6h

Odtworzyć to, co live ma, a nowa zgubiła — inaczej tracimy SEO i wiarygodność.

| # | Zadanie | Wpływ |
|---|---|---|
| 1.1 | **Banery zaufania na home/o-nas:** certyfikaty (Fair Trade, GlobalG.A.P.), Rzetelna Firma, (UE jeśli 0.3) | Konwersja B2B, wiarygodność |
| 1.2 | **Audyt brakujących podstron oferty** z live (`produkty-ekologiczne`, `produkty-spozywcze`, `owoce-i-warzywa-do-biura`) → odtworzyć lub 301 na `oferta` | Zachowanie rankingów tych URL |
| 1.3 | **Treść firmowa:** sprawdzić, czy NIP/REGON/adres, polityka jakości, dostawcy są kompletne | Zaufanie + zgodność |

---

## FAZA 2 — Migracja SEO-safe (najważniejsza technicznie) · ~3–4h

To decyduje, czy zachowamy ruch organiczny. **Bez tego relaunch może skasować pozycje.**

| # | Zadanie | Wpływ |
|---|---|---|
| 2.1 | **Pełny audyt 301:** wyeksportować WSZYSTKIE indeksowane URL live (Search Console / Screaming Frog), zmapować każdy stary → nowy. Dziś 55 redirectów — domknąć do 100%. | Krytyczne — utrata ruchu |
| 2.2 | **Przełączyć canonical** na nowych stronach z `dailyfruits.pl` (preview) na docelową domenę produkcyjną | Inaczej Google indeksuje starą |
| 2.3 | **Sitemap.xml** zaktualizowany do 66 publicznych URL, prywatne/robocze wyłączone | Czysty crawl |
| 2.4 | **robots.txt** finalny + wskazanie sitemap | Kontrola indeksacji |

---

## FAZA 3 — Pomiar (odłożone, ale przed pełnym launchem) · ~2h

| # | Zadanie | Wpływ |
|---|---|---|
| 3.1 | **Podmiana `GTM-XXXXXXX`** na realne ID (120 wystąpień, 71 stron) | Bez tego — zero danych |
| 3.2 | **GA4 + konwersje:** formularz `zapytanie`, kliknięcia CTA, kalkulator | Atrybucja leadów do 1M PLN |
| 3.3 | **Search Console** dla nowej domeny + przesłanie sitemap w dniu cutoveru | Monitoring migracji |

---

## FAZA 4 — Go-live (cutover) · ~1–2h + monitoring

1. Merge wszystkich zmian do `main`, deploy na Vercel
2. Przepięcie domeny `dailyfruits.pl` na nowy projekt
3. **Natychmiast:** przesłać nowy sitemap w Search Console, „Validate" redirecty
4. **Pierwsze 48h:** monitoring 404 (Vercel logs + GSC), Core Web Vitals, spadków ruchu
5. Rollback plan gotowy (stary WordPress w standby przez ~2 tygodnie)

---

## FAZA 5 — Post-launch (2–4 tyg.) · iteracja

- Monitoring pozycji organicznych vs baseline (nie powinny spaść; po 2–4 tyg. powinny rosnąć)
- Iteracja copy oferty/kart (z osobnej oceny treści — benefit-framing, „dla X osób", warianty CTA)
- Dokończenie elevation packshotów (gdy prompt dopracowany)
- Higiena repo: czyszczenie historii git (1.3 GB → ~100 MB)

---

## Definicja sukcesu (KPI relaunchu)

| Metryka | Cel |
|---|---|
| Ruch organiczny (4 tyg. po) | ≥ baseline, trend wzrostowy |
| 404 z dawnych URL | 0 (wszystko złapane przez 301) |
| Core Web Vitals | wszystkie zielone (LCP < 2,5s) |
| Lead rate (zapytania / sesje) | ≥ obecny + mierzony od dnia 1 |
| Pozycje TOP fraz (owoce do biura + miasta) | utrzymane, potem wzrost |

---

## Ryzyka i jak je zbijamy

1. **Utrata rankingów** → pełna mapa 301 + canonical + GSC monitoring (Faza 2). Największe ryzyko, największy priorytet.
2. **Luka treściowa vs live** → Faza 1 (parytet), audyt brakujących URL.
3. **Ryzyko prawne logotypów** → decyzja 0.1 przed go-live.
4. **Brak pomiaru w dniu 1** → Faza 3 wykonana PRZED cutoverem, nie po.

---

## Rekomendowana kolejność

**0 (decyzje) → 2 (SEO-safe) → 1 (parytet) → 3 (pomiar) → 4 (go-live) → 5 (post).**

Faza 2 jest technicznym sercem — to ona chroni ruch. Faza 1 i 3 mogą iść równolegle. Reszta (copy, packshoty, repo) to iteracja po launchu — nie blokuje uruchomienia.

**Pierwszy ruch:** podjąć 4 decyzje z Fazy 0 i wyeksportować pełną listę URL z Search Console pod mapę 301. To odblokowuje całą resztę.
