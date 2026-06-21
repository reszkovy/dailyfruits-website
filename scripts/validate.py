#!/usr/bin/env python3
"""Walidator strukturalny DailyFruits — bramka CI (blokujaca).
Chroni przed regresjami wprowadzonymi przez edycje masowe (np. konsolidacja CSS):
  1. Balans tagow <style>/</style> w kazdym pliku.
  2. Strony z <body> maja domkniete </body> i </html>.
  3. Pliki odwolujace sie do shared.css -> plik istnieje.
  4. (informacyjnie) bilans <div> — nie blokuje (znany dlug, 25 plikow).
Wyjscie != 0 => CI faili.
"""
import glob, re, sys, os

errors = []
warnings = []

shared_exists = os.path.exists('shared.css')

for f in sorted(glob.glob('*.html')) + sorted(glob.glob('oferta/**/*.html', recursive=True)):
    src = open(f, encoding='utf-8', errors='replace').read()

    # 1. balans <style>
    o, c = src.count('<style'), src.count('</style>')
    if o != c:
        errors.append(f"{f}: niezbalansowane <style> ({o} otwarc / {c} zamkniec)")

    # 2. domkniecie dokumentu (tylko pliki ze stroną — maja <body)
    if '<body' in src.lower():
        if '</body>' not in src.lower():
            errors.append(f"{f}: brak </body>")
        if '</html>' not in src.lower():
            errors.append(f"{f}: brak </html>")

    # 3. odwolanie do shared.css musi wskazywac istniejacy plik
    if re.search(r'href=["\']shared\.css', src) and not shared_exists:
        errors.append(f"{f}: linkuje shared.css, ale plik nie istnieje")

    # 4. (info) bilans div
    do, dc = len(re.findall(r'<div\b', src)), src.count('</div>')
    if do != dc:
        warnings.append(f"{f}: bilans <div> {do}/{dc} (diff {do-dc})")

print(f"Sprawdzono plikow: {len(glob.glob('*.html')) + len(glob.glob('oferta/**/*.html', recursive=True))}")
if warnings:
    print(f"\n[INFO] niezbalansowane <div> (znany dlug, nie blokuje): {len(warnings)} plikow")
    for w in warnings[:30]:
        print("   -", w)
if errors:
    print(f"\n[FAIL] bledy krytyczne: {len(errors)}")
    for e in errors:
        print("   !", e)
    sys.exit(1)
print("\n[OK] brak bledow krytycznych")
