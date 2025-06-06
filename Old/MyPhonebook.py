# MyPhonebook.py

# Trinn 1: Definer en ordbok/dictionary med 5 bedrifter. Legg merke til komma. Jeg har lagt inn linjebytte bare for at det skal være penere å se på.
telefonbok = {
    "Bajazzo": "+47 69266800",
    "Snap Drive": "+47 97703010",
    "Narvesen Sykehuset": "+47 69257055",
    "Norli Amdi Moss": "+47 94137705",
    "Nguyen Mobile Repair": "+47 40146820"
}

# Trinn 2: Spør brukeren om å legge til en bedrift og dens telefon nummer
ny_bedrift = input("Legg til navn på enda ett firma: ")
nytt_nummer = input(f"Legg til telefonnummer for {ny_bedrift}: ")
telefonbok[ny_bedrift] = nytt_nummer  # Legger til i ordbok/dictionary

# Trinn 3: Spør brukeren om å lete frem en bedrift fra listen
let_bedrift = input("Skriv inn navnet på bedriften du leter etter: ")

# Trinn 4: Vis telefonnummer dersom det eksisterer
if let_bedrift in telefonbok:
    print(f"Telefonnummer til {let_bedrift} is {telefonbok[let_bedrift]}")
else:
    print(f"{let_bedrift} finnes ikke i telefonboken.")

# Trinn 5: Vis frem hele telefonboken
print("\nFull telefonbok:")
for name, number in telefonbok.items():
    print(f"{name}: {number}")

# Trinn 6: Vis frem kun firma navn
print("\nFirma Navn:")
for name in telefonbok.keys():
    print(name)


