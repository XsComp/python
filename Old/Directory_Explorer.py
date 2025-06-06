import os
import datetime

# Ber brukeren om en fil-sti
sti = input("Oppgi en gyldig fil-sti: ")

# Sjekk om stien faktisk eksisterer
if not os.path.exists(sti):
    print("Eeeh... nei... den stien finnes ikke. Er det stavingen som er vrien kanskje?")
else:
    print(f"\nDu fant '{sti}':\n")

    # 🚶‍♂️ Går gjennom mapper og filer rekursivt
    for nåværende_sti, undermapper, filer in os.walk(sti):
        print(f"[Mappe] {nåværende_sti}")
        for undermappe in undermapper:
            print(f"  |- [Undermappe] {undermappe}")
        for fil in filer:
            print(f"  |- [Fil] {fil}")
        print()

    # Spør brukeren om de vil se detaljer for en fil
    svar = input("Har du lyst til å leke detektiv på en eller annen fil? (y/n): ").lower()

    if svar == 'y':
        filnavn = input("Ok, hva heter filen da? Ikke glem å ta med fil-sti hvis den ligger i en eller annen undermappe): ")
        full_sti = os.path.join(sti, filnavn)

        if os.path.exists(full_sti) and os.path.isfile(full_sti):
            detaljer = os.stat(full_sti)

            # Konverterer tidsstempler til lesbare datoer
            def lesbar_tid(stempel):
                return datetime.datetime.fromtimestamp(stempel).strftime("%Y-%m-%d %H:%M:%S")

            print("\nFildetaljer:")
            print(f"- Filsti:     {full_sti}")
            print(f"- Størrelse:  {detaljer.st_size} bytes")
            print(f"- Opprettet:  {lesbar_tid(detaljer.st_ctime)}")
            print(f"- Endret:     {lesbar_tid(detaljer.st_mtime)}")
            print(f"- Sist brukt: {lesbar_tid(detaljer.st_atime)}")
        else:
            print("Har du lyst til å prøve med en normal fil som... jeg vet ikke... eksisterer?")
    else:
        print("Avslutter programmet. Good.... day sir!")
