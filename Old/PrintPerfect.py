# PrintPerfect.py



def main():
    # Be brukeren om en maksverdi
    maxverdi = int(input("Skriv inn et heltall som øvre grense: "))

    print(f"\nPerfekte tall mellom 1 og {maxverdi}:")

    # Gå gjennom alle tall fra 1 til maksverdi
    for tall in range(1, maxverdi + 1):
        divisorer = []

        # Sjekk hvilke tall som går opp i 'tall'
        for d in range(1, tall):
            if tall % d == 0:
                divisorer.append(d)

        if sum(divisorer) == tall:
            print(f"{tall} er perfekt (fordi {divisorer} summeres til {tall})")

if __name__ == "__main__":
    main()
