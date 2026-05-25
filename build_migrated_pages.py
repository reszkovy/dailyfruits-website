"""
Migracja 10 podstron ze starej dailyfruits.pl
SEO-friendly landing pages z zachowanymi slugami URL.
"""
import os

OUT_DIR = '/sessions/zen-modest-ride/mnt/Fruityyyy'

# 10 podstron do migracji
# Slug zachowany ze starej dailyfruits.pl → 1:1 mapping (brak potrzeby 301 redirect)
CATEGORIES = [
    {
        'slug': 'dailyfruits-welcome-pack',
        'h1': 'Welcome Pack — pierwsza paczka dla nowego pracownika',
        'tagline': 'Onboarding, który zostaje w pamięci',
        'title_seo': 'Welcome Pack dla pracowników — paczka powitalna | DailyFruits',
        'meta': 'Welcome Pack DailyFruits — paczka powitalna dla nowych pracowników. Brandowane gadżety, zdrowe przekąski, materiały firmowe. Onboarding z klasą.',
        'sticker': 'Onboarding',
        'intro': '''Pierwszy dzień w pracy zapamiętuje się na lata. Welcome Pack to fizyczne wcielenie kultury Twojej firmy — paczka, którą nowy pracownik dostaje pierwszego dnia (lub kilka dni przed startem, jeśli pracuje zdalnie). W środku: brandowane gadżety, zdrowe przekąski na pierwsze tygodnie, materiały firmowe, czasem kawa lub czekoladowa niespodzianka.

To narzędzie HR-owe z mierzalnym efektem — firmy wprowadzające ustrukturyzowany onboarding mają o 50% wyższą retencję w pierwszym roku. DailyFruits komponuje Welcome Packi dla zespołów 10–500+ osób, w pełni brandowane Twoimi kolorami i logo. Składamy, pakujemy, dostarczamy do biura albo bezpośrednio do domu zdalnego pracownika.''',
        'props': [
            ('handshake', 'Pierwsze wrażenie', 'Welcome Pack to wizytówka kultury firmy — pierwszy fizyczny kontakt nowego pracownika z marką.'),
            ('lightning', 'Mierzalna retencja', 'Strukturyzowany onboarding podnosi retencję 1-roczną o 30–50%. Welcome Pack to fundament tej struktury.'),
            ('apple', 'Brand-aware kompozycja', 'Każdy element brandowany w Twoich kolorach — od opakowania po stickery na przekąskach.'),
            ('refresh', 'Skala dopasowana', 'Od jednorazowych zamówień (10 packów) po regularną subskrypcję (każdy nowy pracownik = paczka).'),
        ],
        'products': [
            ('Welcome Pack Basic', 'Branded notes, długopis, kubek, zdrowe przekąski (bakalie, batony). Idealne dla firm 50+ osób z niskim turnoverem.'),
            ('Welcome Pack Standard', 'Powyższe + branded torba, butelka, koszulka, świeże owoce, kawa do firmy (jednorazowy zestaw).'),
            ('Welcome Pack Premium', 'Pełny zestaw + tablet sleeve, headphones cover, custom slippers, ekskluzywne przekąski. Dla executive levels.'),
            ('Welcome Pack Remote', 'Kurierka do domu pracownika zdalnego — w pełni zapakowane, gotowe do otwarcia pierwszego dnia.'),
        ],
        'faq': [
            ('Kiedy dostarczacie Welcome Pack?', 'Standardowo 3-5 dni przed pierwszym dniem pracy (do domu) lub w dzień startu (do biura). Customowy harmonogram dostępny.'),
            ('Czy mogę brandować opakowania?', 'Tak — pełne brandowanie kolorów, logo, claimów. Minimum 20 sztuk dla full custom, 50 dla niestandardowych elementów.'),
            ('Co jeśli pracownik ma alergie?', 'Każdy Welcome Pack możemy dostosować — wystarczy wcześniej wskazać alergie. Robimy też wersje wegańskie i bezglutenowe.'),
        ],
    },
    {
        'slug': 'paczki-dla-pracownikow-zdalnych',
        'h1': 'Paczki dla pracowników zdalnych',
        'tagline': 'Wellbeing w home office, kultura w hybrydzie',
        'title_seo': 'Paczki dla pracowników zdalnych — wellbeing home office | DailyFruits',
        'meta': 'Paczki dla pracowników zdalnych — owoce, przekąski, kawa dostarczane prosto do domu. Utrzymaj kulturę firmową w hybrydzie. Sprawdź ofertę.',
        'sticker': 'Home office',
        'intro': '''Praca zdalna zniszczyła rytuały biurowe — kuchnia z owocami, kawa z koleżanką, spontaniczne rozmowy przy ekspresie. Pracownik zdalny dostaje wszystko samodzielnie i sam dba o nawodnienie, śniadanie, przerwy. To zła wiadomość dla zaangażowania.

Paczka dla pracownika zdalnego to nasza odpowiedź — regularna dostawa owoców, przekąsek i kawy bezpośrednio do domu pracownika. Raz w tygodniu, dwa razy w miesiącu albo na okazję (rocznica, jubileusz, święta). Pracownik dostaje fizyczny dowód że firma o nim pamięta — i jednocześnie dostaje paliwo, żeby pracować lepiej. Skala: od pojedynczych pracowników po cały zdalny zespół 500+ osób w Polsce.''',
        'props': [
            ('apple', 'Owoce do domu', 'Świeże owoce i warzywa dostarczane bezpośrednio pod drzwi pracownika — w abonamencie albo jednorazowo.'),
            ('handshake', 'Kultura w hybrydzie', 'Pracownik zdalny dostaje fizyczny dowód, że firma o nim pamięta. Mocniejsza retencja zespołów rozproszonych.'),
            ('lightning', 'Logistyka po naszej stronie', 'Dostawa kurierska w 24-48h do każdej miejscowości w Polsce. Zerowy stres dla HR.'),
            ('refresh', 'Elastyczność', 'Pracownik wyjeżdża? Zmień adres dostawy jednym mailem. Nowy pracownik? Dodajemy bez problemu.'),
        ],
        'products': [
            ('Paczka tygodniowa', 'Box z 4–6 kg owoców, 1–2 kg przekąsek, 1 produkt kawowy. Co tydzień pod drzwi.'),
            ('Paczka miesięczna', 'Mniejsza częstotliwość, większy box — owoce, bakalie, kawa, premium snacks na 4 tygodnie.'),
            ('Paczka okolicznościowa', 'Jednorazowa — rocznica zatrudnienia, jubileusz firmy, Boże Narodzenie, Wielkanoc.'),
            ('Paczka Remote Welcome', 'Pierwszy Welcome Pack dla zdalnego pracownika — pełne brand experience od dnia pierwszego.'),
        ],
        'faq': [
            ('Ile kosztuje dostawa do domu pracownika?', 'Standardowo wliczona w cenę paczki dla zamówień powyżej 5 pracowników. Pojedyncze adresy: 15-25 zł.'),
            ('Czy mogę zmienić adres dostawy pracownika?', 'Tak — wystarczy mail na 3 dni przed kolejną dostawą. Bez kar.'),
            ('Jakie miasta obsługujecie?', 'Cała Polska — każda miejscowość pod adres pocztowy. Dostawa 24-48h od pakowania.'),
        ],
    },
    {
        'slug': 'paczki-dla-dzieci-pracownikow',
        'h1': 'Paczki dla dzieci pracowników',
        'tagline': 'Mikołajki, Dzień Dziecka, urodziny',
        'title_seo': 'Paczki dla dzieci pracowników — Mikołajki, Dzień Dziecka | DailyFruits',
        'meta': 'Paczki dla dzieci pracowników — Mikołajki, Dzień Dziecka, urodzinowe niespodzianki. Zdrowe przekąski, gry, książeczki. Zamów dla firm.',
        'sticker': 'Dla dzieci',
        'intro': '''Paczka dla dziecka pracownika to benefit, który zapamiętuje cały dom. Mikołajki, Dzień Dziecka, urodziny, rozpoczęcie roku szkolnego — kilka razy w roku firma może pokazać, że dba nie tylko o pracownika, ale o jego rodzinę. To buduje lojalność na zupełnie innym poziomie niż standardowe benefity.

Komponujemy paczki dopasowane do wieku dzieci (3-6, 7-12, 13-16) i okazji. Mix zdrowych przekąsek (bakalie, suszone owoce, granola), edukacyjnych zabawek, książeczek, gier planszowych, słodyczy bez nadmiaru cukru. Każda paczka brandowana logo firmy, pakowana w eko-przyjazne materiały. Dostawa do biura na ręczne przekazanie albo bezpośrednio do domu pracownika.''',
        'props': [
            ('handshake', 'Lojalność na poziomie rodziny', 'Pracownik widzi, że firma dba o jego dziecko. To buduje retencję mocniej niż jakikolwiek bonus pieniężny.'),
            ('apple', 'Zdrowo, nie cukrowo', 'Stawiamy na bakalie, suszone owoce, granolę. Słodycze tylko jako akcent, nie jako baza paczki.'),
            ('lightning', 'Dopasowane do wieku', 'Paczki w trzech grupach wiekowych (3-6 / 7-12 / 13-16) — każda z innym zestawem zabawek i przekąsek.'),
            ('refresh', 'Sezonowo', 'Mikołajki, Dzień Dziecka, Wielkanoc, rozpoczęcie roku szkolnego — gotowy katalog na każdą okazję.'),
        ],
        'products': [
            ('Paczka Mikołajkowa', 'Klasyk grudniowy — mix słodyczy, bakalie, książeczka, mały prezent zabawkowy. Wszystko w brandowanym opakowaniu.'),
            ('Paczka na Dzień Dziecka', 'Owoce, lemoniada, lody, gra planszowa albo puzzle. Letnia kompozycja.'),
            ('Paczka Wielkanocna', 'Czekoladowy zajączek, kolorowe jajka, kolorowanka, bakalie. Wersje wegańskie dostępne.'),
            ('Paczka Back to School', 'Wrzesień — przybory szkolne, śniadaniowe granole, suszone owoce do tornistra.'),
        ],
        'faq': [
            ('Jak zbieracie informacje o dzieciach pracowników?', 'Wysyłamy do HR formularz — pracownik podaje imię, wiek, ew. alergie. RODO compliant, dane usuwane po dostawie.'),
            ('Czy mogę zamówić paczki dla zdalnego zespołu?', 'Tak — dostawa bezpośrednio do domu pracownika. Idealne na Mikołajki w hybrydzie.'),
            ('Co jeśli dziecko ma alergie?', 'Każdą paczkę dostosowujemy. Wystarczy wskazać alergie w zamówieniu — komponujemy alternatywy.'),
        ],
    },
    {
        'slug': 'pracuj-z-nami',
        'h1': 'Pracuj z nami',
        'tagline': 'Dołącz do zespołu, który buduje lepsze miejsca pracy',
        'title_seo': 'Pracuj z nami — kariera w DailyFruits | BetterWorkplace',
        'meta': 'Pracuj z nami — DailyFruits / BetterWorkplace. Otwarte stanowiska, kultura organizacji, benefity dla naszego zespołu. Wyślij CV.',
        'sticker': 'Kariera',
        'intro': '''Budujemy kulturę, którą sprzedajemy innym firmom — i staramy się żyć tym standardem na co dzień. Pracujemy w hybrydzie, dbamy o codzienne rytuały żywieniowe (oczywiście — sami zostajemy zawalani owocami), dajemy realną autonomię w pracy. Zespół DailyFruits to ~30 osób w obszarach: logistyka, obsługa klienta, sprzedaż B2B, marketing, IT, kuchnia produkcyjna.

Szukamy ludzi, którzy chcą budować, a nie tylko wykonywać. Płaska struktura, krótkie decyzje, mocne onboarding. Nasi pracownicy mówią o nas: "tu naprawdę słychać twój głos". Jeśli to rezonuje — zerknij na otwarte stanowiska albo wyślij CV mailem, nawet jeśli nie widzisz idealnego dopasowania.''',
        'props': [
            ('apple', 'Codzienny wellbeing', 'Owoce, kanapki, świeże soki na miejscu — jak u naszych klientów. Płacimy też dietetyka konsultacje 1-na-1.'),
            ('handshake', 'Krótkie decyzje', 'Płaska struktura, dostęp do decyzyjnych na każdym poziomie. Brak korpo-bullshitu, dużo działania.'),
            ('lightning', 'Realny rozwój', 'Szkolenia branżowe, konferencje, mentoring wewnętrzny. Budżet rozwojowy per pracownik raz w roku.'),
            ('refresh', 'Hybryda + elastyczność', 'Mix biuro/home — Ty decydujesz. Praca rezultatami, nie godzinami. Tylko spotkania zespołowe są punktualne.'),
        ],
        'products': [
            ('Specjalista ds. obsługi klienta', 'Codzienna obsługa zamówień, kontakt z office managerami, wsparcie sprzedaży. Warszawa lub Raszyn.'),
            ('Account Manager B2B', 'Praca z dużymi klientami enterprise, rozwój pakietów, retencja. Doświadczenie HR/Procurement mile widziane.'),
            ('Specjalista ds. marketingu', 'Content, social media, kampanie. Praca blisko produktu — owoce, wellbeing, kultura pracy.'),
            ('Kierowca-zaopatrzeniowiec', 'Dostawy do firm w wybranym mieście. Własny van firmowy, ustawione trasy, premia od KPI.'),
        ],
        'faq': [
            ('Czy mogę aplikować bez doświadczenia?', 'Tak — na stanowiska junior. Cenimy postawę bardziej niż CV. Wyślij list motywacyjny dlaczego nas wybrałeś.'),
            ('Czy oferujecie pracę zdalną w 100%?', 'Niektóre stanowiska tak (marketing, IT), inne wymagają biura (logistyka, kuchnia). W ogłoszeniu zawsze jest jasno napisane.'),
            ('Gdzie wysłać CV?', 'Mailem na kontakt@dailyfruits.pl z tematem "CV — [stanowisko]". Odpowiadamy zazwyczaj w ciągu tygodnia.'),
        ],
    },
    {
        'slug': 'baza-wiedzy',
        'h1': 'Baza wiedzy',
        'tagline': 'Wellbeing pracowniczy w faktach i liczbach',
        'title_seo': 'Baza wiedzy DailyFruits — wellbeing, dietetyka, employer branding',
        'meta': 'Baza wiedzy DailyFruits — artykuły, raporty, badania o wellbeingu pracowniczym, dietetyce w biurze, kulturze organizacji. Hub wiedzy dla HR.',
        'sticker': 'Wiedza',
        'intro': '''Sprzedajemy wellbeing oparty na liczbach, nie na intuicji. Dlatego sami inwestujemy w badania własne, monitorujemy raporty Instytutu Medycyny Pracy, śledzimy trendy globalne. Baza wiedzy DailyFruits to nasz publiczny hub — artykuły, raporty, podsumowania badań, gotowe materiały dla działów HR.

Korzystaj swobodnie. Wykorzystuj fragmenty w prezentacjach zarządu (z atrybucją). Wysyłaj wpisy zespołowi. To zasób, który ma przekształcić rozmowę o "fajnym benefit żywieniowym" w rozmowę o "infrastrukturze wellbeingu z mierzalnym ROI".''',
        'props': [
            ('lightning', 'Raporty i statystyki', 'Aktualne dane z Instytutu Medycyny Pracy, GUS, własne badania DailyFruits. Liczby dla zarządu i CFO.'),
            ('apple', 'Praktyczne poradniki', 'Jak wybrać benefit żywieniowy, jak skalować na multi-lokalizacje, jak zmierzyć efekty wellbeingu.'),
            ('handshake', 'Case studies', 'Realne historie firm — od 50-osobowych startupów po enterprise 5000+. Z liczbami, kwartalnymi efektami, wnioskami.'),
            ('refresh', 'Aktualizacje', 'Nowy artykuł co 2 tygodnie. Subskrypcja newslettera dla HR-ów — kuratorzy treści za Ciebie.'),
        ],
        'products': [
            ('Raport Żywieniowych Nawyków Pracujących Polaków 2025/2026', 'Coroczne badanie własne na próbie 2000+ pracowników biurowych. Trendy, alertny, rekomendacje.'),
            ('Wellbeing pracowników — klucz do efektywnej organizacji', 'Long-form artykuł podsumowujący 12 miesięcy badań. Z liczbami absencji, retencji, produktywności.'),
            ('Jak zaplanować Owocowy Czwartek — praktyczny plan', 'Krok po kroku — od pierwszego maila do zarządu, przez wybór dostawcy, po pomiar efektów.'),
            ('Reputacja firmy w 2026 — co naprawdę liczy się dla pracowników', 'Analiza top czynników employer brand. Wellbeing żywieniowy w top 10.'),
        ],
        'faq': [
            ('Czy mogę cytować Wasze raporty?', 'Tak, z atrybucją "Źródło: DailyFruits, [tytuł raportu], [rok]". Pełne raporty PDF dostępne na żądanie.'),
            ('Jak często publikujecie nowe materiały?', 'Nowy artykuł średnio co 2 tygodnie. Raport roczny w styczniu, raporty kwartalne dla newslettera VIP.'),
            ('Czy macie newsletter?', 'Tak — 2 razy miesięcznie. Zapisz się: kontakt@dailyfruits.pl z tematem "Newsletter HR".'),
        ],
    },
    {
        'slug': 'polityka-jakosci',
        'h1': 'Polityka jakości',
        'tagline': 'Standardy HACCP, ręczna selekcja, transport chłodzony',
        'title_seo': 'Polityka jakości DailyFruits — HACCP, certyfikaty, łańcuch dostaw',
        'meta': 'Polityka jakości DailyFruits — system HACCP, certyfikowani dostawcy, ręczna selekcja, transport chłodzony. Standardy bezpieczeństwa żywności.',
        'sticker': 'Jakość',
        'intro': '''Dostarczamy żywność do biur — to oznacza pełną odpowiedzialność za bezpieczeństwo każdej dostawy. Nasza polityka jakości obejmuje cały łańcuch: od wyboru dostawców (certyfikacja GlobalG.A.P., Fair Trade, EU Organic), przez ręczną selekcję owoców w naszej kuchni produkcyjnej, po transport chłodzony własną flotą.

Pracujemy w systemie HACCP od pierwszego dnia. Co kwartał audytujemy łańcuch dostaw. Każda partia produktów ma dokumentację pochodzenia, datę pakowania, kontrolę temperatury w transporcie. To nie marketing — to operacyjny standard.''',
        'props': [
            ('handshake', 'System HACCP', 'Wszystkie procesy zgodne z normami Hazard Analysis and Critical Control Points. Audyt zewnętrzny rocznie.'),
            ('apple', 'Certyfikowani dostawcy', 'GlobalG.A.P., Fair Trade, EU Organic, Rainforest Alliance. Pełna dokumentacja na żądanie.'),
            ('lightning', 'Ręczna selekcja', 'Każdy owoc przechodzi przez ręce naszych pracowników. Odrzucamy wszystko z najmniejszymi wadami.'),
            ('refresh', 'Transport chłodzony', 'Własna flota z termoizolacją i kontrolą temperatury. 2-6°C utrzymywane od magazynu do biura.'),
        ],
        'products': [
            ('Audyt łańcucha dostaw', 'Kwartalne wizyty u dostawców, kontrola dokumentacji, próbki kontrolne w laboratorium.'),
            ('System HACCP', 'Procedury, dokumentacja, szkolenia pracowników. Reaudyt zewnętrzny co 12 miesięcy.'),
            ('Kontrola jakości produktów', 'Każda partia: oględziny, ocena dojrzałości, sprawdzenie etykiet, foto-dokumentacja.'),
            ('Chłodzony transport', 'GPS-monitoring temperatury w transporcie. Alerty jeśli temperatura przekroczy zakres 2-6°C.'),
        ],
        'faq': [
            ('Jakie certyfikaty posiadacie?', 'HACCP (system bezpieczeństwa żywności), współpracujemy z dostawcami z EU Organic, Fair Trade, GlobalG.A.P., Rainforest Alliance.'),
            ('Czy mogę otrzymać dokumentację jakości?', 'Tak — na żądanie wysyłamy karty pochodzenia, certyfikaty dostawców, raporty audytów. Pełen pakiet dla klientów enterprise.'),
            ('Co się dzieje, gdy partia ma wady?', 'Cała partia odrzucana, alternatywa wysłana w tym samym dniu lub następnym rano. Nie ryzykujemy reputacji klienta.'),
        ],
    },
    {
        'slug': 'dla-pracodawcy',
        'h1': 'Korzyści dla pracodawcy',
        'tagline': 'Wellbeing żywieniowy z mierzalnym ROI',
        'title_seo': 'Owoce do biura — korzyści dla pracodawcy i firmy | DailyFruits',
        'meta': 'Owoce w biurze — korzyści dla pracodawcy: niższa absencja, wyższa retencja, lepsze employer branding. Dane z badań. Sprawdź mierzalne efekty.',
        'sticker': 'Dla pracodawcy',
        'intro': '''Wellbeing żywieniowy to jedna z niewielu kategorii benefitów, które dają mierzalny ROI. Badania Instytutu Medycyny Pracy pokazują, że firmy wprowadzające systematyczne dostawy zdrowej żywności obserwują: spadek absencji chorobowej o 8-15%, wzrost zaangażowania o 12-20%, lepsze wyniki rekrutacyjne (Glassdoor +15%).

To nie tylko miły gest — to konkretna decyzja biznesowa. Średni koszt programu owoców do biura to 30-60 zł per pracownik miesięcznie. Średnia oszczędność z mniejszej absencji + lepsze zaangażowanie + niższy turnover daje ROI 2-4x w skali roku. Liczby z naszych własnych klientów (2000+ firm) potwierdzają trend.''',
        'props': [
            ('lightning', 'Spadek absencji o 8–15%', 'Lepiej odżywiony zespół rzadziej choruje. Z 12 dni rocznie absencji = 1 dzień zaoszczędzony per pracownik.'),
            ('handshake', 'Wzrost retencji', 'Pracownicy z benefitami wellbeing zostają o 25% dłużej. Mniej rekrutacji = niższe koszty operacyjne.'),
            ('apple', 'Lepszy employer brand', 'Owoce w biurze są często pierwszą rzeczą, którą widzi kandydat. Pozycja na Glassdoor + 15% średnio.'),
            ('refresh', 'Wzrost produktywności', 'Stabilny poziom cukru = brak sugar crashy o 14:00. Pracownik jedzący zdrowo pracuje efektywniej w godzinach 14-17.'),
        ],
        'products': [
            ('Programy dla startupów (10-50 osób)', 'Małe biuro, ograniczony budżet, maksymalny efekt. Skrzynka tygodniowa + okazjonalne uzupełnienia.'),
            ('Programy dla SME (50-250 osób)', 'Standardowy zakres — owoce + kanapki + soki + okolicznościowe paczki. Najczęstszy wybór polskich firm.'),
            ('Programy enterprise (250-2000+ osób)', 'Pełen ekosystem benefitów, multi-lokalizacja, dedykowany opiekun, raporty miesięczne dla zarządu.'),
            ('Programy edukacyjne i wellbeingowe', 'Dostawa + warsztaty + dietetyka + raporty. Dla firm budujących pełną strategię wellbeing.'),
        ],
        'faq': [
            ('Jak zmierzyć ROI programu?', 'Pre-survey + post-survey absencji i zaangażowania, łatwo policzalne. Dostarczamy też nasze własne dashboard-y dla klientów enterprise.'),
            ('Czy program można zapisać w ZFŚS?', 'Tak — większość programów żywieniowych kwalifikuje się jako benefity pozapłacowe w ZFŚS. Wystawiamy fakturę z odpowiednim opisem.'),
            ('Ile czasu zajmuje wdrożenie?', '7-14 dni od podpisania umowy. Pierwszy zestaw zazwyczaj w drugim tygodniu, regularnie od trzeciego.'),
        ],
    },
    {
        'slug': 'dla-pracownika',
        'h1': 'Co zyskuje pracownik',
        'tagline': 'Energia, zdrowie, codzienny rytuał',
        'title_seo': 'Owoce w biurze — co zyskuje pracownik | DailyFruits',
        'meta': 'Owoce w biurze dla pracownika — więcej energii, lepsza koncentracja, zdrowsze nawyki. Sprawdź jak owoce wpływają na codzienną pracę.',
        'sticker': 'Dla pracownika',
        'intro': '''Z perspektywy pracownika: zdrowy benefit żywieniowy w biurze to różnica między dobrym a złym dniem pracy. Mniej sięgania po automaty z batonami, niższy poziom cukru, większa energia po 14:00, lepsza koncentracja podczas spotkań. To brzmi miękko, ale ma twarde fundamenty — średnia osoba sięga po niezdrową przekąskę 2-3 razy dziennie w pracy bez dostępu do zdrowych alternatyw.

Owoce w biurowej kuchni działają jak "default option". Pracownik, który ma pod ręką jabłko, banana, marchewkę, mniej chętnie idzie do automatu. To nie wymaga silnej woli — wymaga tylko, żeby zdrowe było dostępne. DailyFruits zapewnia tę dostępność: świeże, selekcjonowane, gotowe do jedzenia, codziennie.''',
        'props': [
            ('apple', 'Stabilna energia', 'Naturalne cukry z owoców uwalniają się stopniowo. Brak sugar crashu o 14:00. Stabilna koncentracja przez cały dzień.'),
            ('lightning', 'Mniej sięgania po automaty', 'Gdy zdrowe jest pod ręką, niezdrowe traci atrakcyjność. Średnio 60% pracowników w firmach z DailyFruits przestaje używać automatów z słodyczami.'),
            ('handshake', 'Codzienny rytuał', 'Owocowy Czwartek, Smoothie Monday, kanapkowy lunch. Mały rytuał, który zostaje w pamięci tygodnia.'),
            ('refresh', 'Wsparcie zdrowych nawyków', 'Łatwiej utrzymać zdrową dietę gdy lubrykant (zdrowe jedzenie pod ręką) jest poza Tobą — w biurowej kuchni.'),
        ],
        'products': [
            ('Owoce świeże', 'Selekcjonowane, dojrzałe, gotowe do jedzenia. Standardowe + sezonowe + egzotyczne miksy.'),
            ('Warzywa krojone', 'Marchewki baby, papryka w paskach, ogórki — gotowe na lunch lub między posiłkami.'),
            ('Zdrowe przekąski', 'Bakalie, suszone owoce, batoniki bez cukru, granole. Zamiast batonów z automatu.'),
            ('Tłoczone soki', 'Świeże soki i smoothie. Smoothie Monday — energetyczny start tygodnia.'),
        ],
        'faq': [
            ('Czy mogę zabierać owoce do domu?', 'To zależy od polityki firmy — większość pozwala na 1-2 owoce dziennie. Standardowo zachęcamy do dzielenia się z zespołem.'),
            ('Co jeśli mam alergie?', 'Powiedz HR-owi — informujemy o składzie każdej partii. Większość alergii uda się ominąć przez customowy skład.'),
            ('Czy macie wersje wegańskie/bezglutenowe?', 'Tak — wszystkie owoce naturalnie wegańskie, większość bakalii bezglutenowa. Granole i kanapki w wersjach BG/wegańskich.'),
        ],
    },
    {
        'slug': 'upominki-dla-pracownikow',
        'h1': 'Upominki dla pracowników',
        'tagline': 'Paczki świąteczne i okolicznościowe',
        'title_seo': 'Upominki dla pracowników — paczki świąteczne i okolicznościowe | DailyFruits',
        'meta': 'Upominki dla pracowników — paczki na Boże Narodzenie, Wielkanoc, jubileusze, urodziny. Brandowane opakowania, zdrowe składy.',
        'sticker': 'Upominki',
        'intro': '''Paczka okolicznościowa to mały gest z dużym wpływem. Boże Narodzenie, Wielkanoc, jubileusz firmy, rocznica zatrudnienia, urodziny pracownika — każda okazja to szansa, żeby zespół poczuł się zauważony. DailyFruits komponuje paczki dopasowane do okazji, w pełni brandowane, dostarczane do biura lub bezpośrednio do domu pracownika.

Najwięcej zamówień obsługujemy w listopadzie-grudniu (paczki świąteczne) i w marcu-kwietniu (Wielkanoc). Dla zespołów hybrydowych dostarczamy bezpośrednio do domów — z personalizowaną kartką, brandowanym opakowaniem, gotową do wręczenia. Plan logistyczny: zamówienie składamy minimum 4 tygodnie wcześniej, gwarantujemy dostarczenie do 23 grudnia.''',
        'props': [
            ('handshake', 'Brand experience', 'Każda paczka brandowana — opakowanie, etykiety, kartka. Pierwsze co pracownik widzi to logo Twojej firmy.'),
            ('apple', 'Zdrowe składy', 'Stawiamy na bakalie, suszone owoce, naturalne słodycze, kawę specialty. Bez bałaganu cukrowo-tłuszczowego.'),
            ('lightning', 'Skala 10–5000', 'Od małych zespołów po multi-lokalizacyjne enterprise. Logistyka po naszej stronie, Ty zatwierdzasz skład.'),
            ('refresh', 'Dostawa wszędzie', 'Biuro? Tak. Dom pracownika zdalnego? Tak. Multi-lokalizacja w 15 miastach? Też tak.'),
        ],
        'products': [
            ('Paczka Świąteczna Boże Narodzenie', 'Klasyczna — bakalie, czekolady premium, kawa, mandarynki, naturalne słodycze. Minimum 20 sztuk, deadline: 4 tygodnie.'),
            ('Paczka Wielkanocna', 'Czekoladowy zajączek, kolorowe jajka, granola z owocami suszonymi. Wersja klasyczna i wegańska.'),
            ('Paczka Jubileuszowa', 'Dla pracowników z 5, 10, 15 latami stażu. Personalizowana kartka, premium kawa, butelka oliwy, snacki.'),
            ('Paczka Urodzinowa', 'Mała, ale wysmakowana — owoce, mała kompozycja przekąsek, kartka. Subskrypcyjny model: paczka co miesiąc dla obchodzących urodziny.'),
        ],
        'faq': [
            ('Kiedy zamówić paczki świąteczne?', 'Najpóźniej do połowy listopada. Im wcześniej, tym lepiej (dla nas i dla cen). Limit 5000 paczek na sezon.'),
            ('Czy mogę dostosować zawartość?', 'Tak — od 50 sztuk pełna customyzacja składu. Poniżej tej liczby gotowe paczki z opcjami brandowania.'),
            ('Czy dostarczacie do domów pracowników?', 'Tak — paczkomat, kurier, czy własna logistyka. Pojedyncze adresy lub multi-shipment do 500+ pracowników jednocześnie.'),
        ],
    },
    {
        'slug': 'faq',
        'h1': 'Najczęstsze pytania',
        'tagline': 'Wszystko, co warto wiedzieć przed rozpoczęciem',
        'title_seo': 'FAQ — najczęstsze pytania o DailyFruits | Owoce do biura',
        'meta': 'FAQ DailyFruits — odpowiedzi na najczęstsze pytania o dostawy owoców do biura, abonament, fakturowanie, logistykę, reklamacje.',
        'sticker': 'FAQ',
        'intro': '''Zebrane w jednym miejscu odpowiedzi na pytania, które najczęściej zadają nowi klienci. Jeśli czegoś tu nie znajdziesz — napisz do nas na kontakt@dailyfruits.pl albo zadzwoń: 22 868 04 99. Zawsze odpowiadamy w ciągu 24 godzin.

Podzieliliśmy pytania na cztery obszary: ogólne (jak działa współpraca), techniczne (logistyka, dostawa), finansowe (płatności, abonament), praktyczne (reklamacje, zmiany, RODO). Jeśli zaczynasz dopiero rozmowę z nami — przeczytaj sekcję "Ogólne". Jeśli już jesteś klientem — szukaj w pozostałych.''',
        'props': [
            ('handshake', 'Ogólne — jak zaczynamy współpracę', 'Wypełnienie formularza zapytania, oferta dopasowana, pierwsza dostawa próbna. 7-14 dni od decyzji do startu.'),
            ('lightning', 'Logistyka — kiedy i jak dostarczamy', 'Pon-pt rano (7:00-10:00), własna flota z chłodzeniem, harmonogram dostosowany do Twojego biura.'),
            ('apple', 'Finanse — fakturowanie i płatności', 'Faktura VAT 14 dni, możliwość ZFŚS, brak ukrytych kosztów. Pełna transparentność cen przed startem.'),
            ('refresh', 'Praktyczne — zmiany i reklamacje', '24h na zgłoszenie reklamacji, zmiany w abonamencie jednym mailem, zerwanie bez kar.'),
        ],
        'products': [
            ('Czy mogę przetestować zanim podpiszę umowę?', 'Tak — pierwsza dostawa próbna jest bezpłatna. Bez zobowiązań. Trwa tyle, żebyś podjął decyzję komfortowo.'),
            ('Jak działa abonament — czy jest stała umowa?', 'Subskrypcja, nie kontrakt. Zmieniasz lub anulujesz w dowolnym momencie, jednym mailem, bez okresu wypowiedzenia.'),
            ('Co jeśli moja firma rośnie / kurczy się?', 'Skalujemy razem z Tobą. Zmiana ilości, częstotliwości, lokalizacji — wszystko mailem na 3 dni przed kolejną dostawą.'),
            ('Czy mogę zamówić jednorazowo, bez abonamentu?', 'Tak — jednorazowe dostawy też dostępne (paczki świąteczne, eventy, jubileusze). Cennik jednorazowy widoczny w ofercie.'),
        ],
        'faq': [
            ('Jakie miasta obsługujecie?', '14 city pages dedykowanych: Warszawa, Kraków, Wrocław, Poznań, Katowice, Łódź, Trójmiasto (Gdańsk/Gdynia), Szczecin, Lublin, Rzeszów, Bydgoszcz, Białystok, Kielce, Gliwice. Dostarczamy też w całej Polsce.'),
            ('Czy macie certyfikat HACCP?', 'Tak — pełna dokumentacja HACCP, audyt zewnętrzny rocznie, kontrola każdej partii. Patrz: polityka jakości.'),
            ('Jak długo trzeba czekać na ofertę?', '24 godziny w dni robocze od wypełnienia formularza zapytania. Często szybciej.'),
        ],
    },
]


