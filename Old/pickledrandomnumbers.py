# pickledrandomnumbers.py

import pickle
import os
import random
import string

lager = "random_dict.pkl"

def generer_dict():
    return {bokstav: random.randint(0, 1000) for bokstav in string.ascii_lowercase}

# Forsøk å laste eksisterende dictionary
if os.path.exists(lager):
    with open(lager, "rb") as fil:
        data = pickle.load(fil)
    print("Henter data.")
else:
    data = generer_dict()
    print("Laget nytt lager.")
    with open(lager, "wb") as fil:
        pickle.dump(data, fil)

# Viser innholdet
print("\nInnhold i dictionary:")
for k, v in sorted(data.items()):
    print(f"{k}: {v}")

# Brukeren kan oppdatere verdier
oppdater = input("\nØnsker du å oppdatere en verdi? (y/n): ").lower()
if oppdater == "y":
    while True:
        valgt_nokkel = input("Hvilken bokstav (a-z) vil du oppdatere? ('stopp' for å avslutte): ").lower()
        if valgt_nokkel == "stopp":
            break
        elif valgt_nokkel in data:
            try:
                ny_verdi = int(input(f"Oppgi ny verdi for '{valgt_nokkel}': "))
                data[valgt_nokkel] = ny_verdi
                print(f"'{valgt_nokkel}' er oppdatert til {ny_verdi}.")
            except ValueError:
                print("Ugyldig verdi. Du må bruke tall. Bokstaver er ikke tall.")
        else:
            print("Ugyldig nøkkel. Prøv en (en betyr 1... som er 20 mindre enn tre...) \"BOKSTAV\" fra a til z.")

    # Lagre oppdatert dictionary
    with open(lager, "wb") as fil:
        pickle.dump(data, fil)
    print("Endringene ble lagret til lager.")
else:
    print("Ingen endringer ble gjort.")
