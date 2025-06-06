# SummingMachine.py

# Vi lager en funksjon som spør brukeren om tall helt til han skriver 's'
def summerings_maskin():
    total = 0
    while True:
        bruker_input = input("Skriv inn et tall (eller 's' for å stoppe): ")
        if bruker_input.lower() == 's':
            break
        try:
            nummer = float(bruker_input)
            total += nummer
        except ValueError:
            print("Ugyldig verdi. Vennligst skriv inn et tall eller 's'.")

    return total

# Hovedseksjonen
if __name__ == "__main__":
    resultat = summerings_maskin()
    print(f"Summen av alle tallene er: {resultat}")