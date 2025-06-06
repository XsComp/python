# ansatt_module_2.py

class Ansatt:
    telling = 0  # Klassevariabel for å holde styr på antall ansatte totalt

    def __init__(self, navn, etternavn):
        self.navn = navn                      # Instansvariabel for fornavn
        self.etternavn = etternavn            # Instansvariabel for etternavn
        Ansatt.telling += 1                  # Øker teller ved hver ny ansatt
        self.nummer = Ansatt.telling         # Hver ansatt får sitt eget nummer
        self.prosjekter = {}                  # Tom ordbok for prosjekter og vurdering

    def vis_info(self):
        print(f"{self.nummer}:\t{self.navn} {self.etternavn}\n")

        if len(self.prosjekter) == 0:
            print("\tIngen prosjekter eller vurderinger er lagt til")
        else:
            for prosjekt in self.prosjekter:
                print(f"\t{prosjekt}:\t\t{self.prosjekter[prosjekt]}")

            # Bruker self til å kalle på beregn_snitt-metoden
            print(f"\tGjennomsnitt:\t{self.beregn_snitt()}")

        print("-" * 50)

    def legg_til_prosjekt(self, prosjekt, vurdering):
        self.prosjekter[prosjekt] = vurdering  # Legger til prosjekt og vurdering i ordboka

    def beregn_snitt(self):
        total = 0
        for prosjekt in self.prosjekter:
            total += self.prosjekter[prosjekt]  # Summerer alle vurderingene

        return total / len(self.prosjekter)     # Returnerer gjennomsnittet