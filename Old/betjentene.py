# betjenten.py

# Dette er klassen vår som representerer en politibetjent.
# Den holder styr på navn, alder og hvor mange forbrytelser betjenten har stoppet.

class Politibetjent:
    def __init__(self, fornavn, etternavn, alder):
        self.fornavn = fornavn                          # Navnet på helten
        self.etternavn = etternavn                      # Etternavnet på helten
        self.alder = alder                              # Hvor lenge helten har vært på jorda
        self.stoppet_forbrytelser = 0                   # Starter på 0. Gjelder ikke minor crimes, men ekte skurker!

    def stopp_forbrytelse(self):
        self.stoppet_forbrytelser += 1                  # Øker antall forbrytelser stoppet med 1. Kapow!

    def fullt_navn(self):
        return f"{self.fornavn} {self.etternavn}"       # For de gangene vi trenger å rope navnet dramatisk i radioen

    def rapport(self):
        print(f"{self.fullt_navn()} (Alder: {self.alder}) har stoppet {self.stoppet_forbrytelser} forbrytelser.")  # All creds fortjent
