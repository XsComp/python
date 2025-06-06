# pickle_restore.py

import pickle      # Fordi vi elsker å lagre ting på en måte som bare Python forstår
import os          # Så vi kan sjekke om ting faktisk eksisterer før vi roter det til

filnavn = "lager.pkl"   # Dette er din magiske skattekiste – eller et svart hull, alt ettersom

# Prøver å hente eksisterende data – hvis den finnes og ikke er ødelagt av tidligere udugelighet
if os.path.exists(filnavn):
    try:
        with open(filnavn, "rb") as fil:
            lager = pickle.load(fil)  # Leser inn alle dine tidligere (forhåpentligvis gyldige) tastetrykk
            print("\nGammelt innhold gjenopplivet fra dypet av pickle-filen:\n")
            for kode, beskrivelse in lager.items():
                print(f" - {kode}: {beskrivelse}")
    except Exception as e:
        print(f"Klarte ikke å åpne pickle-filen. Noe gikk fryktelig galt: {e}")
        lager = {}  # Starter på nytt, og later som om ingenting skjedde
else:
    print("\nFant ingen gammel fil. Vi begynner med blanke ark og fargestifter.")
    lager = {}

# Tid for brukeren å briljere med tastaturet
print("\nSkriv inn nye oppføringer. Forlat feltet tomt og trykk Enter når du går lei.")
while True:
    kode = input("Skriv inn varekode (eller bare trykk Enter for å avslutte): ").strip()
    if not kode:
        print("Eeeh... du gir opp? Personen før deg la inn mye mer arbeid enn deg... Men hvis du mener dette er ditt beste så...")
        break
    beskrivelse = input("Beskriv varen du nettopp Googlet rett staving på: ").strip()
    lager[kode] = beskrivelse
    print(f"Lagt til: '{kode}' med beskrivelsen '{beskrivelse}'. Jeg håper du vet hva du driver med...\n")

# Og så – tiden kommer... for å lagre alt sammen igjen (i håp om at vi ikke mister alt i morgen)
try:
    with open(filnavn, "wb") as fil:
        pickle.dump(lager, fil)  # Kast hele rotet inn i en binær sylinder
    print(f"\nDataene dine ble reddet og stuet bort i '{filnavn}'. Og denne gangen... Try not to f**k it up.")
except Exception as e:
    print(f"\nVent... hva? Data? Hvilken data..? Jeg har ikke sett noe... Systemet sier: {e}")
