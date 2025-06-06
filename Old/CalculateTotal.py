# CalculateTotal.py


def main():
    # Vi starter med en total på 0
    total = 0

    # Vi bruker en while-løkke som kjører helt til brukeren skriver -1
    while True:
        try:
            verdi = int(input("Skriv inn et heltall (-1 for å avslutte): "))
            if verdi == -1:
                break  # Avslutt løkken hvis brukeren skriver -1
            total += verdi  # Legg verdien til totalen
        except ValueError:
            print("Vennligst skriv inn et gyldig heltall.")

    # Når vi er ferdig, skriver vi ut totalen (uten å inkludere -1)
    print(f"\nTotalt: {total}")

if __name__ == "__main__":
    main()