def html_for(cat):
    slug = cat['slug']
    icons_map = {
        'refresh': 'icons/icon-refresh.webp',
        'handshake': 'icons/icon-handshake.webp',
        'apple': 'icons/icon-apple.webp',
        'lightning': 'icons/icon-lightning.webp',
    }

    props_html = ''
    for icon, h, p in cat['props']:
        props_html += f'''
            <div class="value-card reveal">
                <img src="{icons_map[icon]}" alt="" loading="lazy" width="48" height="48">
                <h3>{h}</h3>
                <p>{p}</p>
            </div>'''

    products_html = ''
    for name, desc in cat['products']:
        products_html += f'''
            <div class="product-item reveal">
                <h3>{name}</h3>
                <p>{desc}</p>
            </div>'''

    faq_html = ''
    for q, a in cat['faq']:
        faq_html += f'''
            <details class="faq-item">
                <summary>{q}</summary>
                <p>{a}</p>
            </details>'''

    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cat['title_seo']}</title>
    <meta name="description" content="{cat['meta']}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://dailyfruits.pl/{slug}">
    <meta property="og:title" content="{cat['title_seo']}">
    <meta property="og:description" content="{cat['meta']}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://dailyfruits.pl/{slug}">
    <meta property="og:image" content="https://dailyfruits.pl/HORIZONTAL.webp">
    <link rel="icon" type="image/png" href="favicon_.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;900&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
    <noscript><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;900&display=swap" rel="stylesheet"></noscript>
    <link rel="stylesheet" href="shared.css?v=4">
