import os
import subprocess
from datetime import datetime

#Sti til meldingsfilen
filsti = os.path.join(os.getcwd(), "velkommen.txt")

#Kommando for å vise innholdet i filen
vis_melding_kommando = f'cmd /c type "{filsti}" && pause'

#Planlegger visning av velkomstmelding mandag til fredag kl 08:00
subprocess.run([
    "schtasks", "/Create", "/SC", "WEEKLY", "/D", "MON,TUE,WED,THU,FRI",
    "/TN", "VisVelkomstMelding", "/TR", vis_melding_kommando,
    "/ST", "08:00", "/F"
], shell=True)

#Kommando for å åpne Noroff-nettsiden
nettleser_kommando = r'start "" "http://www.noroff.no"'

#Planlegger åpning av nettleser hver time
subprocess.run([
    "schtasks", "/Create", "/SC", "HOURLY", "/TN", "ÅpneNoroff",
    "/TR", nettleser_kommando, "/F"
], shell=True)

print("Oppgaver er planlagt! Sjekk Task Scheduler for detaljer.")
