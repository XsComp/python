"""
Testmodul som prøver å importere alle viktige moduler du bruker i prosjektet.
Hvis noe feiler, får du en klar beskjed i terminalen.
"""

moduler = [
    "rich", "requests", "pandas", "pyfiglet", "termcolor",
    "numpy", "matplotlib", "seaborn", "scapy", "pysnmp",
    "python_nmap", "cryptography", "pycryptodome", "passlib"
]

print("🧪 Tester import av moduler...\n")

for modul in moduler:
    try:
        __import__(modul)
        print(f"✅ {modul} importert OK")
    except ImportError as e:
        print(f"❌ FEIL: {modul} kunne ikke importeres - {e}")

print("\n🎯 Ferdig.")

import nmap
