import base64
import re
import sys
import random
import string

def generiere_verschleierten_namen(laenge=8):
    return ''.join(random.choices(string.ascii_letters, k=laenge))

def verschleiere_variablen(code):
    variablen = set(re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\b", code))
    ausschlussliste = {
        "def", "return", "import", "as", "from", "if", "else", "for", "while",
        "with", "try", "except", "True", "False", "None", "class", "print",
        "open", "in", "not", "is", "and", "or", "self"
    }
    ersetzungen = {}
    for var in variablen:
        if var not in ausschlussliste and not var.startswith("__") and len(var) > 2:
            ersetzungen[var] = generiere_verschleierten_namen()
    for original, verschluesselt in ersetzungen.items():
        code = re.sub(rf"\b{original}\b", verschluesselt, code)
    return code

def entferne_leerzeichen_und_kommentare(code):
    zeilen = code.splitlines()
    gefiltert = []
    for zeile in zeilen:
        zeile = zeile.strip()
        if zeile and not zeile.startswith("#"):
            gefiltert.append(zeile)
    return " ".join(gefiltert)

def base64_kodieren(code):
    kodiert = base64.b64encode(code.encode("utf-8")).decode("utf-8")
    umschlag = f"""
import base64
exec(base64.b64decode("{kodiert}").decode("utf-8"))
"""
    return umschlag.strip()

def verschluessle_datei(eingabe_datei, ausgabe_datei, mit_base64=True):
    with open(eingabe_datei, "r", encoding="utf-8") as f:
        code = f.read()

    code = verschleiere_variablen(code)
    code = entferne_leerzeichen_und_kommentare(code)

    if mit_base64:
        code = base64_kodieren(code)

    with open(ausgabe_datei, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"[✓] Verschleierte Datei gespeichert als: {ausgabe_datei}")

# Hauptprogramm
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Verwendung: python obfuscator.py quellcode.py ausgabe.py [--nobase64]")
        sys.exit(1)

    quellcode = sys.argv[1]
    zielcode = sys.argv[2]
    base64_aktiv = "--nobase64" not in sys.argv

    verschluessle_datei(quellcode, zielcode, mit_base64=base64_aktiv)
