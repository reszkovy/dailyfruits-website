"""
Generator 11 dedykowanych podstron /oferta/{slug}
SEO-friendly landing pages z unikatową treścią per kategoria.
"""
import os

OUT_DIR = '/sessions/zen-modest-ride/mnt/Fruityyyy/oferta'
os.makedirs(OUT_DIR, exist_ok=True)

# Definicja 11 kategorii — slug, title H1, meta, intro, value props, produkty, FAQ
CATEGORIES = [
    {
        'slug': 'skrzynki-abonamentowe',
        'h1': 'Skrzynki abonamentowe',
        'tagline': 'Owoce do biura w abonamencie',
        'title_seo': 'Skrzynki abonamentowe — owoce do biura w subskrypcji | DailyFruits',
        'meta': 'Skrzynki z owocami w abonamencie do Twojego biura. Elastyczna częstotliwość, brak długoterminowych zobowiązań, dostawa w 24h. Sprawdź ofertę.',
        'sticker': 'Subskrypcja',
        'intro': '''Skrzynka abonamentowa to najprostszy sposób, żeby zacząć dbać o zdrowie zespołu — bez negocjowania nowej umowy co miesiąc i bez 24-miesięcznych kontraktów. Wybierasz rozmiar, częstotliwość i skład, my dostarczamy. Możesz zmienić abonament w każdej chwili, anulować jednym mailem, bez kar.

Skrzynka trafia do biura w drewnianej, eco-przyjaznej formie — od początku staje się elementem rytuału zespołu (Owocowy Czwartek to nasza klasyka). Selekcjonujemy owoce ręcznie, dobieramy mix sezonowo, dostarczamy tak, żeby każda dostawa była świeża na cały tydzień.''',
        'props': [
            ('refresh', 'Elastyczna częstotliwość', 'Co tydzień, co 2 tygodnie albo co miesiąc — wybierasz Ty.'),
            ('handshake', '0 zł kar', 'Subskrypcja, nie kontrakt. Anuluj mailem, bez okresu wypowiedzenia.'),
            ('apple', 'Świeżość gwarantowana', 'Ręczna selekcja, transport w chłodzonej flocie, dostawa do 24h od pakowania.'),
            ('lightning', 'Skala dopasowana do firmy', 'Od skrzynek na 10 osób do dziennych dostaw na 500+. Skala razem z Tobą.'),
        ],
        'products': [
            ('Skrzynka S — do 15 osób', '5 kg owoców selekcjonowanych sezonowo. Idealna dla małych zespołów.'),
            ('Skrzynka M — do 30 osób', '10 kg mixu owoców (standard + sezon). Najczęściej zamawiana wielkość.'),
            ('Skrzynka L — do 60 osób', '20 kg owoców plus 2 kg dodatków (bakalie, suszone). Dla większych biur.'),
            ('Skrzynka XL — od 60 osób', '30+ kg z customowym składem. Dla zespołów multilokalowych.'),
        ],
        'faq': [
            ('Czy mogę zmienić częstotliwość?', 'Tak, w każdej chwili. Wystarczy mail na minimum 3 dni przed kolejną dostawą.'),
            ('Co jeśli zespół rośnie?', 'Skalujemy razem z Tobą. Zwiększamy rozmiar skrzynki, dokładamy lokalizacje, dopinamy logistykę.'),
            ('Czy mogę zamówić jednorazowo?', 'Tak. Jednorazowa skrzynka też dostępna, choć abonament wychodzi taniej per dostawa.'),
        ],
    },
    {
        'slug': 'soki-i-syropy',
        'h1': 'Soki i syropy',
        'tagline': 'Tłoczone soki do biura',
        'title_seo': 'Soki tłoczone i syropy do biura | DailyFruits',
        'meta': 'Świeżo tłoczone soki, smoothie i syropy owocowe z dostawą do firm. Smoothie Monday, naturalne składniki, bez konserwantów. Zamów dla zespołu.',
        'sticker': 'Smoothie Monday',
        'intro': '''Tłoczone na zimno soki z prawdziwych owoców i warzyw — bez koncentratów, bez sztucznych aromatów, bez konserwantów. Dostarczamy w szklanych butelkach albo w wygodnych kanistrach na większe zespoły.

Smoothie Monday to nasza klasyka — poniedziałkowa dostawa świeżych soków jako energetyczny reset po weekendzie. Klasyczne kompozycje (jabłko-marchew-imbir, buraczek-jagoda, szpinak-ananas) plus mixy customizowane pod profil zespołu. Sezonowo dorzucamy syropy domowej roboty — bzowy, malinowy, owocy leśnych — do wody, kawy, herbaty.''',
        'props': [
            ('lightning', 'Tłoczone na zimno', 'Maksymalna zachowana wartość odżywcza. Bez pasteryzacji, bez konserwantów.'),
            ('apple', '100% naturalne', 'Tylko owoce i warzywa od certyfikowanych dostawców. Zero dodatków.'),
            ('refresh', 'Dostosowane do zespołu', 'Wybierasz proporcje słodkie / wytrawne, sezonowe / klasyczne — my komponujemy.'),
            ('handshake', 'Szkło lub kanister', 'Małe biura: butelki 250ml. Większe zespoły: kanistry 5L lub dystrybutory z kranikiem.'),
        ],
        'products': [
            ('Klasyk: Jabłko–marchew–imbir', 'Najczęściej zamawiany — energia i odporność w jednym.'),
            ('Power: Burak–jagoda–jabłko', 'Antyoksydanty, mocny smak, naturalna słodycz.'),
            ('Green: Szpinak–jabłko–cytryna', 'Lekki, świeży, idealny na 14:00.'),
            ('Syrop: bez czarny / malinowy / owoców leśnych', 'Sezonowo do wody, kawy, herbaty. Domowa receptura.'),
        ],
        'faq': [
            ('Jaki jest okres przydatności soku?', 'Tłoczonego na zimno: 3-4 dni w lodówce. Po HPP (pasteryzacja ciśnieniowa): do 21 dni.'),
            ('Czy mogę zamówić mix własny?', 'Tak. Komponujemy receptury pod preferencje zespołu — minimum 50 litrów na zamówienie.'),
            ('Co z opakowaniami?', 'Szkło zwrotne (kaucja 1 zł/butelka) lub PET 100% recyklowalny. Stawiamy na obieg zamknięty.'),
        ],
    },
    {
        'slug': 'warzywa-krojone',
        'h1': 'Warzywa krojone',
        'tagline': 'Świeże warzywa do biurowej kuchni',
        'title_seo': 'Warzywa krojone do biura — gotowe, świeże, na już | DailyFruits',
        'meta': 'Krojone warzywa do biura: marchewki baby, ogórki, papryka, sałatki gotowe. Higieniczne pakowanie, dostawa codziennie. Sprawdź ofertę.',
        'sticker': 'Ready-to-eat',
        'intro': '''Krojone warzywa to najszybsza zdrowa przekąska, jaką możesz dać zespołowi — minimum przygotowania, maksimum efektu. Marchewki baby, plastrowane ogórki, paski papryki, kalafior w różyczkach, gotowe sałatki w jednorazowych miseczkach.

Idealne na biurowe lunche, podgryzanie podczas spotkań, calle wideo, deadline'y. Pakowane higienicznie zgodnie z systemem HACCP, transportowane w temperaturze 2-6°C. Niska bariera wejścia dla pracowników, którzy do tej pory sięgali po batony i chipsy.''',
        'props': [
            ('lightning', 'Gotowe do jedzenia', 'Zero przygotowania. Otwierasz, wyjmujesz, jesz. Sytuacja 14:00 rozwiązana.'),
            ('handshake', 'Higiena HACCP', 'Pakowane w sterylnych warunkach, transport chłodzony, oznaczenia daty.'),
            ('apple', 'Sezonowy mix', 'Wybór dopasowany do pory roku — wiosną młode marchewki, latem ogórek-pomidor, jesienią dyniowe sticky.'),
            ('refresh', 'Indywidualne porcje', 'Mini boxy 80g pod każde biurko albo wspólne miski w kuchni — Ty wybierasz format.'),
        ],
        'products': [
            ('Marchewki baby + hummus', 'Klasyk biurowy — 100g marchewek + 30g hummusu, gotowe.'),
            ('Mix warzywny w mini boxach', 'Marchew, ogórek, papryka, kalafior — 5 warzyw, 1 porcja.'),
            ('Sałatka komponowana', 'Mix sałat + dressing osobno. 250g/porcja, 5-7 wariantów.'),
            ('Crudités na spotkania', 'Plater 30 osób — gotowe na catering wewnętrzny lub szkolenie.'),
        ],
        'faq': [
            ('Jak długo zachowują świeżość?', '2-3 dni od pakowania, w lodówce do 5 dni. Dostarczamy codziennie świeże.'),
            ('Czy są opcje wegańskie?', 'Wszystkie warzywa krojone są wegańskie. Hummusy i dressingi — w wersjach wegańskich i klasycznych.'),
            ('Czy mogę zamówić tylko marchewki?', 'Tak. Single SKU też dostępne — np. tylko mini marchewki w opakowaniach 80g.'),
        ],
    },
    {
        'slug': 'zestawy-indywidualne',
        'h1': 'Zestawy indywidualne',
        'tagline': 'Lunchbox dla każdego pracownika',
        'title_seo': 'Zestawy indywidualne do biura — lunchbox per pracownik | DailyFruits',
        'meta': 'Indywidualne zestawy żywieniowe dla każdego pracownika — lunchbox, śniadaniówka, przekąski w jednym. Personalizacja składu i dieta. Sprawdź.',
        'sticker': 'Per pracownik',
        'intro': '''Zestaw indywidualny to kompleksowy lunchbox per pracownik — śniadanie, drugie śniadanie, przekąski popołudniowe w jednej dostawie. Każdy zespół ma profil dietetyczny: vege, klasyk, fit, low-carb. Łatwo skalowalne od 20 do 500+ pracowników.

Dla firm, które chcą zastąpić chaotyczne kuchnie biurowe (każdy przynosi własne) zorganizowanym systemem — bez przerw, bez wycieczek do sklepu, z konkretnym kontrolowanym składem. Audytorzy HR doceniają, bo to jeden z najbardziej widocznych benefitów codziennych.''',
        'props': [
            ('handshake', 'Personalizacja per pracownik', 'Każdy zespół wybiera profil: klasyk / vege / fit / bezglutenowy. Zmieniacie w dowolnym momencie.'),
            ('lightning', 'Wszystko w jednym boxie', 'Śniadanie + przekąska + lunch + napój. Pracownik ma plan na cały dzień.'),
            ('apple', 'Świeża dostawa codzienna', 'Rano przed startem dnia, prosto do biura. Bez magazynowania.'),
            ('refresh', 'Skala 20–500+', 'Ten sam standard niezależnie od wielkości firmy. Multi-lokalizacja bez problemu.'),
        ],
        'products': [
            ('Zestaw Classic', 'Klasyczne lunche: kanapka, sałatka, owoc, woda. Najbezpieczniejsza opcja.'),
            ('Zestaw Vege', 'Wegetariańskie/wegańskie alternatywy. Bogactwo białka roślinnego.'),
            ('Zestaw Fit', 'Niska kaloryczność, wysoka zawartość białka. Dla zespołów aktywnych.'),
            ('Zestaw Low-carb', 'Bezglutenowy, niskowęglowodanowy. Dla zespołów z dietetycznymi ograniczeniami.'),
        ],
        'faq': [
            ('Czy mogę mieć różne profile w jednym zespole?', 'Tak. To podstawa działania zestawów indywidualnych — każdy pracownik ma swój wybór.'),
            ('Czy zmiana profilu jest płatna?', 'Nie. Pracownik może zmienić profil w dowolnym momencie, raz na tydzień.'),
            ('Jakie są minimum zamówienia?', 'Od 20 pracowników. Poniżej polecamy skrzynki abonamentowe lub kanapki w boxach.'),
        ],
    },
    {
        'slug': 'zestawy-sniadaniowe',
        'h1': 'Zestawy śniadaniowe',
        'tagline': 'Poranek z zespołem zaczyna się od kuchni',
        'title_seo': 'Zestawy śniadaniowe do biura — granola, jogurty, musli | DailyFruits',
        'meta': 'Śniadania do biura: granola, jogurty, musli, owsianki, smoothie bowls. Poranny rytuał dla zespołu. Sprawdź ofertę zestawów śniadaniowych.',
        'sticker': 'Dzień dobry',
        'intro': '''Śniadanie w biurze to najbardziej niedoceniany benefit — większość firm pomija go całkowicie, choć badania pokazują, że pracownicy jedzący śniadanie w pracy mają o 23% wyższą produktywność w pierwszych godzinach dnia. Granola, jogurty, owsianki, smoothie bowls, świeże pieczywo, dżemy domowe.

Stawiamy na lekkie składy — energetyczne, ale nie spowalniające. Dostawa rano, przed startem dnia. Wystarczy 15 minut na zjedzenie i zespół ma stabilny poziom cukru na cały blok porannych spotkań.''',
        'props': [
            ('lightning', 'Energia bez sugar crashu', 'Owsianki, granole, jogurty — wolne uwalnianie energii zamiast cukrowego peaka.'),
            ('apple', 'Świeże codziennie', 'Pieczywo, owoce, jogurty z dostawą rano. Bez magazynowania, bez przekształcania.'),
            ('handshake', 'Dla całego zespołu', 'Buffet dla 20–200 osób. Każdy sam komponuje sobie miskę.'),
            ('refresh', 'Sezonowy mix', 'Latem owocowe smoothie bowls, zimą owsianki z gorącym mlekiem.'),
        ],
        'products': [
            ('Granola DIY', 'Owsianka + jogurty greckie + 6 toppingów (orzechy, owoce, miód) — każdy komponuje swoje.'),
            ('Smoothie bowls', 'Acai, mango-marakuja, kakao-banan. Mocno owocowe, mocno antyoksydacyjne.'),
            ('Pieczywo + dodatki', 'Świeże bułki, chleb na zakwasie + dżemy domowe, masło, awokado.'),
            ('Owsianki', 'Zimowy klasyk — owsianka z bakaliami, miodem, sezonowymi owocami.'),
        ],
        'faq': [
            ('O której rano dostarczacie?', 'Standardowo 7:00–8:30, dostosowane do godziny startu pracy w Twoim biurze.'),
            ('Czy są opcje wegańskie?', 'Tak. Jogurty roślinne, mleko owsiane/migdałowe, smoothie bowls 100% roślinne.'),
            ('Można łączyć ze skrzynkami owoców?', 'Oczywiście. Śniadanie + skrzynka owoców popołudniu to klasyczny mix.'),
        ],
    },
    {
        'slug': 'programy-zywieniowe-i-edukacyjne',
        'h1': 'Programy żywieniowe i edukacyjne',
        'tagline': 'Wellbeing z mierzalnym wpływem',
        'title_seo': 'Programy żywieniowe dla firm — edukacja, dietetyka, warsztaty | DailyFruits',
        'meta': 'Programy żywieniowe i edukacyjne dla pracowników — warsztaty z dietetykiem, konsultacje, edukacja przez aplikację. Wellbeing z liczbami.',
        'sticker': 'Wellbeing',
        'intro': '''Dostawy jedzenia to dopiero pierwszy krok. Program żywieniowy to drugi — edukacja zespołu w temacie zdrowego odżywiania, indywidualne konsultacje z dietetykiem, warsztaty kulinarne, materiały edukacyjne w intranecie.

Łączymy fizyczne dostawy z wiedzą. Pracownicy nie tylko jedzą zdrowiej — rozumieją dlaczego. To buduje trwałe nawyki, a nie tylko punktowy benefit. Mierzalne efekty: spadek absencji, wyższa retencja w zespołach z programem (badania własne, 2024).''',
        'props': [
            ('handshake', 'Konsultacje z dietetykiem', 'Indywidualne sesje 1-na-1 dla pracowników. Online lub w biurze.'),
            ('lightning', 'Warsztaty kulinarne', 'Praktyczne: jak zaplanować lunch box, jak nawodnić zespół, jak czytać etykiety.'),
            ('apple', 'Materiały edukacyjne', 'Newslettery, infografiki do intranetu, plakaty do kuchni. Wszystko brandowane.'),
            ('refresh', 'Pomiar efektów', 'Pre-survey + post-survey + dashboard dla HR. Liczby zamiast wrażeń.'),
        ],
        'products': [
            ('Program Starter — 3 miesiące', '6 warsztatów + materiały edukacyjne + raport końcowy. Dla firm rozpoczynających wellbeing.'),
            ('Program Standard — 6 miesięcy', 'Powyższe + 10 indywidualnych konsultacji + monthly newsletter.'),
            ('Program Premium — 12 miesięcy', 'Pełen program + 30 konsultacji + dashboard HR + warsztaty managerskie.'),
            ('Firmowy Dzień Zdrowia', 'Eventowy format — 1 dzień intensywnej edukacji + degustacje + materiały (zobacz osobno).'),
        ],
        'faq': [
            ('Czy programy są rozliczane jak benefit pozapłacowy?', 'Tak. Programy żywieniowe wpadają w kategorię ZFŚS / benefitów pozapłacowych.'),
            ('Czy konsultacje są obowiązkowe?', 'Nie. Każdy pracownik zapisuje się dobrowolnie. Średnio 30-45% zespołu korzysta.'),
            ('Co mierzy raport końcowy?', 'Wskaźniki: poprawa nawyków, BMI, energia, satysfakcja z benefitu, ROI dla firmy.'),
        ],
    },
    {
        'slug': 'bakalie-i-owoce-suszone',
        'h1': 'Bakalie i owoce suszone',
        'tagline': 'Przekąska, która nie wymaga lodówki',
        'title_seo': 'Bakalie i suszone owoce do biura — orzechy, daktyle, mix | DailyFruits',
        'meta': 'Bakalie do biura: orzechy, daktyle, suszone mango, żurawina, kakao. Zdrowa przekąska bez lodówki. Sprawdź ofertę dla firm.',
        'sticker': 'Cały tydzień',
        'intro': '''Bakalie to najwygodniejszy benefit żywieniowy — nie wymagają lodówki, nie tracą świeżości w ciągu dnia, można je trzymać w kuchni czy na biurkach. Idealne dla biur z lekkim ruchem, hot-desków, multi-lokalizacji bez dedykowanej kuchni.

Mix orzechów (włoskie, nerkowce, migdały), suszone owoce (daktyle, żurawina, mango, ananas), pestki dyni i słonecznika, naturalne batoniki bakaliowe. Zero dodatku cukru, zero konserwantów. Pakowane w jednorazowe miarki 30-50g (snackbox) lub w większych słoikach na buffet.''',
        'props': [
            ('apple', 'Bez lodówki', 'Trwałość do 6 miesięcy. Idealne dla biur bez dedykowanej kuchni.'),
            ('lightning', 'Energy bez sugar crashu', 'Tłuszcze omega + włókna + naturalne cukry = stabilny poziom energii.'),
            ('handshake', 'Snackbox lub buffet', 'Indywidualne mini-paczki na biurka albo wspólny słój w kuchni.'),
            ('refresh', 'Customowy mix', 'Wybierasz proporcje pod profil zespołu. Możemy też brandować opakowania.'),
        ],
        'products': [
            ('Snackbox Mix Premium', 'Mix orzechów 30g/saszetka. Klasyczny — migdały, nerkowce, włoskie, brazylijskie.'),
            ('Daktyle Medjool', 'Słodka alternatywa dla batonów. Energetyczny bomba z naturalnych źródeł.'),
            ('Mix suszonych owoców', 'Żurawina, mango, ananas, morela. Dla biur z lekkim apetytem na słodkie.'),
            ('Batoniki bakaliowe', 'Domowej roboty, bez cukru. Klejone daktylami, smaki: kakao / matcha / kokos.'),
        ],
        'faq': [
            ('Czy są opcje bezglutenowe?', 'Tak. Większość bakalii naturalnie bezglutenowa, mamy też batoniki BG-certyfikowane.'),
            ('Jak długo można je przechowywać?', 'W szczelnym opakowaniu: 6-12 miesięcy. Po otwarciu: 4-6 tygodni.'),
            ('Można brandować opakowania?', 'Tak, od 200 sztuk. Logo + Twój claim na każdej saszetce 30g.'),
        ],
    },
    {
        'slug': 'przechowywanie-i-ekspozycja',
        'h1': 'Przechowywanie i ekspozycja',
        'tagline': 'Estetyka biurowej kuchni',
        'title_seo': 'Sprzęt do przechowywania i ekspozycji owoców w biurze | DailyFruits',
        'meta': 'Drewniane skrzynki, kosze, dystrybutory, lodówki do biura. Pełna infrastruktura ekspozycji żywności w kuchni firmowej. Sprawdź ofertę.',
        'sticker': 'Infrastruktura',
        'intro': '''Owoce i przekąski w plastikowej torbie na blacie kuchni — to brak wykorzystania benefitu. Estetyczna ekspozycja zwiększa konsumpcję nawet o 60%. Dlatego dostarczamy też infrastrukturę — drewniane skrzynki, kosze wiklinowe, dystrybutory soków, mini lodówki, regały serwisowe.

Nasze drewniane skrzynki z grawerowanym logo DailyFruits to już element wizualny biur wielu firm. Customowe brandowanie dostępne od 5 skrzynek — opcja dla zespołów employer brand i HR-marketingu.''',
        'props': [
            ('apple', 'Drewniane skrzynki', 'Naturalne drewno, lakierowane spożywczo, grawer + Twoje logo opcjonalnie.'),
            ('refresh', 'Wymiana / zwroty', 'Skrzynki w obiegu zamkniętym — dostawa = zwrot pustej, zero nadmiaru w biurze.'),
            ('lightning', 'Dystrybutory napojów', 'Stacjonarne dystrybutory soków, herbat, wody owocowej. Plug & play.'),
            ('handshake', 'Mini lodówki', 'Dedykowane lodówki na warzywa krojone i kanapki. Z brandingiem albo czysto.'),
        ],
        'products': [
            ('Skrzynka drewniana — standard', 'Klasyczna skrzynka 40x30 cm, grawer DailyFruits. W cenie abonamentu.'),
            ('Skrzynka brandowana', 'Twoje logo + claim. Customowa kolorystyka. Minimum 5 sztuk.'),
            ('Dystrybutor soków', 'Stojący dystrybutor 8L z chłodzeniem. Wynajem albo zakup.'),
            ('Mini lodówka biurowa', 'Brand-aware lodówki 60L z naszym oznaczeniem. Idealne na hot-desky.'),
        ],
        'faq': [
            ('Czy skrzynki są wliczone w cenę?', 'Tak — standardowe drewniane skrzynki krążą w obiegu (dostawa = zwrot). Brandowane to opcja extra.'),
            ('Czy obsługujecie dystrybutory soków?', 'Tak. Wynajem + serwis + uzupełnianie syropów. Pełna obsługa.'),
            ('Co z higieną przechowywania?', 'Wszystkie produkty z systemem HACCP. Termin przydatności i temperatury przechowywania w każdej dostawie.'),
        ],
    },
    {
        'slug': 'firmowy-dzien-zdrowia',
        'h1': 'Firmowy Dzień Zdrowia',
        'tagline': 'Eventowy format wellbeingu',
        'title_seo': 'Firmowy Dzień Zdrowia — eventy wellbeing dla pracowników | DailyFruits',
        'meta': 'Firmowy Dzień Zdrowia — 1-dniowy event w Twojej firmie: konsultacje, warsztaty, degustacje, badania, materiały edukacyjne. Sprawdź ofertę.',
        'sticker': 'Event',
        'intro': '''Firmowy Dzień Zdrowia to skoncentrowany format wellbeingu — 1 dzień w siedzibie firmy, intensywny program edukacyjny, degustacje, konsultacje, badania. Idealne na Tydzień Zdrowia, miesiąc wellbeingu albo jako punkt startowy długoterminowego programu.

Przyjeżdżamy z całym sprzętem (stanowiska degustacyjne, materiały, dietetyk, kucharz). Twoja rola: udostępnić salę i powiadomić zespół. Średnia frekwencja na evencie: 60-70% zespołu (vs 30% przy abonamencie samym).''',
        'props': [
            ('lightning', 'Pełna logistyka po naszej stronie', 'Stanowiska, materiały, dietetyk, kucharz, sprzęt — wszystko od nas.'),
            ('handshake', 'Konsultacje 1-na-1', 'Indywidualne 30-min sesje dla zainteresowanych. Do 30 sesji w dniu.'),
            ('apple', 'Degustacje', 'Smoothie bar, owoce sezonowe, zdrowe przekąski, edukacja przez smak.'),
            ('refresh', 'Materiały do przekazania', 'Plakaty, infografiki, kartki z przepisami — do zostawienia w biurze po evencie.'),
        ],
        'products': [
            ('Dzień Standard', 'Smoothie bar + 1 warsztat (1h) + materiały edukacyjne. Dla firm 50-100 osób.'),
            ('Dzień Premium', 'Powyższe + dietetyk z konsultacjami + degustacje przez cały dzień. Firmy 100-300 osób.'),
            ('Dzień Enterprise', 'Multi-stanowiskowy format dla 300+ osób. Wiele lokalizacji w jednej firmie.'),
            ('Event multi-lokalizacja', 'Synchronizowany Dzień Zdrowia w 3-10 biurach jednocześnie. Dla firm rozproszonych.'),
        ],
        'faq': [
            ('Ile to trwa?', 'Standardowo 1 dzień (8h), z możliwością rozszerzenia do 2 dni.'),
            ('Ile potrzeba miejsca?', 'Sala konferencyjna 30-50m² na stanowiska + obszar do degustacji. Mniejsze biura: kuchnia + open space.'),
            ('Czy zostawiacie materiały?', 'Tak. Po evencie zostają plakaty, infografiki, książeczki z przepisami i podsumowanie dla HR.'),
        ],
    },
    {
        'slug': 'produkty-ekologiczne',
        'h1': 'Produkty ekologiczne',
        'tagline': 'Eko-certyfikowane dostawy do biura',
        'title_seo': 'Produkty ekologiczne BIO do biura — owoce, warzywa, soki | DailyFruits',
        'meta': 'Ekologiczne BIO produkty do firm — owoce, warzywa, soki, bakalie z certyfikatami EU Organic, Fair Trade. Sprawdź ofertę dla firm odpowiedzialnych.',
        'sticker': 'EU Organic',
        'intro': '''Ekologia to nie marketing — to konkretne certyfikaty i konkretni dostawcy. Pracujemy z gospodarstwami posiadającymi certyfikaty EU Organic, GlobalG.A.P., Fair Trade, Rainforest Alliance. Każda partia produktów ma dokumentację pochodzenia i certyfikacji.

Dla firm budujących pozycję ESG to nie tylko benefit dla pracowników, ale element strategii zrównoważonego rozwoju. Dostarczamy raporty śladu węglowego dostaw, certyfikaty na żądanie i materiały do komunikacji ESG dla działu PR.''',
        'props': [
            ('handshake', 'Certyfikaty EU Organic', 'Każdy produkt z dokumentacją certyfikacji. Audytujemy łańcuch dostaw raz na kwartał.'),
            ('apple', 'Fair Trade & Rainforest', 'Etyczny łańcuch dostaw — uczciwe wynagrodzenie producentów, zero pracy dzieci.'),
            ('refresh', 'Raporty ESG', 'Roczne raporty śladu węglowego Twoich dostaw. Do wykorzystania w raportach niefinansowych.'),
            ('lightning', 'Sezonowe i lokalne', 'Priorytet dla polskich gospodarstw BIO. Mniej transportu, mniej śladu węglowego.'),
        ],
        'products': [
            ('BIO Skrzynka owoców', 'Sezonowy mix owoców EU Organic. Mocno owocowy, mocno smakowy.'),
            ('BIO Warzywa krojone', 'Marchewki, ogórki, papryki z gospodarstw certyfikowanych. Pakowane bezpiecznie.'),
            ('BIO Soki tłoczone', 'Soki z owoców i warzyw EU Organic. Pełne raporty pochodzenia.'),
            ('BIO Bakalie premium', 'Daktyle Medjool, orzechy włoskie ze Słowacji, suszone mango Fair Trade.'),
        ],
        'faq': [
            ('Ile droższe są produkty BIO?', 'Średnio 25-40% w stosunku do konwencji. Zwraca się w komunikacji ESG i jakości produktu.'),
            ('Czy macie wszystkie certyfikaty?', 'Tak. EU Organic, GlobalG.A.P., Fair Trade, Rainforest Alliance. Dokumentacja na żądanie.'),
            ('Dostajemy raport do ESG?', 'Tak — roczny raport śladu węglowego + lista certyfikacji + opis łańcucha dostaw.'),
        ],
    },
    {
        'slug': 'zestawy-batonow-i-ciastek',
        'h1': 'Zestawy batonów i ciastek',
        'tagline': 'Słodka przekąska bez wyrzutów sumienia',
        'title_seo': 'Zdrowe batony i ciastka do biura — naturalne, bez cukru | DailyFruits',
        'meta': 'Naturalne batony i ciastka do biura — bez dodatku cukru, ze zdrowych składników. Energy snack dla zespołu. Sprawdź ofertę.',
        'sticker': 'Sweet but smart',
        'intro': '''Ludzie chcą czasem czegoś słodkiego — to nie znika nawet w najzdrowszych zespołach. Pytanie tylko, co dostają: dropsy z automatu czy naturalne batony z prawdziwych składników. Wybieramy to drugie.

Nasze batony i ciastka są na bazie daktyli, orzechów, kakao, owsa — bez dodatku białego cukru, bez konserwantów, bez transtłuszczów. Klejone naturalnie, słodzone owocami. Smaki: kakao-orzech, kokos-malina, matcha-migdał, klasyka jabłko-cynamon. Lokalna mała produkcja, dostawa świeża.''',
        'props': [
            ('apple', '0% rafinowanego cukru', 'Słodycz tylko z owoców (daktyle, banany). Bez sztucznych słodzików.'),
            ('lightning', 'Energy snack na 14:00', 'Tłuszcze + włókna + naturalne cukry = stabilny zastrzyk energii.'),
            ('handshake', 'Lokalnie produkowane', 'Polski mały producent, tygodniowe partie produkcyjne. Świeżość gwarantowana.'),
            ('refresh', 'Snackbox albo platery', 'Indywidualne 40g batony albo platery 30+ ciastek na spotkania.'),
        ],
        'products': [
            ('Baton Energy', 'Daktyle + orzechy + kakao. Klasyczny boost energii. 40g/sztuka.'),
            ('Baton Power', 'Z dodatkiem białka roślinnego (groch, ryż). Dla zespołów aktywnych fizycznie.'),
            ('Ciastko bezglutenowe', 'Mąka migdałowa + daktyle + kakao. Crunchy, słodkie, bez glutenu.'),
            ('Plater na spotkania', 'Mix 30 sztuk różnych smaków. Idealne na warsztaty i szkolenia.'),
        ],
        'faq': [
            ('Jak długo zachowują świeżość?', 'Batony: 4-6 tygodni. Ciastka: 2-3 tygodnie (świeższe, bez konserwantów).'),
            ('Czy są wegańskie?', 'Większość tak. Mamy też wersje z miodem (wegetariańskie). Filtruj po preferencjach.'),
            ('Można brandować?', 'Tak, od 100 sztuk. Logo + claim na każdym opakowaniu 40g.'),
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
                <img src="../{icons_map[icon]}" alt="" loading="lazy" width="48" height="48">
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

    other_links_html = ''
    for other in CATEGORIES:
        if other['slug'] != slug:
            other_links_html += f'<a href="{other["slug"]}" class="cross-link">{other["h1"]} →</a>\n            '

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
    <link rel="canonical" href="https://dailyfruits.pl/oferta/{slug}">
    <meta property="og:title" content="{cat['title_seo']}">
    <meta property="og:description" content="{cat['meta']}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://dailyfruits.pl/oferta/{slug}">
    <meta property="og:image" content="https://dailyfruits.pl/HORIZONTAL.webp">
    <link rel="icon" type="image/png" href="../favicon_.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;900&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
    <noscript><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;900&display=swap" rel="stylesheet"></noscript>
    <link rel="stylesheet" href="../shared.css?v=4">
<style>
@font-face {{ font-family: 'Achiko'; src: url('../Achiko.woff2') format('woff2'), url('../Achiko.ttf') format('truetype'); font-weight: 400; font-display: swap; }}
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
.page-hero h1 {{ font-weight: 900; font-size: clamp(36px, 5vw, 56px); color: var(--green-dark); line-height: 1.05; letter-spacing: -0.5px; margin-bottom: 14px; }}
.page-hero h1 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.08em; }}
.page-hero .tagline {{ font-size: 19px; color: var(--gray); max-width: 640px; line-height: 1.5; }}

.intro-section {{ padding: 64px 0; background: var(--white); }}
.intro-section .container {{ max-width: 820px; }}
.intro-section p {{ font-size: 17px; line-height: 1.75; color: var(--gray); margin-bottom: 18px; }}

.value-section {{ padding: 80px 0; }}
.value-section h2 {{ font-weight: 900; font-size: clamp(28px, 3vw, 40px); color: var(--green-dark); text-align: center; margin-bottom: 12px; }}
.value-section h2 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.05em; }}
.value-section .sub {{ text-align: center; font-size: 16px; color: var(--gray-500); margin-bottom: 48px; }}
.value-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; }}
.value-card {{ background: var(--white); border-radius: var(--radius); padding: 32px; border: 1px solid rgba(27,94,58,0.08); transition: transform 0.3s, box-shadow 0.3s; }}
.value-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 36px rgba(27,94,58,0.1); }}
.value-card img {{ margin-bottom: 18px; }}
.value-card h3 {{ font-weight: 800; font-size: 18px; color: var(--green-dark); margin-bottom: 8px; }}
.value-card p {{ font-size: 15px; line-height: 1.6; color: var(--gray-500); margin: 0; }}

