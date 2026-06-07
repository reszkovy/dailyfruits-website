#!/usr/bin/env python3
# Pobiera grafiki produktowe z dailyfruits.pl i przepina oferta-v2.html na lokalne pliki.
# Uruchom NA SWOIM komputerze:  python3 live-assets/pobierz-grafiki.py
import urllib.request, urllib.parse, os, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAP = {
 "https://dailyfruits.pl/app/uploads/2020/01/34_stojak_metalowy-600x953.jpg": "live-assets/34_stojak_metalowy-600x953.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/4_premium_mix_2.jpg": "live-assets/4_premium_mix_2.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/4_premium_mix_3.jpg": "live-assets/4_premium_mix_3.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/4_zestaw-premium-mix--600x456.jpg": "live-assets/4_zestaw-premium-mix--600x456.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/5_skrzynka-banan-i-owoce-sezonowe-600x434.jpg": "live-assets/5_skrzynka-banan-i-owoce-sezonowe-600x434.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/5_skrzynka-cytursów-600x421.jpg": "live-assets/5_skrzynka-cytursow-600x421.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/5_skrzynka_jablek.jpg": "live-assets/5_skrzynka_jablek.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/6_zestaw-letni-standard-600x392.jpg": "live-assets/6_zestaw-letni-standard-600x392.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/6_zestaw-zimowy-premium-600x486.jpg": "live-assets/6_zestaw-zimowy-premium-600x486.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/6_zestaw-zimowy-standard-600x452.jpg": "live-assets/6_zestaw-zimowy-standard-600x452.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/7_skrzynka-warzywna-premium-mix-600x454.jpg": "live-assets/7_skrzynka-warzywna-premium-mix-600x454.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/Marchew-krojona-600x452.jpg": "live-assets/Marchew-krojona-600x452.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/Sady-Wincenta-330-ml_Obszar-roboczy-1.jpg": "live-assets/Sady-Wincenta-330-ml_Obszar-roboczy-1.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/Skrzynka-warzywa-standard-600x475.jpg": "live-assets/Skrzynka-warzywa-standard-600x475.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/Soki-Dailyfruits.jpg": "live-assets/Soki-Dailyfruits.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/Soki-NFC-„Sady-Wincenta”-5-l-1.jpg": "live-assets/Soki-NFC-Sady-Wincenta-5-l-1.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/cymes-600x529.jpg": "live-assets/cymes-600x529.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/lodówka-600x771.jpg": "live-assets/lodowka-600x771.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/produkt-soki-rodziny-rembowskich.jpg": "live-assets/produkt-soki-rodziny-rembowskich.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/produkt-soki-zielona-tlocznia-200-ml.jpg": "live-assets/produkt-soki-zielona-tlocznia-200-ml.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/produkt-soki-zielona-tlocznia-400-ml.jpg": "live-assets/produkt-soki-zielona-tlocznia-400-ml.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/produkt-syropy-rebmowskich.jpg": "live-assets/produkt-syropy-rebmowskich.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/zestaw-soków-na-palecie-20szt-DF-mix-600x379.jpg": "live-assets/zestaw-sokow-na-palecie-20szt-DF-mix-600x379.jpg",
 "https://dailyfruits.pl/app/uploads/2020/01/zestaw-standard-mix-600x509.png": "live-assets/zestaw-standard-mix-600x509.png",
 "https://dailyfruits.pl/app/uploads/2020/01/zestaw-warzyw-krojonych-12szt-tacka-600x459.jpg": "live-assets/zestaw-warzyw-krojonych-12szt-tacka-600x459.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/Bez-nazwy-2_Obszar-roboczy-1-600x558.png": "live-assets/Bez-nazwy-2_Obszar-roboczy-1-600x558.png",
 "https://dailyfruits.pl/app/uploads/2020/02/Etykiety_bakalie-wizualizacja-szkic.jpg": "live-assets/Etykiety_bakalie-wizualizacja-szkic.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/Musli-600x600.png": "live-assets/Musli-600x600.png",
 "https://dailyfruits.pl/app/uploads/2020/02/ankieta-01-600x540.jpg": "live-assets/ankieta-01-600x540.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/bakalie-duże-600x580.jpg": "live-assets/bakalie-duze-600x580.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/cherry.png": "live-assets/cherry.png",
 "https://dailyfruits.pl/app/uploads/2020/02/do-pieczywa-600x600.png": "live-assets/do-pieczywa-600x600.png",
 "https://dailyfruits.pl/app/uploads/2020/02/do-pieczywa_Obszar-roboczy-1-600x600.png": "live-assets/do-pieczywa_Obszar-roboczy-1-600x600.png",
 "https://dailyfruits.pl/app/uploads/2020/02/do-płatków-600x600.png": "live-assets/do-patkow-600x600.png",
 "https://dailyfruits.pl/app/uploads/2020/02/eco-produkty.jpg": "live-assets/eco-produkty.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/ekspozytor-drewniany.jpg": "live-assets/ekspozytor-drewniany.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/event-sok.jpg": "live-assets/event-sok.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/kalarepa.png": "live-assets/kalarepa.png",
 "https://dailyfruits.pl/app/uploads/2020/02/kiszony.png": "live-assets/kiszony.png",
 "https://dailyfruits.pl/app/uploads/2020/02/marchewka-krojona-500-g-1-600x436.jpg": "live-assets/marchewka-krojona-500-g-1-600x436.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/materiały-edukacyjne-600x508.jpg": "live-assets/materiay-edukacyjne-600x508.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/mix-warzyw-tacka-600x389.jpg": "live-assets/mix-warzyw-tacka-600x389.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/miód-skarby-roztocza-600x600.png": "live-assets/miod-skarby-roztocza-600x600.png",
 "https://dailyfruits.pl/app/uploads/2020/02/ogórek.png": "live-assets/ogorek.png",
 "https://dailyfruits.pl/app/uploads/2020/02/rzodkiewka.png": "live-assets/rzodkiewka.png",
 "https://dailyfruits.pl/app/uploads/2020/02/serek-wiejski-paletka-600x341.jpg": "live-assets/serek-wiejski-paletka-600x341.jpg",
 "https://dailyfruits.pl/app/uploads/2020/02/szkolenia_Obszar-roboczy-1.jpg": "live-assets/szkolenia_Obszar-roboczy-1.jpg",
 "https://dailyfruits.pl/app/uploads/2020/04/21_papryka-krojona-tacka-600x373.jpg": "live-assets/21_papryka-krojona-tacka-600x373.jpg",
 "https://dailyfruits.pl/app/uploads/2020/04/Ciasteczka-zbozowe-400-g-600x600.png": "live-assets/Ciasteczka-zbozowe-400-g-600x600.png",
 "https://dailyfruits.pl/app/uploads/2020/04/DOBRA-KALORIA-600x677.png": "live-assets/DOBRA-KALORIA-600x677.png",
 "https://dailyfruits.pl/app/uploads/2020/04/ciasteczka-zbozowe-30g-600x600.png": "live-assets/ciasteczka-zbozowe-30g-600x600.png",
 "https://dailyfruits.pl/app/uploads/2020/06/zestawy-0602-600x509.jpg": "live-assets/zestawy-0602-600x509.jpg",
 "https://dailyfruits.pl/app/uploads/2020/06/zestawy-0604-600x509.jpg": "live-assets/zestawy-0604-600x509.jpg",
 "https://dailyfruits.pl/app/uploads/2020/06/zestawy-0605-600x509.jpg": "live-assets/zestawy-0605-600x509.jpg",
 "https://dailyfruits.pl/app/uploads/2020/06/zestawy-0606-600x509.jpg": "live-assets/zestawy-0606-600x509.jpg",
 "https://dailyfruits.pl/app/uploads/2023/03/kanapki-zestaw-4-300x300.png": "live-assets/kanapki-zestaw-4-300x300.png",
 "https://dailyfruits.pl/app/uploads/2023/03/kanapki-zestaw-5-300x300.png": "live-assets/kanapki-zestaw-5-300x300.png",
 "https://dailyfruits.pl/app/uploads/2023/03/kanapki-zestaw-6-300x300.png": "live-assets/kanapki-zestaw-6-300x300.png",
 "https://dailyfruits.pl/app/uploads/2023/10/Kanapki-do-pracy1-300x300.jpg": "live-assets/Kanapki-do-pracy1-300x300.jpg",
 "https://dailyfruits.pl/app/uploads/2023/10/Kanapki-do-pracy2-300x300.jpg": "live-assets/Kanapki-do-pracy2-300x300.jpg",
 "https://dailyfruits.pl/app/uploads/2023/10/Kanapki-do-pracy3-300x300.jpg": "live-assets/Kanapki-do-pracy3-300x300.jpg",
 "https://dailyfruits.pl/app/uploads/2023/10/Kanapki-do-pracy4-300x300.jpg": "live-assets/Kanapki-do-pracy4-300x300.jpg",
 "https://dailyfruits.pl/app/uploads/2023/10/Kanapki-do-pracy5-300x300.jpg": "live-assets/Kanapki-do-pracy5-300x300.jpg",
 "https://dailyfruits.pl/app/uploads/2023/10/Kanapki-do-pracy6-300x300.jpg": "live-assets/Kanapki-do-pracy6-300x300.jpg",
 "https://dailyfruits.pl/app/uploads/2024/02/kanapki-katalog1-600x600.png": "live-assets/kanapki-katalog1-600x600.png",
 "https://dailyfruits.pl/app/uploads/2024/03/s2-600x578.jpg": "live-assets/s2-600x578.jpg",
 "https://dailyfruits.pl/app/uploads/2024/03/s4-600x592.jpg": "live-assets/s4-600x592.jpg",
 "https://dailyfruits.pl/app/uploads/2024/03/s6.jpg": "live-assets/s6.jpg",
 "https://dailyfruits.pl/app/uploads/2024/03/s7-600x600.jpg": "live-assets/s7-600x600.jpg",
 "https://dailyfruits.pl/app/uploads/2024/03/s8-600x600.jpg": "live-assets/s8-600x600.jpg"
}
ok=fail=0
for url,local in MAP.items():
    if os.path.exists(local): ok+=1; continue
    try:
        req=urllib.request.Request(urllib.parse.quote(url,safe=':/?&=%'),headers={'User-Agent':'Mozilla/5.0'})
        open(local,'wb').write(urllib.request.urlopen(req,timeout=30).read())
        ok+=1; print('OK ',local)
    except Exception as e:
        fail+=1; print('FAIL',url,e)
print(f'Pobrano {ok}, bledow {fail}')
if fail==0:
    t=open('oferta-v2.html',encoding='utf-8').read()
    for url,local in MAP.items():
        t=t.replace(urllib.parse.quote(url,safe=':/?&=%'),local)
    open('oferta-v2.html','w',encoding='utf-8').write(t)
    print('oferta-v2.html przepieta na lokalne grafiki. Zrob: git add -A && git commit && git push')
else:
    print('Sa bledy pobierania - oferta-v2.html NIE zostala przepieta (nadal uzywa URL-i live).')
