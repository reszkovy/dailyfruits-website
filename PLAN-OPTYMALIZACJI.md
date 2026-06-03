# DailyFruits — Plan Optymalizacji

**Punkt wyjścia:** audyt **735 / 1000** (10 kategorii, analityka pominięta świadomie)
**Cel:** **820+ / 1000** + odblokowanie ścieżki konwersji blog → oferta → lead
**Data:** czerwiec 2026
**Branch roboczy:** `cleanup-webp-refactor` (main nietknięty — wymaga merge + push)

---

## Zasada priorytetyzacji

Kolejność = **dźwignia biznesowa ÷ koszt**. Najpierw rzeczy, które ruszają KPI (konwersja, SEO, czas ładowania) przy minimalnym nakładzie. Estetyka i refactor dla samego refactoru — na końcu.

Skala: Wpływ (1–5) · Koszt (1–5) · ⚡ = quick win (wpływ ≥ koszt, < 1h)

---

## FAZA 1 — Quick wins (1 sesja, ~2–3h) → +35 pkt

| # | Zadanie | Wpływ | Koszt | KPI |
|---|---|---|---|---|
| 1.1 ⚡ | **Katalog + kluczowe strony oferty do nawigacji na WSZYSTKICH stronach** (dziś katalog linkowany z 1/79) | 5 | 2 | Konwersja, internal linking, crawl budget |
| 1.2 ⚡ | **Spójna stopka z linkami do oferty/katalogu/miast** na wszystkich stronach | 4 | 2 | SEO internal linking, nawigacja |
| 1.3 ⚡ | **CTA „bezpłatna wycena" na końcu każdego wpisu blogowego** (30+ wpisów = martwy ruch bez ścieżki do leada) | 5 | 2 | Lead capture — bezpośrednio 1M PLN |
| 1.4 ⚡ | Audyt stron-sierot (faq, baza-wiedzy, dla-pracownika itd.) — podlinkować lub zdeindeksować | 3 | 2 | SEO |

> **Dlaczego najpierw:** masz głęboki content (30+ wpisów, kalkulator) i 14 landingów miastowych, ale ruch z nich nie ma ścieżki do konwersji. To największa dziura biznesowa w całym serwisie — nie kod, tylko brak lejka.

---

## FAZA 2 — Odchudzenie repo i wydajność (~3–4h) → +25 pkt

| # | Zadanie | Wpływ | Koszt | KPI |
|---|---|---|---|---|
| 2.1 | **`.gitignore` na ciężkie media** (`video/`, `PACK_SZO/`, `*.mp4`, duże PDF, katalogi źródłowe) | 4 | 2 | Szybkość deploy/clone |
| 2.2 | **Czyszczenie historii git** (`git filter-repo`) — repo 1.3 GB → ~100 MB | 5 | 4 | DevOps, koszt hostingu, prędkość |
| 2.3 | **Lazy-load + `preload` audyt na hero** wszystkich landingów (dziś 94% lazy — dobić do 100% poza LCP) | 3 | 2 | Core Web Vitals (LCP) |
| 2.4 | **Konwersja `karta-*.mp4` (5 plików, ~18 MB) do lżejszego kodeka / poster-first** | 3 | 3 | LCP, mobile |

> **Uwaga:** 2.2 przepisuje historię → wymaga `--force` push i skoordynowania (jeśli pracujesz solo, bezpieczne). To największy techniczny skok jakości repo.

---

## FAZA 3 — Kod i utrzymywalność (~4–6h) → +20 pkt

| # | Zadanie | Wpływ | Koszt | KPI |
|---|---|---|---|---|
| 3.1 | **Dokończenie inline → utility-klasy** na pozostałych ~79 stronach (zostało ~1160 wystąpień; index+oferta już zrobione jako pilot) | 3 | 4 | Utrzymywalność, spójność |
| 3.2 | **Wspólny header/footer jako include** (dziś duplikowane w 79 plikach → każda zmiana nawigacji = 79 edycji) | 5 | 4 | Leverage — Twój temat: 1 zmiana zamiast 79 |
| 3.3 | **Konsolidacja build-scriptów** (`build_*.py`) w jeden pipeline z szablonem | 4 | 3 | Skalowalność, AI-first workflow |

> **3.2 to Twój filtr leverage w czystej postaci:** brak komponentów nawigacji oznacza, że każda zmiana w menu to 79 ręcznych edycji. Wprowadzenie include'ów (np. prosty build-step) zamienia to w jedną edycję — dokładnie odejście od liniowego nakładu.

---

## FAZA 4 — Dostępność i SEO domknięcie (~2–3h) → +10 pkt

| # | Zadanie | Wpływ | Koszt | KPI |
|---|---|---|---|---|
| 4.1 | **Audyt kontrastu WCAG AA** (lime/yellow na białym — ryzyko) | 3 | 2 | A11y, ryzyko prawne |
| 4.2 | **Nawigacja klawiaturą + focus states** | 3 | 2 | A11y |
| 4.3 | **Canonical na pozostałych 11 stronach bez niego** (70/81 ma) | 3 | 1 | SEO |
| 4.4 | **Schema JSON-LD na stronach bez (33 brakuje)** — Organization, Product, FAQ | 4 | 3 | Rich snippets, AEO |

---

## FAZA 5 — Ostatnia faza (przed launchem / po stabilizacji)

| # | Zadanie | KPI |
|---|---|---|
| 5.1 | **Podmiana `GTM-XXXXXXX` na prawdziwe ID** (120 wystąpień, 71 stron) | Pomiar — odblokowanie wszystkich KPI |
| 5.2 | **Konfiguracja konwersji w GA4/GTM** (formularz wyceny, kliknięcia CTA) | Atrybucja leadów |
| 5.3 | **Event tracking na kalkulatorze** (świetne narzędzie, dziś niemierzone) | Optymalizacja lejka |

> Świadomie odłożone przez Ciebie na koniec. Pamiętaj: do tego momentu **wszystkie decyzje optymalizacyjne są na ślepo** — brak danych o tym, co realnie konwertuje.

---

## Mapa wpływu na wynik

| Po fazie | Wynik | Główny zysk |
|---|---|---|
| Teraz | 735 | — |
| Faza 1 | ~770 | Lejek konwersji + internal linking |
| Faza 2 | ~795 | Repo 13× lżejsze, lepszy LCP |
| Faza 3 | ~815 | Leverage: komponenty zamiast 79 kopii |
| Faza 4 | ~825 | A11y + SEO domknięte |
| Faza 5 | 850+ | Pełen pomiar |

---

## Rekomendacja sekwencji

Zacznij od **Faza 1** w całości — to jedyna faza z bezpośrednim wpływem na 1M PLN (lejek lead-gen), a koszt mały. Potem **3.2** (komponenty nav/footer) przeskocz przed resztą Fazy 2/3 — bo każda kolejna zmiana nawigacji bez tego mnoży się przez 79. Reszta sekwencyjnie.

**Najtańszy pojedynczy ruch o największym wpływie:** 1.3 — CTA wyceny pod każdym wpisem blogowym. Masz ruch, nie masz lejka.