.products-section {{ padding: 80px 0; background: var(--lime-bg); }}
.products-section h2 {{ font-weight: 900; font-size: clamp(28px, 3vw, 40px); color: var(--green-dark); text-align: center; margin-bottom: 12px; }}
.products-section h2 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.05em; }}
.products-section .sub {{ text-align: center; font-size: 16px; color: var(--gray-500); margin-bottom: 48px; }}
.products-list {{ display: grid; gap: 14px; }}
.product-item {{ background: var(--white); border-radius: var(--radius); padding: 24px 28px; border-left: 5px solid var(--lime); }}
.product-item h3 {{ font-weight: 800; font-size: 17px; color: var(--green-dark); margin-bottom: 6px; }}
.product-item p {{ font-size: 15px; line-height: 1.55; color: var(--gray-500); margin: 0; }}

.faq-section {{ padding: 80px 0; }}
.faq-section h2 {{ font-weight: 900; font-size: clamp(28px, 3vw, 40px); color: var(--green-dark); text-align: center; margin-bottom: 40px; }}
.faq-section h2 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.05em; }}
.faq-item {{ background: var(--white); border-radius: var(--radius); padding: 22px 28px; margin-bottom: 14px; border: 1px solid rgba(27,94,58,0.08); }}
.faq-item summary {{ font-weight: 700; font-size: 16px; color: var(--green-dark); cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; }}
.faq-item summary::after {{ content: '+'; font-size: 24px; color: var(--lime); font-weight: 300; }}
.faq-item[open] summary::after {{ content: '−'; }}
.faq-item p {{ font-size: 15px; line-height: 1.7; color: var(--gray-500); margin-top: 14px; padding-top: 14px; border-top: 1px solid rgba(27,94,58,0.06); }}

