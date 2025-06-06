# PLC_and_calc.py



# Beskrivelse: Utfører en boolsk AND-operasjon på to binære verdier fra brukeren

def hent_binær_input(prompt):
    while True:
        verdi = input(prompt)
        if verdi in ("0", "1"):
            return int(verdi)
        else:
            print("Ugyldig input. Skriv inn kun 0 eller 1.")

def main():
    print("Vår logiske PLC (PLS) \"AND\" kalkulator!")

    bin1 = hent_binær_input("Skriv inn 0 eller 1: ")
    bin2 = hent_binær_input("Skriv inn 0 eller 1 igjen: ")

    resultat = bin1 & bin2

    print(f"\nResultat av AND mellom {bin1} og {bin2} er: {resultat}")

# Kjør hovedfunksjonen kun hvis skriptet kjøres direkte
if __name__ == "__main__":
    main()