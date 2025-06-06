# SalesCalculator.py


def main():
    total_salg = 0
    antall_salg = 0

    for i in range(10):
        try:
            verdi = float(input(f"Skriv inn salgsverdi #{i+1}: "))

            if verdi < 5000:
                # Vi hopper over resten av løkken for denne runden
                continue

            elif verdi <= 10000:
                total_salg += verdi
                antall_salg += 1
                gjennomsnitt = total_salg / antall_salg
                print(f"  Totalt salg: {total_salg}")
                print(f"  Gjennomsnitt: {gjennomsnitt:.2f}")

            else:
                print("  Mulig feil – verdien overstiger 10 000. Avslutter.")
                break

        except ValueError:
            print("Ugyldig verdi. Vennligst skriv inn et gyldig tall.")

if __name__ == "__main__":
    main()
