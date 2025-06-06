import zipfile
import os

zip_navn = input("Oppgi navn på zip-filen (inkluder .zip): ").strip() # Be brukeren om navn på zip-filen
# Opprett zip-fil hvis den ikke finnes
if not os.path.exists(zip_navn):    # Sjekker om zip-filen allerede finnes
    with zipfile.ZipFile(zip_navn, 'w') as ny_zip:  # 'w' for write, oppretter en ny zip-fil
        print(f"Zip-filen '{zip_navn}' ble opprettet.") # Informer brukeren om at zip-filen ble opprettet
else:
    print(f"Zip-filen '{zip_navn}' finnes allerede, vi legger til flere filer.")

# Legg til filer én etter én
while True:
    filsti = input("Oppgi filen du vil legge til (eller skriv 'q' for å avslutte): ").strip()   # Be brukeren om filsti

    if filsti.lower() == 'q':   # Sjekk om brukeren vil avslutte
        print("Avslutter fil-tillegging.")  # Informer brukeren om at vi avslutter
        break   # Avslutter løkken hvis brukeren skriver 'q'

    if not os.path.exists(filsti):  # Sjekker om filen finnes
        print(f"Filen '{filsti}' ble ikke funnet. Prøv igjen.")
        continue

    try:
        filnavn_i_zip = os.path.basename(filsti)  # Kun filnavn, ikke hele stien, lagres i variabelen.

        with zipfile.ZipFile(zip_navn, 'r') as sjekk_zip:   # Åpner zip-filen for lesing
            eksisterende_filer = sjekk_zip.namelist()   # Hent liste over eksisterende filer i zip-filen

        if filnavn_i_zip in eksisterende_filer: # Sjekk om filen allerede finnes i zip-filen
            # Filen finnes fra før – spør brukeren om vi skal skrive over, eller hoppe over.
            valg = input(f"Filen '{filnavn_i_zip}' finnes allerede i arkivet. Overskriv? (y=skriv over - n=hopp over) (y/n): ").lower()
            if valg != 'y':
                print("Da hopper vi over filen.")
                continue

            #For å overskrive: lag en ny zip med alt unntatt denne filen
            midlertidig_zip = "temp_" + zip_navn    # Midlertidig zip-fil for å lagre endringene
            # Åpne den eksisterende zip-filen og skriv til en ny zip-fil uten den eksisterende filen
            with zipfile.ZipFile(zip_navn, 'r') as original, \
                 zipfile.ZipFile(midlertidig_zip, 'w') as ny_zip:   # Åpne den eksisterende zip-filen for lesing og en ny for skriving
                for item in original.infolist():    # Iterer gjennom alle filer i den eksisterende zip-filen
                    if item.filename != filnavn_i_zip:  # Hvis filen ikke er den vi skal overskrive
                        ny_zip.writestr(item, original.read(item.filename)) # Skriv den til den nye zip-filen

            os.remove(zip_navn) # Slett den gamle zip-filen
            os.rename(midlertidig_zip, zip_navn)    # Gi den nye zip-filen det opprinnelige navnet

        #Legg til filen til zip-filen
        with zipfile.ZipFile(zip_navn, 'a') as arkiv:   # 'a' for append, slik at vi kan legge til filer uten å slette eksisterende innhold
            arkiv.write(filsti, arcname=filnavn_i_zip)  # arcname brukes for å lagre filen med kun filnavnet i zip-filen
            print(f"La til: {filnavn_i_zip}")    # Bekreft at filen ble lagt til

    except PermissionError:
        print(f"Ingen tilgang til '{filsti}'.") # Håndterer tilgangsfeil
    except Exception as e:  # Generell feilbehandling
        print(f"⚠️ En feil oppstod: {e}")   # Skriver ut feilmeldingen


# Output test:
# Oppgi navn på zip-filen (inkluder .zip): Andreas.zip
# Zip-filen 'Andreas.zip' ble opprettet.
# Oppgi filen du vil legge til (eller skriv 'q' for å avslutte): Test1.txt
# La til: Test1.txt
# Oppgi filen du vil legge til (eller skriv 'q' for å avslutte): TEst3.txt
# La til: TEst3.txt
# Oppgi filen du vil legge til (eller skriv 'q' for å avslutte): Test1.txt
# Filen 'Test1.txt' finnes allerede i arkivet. Overskriv? (y=skriv over - n=hopp over) (y/n): n
# Da hopper vi over filen.
# Oppgi filen du vil legge til (eller skriv 'q' for å avslutte): TEst3.txt
# Filen 'TEst3.txt' finnes allerede i arkivet. Overskriv? (y=skriv over - n=hopp over) (y/n): y
# La til: TEst3.txt
# Oppgi filen du vil legge til (eller skriv 'q' for å avslutte): q
# Avslutter fil-tillegging.