# HandleExceptions.py

def handtere_salg():
    salg = []
    print("Tast inn salgsverdier (float). Skriv 'ferdig' for å avslutte innskriving.")

    while True:
        bruker_input = input("Salgsverdi: ").strip().lower()
        if bruker_input == "ferdig":
            break
        try:
            verdi = float(bruker_input)
            salg.append(verdi)
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et desimaltall (float), eller 'ferdig'.")

    if not salg:
        print("Ingen salgsverdier ble lagt inn.")
        return

    print(f"Du har lagt inn {len(salg)} salgsverdier.")

    try:
        tell = int(input("Hvor mange av disse vil du summere?: "))
        if tell < 1:
            raise ValueError("Tallet må være større enn 0.")
        if tell > len(salg):
            raise ValueError("Du har ikke lagt inn så mange salgsverdier.")
        total = sum(salg[:tell])
        print(f"Summen av de første {tell} verdiene er {total}.")
    except ValueError as e:
        print(f"Feil ved input: {e}")
    except Exception as e:
        print(f"En uventet feil oppstod: {e}")


if __name__ == "__main__":
    print("\n--- Start av HandleExceptions ---")
    handtere_salg()
