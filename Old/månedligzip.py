import os
import shutil
import zipfile
from datetime import datetime

#Brukeren får spørsmålet: Hva skal den nye mappen hete?
ny_mappe = input("Hva skal den nye mappen hete? ")

#Sti til scriptets nåværende mappe
gjeldende_sti = os.getcwd()

#Full sti til den nye mappen
ny_mappe_sti = os.path.join(gjeldende_sti, ny_mappe)

#Opprett den nye mappen (hvis den ikke finnes fra før)
os.makedirs(ny_mappe_sti, exist_ok=True)

#Forhåndsdefinert mappe med filer som skal kopieres
kilde_mappe = os.path.join(gjeldende_sti, "old")

#Løper gjennom hver fil i kildemappen
for filnavn in os.listdir(kilde_mappe):
    kilde_fil = os.path.join(kilde_mappe, filnavn)
    
    if os.path.isfile(kilde_fil):
        #Henter opprettelsesdato og formatterer den
        opprettet_tid = os.path.getctime(kilde_fil)
        dato_str = datetime.fromtimestamp(opprettet_tid).strftime("%Y-%m-%d")

        #Lager nytt filnavn med datoen lagt til før filendelsen
        navn, endelse = os.path.splitext(filnavn)
        nytt_navn = f"{navn}_{dato_str}{endelse}"

        dest_fil = os.path.join(ny_mappe_sti, nytt_navn)

        #Kopierer filen og gir den nytt navn
        shutil.copy2(kilde_fil, dest_fil)

#Viser hva som ble kopiert til brukeren
print(f"\nFiler opprettet i '{ny_mappe}':\n")
for fil in os.listdir(ny_mappe_sti):
    print(f"  - {fil}")

#Lager en zip med dagens dato som navn
zip_navn = datetime.today().strftime("backup_%Y-%m-%d.zip")
zip_sti = os.path.join(gjeldende_sti, zip_navn)

#Pakker hele mappen i zip-filen
with zipfile.ZipFile(zip_sti, 'w') as arkiv:
    for fil in os.listdir(ny_mappe_sti):
        full_sti = os.path.join(ny_mappe_sti, fil)
        arkiv.write(full_sti, arcname=fil)

print(f"\nZip-fil opprettet: {zip_navn}")