<style>
@font-face {{ font-family: 'Achiko'; src: url('Achiko.woff2') format('woff2'), url('Achiko.ttf') format('truetype'); font-weight: 400; font-display: swap; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
:root {{
    --green-dark: #1B5E3A; --lime: #8DC63F; --lime-light: #A4C348; --lime-bg: #FFF9E0;
    --yellow: #FFF200; --yellow-bg: #FFF8D8; --red: #E43020; --coral: #F06878;
    --cream: #FFF9E0; --white: #FFFFFF; --gray: #3D5A1E; --gray-500: #555;
    --radius: 20px; --radius-lg: 28px; --radius-pill: 100px;
    --font: 'DM Sans', sans-serif; --font-fun: 'Achiko', 'Lobster', cursive;
}}
body {{ font-family: var(--font); color: var(--gray); background: var(--cream); -webkit-font-smoothing: antialiased; }}
a {{ text-decoration: none; color: inherit; }}
.container {{ max-width: 1100px; margin: 0 auto; padding: 0 32px; }}

.page-hero {{ padding: 140px 0 56px; background: var(--lime-bg); position: relative; overflow: hidden; }}
.page-hero .container {{ position: relative; z-index: 2; }}
.breadcrumb {{ font-size: 14px; color: var(--gray-500); margin-bottom: 14px; }}
.breadcrumb a {{ color: var(--lime); font-weight: 700; }}
.page-hero .sticker {{ display: inline-block; padding: 8px 18px; background: var(--lime-light); color: var(--green-dark); border-radius: var(--radius-pill); font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; transform: rotate(-2deg); margin-bottom: 18px; box-shadow: 2px 3px 0 rgba(0,0,0,0.08); }}
.page-hero h1 {{ font-weight: 900; font-size: clamp(36px, 5vw, 56px); color: var(--green-dark); line-height: 1.05; letter-spacing: -0.04em; margin-bottom: 14px; }}
.page-hero h1 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.08em; }}
.page-hero .tagline {{ font-size: 19px; color: var(--gray); max-width: 640px; line-height: 1.5; }}

