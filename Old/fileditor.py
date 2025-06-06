# fileditor.py

try:
    with open("fil.txt","r+") as fil:               # Vi åpner filen i lesbar og skrivbar modus (r+). Ved å kjøre koden i en with-blokk, vil filen bli lukket når blokken er ferdig.
        fil.seek(54)                                # Flytter filpekeren til posisjon 50 i filen. Dette er nyttig hvis vi ønsker å skrive over noe som allerede finnes i filen.
        fil.write("######")                         # Skriver "#####" på posisjon 50 i filen. Dette vil overskrive det som allerede er der.
except Exception as e:                              # Hvis det oppstår en feil under filoperasjonen, vil vi fange den i en variabel.
    print(f"Oh shit... noe rart skjedde: {e}")      # Skriver ut en feilmelding hvis noe går galt.
finally:
    fil.close()                                     # Lukker filen. Dette er viktig for å frigjøre ressurser og sikre at endringene blir lagret.
    print("Fil? Hvilken fil... den er lukket...")   # Skriver ut en bekreftelse på at filen er lukket.