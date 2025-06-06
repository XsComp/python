# randomnumbers.py

import random  # Importerer for å generere tilfeldige tall

# Lager en liste med 100 tilfeldige tall mellom 0 og 500
tilfeldige_tall = [random.randint(0, 500) for _ in range(100)]

# Spør brukeren om filnavn for lagring
filnavn = input("Oppgi filnavnet du vil lagre tallene i (f.eks. tall.txt): ").strip()

# Skriver tallene til filen
try:
    with open(filnavn, "w") as fil:
        for tall in tilfeldige_tall:
            fil.write(f"{tall}\n")
    print(f"Tallene ble lagret i '{filnavn}'.")
except Exception as e:
    print(f"Noe gikk galt ved skriving til fil: {e}")
