#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DailyFruits — AI-elevation packshotów (gpt-image-1, OpenAI Images Edit API)

Bierze REALNE packshoty z live-assets/ i podbija je do poziomu premium:
czyste białe tło studyjne, miękkie światło, delikatny cień, wyśrodkowany kadr.
Produkt, opakowanie i etykiety zostają DOKŁADNIE jak na oryginale — to edycja,
nie generacja fikcyjnego produktu.

Zdjęcia z ludźmi mają zostać realne (zaufanie) — dopisz nazwy plików do KEEP_REAL.

UŻYCIE (na swoim komputerze, po uruchomieniu pobierz-grafiki.py):
    pip3 install openai
    export OPENAI_API_KEY="sk-..."
    python3 live-assets/elevate-packshoty.py            # jakość medium (~$0.06/obraz)
    python3 live-assets/elevate-packshoty.py --quality high   # (~$0.17/obraz)

Skrypt jest wznawialny — pomija już przetworzone pliki w live-assets/elevated/.
Po komplecie przepina oferta-v2.html na wersje elevated.
"""
import os, sys, glob, base64

# ── konfiguracja ──────────────────────────────────────────────────────────
QUALITY = "high" if "--quality" in sys.argv and "high" in sys.argv else "medium"
SIZE = "1536x1024"   # landscape, pasuje do kart 4:3 (contain)

# Pliki, które mają ZOSTAĆ realne (np. zdjęcia z ludźmi) — nazwa pliku z live-assets/
KEEP_REAL = [
    # "przyklad-zdjecie-z-ludzmi.jpg",
]

PROMPT = (
    "Professional e-commerce product packshot, elevated premium quality. "
    "Take this real product photo and improve it: pure white seamless studio background, "
    "soft diffused studio lighting, gentle realistic shadow under the product, "
    "centered composition with even margins on all sides. "
    "Keep the actual food products, their quantities, arrangement and composition unchanged — "
    "do not add, remove or replace any items. "
    "IMPORTANT: if any packaging, wrapper, box or bottle shows a brand name, logo or trademark, "
    "remove the branding completely — replace it with clean, plain, unbranded packaging of the "
    "same shape, material and color, with no text or logos. "
    "Photorealistic, sharp, high-end food photography look."
)

# ── przygotowanie ─────────────────────────────────────────────────────────
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SRC = "live-assets"
OUT = "live-assets/elevated"
os.makedirs(OUT, exist_ok=True)

if not os.environ.get("OPENAI_API_KEY"):
    sys.exit("Brak OPENAI_API_KEY w środowisku. Ustaw: export OPENAI_API_KEY=\"sk-...\"")

try:
    from openai import OpenAI
except ImportError:
    sys.exit("Brak biblioteki openai. Zainstaluj: pip3 install openai")

client = OpenAI()

imgs = [f for f in sorted(glob.glob(f"{SRC}/*"))
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        and os.path.basename(f) not in KEEP_REAL]

if not imgs:
    sys.exit(f"Brak obrazów w {SRC}/ — najpierw uruchom: python3 live-assets/pobierz-grafiki.py")

print(f"Do przetworzenia: {len(imgs)} obrazów | jakość: {QUALITY} | rozmiar: {SIZE}")
est = 0.17 if QUALITY == "high" else 0.06
print(f"Szacunkowy koszt: ~${len(imgs)*est:.2f}\n")

ok = fail = skip = 0
mapping = {}
for path in imgs:
    name = os.path.splitext(os.path.basename(path))[0] + ".png"
    out = f"{OUT}/{name}"
    mapping[f"{SRC}/{os.path.basename(path)}"] = out
    if os.path.exists(out):
        skip += 1
        continue
    try:
        with open(path, "rb") as fh:
            r = client.images.edit(model="gpt-image-1", image=fh,
                                   prompt=PROMPT, size=SIZE, quality=QUALITY)
        data = base64.b64decode(r.data[0].b64_json)
        with open(out, "wb") as o:
            o.write(data)
        ok += 1
        print(f"OK   {name}")
    except Exception as e:
        fail += 1
        print(f"FAIL {name}: {e}")

print(f"\nGotowe: {ok} nowych, {skip} pominiętych (już były), {fail} błędów")

# ── przepięcie oferta-v2.html ────────────────────────────────────────────
if fail == 0 and (ok or skip):
    html = open("oferta-v2.html", encoding="utf-8").read()
    n = 0
    for src, dst in mapping.items():
        if os.path.exists(dst) and src in html:
            html = html.replace(src, dst)
            n += 1
    open("oferta-v2.html", "w", encoding="utf-8").write(html)
    print(f"oferta-v2.html: przepięto {n} referencji na wersje elevated.")
    print("Teraz: git add -A && git commit -m 'packshoty elevated' && git push")
else:
    print("Były błędy — oferta-v2.html NIE została przepięta. Uruchom ponownie (wznowi od brakujących).")