.cta-section {{ padding: 80px 0; background: var(--white); text-align: center; }}
.cta-section h2 {{ font-weight: 900; font-size: clamp(28px, 3vw, 40px); color: var(--green-dark); margin-bottom: 14px; }}
.cta-section h2 .fun {{ font-family: var(--font-fun); font-weight: 400; color: var(--lime); font-size: 1.05em; }}
.cta-section p {{ font-size: 17px; color: var(--gray-500); margin-bottom: 28px; max-width: 540px; margin-left: auto; margin-right: auto; }}
.cta-row {{ display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }}

.cross-section {{ padding: 60px 0 80px; background: var(--cream); }}
.cross-section h3 {{ font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 0.8px; color: var(--gray-500); margin-bottom: 18px; }}
.cross-links {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.cross-link {{ display: inline-block; padding: 8px 16px; background: var(--white); border-radius: var(--radius-pill); font-size: 14px; font-weight: 600; color: var(--green-dark); border: 1px solid rgba(27,94,58,0.1); transition: all 0.2s; }}
.cross-link:hover {{ background: var(--lime); color: var(--white); border-color: var(--lime); }}

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
        <div class="logo-wrap"><a href="/"><img src="../fruitttt.svg" alt="DailyFruits — owoce, kanapki, soki, przekąski i więcej do biura" class="logo-img" loading="lazy" width="64" height="64"></a><a href="https://betterworkplace.pl" target="_blank" rel="noopener noreferrer" class="logo-sub">by BetterWorkplace</a></div>
        <nav><ul class="nav-links">
            <li><a href="/oferta">Oferta</a></li>
            <li><a href="/dostawa">Dostawa</a></li>
            <li><a href="/o-nas">O nas</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/kontakt">Kontakt</a></li>
        </ul></nav>
        <div class="nav-buttons">
            <span class="nav-trust">Zaufało nam ponad<br>2 000 firm w Polsce</span>
            <a href="/zapytanie" class="btn btn-nav-cta">Bezpłatna wycena</a>
            <button class="mn-burger" id="mnBurger" aria-label="Menu"><i></i><i></i><i></i></button>
        </div>
    </div>
</header>

<!-- MOBILE NAV -->
<div id="mnOverlay">
    <nav class="mn-links">
        <a href="/oferta" class="mn-link">Oferta</a>
        <a href="/dostawa" class="mn-link">Dostawa</a>
        <a href="/o-nas" class="mn-link">O nas</a>
        <a href="/blog" class="mn-link">Blog</a>
        <a href="/kontakt" class="mn-link">Kontakt</a>
        <a href="/zapytanie" class="mn-cta">Bezpłatna wycena →</a>
    </nav>
</div>

<section class="page-hero">
    <div class="container">
        <nav class="breadcrumb" aria-label="breadcrumb"><a href="/">DailyFruits</a> › <a href="/oferta">Oferta</a> › {cat['h1']}</nav>
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
        <h2>Co to <span class="fun">daje</span> Twojej firmie</h2>
        <p class="sub">Cztery rzeczy, które realnie ruszą KPI zespołu.</p>
        <div class="value-grid">{props_html}
        </div>
    </div>
</section>

<section class="products-section">
    <div class="container">
        <h2>Co dokładnie <span class="fun">dostajesz</span></h2>
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
        <h2>Wycena w <span class="fun">24 godziny</span></h2>
        <p>Bezpłatne zapytanie, dopasowana propozycja, pierwsza dostawa próbna. Bez zobowiązań.</p>
        <div class="cta-row">
            <a href="/zapytanie" class="btn btn-red-solid btn-arrow">Złóż zapytanie</a>
            <a href="/oferta" class="btn btn-outline">Wróć do oferty →</a>
        </div>
    </div>
</section>

<section class="cross-section">
    <div class="container">
        <h3>Sprawdź też inne kategorie</h3>
        <div class="cross-links">
            {other_links_html}
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer>
    <div class="container" style="max-width:1240px;">
        <div class="footer-grid">
            <div class="footer-brand">
                <div style="display:flex;align-items:center;gap:16px;">
                    <img src="../fruitttt.svg" alt="DailyFruits logo" style="height:56px;filter:brightness(10);" loading="lazy" width="56" height="56">
                    <img src="../dailyfoods-logo.svg" alt="DailyFoods" style="height:56px;" loading="lazy" width="64" height="64">
                </div>
                <p>Zdrowsze jedzenie, lepsza praca – zaczynając od kuchni. Część ekosystemu BetterWorkplace.</p>
            </div>
            <div class="footer-col"><h4>Nawigacja</h4><ul><li><a href="/">Start</a></li><li><a href="/oferta">Oferta</a></li><li><a href="/dostawa">Dostawa</a></li><li><a href="/o-nas">O nas</a></li><li><a href="/blog">Blog</a></li><li><a href="/kontakt">Kontakt</a></li></ul></div>
            <div class="footer-col"><h4>Oferta</h4><ul><li><a href="/oferta/skrzynki-abonamentowe">Skrzynki</a></li><li><a href="/oferta/soki-i-syropy">Soki</a></li><li><a href="/oferta/zestawy-sniadaniowe">Śniadania</a></li><li><a href="/oferta/bakalie-i-owoce-suszone">Bakalie</a></li></ul></div>
            <div class="footer-col"><h4>Kontakt</h4><ul><li><a href="mailto:kontakt@dailyfruits.pl">kontakt@dailyfruits.pl</a></li><li><p>tel: <a href="tel:+48228680499">22 868 04 99</a></p></li></ul></div>
        </div>
        <div class="footer-bottom">
            <p style="margin-bottom:8px;"><a href="/polityka-prywatnosci" style="color:rgba(255,255,255,0.5);text-decoration:underline;">Polityka prywatności</a> · <a href="/regulamin" style="color:rgba(255,255,255,0.5);text-decoration:underline;">Regulamin</a></p>
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
    print(f"  ✓ {path} ({len(content)/1024:.1f} KB)")

print(f"\nUtworzono {count} podstron, łącznie {total_size/1024:.1f} KB")
