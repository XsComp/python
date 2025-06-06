#filbehandler_3000.py


import os  # Vi bruker os-modulen for å sjekke og manipulere filer

print("Velkommen til Filbehandleren 3000, hvor \"drag and drop\" bare er en fantasi!")
fil_navn = input("Oppgi filnavn (med .txt eller annet filformat): ").strip()

# I tilfelle brukeren bare trykker enter eller skriver noe tomt (space)
if not fil_navn:
    print("Du må oppgi et filnavn. Prøv å skrive bokstaver? Jeg gir opp, avslutter.")
else:
    print("\nNice!! Hva ønsker du gjøre med denne?")
    print("1: Opprette filen")
    print("2: Slette filen")

    valg = input("Skriv inn 1 eller 2: ").strip()

    try:
        if valg == "1":
            if os.path.exists(fil_navn):
                print(f"Filen '{fil_navn}' eksisterer allerede. Ingen endringer ble gjort. Kaste bort tid... ja det kan du.")
            else:
                with open(fil_navn, "w") as ny_fil:
                    pass  # Vi oppretter bare en tom fil
                print(f"Filen '{fil_navn}' ble opprettet. Gi deg selv en klapp på skulderen!")

        elif valg == "2":
            if os.path.exists(fil_navn):
                os.remove(fil_navn)
                print(f"Filen '{fil_navn}' ble slettet. Du fikk til noe... Gratulerer... det er nå du oppdager at du slettet feil fil.")
            else:
                print(f"Filen '{fil_navn}' finnes ikke. Ingenting å slette. Du skal ikke dele på null mens du er i gang da... det er minst like mulig som å slette en fil som ikke finnes.")

        else:
            print("Du skrev ikke inn 1 eller 2... kanskje ta en kaffe og prøve igjen senere? Eller kanskje du er fornøyd med resultatet?")

    except PermissionError:
        print(f"Tillatelse nektet. Du er nok ikke priveligert nok til å endre '{fil_navn}'.")

    except Exception as e:
        print(f"Hva i svarte natta var det du gjorde nå??? Det måtte deg til... ikke sant?: {e}")
