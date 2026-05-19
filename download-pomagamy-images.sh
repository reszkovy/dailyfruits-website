#!/bin/bash
# Download all CSR/pomagamy images from old WordPress site
# Run from the Fruityyyy folder: bash download-pomagamy-images.sh

mkdir -p pomagamy

echo "Downloading pomagamy images..."

# Młodzieżowy Ośrodek Socjoterapii
curl -sL "https://dailyfruits.pl/app/uploads/2024/06/zdjecie2-380x380.jpg" -o pomagamy/mos.jpg
curl -sL "https://dailyfruits.pl/app/uploads/2024/06/zdjecie1-380x380.jpeg" -o pomagamy/mos-2.jpg

# Fundacja Inna Przestrzeń
curl -sL "https://dailyfruits.pl/app/uploads/2023/09/dom-matki.jpg" -o pomagamy/inna-przestrzen.jpg
curl -sL "https://dailyfruits.pl/app/uploads/2023/09/dommatki-380x380.jpg" -o pomagamy/inna-przestrzen-2.jpg

# Teatr za Jeden Uśmiech
curl -sL "https://dailyfruits.pl/app/uploads/2023/09/logotyp-teatr-jeden-usmiech.jpg" -o pomagamy/teatr-usmiech.jpg

# Wieczór Marzeń / Fundacja Dziecięca Fantazja
curl -sL "https://dailyfruits.pl/app/uploads/2023/09/Wiecz%C3%B3r-Marze%C5%84-1024x681.jpg" -o pomagamy/wieczor-marzen.jpg

# Olimpiada Zdrowia PCK
curl -sL "https://dailyfruits.pl/app/uploads/2023/09/podziekowanie-olipiada-zdrowia-z-pck.jpg" -o pomagamy/olimpiada-pck.jpg

# WOŚP
curl -sL "https://dailyfruits.pl/app/uploads/2020/05/wosp-2401.jpg" -o pomagamy/wosp-1.jpg
curl -sL "https://dailyfruits.pl/app/uploads/2020/05/DF-wo%C5%9Bp-2020.jpg" -o pomagamy/wosp-2.jpg
curl -sL "https://dailyfruits.pl/app/uploads/2018/01/5m.jpg" -o pomagamy/wosp-3.jpg
curl -sL "https://dailyfruits.pl/app/uploads/2018/01/7m.jpg" -o pomagamy/wosp-4.jpg

# Akcja #wspieram
curl -sL "https://dailyfruits.pl/app/uploads/2020/04/bank-%C5%BCywno%C5%9Bci-1-1.jpg" -o pomagamy/wspieram-1.jpg
curl -sL "https://dailyfruits.pl/app/uploads/2020/04/ludzie.jpg" -o pomagamy/wspieram-2.jpg
curl -sL "https://dailyfruits.pl/app/uploads/2020/04/df-bank-%C5%BCywno%C5%9Bci-2-scaled.jpg" -o pomagamy/wspieram-3.jpg

# Stowarzyszenie UNICORN
curl -sL "https://dailyfruits.pl/app/uploads/2020/05/Fundacja-Unicorn-1024x719.png" -o pomagamy/unicorn.png

# Fundacja NEBO
curl -sL "https://dailyfruits.pl/app/uploads/2016/01/nebo2.jpg" -o pomagamy/nebo.jpg

# Ognisko Gocław i Ursynów
curl -sL "https://dailyfruits.pl/app/uploads/2020/05/ognisko-ursyn%C3%B3w.jpeg" -o pomagamy/ognisko.jpg

# Fundacja Centaurus
curl -sL "https://dailyfruits.pl/app/uploads/2016/01/koniki-292x300.png" -o pomagamy/centaurus.png

# ZOO Warszawa
curl -sL "https://dailyfruits.pl/app/uploads/2020/05/PANDA-206x300.png" -o pomagamy/zoo.png

# Szlachetna Paczka
curl -sL "https://dailyfruits.pl/app/uploads/2020/05/Zjazd-Wolontariuszy-SZLACHETNEJ-PACZKI-i-AKADEMII-PRZYSZ%C5%81O%C5%9ACI2-1-scaled.jpg" -o pomagamy/szlachetna-paczka.jpg
curl -sL "https://dailyfruits.pl/app/uploads/2020/05/pomagamy-dzieciom.png" -o pomagamy/szlachetna-paczka-2.png

echo "Done! Downloaded $(ls pomagamy/ | wc -l) images to pomagamy/"
ls -lh pomagamy/
