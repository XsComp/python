# politibetjent.py

# politibetjent.py
# Klassen for vår hverdagshelt – Politibetjenten

class Politibetjent:
    def __init__(self, fornavn, etternavn, alder, antall_forbrytelser=0):
        self.fornavn = fornavn                                              # Fornavn til helten vår
        self.etternavn = etternavn                                          # Etternavn – viktig for navneskiltet!
        self.alder = alder                                                  # Hvor lenge har de patruljert jorda
        self.antall_forbrytelser = antall_forbrytelser                      # Hvor mange skurker har de stoppet?
        self.utmerkelser = []                                               # Tom liste for heder og ære

    def legg_til_utmerkelse(self, utmerkelse):
        self.utmerkelser.append(utmerkelse)                                 # Legger til ny utmerkelse i lista

    def vis_info(self):
        print(f"Navn: {self.fornavn} {self.etternavn}")
        print(f"Alder: {self.alder} år")
        print(f"Forbrytelser stoppet: {self.antall_forbrytelser}")
        
        if len(self.utmerkelser) == 0:
            print("Utmerkelser: Ingen... men dagen er ennå ung! Alt vi trenger nå, er LITT insats")
        else:
            print("Utmerkelser:")
            for utmerkelse in self.utmerkelser:
                print(f"  - {utmerkelse}")
        
        print("-" * 50)                                                     # Bare for å gjøre det pent