# rektangel_administrator.py

from rektangel_modul import Rektangel   # Importerer Rektangel-klassen fra egen modul

rektangler = []  # Liste som skal holde på alle rektangel-objekter brukeren lager

print("Velkommen til Rektangel-Generatore")  # Litt flair for interaktiv moro

while True:
    try:
        # Samler inn brukerinput og konverterer til riktig datatype
        print("\nVi skal tegne et rektangel laget av tegn:")
        lengde = int(input("Oppgi tegn-lengde: "))       # Lengde i antall tegn
        bredde = int(input("Oppgi tegn-bredde: "))       # Bredde i antall linjer
        tegn = input("Oppgi visningstegn (f.eks. * eller #): ")  # Hvilket tegn skal brukes

        # Lager nytt rektangel-objekt og legger det til i listen
        nytt_rektangel = Rektangel(lengde, bredde, tegn)
        rektangler.append(nytt_rektangel)

        # Spør brukeren om man vil fortsette
        fortsette = input("Vil du legge til et nytt rektangel? (j/n): ").strip().lower()
        if fortsette != "j":
            break  # Avslutter loopen hvis brukeren ikke svarer "j"
    except ValueError:
        # Fanger opp hvis brukeren skriver noe annet enn tall
        print("Ugyldig input. Prøv igjen med tall for lengde og bredde.")

# Når loopen er over – vis alle lagrede rektangler
print("\nViser alle rektangler:")
for rektangel in rektangler:
    rektangel.display()
    print("-")  # Litt separator for oversikt