.intro-section {{ padding: 64px 0; background: var(--white); }}
.intro-section .container {{ max-width: 820px; }}
.intro-section p {{ font-size: 17px; line-height: 1.75; color: var(--gray); margin-bottom: 18px; }}

.value-section {{ padding: 80px 0; }}
.value-section h2 {{ font-weight: 900; font-size: clamp(28px, 3vw, 40px); color: var(--green-dark); text-align: center; margin-bottom: 12px; letter-spacing: -0.04em; }}
.value-section h2 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.05em; }}
.value-section .sub {{ text-align: center; font-size: 16px; color: var(--gray-500); margin-bottom: 48px; }}
.value-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; }}
.value-card {{ background: var(--white); border-radius: var(--radius); padding: 32px; border: 1px solid rgba(27,94,58,0.08); transition: transform 0.3s, box-shadow 0.3s; }}
.value-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 36px rgba(27,94,58,0.1); }}
.value-card img {{ margin-bottom: 18px; }}
.value-card h3 {{ font-weight: 800; font-size: 18px; color: var(--green-dark); margin-bottom: 8px; letter-spacing: -0.02em; }}
.value-card p {{ font-size: 15px; line-height: 1.6; color: var(--gray-500); margin: 0; }}

.products-section {{ padding: 80px 0; background: var(--lime-bg); }}
.products-section h2 {{ font-weight: 900; font-size: clamp(28px, 3vw, 40px); color: var(--green-dark); text-align: center; margin-bottom: 12px; letter-spacing: -0.04em; }}
.products-section h2 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.05em; }}
.products-section .sub {{ text-align: center; font-size: 16px; color: var(--gray-500); margin-bottom: 48px; }}
.products-list {{ display: grid; gap: 14px; }}
.product-item {{ background: var(--white); border-radius: var(--radius); padding: 24px 28px; border-left: 5px solid var(--lime); }}
.product-item h3 {{ font-weight: 800; font-size: 17px; color: var(--green-dark); margin-bottom: 6px; letter-spacing: -0.02em; }}
.product-item p {{ font-size: 15px; line-height: 1.55; color: var(--gray-500); margin: 0; }}

