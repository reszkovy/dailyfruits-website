# CMS DailyFruits — dokumentacja i przenoszenie na inne strony

Lekki CMS dla statycznych stron HTML hostowanych na Vercelu. Zero bazy danych,
zero frameworka: **treść mieszka w repo**, każdy zapis z panelu to commit przez
GitHub API, a Vercel automatycznie publikuje zmianę (~1 min). Pełna historia
zmian i rollback = `git revert`.

## Architektura

```
/admin (admin.html)      panel: Blog / Strony / Produkty / Menu (vanilla JS)
/api/auth.js             logowanie: haslo -> token (env CMS_PASSWORD)
/api/posts.js            blog: CRUD wpisow + karty na liscie + sitemap + upload
/api/content.js          strony: inwentarz tekstow/zdjec, produkty, menu, status deployu
/api/_config.js          KONFIGURACJA — jedyny plik do edycji przy przenoszeniu
```

Kluczowe mechanizmy:

- **Inwentarz offsetowy (Strony):** serwer wyciąga z HTML listę tekstów
  (title, meta, nagłówki, akapity, przyciski, alty, src obrazków) z dokładnymi
  offsetami znakowymi. Zapis podmienia wyłącznie wskazane fragmenty po
  weryfikacji `sha` pliku i zgodności starego brzmienia — struktury strony
  nie da się zepsuć z panelu. Działa na KAŻDYM w miarę poprawnym HTML-u,
  bez adaptacji.
- **Commit wielu plików naraz** (Git Data API) — np. nowy wpis = plik wpisu +
  karta na liście bloga + sitemap w JEDNYM commicie i jednym deployu.
- **Status publikacji:** panel odpytuje GitHub deployments API o stan wdrożenia
  commita i pokazuje „Publikowanie… → Opublikowano".
- **Strony niepubliczne** (wykluczone w `.vercelignore`) są niewidoczne
  i zablokowane w edytorze.

## Env vary (Vercel → Settings → Environment Variables)

| Nazwa | Co to |
|---|---|
| `GITHUB_TOKEN` | token z uprawnieniem contents:write do repo strony (zalecany fine-grained PAT ograniczony do tego repo) |
| `GITHUB_REPO` | `owner/nazwa-repo` |
| `CMS_PASSWORD` | hasło do panelu |
| `GITHUB_BRANCH` | opcjonalnie, domyślnie `main` |

Po zmianie env varów wymagany redeploy.

## Przenoszenie na inną stronę — checklist

1. Skopiuj `admin.html` + katalog `api/` do repo nowej strony (Vercel,
   deploy z GitHuba).
2. Ustaw 3 env vary (tabela wyżej) i zrób redeploy.
3. Dostosuj **`api/_config.js`**: SITE_URL, prefiks wpisów, strona listy bloga,
   katalogi podstron, strona produktów (albo wyłącz produkty), limity uploadu.
4. Dostosuj miejsca oznaczone komentarzem **`// MARKUP:`** w `api/posts.js`
   i `api/content.js` — to szablony i selektory zależne od HTML konkretnej
   strony (karta wpisu na liście, struktura wpisu, karty produktów, nawigacja).
   Zakładka **Strony** (teksty + zdjęcia) działa bez żadnej adaptacji.
5. W `admin.html` podmień branding (tytuł, kolory w `:root`, favicon)
   i ewentualnie skróć zakładki (np. bez Produktów).
6. Upewnij się, że w `vercel.json` jest `X-Robots-Tag: noindex` dla `/admin`
   i że `admin.html` NIE jest wykluczony w `.vercelignore`.

Poziomy adaptacji: **zakładki Strony + Menu ≈ 0–1 h** (uniwersalne),
**Blog ≈ 1–3 h** (szablon wpisu i karty), **Produkty ≈ 1–2 h** (selektory kart).

## Bezpieczeństwo — świadome kompromisy

- jedno wspólne hasło, token = `base64("cms:"+haslo)` (odwracalny), CORS `*`,
  brak rate-limitu. Wystarczające dla panelu jednoosobowego za hasłem;
  przy większym zespole: HMAC token + CORS same-origin + limity.
- panel tylko decyduje o TREŚCI — struktura/layout są poza jego zasięgiem
  (decyzja projektowa).

## Testy

Harness na czystych funkcjach (parsowanie/splice na realnych plikach repo)
trzymany poza repo (sesyjny scratchpad). Bramki CI repo: `scripts/validate.py`,
`node scripts/build.js --check`, htmlhint — wszystkie muszą być zielone.
