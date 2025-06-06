# myfunctions.py


def velkommen(navn):                                                    # Definerer en funksjon som tar imot et navn
    return f"Hei, {navn}! Velkommen tilbake."                           # Returnerer en personlig velkomstmelding

def kvadrat(av_tall):                                                   # Definerer en funksjon som tar imot et tall
    return av_tall ** 2                                                 # Returnerer kvadratet av tallet

def kalk_areal_trekant(grunnlinje=0, høyde=0):                          # Definerer en funksjon, og gir den variabler definert med verdi 0
    return (grunnlinje * høyde) / 2                                     # returnerer formelen vi bruker for å beregne areal


# Hvis denne filen blir kjørt direkte (ikke importert), skal vi teste funksjonene:

if __name__ == "__main__":                                              # Dette gjør at koden kun kjøres hvis fila åpnes direkte
    print(velkommen("Testperson"))                                      # Tester velkommen-funksjonen med navnet "Testperson"
    print(f"Kvadrat av 4 er {kvadrat(5)}")                              # Tester kvadrat-funksjonen med verdien 4
    print(f"Areal av trekant (10, 5): {kalk_areal_trekant(10, 5)}")     # Tester trekantareal med grunnlinje 10 og høyde 5