.faq-section {{ padding: 80px 0; }}
.faq-section h2 {{ font-weight: 900; font-size: clamp(28px, 3vw, 40px); color: var(--green-dark); text-align: center; margin-bottom: 40px; letter-spacing: -0.04em; }}
.faq-section h2 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.05em; }}
.faq-item {{ background: var(--white); border-radius: var(--radius); padding: 22px 28px; margin-bottom: 14px; border: 1px solid rgba(27,94,58,0.08); }}
.faq-item summary {{ font-weight: 700; font-size: 16px; color: var(--green-dark); cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; }}
.faq-item summary::after {{ content: '+'; font-size: 24px; color: var(--lime); font-weight: 300; }}
.faq-item[open] summary::after {{ content: '−'; }}
.faq-item p {{ font-size: 15px; line-height: 1.7; color: var(--gray-500); margin-top: 14px; padding-top: 14px; border-top: 1px solid rgba(27,94,58,0.06); }}

.cta-section {{ padding: 80px 0; background: var(--white); text-align: center; }}
.cta-section h2 {{ font-weight: 900; font-size: clamp(28px, 3vw, 40px); color: var(--green-dark); margin-bottom: 14px; letter-spacing: -0.04em; }}
.cta-section h2 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.05em; }}
.cta-section p {{ font-size: 17px; color: var(--gray-500); margin-bottom: 28px; max-width: 540px; margin-left: auto; margin-right: auto; }}
.cta-row {{ display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }}

