#Stringsplit.py

# Vi lager en streng og lagrer den i variabelen minStreng
minStreng = 'Dette er strengen vi lagrer i minStreng.'

# Vi skriver ut strengen minStreng til skjerm
print(minStreng)

# Vi splitter strengen minStreng i en liste av ord og lagrer den i variabelen nyStreng
nyStreng = minStreng.split (" ")

# Igjen skriver vi til skjerm for å se hva denne kommandoen gjorde
print(nyStreng)

# Vi endrer det ene odret i indeks plass 3, med andre ord, ord nummer 4 i strengen.
nyStreng[3] = 'jeg'

# Vi skriver ut liste nyStreng til skjerm igjen for å se hva som har skjedd.
print(nyStreng[0], nyStreng[1], nyStreng[2], nyStreng[3], nyStreng[4], nyStreng[5], nyStreng[6])

#  Jeg bytter rekkefølgen på ett par ord.
print(nyStreng[0], nyStreng[5], nyStreng[2], nyStreng[6], nyStreng[4], nyStreng[5], nyStreng[3], nyStreng[1])

# Vi skriver dette på nytt, med alle indekser i kortere form.
print(nyStreng[0:6])

# Tester å printe til skjerm baklengs.
print(nyStreng[5:0:-1])

