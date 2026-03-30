#!/usr/bin/env python3
import re
import json
import os

# Dateien definieren
quran_file = 'quran-simple-clean (1).txt'
dict_file = 'woerterbuch.json'

# 1. Wörterbuch laden (oder neu erstellen)
def load_dict():
    if os.path.exists(dict_file):
        with open(dict_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# 2. Wörterbuch speichern
def save_dict(d):
    with open(dict_file, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

meanings = load_dict()

# 3. Koran-Text laden
try:
    with open(quran_file, 'r', encoding='utf-8') as f:
        full_text = f.read()
except FileNotFoundError:
    print(f"❌ Datei {quran_file} fehlt!")
    exit()

# 4. Abfrage & Filterung
print("\n--- Intelligentes Koran-System ---")
start_input = input("ANFANG: ").strip()
end_input   = input("ENDE: ").strip()

start_idx = full_text.find(start_input)
end_idx = full_text.find(end_input, start_idx)

if start_idx == -1 or end_idx == -1:
    print("❌ Textstelle nicht gefunden!")
    exit()

text_segment = full_text[start_idx : end_idx + len(end_input)]

# Stopwörter
stop_words = {'من', 'في', 'ما', 'إن', 'لا', 'على', 'الذين', 'إلا', 'ولا', 'وما', 'أن', 'ل', 'إلى'}

all_words = re.findall(r'[\u0600-\u06FF]+', text_segment)
words_cleaned = [w for w in all_words if w not in stop_words]

# 5. Ausgabe mit Lern-Funktion
print("\n📜 Ergebnisse:")
print("="*60)

for i, wort in enumerate(words_cleaned, 1):
    bedeutung = meanings.get(wort, "???")
    print(f"{i:>3}. {wort} → {bedeutung}")

print("="*60)

# Optionale Lern-Funktion: Neue Wörter hinzufügen
update = input("\nMöchtest du neue Wörter zum Wörterbuch hinzufügen? (j/n): ")
if update.lower() == 'j':
    for wort in words_cleaned:
        if wort not in meanings:
            übersetzung = input(f"Bedeutung für '{wort}': ")
            if übersetzung:
                meanings[wort] = übersetzung
    save_dict(meanings)
    print("✅ Wörterbuch aktualisiert!")