@media (max-width: 720px) {{
    .container {{ padding: 0 20px; }}
    .page-hero {{ padding: 120px 0 40px; }}
    .value-grid {{ grid-template-columns: 1fr; }}
}}
</style>
</head>
<body>

<!-- NAV -->
<header>
    <div class="nav-inner">
        <div class="logo-wrap"><a href="/"><img src="fruitttt.svg" alt="DailyFruits — owoce, kanapki, soki, przekąski i więcej do biura" class="logo-img" loading="lazy" width="64" height="64"></a><a href="https://betterworkplace.pl" target="_blank" rel="noopener noreferrer" class="logo-sub">by BetterWorkplace</a></div>
        <nav><ul class="nav-links">
            <li><a href="oferta">Oferta</a></li>
            <li><a href="dostawa">Dostawa</a></li>
            <li><a href="o-nas">O nas</a></li>
            <li><a href="blog">Blog</a></li><li><a href="kontakt">Kontakt</a></li>
        </ul></nav>
        <div class="nav-buttons">
            <span class="nav-trust">Zaufało nam ponad<br>2 000 firm w Polsce</span>
            <a href="zapytanie" class="btn btn-nav-cta">Bezpłatna wycena</a>
            <button class="mn-burger" id="mnBurger" aria-label="Menu"><i></i><i></i><i></i></button>
        </div>
    </div>
