#splitandjoin.py
# Her skal vi splitte og sette sammen tekst basert på brukerens valg

# Ber brukeren om input
tekst = input('Skriv... NOE... hva som helst... og gi det litt lengde, ok? Be a aman... :P : ')

# Spør etter tegn til bruk for splitt
split_tegn = input('Du vet alt det du skrev inn nå... se om du klarer å huske EN av de tegnene? ')

# Vi splitter strengen
deler = tekst.split(split_tegn)

# Ber om nytt tegn for å sette sammen strengen igjen
join_tegn = input("Hvilket tegn vil du bruke for å sette den sammen igjen, tenk føst... så skriv? ")

# Setter sammen listen til en ny streng
ny_streng = join_tegn.join(deler)

# Skriver ut resultatet
print("\nResultat:")
print(ny_streng)

# UNDER HER ER OUTPUT FOR DETTE SCRIPT:
# Skriv... NOE... hva som helst... og gi det litt lengde, ok? Be a aman... :P :
# Ja... jeg kan skrive noe jeg, men jeg er ikke så ille sikker på at det kommer til å ha noen efekt på noe som helst. ;)
#Du vet alt det du skrev inn nå... se om du klarer å huske EN av de tegnene? g
#Hvilket tegn vil du bruke for å sette den sammen igjen, tenk føst... så skriv? e

#Resultat:
#Ja... jee kan skrive noe jee, men jee er ikke så ille sikker på at det kommer til å ha noen efekt på noe som helst. ;)