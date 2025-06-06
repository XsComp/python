# ansatt_module.py

class Ansatt:                           # En Klasse variabel for å holde styr på det totale antall ansatte
    telling = 0                         # Telling av ansatte, starter på 0

    def __init__(self):
        self.navn = ""                   # Instans variabel for fornavn
        self.etternavn = ""                # Instans variabel for etternavn
        Ansatt.telling += 1              # Øk teller i hele Klassen
        self.nummer = Ansatt.telling     # Tildel dette som ansattnummer