</header>

<!-- MOBILE NAV -->
<div id="mnOverlay">
    <nav class="mn-links">
        <a href="oferta" class="mn-link">Oferta</a>
        <a href="dostawa" class="mn-link">Dostawa</a>
        <a href="o-nas" class="mn-link">O nas</a>
        <a href="blog" class="mn-link">Blog</a>
        <a href="kontakt" class="mn-link">Kontakt</a>
        <a href="zapytanie" class="mn-cta">Bezpłatna wycena →</a>
    </nav>
</div>

<section class="page-hero">
    <div class="container">
        <nav class="breadcrumb" aria-label="breadcrumb"><a href="/">DailyFruits</a> › {cat['h1']}</nav>
        <div class="sticker">{cat['sticker']}</div>
        <h1>{cat['h1']}</h1>
        <p class="tagline">{cat['tagline']}</p>
    </div>
</section>

<section class="intro-section">
    <div class="container">
        {''.join('<p>' + p.strip() + '</p>' for p in cat['intro'].split(chr(10) + chr(10)))}
    </div>
</section>

<section class="value-section">
    <div class="container">
        <h2>Co to <span class="fun">daje</span></h2>
        <p class="sub">Cztery konkretne korzyści, z liczbami i argumentami biznesowymi.</p>
        <div class="value-grid">{props_html}
        </div>
    </div>
