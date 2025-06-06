# brannstasjon.py

class Brannmann:
    telling = 0                                                                                 # Klassevariabel for å holde styr på hvor mange brannmenn som er opprettet

    def __init__(self, fornavn, etternavn, ansattnummer, alder):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.ansattnummer = ansattnummer
        self.alder = alder
        Brannmann.telling += 1                                                                  # Øker teller hver gang en ny brannmann opprettes

    def vis_info(self):
        print(f"{self.ansattnummer} - {self.fornavn} {self.etternavn}, Alder: {self.alder}")