</section>

<section class="products-section">
    <div class="container">
        <h2>Co <span class="fun">oferujemy</span></h2>
        <p class="sub">Wybierz wariant albo skomponuj własny — dopasujemy.</p>
        <div class="products-list">{products_html}
        </div>
    </div>
</section>

<section class="faq-section">
    <div class="container">
        <h2>Najczęstsze <span class="fun">pytania</span></h2>{faq_html}
    </div>
</section>

<section class="cta-section">
    <div class="container">
        <h2>Bezpłatna wycena w <span class="fun">24 godziny</span></h2>
        <p>Wypełnij krótkie zapytanie, dopasujemy ofertę pod potrzeby Twojego zespołu. Bez zobowiązań, bez kruczków.</p>
        <div class="cta-row">
            <a href="zapytanie" class="btn btn-red-solid btn-arrow">Złóż zapytanie</a>
            <a href="oferta" class="btn btn-outline">Wróć do oferty →</a>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer>
    <div class="container" style="max-width:1240px;">
        <div class="footer-grid">
            <div class="footer-brand">
                <div style="display:flex;align-items:center;gap:16px;">
                    <img src="fruitttt.svg" alt="DailyFruits logo" style="height:56px;filter:brightness(10);" loading="lazy" width="56" height="56">
                    <img src="dailyfoods-logo.svg" alt="DailyFoods" style="height:56px;" loading="lazy" width="64" height="64">
                </div>
                <p>Zdrowsze jedzenie, lepsza praca – zaczynając od kuchni. Część ekosystemu BetterWorkplace.</p>
            </div>
            <div class="footer-col"><h4>Nawigacja</h4><ul><li><a href="/">Start</a></li><li><a href="oferta">Oferta</a></li><li><a href="dostawa">Dostawa</a></li><li><a href="o-nas">O nas</a></li><li><a href="blog">Blog</a></li><li><a href="kontakt">Kontakt</a></li></ul></div>
            <div class="footer-col"><h4>Dla firm</h4><ul><li><a href="dla-pracodawcy">Dla pracodawcy</a></li><li><a href="dla-pracownika">Dla pracownika</a></li><li><a href="pracuj-z-nami">Pracuj z nami</a></li><li><a href="baza-wiedzy">Baza wiedzy</a></li><li><a href="polityka-jakosci">Polityka jakości</a></li></ul></div>
            <div class="footer-col"><h4>Kontakt</h4><ul><li><a href="mailto:kontakt@dailyfruits.pl">kontakt@dailyfruits.pl</a></li><li><p>tel: <a href="tel:+48228680499">22 868 04 99</a></p></li></ul></div>
        </div>
        <div class="footer-bottom">
            <p style="margin-bottom:8px;"><a href="polityka-prywatnosci" style="color:rgba(255,255,255,0.5);text-decoration:underline;">Polityka prywatności</a> · <a href="regulamin" style="color:rgba(255,255,255,0.5);text-decoration:underline;">Regulamin</a></p>
            <p>&copy; 2026 DailyFruits by BetterWorkplace Sp. z o.o. Wszystkie prawa zastrzeżone.</p>
        </div>
    </div>
</footer>

</body>
</html>
'''


count = 0
total_size = 0
for cat in CATEGORIES:
    path = os.path.join(OUT_DIR, cat['slug'] + '.html')
    content = html_for(cat)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    total_size += len(content)
    count += 1
    print(f"  ✓ {cat['slug']}.html ({len(content)/1024:.1f} KB)")

print(f"\n✅ Utworzono {count} podstron, łącznie {total_size/1024:.1f} KB")
