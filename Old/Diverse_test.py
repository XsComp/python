# Skrip for å teste oppgaver fra skolen.

#a,b = "This is", "a test"
#print(a)
#print()
#print(b)

# Dette er enda en metode

#print() #denne er bare her for å lage linje mellom oppgavene
#a,b = "This is", "my"
#print(a,b,"test")

# Neste type er denne

#print() denne er bare her for å lage linje mellom oppgavene
#a,b  = "This", "is my"
#print(a,b,"output.",sep=',')

# Hver print() lager en ny linje... bare se selv

#print() #denne er bare her for å lage linje mellom oppgavene
#print("first line")
#print("second line")

# Eller vi kan endre slik at vi kan få begge på samme linje

#print() #denne er bare her for å lage linje mellom oppgavene
#print("first line",end='')
#print("second line")

# Eller den kan brukes til å legge til forskjellige eller ekstra tegn på slutten av hver print()-setning.

#print() #denne er bare her for å lage linje mellom oppgavene
#print("Første linje",end=". En form for avslutning.\n")
#print("Andre linje", end=". En annen form for avslutning.\n")

#Nå er vi på oppgave med input

#print("Sett inn navn: ")
#a=input()
#print("Hello,", a)

#Her prøver vi på det samme som linjen over, men med færre lnjer med kode

#a=input("Sett inn ett tall: ")
#print("Hei, din IQ er", a)

# Neste test. Veldig lik den over. Jeg tester for å se om det er forkjell.

#user = input( 'Jeg heter Python. Hva heter du sexy? : ' )

# Output a string and a variable value.

#print( 'Welcome' , user )

# Bruke noe annet enn mellomrom til å separere output

#lang=input('Hva er ditt favoritt programmeringsspråk? : ')

# Output en streng, og en variabel verdi.

#print( lang , ' Is ' , ' Fun ' , sep='*', end='!\n' )

# Oppgave. output navn, etternavn, og alder.

#a=input("Hva heter du til forrnavn? : ")
#b=input("Hva heter du til etternavn? : ")
#c=input("Hvor gammel er du? : ")

#print(a, b, c)

# En test av fire verdier spurt om, gitt tilbake i en linje, og med semikolon mellom hver verdi.




# Filename - 4ValuesOutput.py

#def main():

# Ask the user to input four string values

#    Name = input("Enter full name only : ")
#    Age = input("Enter your age : ")
#    Address = input("Enter street address only : ")
#    Country = input("Enter name of Country of origin only : ")

# Print all values in one line, separated by a semicolon, with ". Output complete!" at the end

#    print(f"{Name};{Age};{Address};{Country}. Output complete!", end="")

#if __name__ == "__main__":
#    main()

# Oppgave fra boken (Python in easy steps).

#quarter = ['January', 'February', 'March' ]

#print( 'First Month :', quarter[0] )
#print( 'Second Month :', quarter[1] )
#print( 'Third Month :', quarter[2] )

#coord = [[1,2,3],[4,5,6]]

#print('\nTop Left 0,0 :', coord[0][0])
#print('Bottom Right 1,2 :', coord[1][2])

#print('\nSecond Month First Letter :', quarter[1][0])

# En test fra vårt eget materiale.

#empty_using_list = list()
#empty_list = []
#int_using_list = list([1,2,3])
#int_list = [1,2,3]

#print(empty_using_list)
#print(empty_list)
#print(int_using_list)
#print(int_list)


#int_list = [34,656,23,2,45,65,7887,45,2,334,67] # 11 ting, laveste indeks er 0, den høyeste er 10

#print("Initial list:",int_list)

# For å finne lengden på listen (antall ting i listen), bruk len() funksjonen

#print("Length of the list:",len(int_list))

# For å legge til en ting i slutten av listen, bruk listens append() funksjon.

#int_list.append(77)
#print("After append 77:",int_list)

# For å legge til en ting, ett spesifikt sted i listen, bruk listens insert() metode.  Insert() methoden
# krever en indeks der verdien skal settes inn og en verdi som skal settes inn.
# Insert skriver ikke over verdien som allerede ligger på den gjeldende indeksen. 
# Den bare øker listens innhold med 1 istedenfor, for å lage plass til den nye tingen.

#int_list.insert(2,55)
#print("After insert 55 at index 2:",int_list)

# Det er også mulig å utvide en liste ved å legge til innholdet i en helt annen liste i slutten av listen vi jobber med.
# Dette gjøre ved å bruke extend() methoden

#another_list = [45,22,11]
#int_list.extend(another_list)
#print("After extend with 45,22,11:", int_list)

# For å fjerne en ting fra en liste, kan vi kalle opp metoden remove() og gi den verdien som skal fjernes.
# Dette vil fjerne den første hendelsen av denne verdien. 

#int_list.remove(2)
#print("After remove value 2:",int_list)

# For å fjerne en spesifik ting fra en liste, bruk Python sin del() funksjon, og gi den rett indeks nummer 
# til tingen i lista

#del(int_list[5])
#print("After del index 5:",int_list)

# En annen måte å fjerne en ting fra en liste ved å bruke en indeks, men også returnere dens verdi, er å bruke pop()
# methoden. Når vi peker pop() til en indeks, vil den returnere den lagrede verdien i index, og så
# fjerne tingen fra listen

#print("Popped from index 6:",int_list.pop(6))
#print("After pop index 6:",int_list)


# Neste test fra materie.

#float_list = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1]
#print("Første liste:",float_list)

#  Slice/skive verdier fra indeks 3 til indeks 7, som returnerer verdier fra indeks 3 til indeks 6
#print("Skive med start 3 og stopp 7:",float_list[3:7])
#  Skive verdier fra indeks 3 til 7 med 2 i step
#print("Skive med start 3 og stopp 7, med 2 i step:",float_list[3:7:2])


# Mer liste laging fra materie

#flyt_liste = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1]
#print("Første liste:",flyt_liste)

# Skive med alle verdier, starter med indeks 3. Legg merke til inkluderingen av kolon. Uten dette ville det simpelthen vært det samme som en vanlig indeks av 3, ikke en skive.
#print("Skive med start på 3",flyt_liste[3:])

# Skive alle verdier stopper på indeks 7.  Legg merke til inkluderingen av kolon. Ellers ville dette vært en vanlig indeks av 7, ikke en skive.
#print("Skive med en stopp på 7",flyt_liste[:7])

# En liste har også metoder som tillater en å finne spesifikke verdier, eller telle dem.

#start_liste = [34,656,23,2,45,65,7887,45,2,334,67]
#print("Start liste:",start_liste)

# For å finne første gangen en verdi dukker opp i en liste, bruker vi index() methoden og gir den en verdi
# å lete etter

#print("Den første indeks med verdi 2:",start_liste.index(2))

# For å finne antall ganger verdien dukker opp i listen, bruk count() methoden og gi den
# verdien vi ønsker å telle
#print("Antall gangen nummeret 2 dukker opp i listen:", start_liste.count(2))


# Så til sist, en metode å sortere innhold, eller reversere i sekvens.

#str_list = ["hund","fulg","elg","laks","katt","esel"]
#print("Start liste:", str_list)

# For å sortere tingene i en liste, bruker vi sort() metoden for lister
#str_list.sort()
#print("Sortert liste:",str_list)

# For å reversere rekkefølgen på tingene i listen, bruker vi reverse() metoden for lister
#str_list.reverse()
#print("Reversert liste:", str_list)

# Fra boken "Python in easy steps".
#Vi lager to lister

#kurv = [ 'Eple' , 'Brød' , 'Cola' ]
#eske = [ 'Egg' , 'Fiken' , 'Drue' ]

#Nå legger vi til uttrykk for å vise innholdet i listene, og deres lengde

#print( 'Kurv Liste:' , kurv )
#print( 'Kurv Elements:' , len( kurv ) )

# Vi legger til ting i liten og viser innhold. Vi fjerner så det siste elementet, og viser listen igjen

#kurv.append( 'Biff' )
#print( 'Legge til:' , kurv )
#print( 'Siste ting fjernet:' , kurv.pop() )
#print( 'Kurv Liste:' , kurv )

# Til slutt, bruk uttrykk for å legge til alle elementene i den andre listen til den føste, og vise det. Så fjerne elementer og vise liste igjen

#kurv.extend( eske )
#print( 'Utvidet:' , kurv )
#del kurv[1]
#print( 'Ting Fjernet:' , kurv )
#del kurv[1:3]
#print( 'Bit Fjernet:' , kurv )



# Trinn 1: Declare two empty lists
#HandelisteN = []
#HandelisteS = []

# Trinn 2: Fyll inn listen med to verdier bestemt av bruker
#HandelisteN.append(input("Vare 1 vi kjøper i Norge: "))
#HandelisteN.append(input("Vare 2 vi kjøper i Norge: "))

# Trinn 3: Fyll inn den andre listen med tre bruker verdier
#HandelisteS.append(input("Ting 1 vi kjøper i Sverige: "))
#HandelisteS.append(input("Ting 2 vi kjøper i Sverige: "))
#HandelisteS.append(input("Ting 3 vi kjøper i Sverige: "))

# Trinn 4: Kombiner de to listene til en liste.
#combined = HandelisteN + HandelisteS

# Trinn 5: Fjern de andre elementet (indeks 1)
#del combined[1]

# Trinn 6: Få enda en verdi fra brukeren
#new_value = input("Putt inn en ting du ville handlet i Sverige og Norge: ")

# Trinn 7: Sette denne verdien inn i midten
#middle_index = len(combined) // 2
#combined.insert(middle_index, new_value)

# Trinn 8: Vis en bit, fra andre til fjerde element (indeks 1 til 4, Inkluderer ikke 4)
#print("Delt opp liste (2. til 4. element):", combined[1:4])

# Vis hele listem

#print(combined)



# Trinn 1: Lag en tom liste
#liste = []

# Trinn 2: Be om 5 verdier fra en bruker
#for i in range(5):
#    verdi = input(f"Sett inn verdi {i+1}: ")
#    liste.append(verdi)

# Trinn 3: Bruk join() til å skrive listen med semi-kolon separert streng
#output = ";".join(liste)
#print("Her er verdiene:", output)


#ny_tuple = (1,2,3,4,5)
#print(ny_tuple)
#print(ny_tuple[2])

#start_tuple = (1,2,3,4,5)
#print(start_tuple)
#a,b,c,d,e = start_tuple
#print(a,b,c,d,e)

#person = ("Andreas", 45, "Norway")
#navn, alder, land = person
#print(f"{navn} is {alder} years old and lives in {land}.")


# Trinn 1: Spør bruker etter tre verdier
#verdi1 = input("Hva er ditt fornavn? : ")
#verdi2 = input("Hvor gammel er du? : ")
#verdi3 = input("Hva heter byen du bor i? : ")

# Trinn 2: Tag en tuple med disse verdiene
#min_tuple = (verdi1, verdi2, verdi3)

# Trinn 3: Pakk ut tuplen inn i de separate variablene i en linje
#a, b, c = min_tuple

# Trinn 4: Vise oss resultatet
#print("Her har du dine utpakkede verdier :")
#print("a =", a)
#print("b =", b)
#print("c =", c)

# Step 4: Print all three values in one line
#print(f"Unpacked values: a = {a}, b = {b}, c = {c}")


#farge_sett = {"sort", "blå", "grønn", "oransje", "hvit"}
#print("Første sett:", farge_sett)

# Bruk add() metoden til å legge til verdier i settet
#farge_sett.add("lilla")
#print("Etter add() av lilla:",farge_sett)

# Bruk discoard() metoden til å fjerne verdier fra settet
#farge_sett.discard("grønn")
#print("Etter discard() av grønn:",farge_sett)

# Bruk intersection() metoden for å bestemme hvilken verdi som dukker opp i to sett
#andre_sett = {"oransje","blå","rød","brun"}
#print("Det andre settet:",andre_sett)
#print("Kryssningen av farge og det andre settet:", farge_sett.intersection(andre_sett))

# Bruk difference() metoden for å bestemme hvilken verdi som skal dukke opp i det første settet, men ikke i den andre
#print("Forskjellene i farge og andre sett:", farge_sett.difference(andre_sett))


# Test fra bok
# Lag en tuple, og vis innhold, lengde, og type.

#dyrepark=('Kenguru', 'Leopard', 'Elg', 'Løve', 'Zebra')
#print('Tuple:',dyrepark,'\tLengde:',len(dyrepark))
#print(type(dyrepark))

# Lag ett nytt sett og legg til ett nytt element, så print innhold, lengde og type.

#veske = { 'Rød' , 'Grønn' , 'Blå' , 'Lilla' , 'Brun'}
#veske.add( 'gul' )
#print( '\nSet:' , veske , '\tLengde' , len( veske ) )
#print( type( veske ) )

# Legg til uttrykk som søker to verdier i settet

#print('\nEr grønn i veske settet?: ' , ' Grønn '  in veske )
#print( 'Er oransje i veske settet?: ' , ' Oransje ' in veske ) 
      

# Til slutt, initializer det andre settet, og vis innhold, lengde, og alle felles verdier.

#boks = { 'Rød' , 'Lilla' , 'Gul' , 'Brun' , 'Sort'}
#print( '\nSet:' , boks , '\t\tLengde' , len( boks ) )
#print( 'Finnes i begge sett:' , veske.intersection( boks ) )


# Aktivitet. Lag to tilfeldige sett
#sett_en = {'Drage', 'Kaffe', 'Koding', 'Skygge'}
#sett_to = {'Koding', 'Lys', 'Kaffe', 'Torden'}

# Vis elementer i begge sett (intersection)
#vanlige_elemener = sett_en.intersection(sett_to)
#print("Elementer i begge sett:", vanlige_elemener)

# Elementer i sett_en men ikke i sett_to (difference)
#unik_til_en = sett_en.difference(sett_to)
#print("Elementer kun i sett_en:", unik_til_en)

# Elementer i sett_to men ikke i sett_en (difference fra det andre perspektivet)
#unik_til_to = sett_to.difference(sett_en)
#print("Elementer kun i sett_to:", unik_til_to)

#salgsperson_salg = {"Gunnar":21040,"Line":7234,"Per":9231,"Ine":15323}
#print("Dictionary:",salgsperson_salg)
#print("Salg for Per:",salgsperson_salg["Per"])
#del (salgsperson_salg["Line"])
#print("Ordbok etter sletting av Line:",salgsperson_salg)
#print("Kun nøklene:", salgsperson_salg.keys())

# Python gir oss mulighet til å bruke "in" nøkkel ordet for å sjekke om en spesifikk nøkkel finnes i ordboken. Den kommer tilbake til oss med "True" dersom ordboken inneholder nøkkelen, og "False" om den ikke gjør det.

#print("Inneholder salg for Per:", "Per" in salgsperson_salg)
#print("Inneholder salg for Line:", "Line" in salgsperson_salg)


# Lag en ordbok/dictionary

#ordb = { 'navn' : 'Erik' , 'ref' : 'Python' , 'system' : 'Windows' }
#print( 'Ordbok:' , ordb )

# Så ønsker vi å vise en verdi ved å referere nøkkel

#print( '\nReferanse:' , ordb[ 'ref' ] )

# Nå viser vi alle nøkler i ordboken

#print( '\nKeys:' , ordb.keys() )

# Vi sletter ett sett, og legger inn ett nytt før print til skjerm

#del ordb[ 'navn' ]
#ordb[ 'user' ] = 'Tor'
#print( '\nOrdbok:' , ordb )

# Til slutt, leter vi i ordboken etter en spesifikk nøkkel, og printer den til skjerm

#print( '\nFinnes det en "navn" nøkkel?:' ,'navn' in ordb )


# My personal digital toolbox (dictionary)
#toolbox = {
#    'os': 'Provides functions for interacting with the operating system.',
#    'sys': 'Access to system-specific parameters and functions.',
#    'math': 'Provides mathematical functions like sqrt, sin, and log.',
#    'random': 'For generating random numbers, choices, and shuffles.',
#    'datetime': 'Helps you work with dates and times.'
#}

# Step 1: Display the description for a specific key
#key_to_lookup = 'math'
#print(f"\nBeskrivelse av '{key_to_lookup}': {toolbox[key_to_lookup]}")

# Step 2: Remove a specific key from the dictionary
#key_to_remove = 'random'
#removed = toolbox.pop(key_to_remove)
#print(f"\n'{key_to_remove}' ble fjernet. Beskrivelse var: {removed}")

# Step 3: Display all the remaining keys
#print("\nTilgjengelige moduler i verktøykassa:")
#for key in toolbox.keys():
#    print("-", key)

# Vi lager en lang streng med tegn og lagrer i en variabel.
#strLangSetning = 'This is a sentence for Python, and it is a long sentence that is not going to say anything. We want to test if is, is going to be seen as is, or not'

#len(strLangSetning) 

# Hvilken vedi kommer opp her.
#value = "string value"
#value = 5
#value = 6.8

#print (value)

# Vi setter to verdier
#value=22
#user_value="22"

# Vi endrer variabelen value
#value=str(22)


# Vi skriver verdiene til skjerm
#print("user_value : ", user_value)
#print("value : ", value)

# Vi sjekker om de er like
#print(value == user_value)

# Vi setter verdier i variabler
#value = "AA"
#user_value = "Aa"

# Vi printer verdien av variablene til skjerm
#print("value : ", value)
#print("user_value : ", user_value)

# Vi konverterer og sammenligner verdiene
#print(value.lower() == user_value.lower())

# Vi lager en verdi, så skriver til skjerm
#value = "Jeg er en \"Python\" programmerer"
#print(value)

# Vi lager en streng-variabel, med spesialtegn.
#value=Jeg er en "Python" programmerer
#print(value)

# Tester å escape med \
#print("Dette er \"ekte\" vare")

# Tester /t tab
#print("This demonstrates a \t horizontal tab")

# Aktivitet, print tekst til skjerm med spesielle karakterer.
#print('The man said: “My name is John. What’s yours?”.')

# Vi lager to strenger, og setter dem sammen
#streng1 = 'Jeg skal sette sammen '
#streng2 = 'disse to strengene nå.'
#ny_streng = streng1+streng2
#print(ny_streng)

# Tester * symbolet for å repetere strenger
#gjennta_meg='Dette er strenger jeg ønsker å gjennta | '
#ny_streng=gjennta_meg*3
#print(ny_streng)

# På samme måte som + og * kan forekomme i samme regnestykke
# kan vi kan koble sammen og repetere i samme linje.

#ny_streng='| '+gjennta_meg*3
#print(ny_streng)

# Aktivitet. 2 X inputt satt sammen og multiplisert.
#verdi1= input("Hva er ditt forrnavn: ")
#verdi2= input("Hva er ditt etternavn: ")

# Vi setter sammen (concatenate) verdiene
#kombinert=verdi1+"\t"+verdi2

# Vi output-er resultatet 10 ganger
#for i in range(10):
#    print(kombinert)

#Teste slicing av strenger og hente ut vorskjellige deler av strengen.
#streng = 'Dette er en test av strenger i Python'

#print("Streng: ", streng)
#print("Slice fra indeks 6 til og med 9: ",streng[12:19])
#print("Slice fra indeks 6 til og med 20, hopp over 1: ",streng[6:20:2])
#print("Slice fra indeks 6 til slutten av strengen: ",streng[5:])
#print("Slice fra indeks 6 til den tredje karakteren fra slutten: ",streng[5:-3])

# Aktivitet
# Vi spør brukeren om å skrive inn en setning
#setning = input("Vær snill å skriv inn en setning: ")

# Vi spør om to integer verdier
#start_indeks = int(input("Putt inn start indeks: "))
#slutt_indeks = int(input("Putt inn en slutt-indeks: "))

# Slice setningen ved  bruke indeksene gitt fra bruker
#understreng = setning[start_indeks:slutt_indeks]

# Og til slutt, viser vi resultatet
#print("Sliced del av setningen:", understreng)


# Bare en test for å se selv
#try:
#    sentence = input("Enter a sentence: ")
#    start_index = int(input("Enter the starting index: "))
#    end_index = int(input("Enter the ending index: "))

#    substring = sentence[start_index:end_index]
#    print("Sliced part of the sentence:", substring)

#except ValueError:
#    print("You must enter valid integers for the indexes.")
#except IndexError:
#    print("The index values are out of range for the sentence.")
#except Exception as e:
#    print("An unexpected error occurred:", e)

# Enda en test
#test_streng = "Dette er min stren" 
#print("Medlemskap inklusiv \"in\":")
#print("Dette" in test_streng)
#print("Det der" in test_streng)
#print()
#print("Medlemskap ekskludert \"not in\":")
#print("Dette" not in test_streng) 
#print("Det der" not in test_streng)

# Test av in operatoren, vi ber brukeren skrive en setning
#setning = input("Vær snill å skriv en setning: ")

# Spør brukeren etter noe å lete etter
#søke_begrep = input("Sett inn ord eller setning du vil søke etter: ")

# Sjekk om det vi leter etter finnes i setningen
#if søke_begrep in setning:
#    print("Funnet!!!")
#else:
#    print("Hahaha, dust. Finnes ikke")

# Vi skriver til skjerm
#print("This is a \t string") # Vanlig oppførsel
#print(r"This is a \t string") # Tolket som en rå streng

# Vi skriver til skjerm
#print("Dette er en \t streng") # Normal oppførsel
#print(r"Dette er en \t streng") # Tolket akkurat som den er

#def min_test_funksjon():
#    Dette er en funksjon for å demonstrere bruken av en docstring. Det er her vi skriver viktig informasjon for senere utviklere.
#    return

#print(min_test_funksjon.__doc__)

#print(input.__doc__)

# Vi importerer modul fra calculatepay.py
#import calculatepay

# Vi skriver innhold i modulen til skjerm.
#for i in dir(calculatepay):
#    print(i)

# Vi skriver innhold i builtins til skjerm.
#for i in dir(calculatepay.__builtins__):
#    print(i)

# We dig further down, this time selecting the __str__ method from builtins
#for i in dir(calculatepay.__builtins__.__str__):
#    print(i)

# Vi definerer en streng, og lager en plass-holder ved bruk av {}.
#min_streng = "{} solgt {} enheter."
# Vi kaller strengens format metode, og sender så mange argumenter til
# format metoden som det finnes sett med {}. Her har vi kun brukt 2.
#print(min_streng.format("Andreas",20))

# Det samme kan gjøres på en strengliteral, uten å bruke en forhåndsdefinert variabel.
#print("Dette eksempelet krever {} argument(s).".format(1))

# En nummerert indeks legges til inni {} krøll-parentesene. Legg merke til at det er 5 set med {}, mens høyeste indeks er 3.
# Dette betyr at selv om det er 5 ting å erstatte, så trenger format metoden kun motta 4 argumenter
# Argumentet på indeks 2 blir brukt 2 ganger.
#min_streng = "{0} bygde {1} stoler. {2} malte {3} skap. {2} var den beste håndverkeren."

#personnr_1 = "Thormod"
#personnr_2 = "Marianne"
#salg_først = 10
#salg_andre = 20

# Tolken ser på listen med argumenter og tildeler dem i forhold til deres indeks i listen med
# argumenter som plass-holderen i strengen.
# Indeksene for argumentene er som følger:
# 0: personnr_1
# 1: personnr_2
# 2: personnr_2 - vil bli brukt to ganger i følge strengen
# 3: salg_andre
#print(min_streng.format(personnr_1, salg_først, personnr_2, salg_andre))


#print("f:  {0:f}".format(50.4756))
#print(".2f:  {0:.2f}".format(50.4756))
#print(".6f:  {0:.6f}".format(50.4756))
#print("e:  {0:e}".format(50.4756))
#print("b:  {0:b}".format(231))
#print("o:  {0:o}".format(231))
#print("x:  {0:x}".format(231))
#print("X:  {0:X}".format(231))

# Fra boken "Python in easy steps".
# Vi starter med å definere en variabel, med en formatert streng.
#matbit='{} og {}'.format('Pizza', 'Fisk')

# Vi skriver ut variabelen til skjerm
#print('\nErstattet:' , matbit)

# Så tildeler en streng variabe med ett annet format til variabelen
#matbit='{1} og {0}'.format('Pizza', 'Fisk')

# Vi skriver ut variabelen til skjerm igjen for å se forskjellen.
#print('\nErstattet:' , matbit)

# Igjen med ett nytt format
#matbit='%s og %s' % ('Pizza', 'Fisk')

# Til slutt, skriver vi ut variabelen til skjerm igjen for å se forskjellen.
#print( '\nErstattet:', matbit)


# Be brukeren om informasjon
#fornavn = input("Skriv inn fornavn: ")
#etternavn = input("Skriv inn etternavn: ")
#alder = int(input("Skriv inn alder: "))
#bank_saldo = float(input("Skriv inn banksaldo: "))

# Formater og skriv ut resultatet
#print("%s %s (%d): %.2f" % (fornavn, etternavn, alder, bank_saldo))

# Vi lager en streng, og lagrer i en variabel
#strengen= "du må ikke tåle så inderlig vel den urett som ikke rammer deg selv. - Arnulf Øvreland."

# Vi skriver variabel til skjerm
#print("Original: ", strengen)

# capitalize() endrer den første bokstaven slik at den blir stor
#print("capitalize(): ", strengen.capitalize())

# title() Endrer første bokstaven i alle ord til stor bokstav
#print("title(): ", strengen.title())

# upper() endrer alle bokstaver til store bokstaver
#print("upper(): ", strengen.upper())

# lower() endrer alle bokstaver til små bokstaver
#print("lower(): ", strengen.lower())

# swapcase() bytter store bokstaver til små, og små til store.
#print("swapcase(): ", strengen.swapcase())

# Be om input fra bruker
#settning = input("Vær snill å skrive inn en setninv: ")

# Så konverterer vi store og små bokstaver
#storebokstaver = settning.upper()
#småbokstaver = settning.lower()
#tittelstor = settning.title()
#bytteut = settning.swapcase()  # Bonus!

# Så var det på tide å skrive til skjerm
#print("\nFormatted Output:")
#print(f"UPPERCASE   : {storebokstaver}")
#print(f"lowercase   : {småbokstaver}")
#print(f"Title Case  : {tittelstor}")
#print(f"Swap Case   : {bytteut}")


# Lager en variabel med en streng-verdi
#input_streng = "Dette er strenger vi ønsker å splitte opp i Python. Med is i magen kan vi se hvordan split() fungerer."

# Vi skriver ut strengen til skjerm i forsjkellige former
#print("Original streng: " )
#print(input_streng)
#print()

#resultat_en = input_streng.split()
#print("Standar splitt (på mellomrom): ")
#print(resultat_en)
#print()

#resultat_to = input_streng.split("i")
#print("Splitt på i: ")
#print(resultat_to)
#print()

#resultat_tre = input_streng.split("is")
#print("Splitt på is: ")
# Legg merke til at dette gir oss ett "whitespace element" siden den var omringet av ti 'is' strenger
#print(resultat_tre)


# Setningssplitter T1000 – En Python-snutt som splitter setninger etter ønsket tegn

# Henter inn en setning fra brukeren
#setning = input("Skriv inn en setning du vil splitte: ")

# Henter inn et tegn (mellomrom, komma, bindestrek eller lignende) som skal brukes til å splitte setningen
#tegn = input("Hvilket tegn vil du splitte setningen på? (tegn eller bokstav) ")

# Splitter setningen basert på tegnet brukeren oppga
#deler = setning.split(tegn)

# Skriver ut resultatet av splitten på en pen måte
#print("\n🔍 Resultat etter splitting:")
#for i, delsetning in enumerate(deler, start=1):
#    print(f"Del {i}: {delsetning}")

# Bonus: Vi teller opp hvor mange deler vi fikk, fordi vi kan.
#print(f"\n📊 Antall deler: {len(deler)}")


# Vi tester fjerning av blanktegn. Vi starter med å lage en streng, og putter den i en variabel.
# # Vi skriver original til skjerm for sammenligning.
#streng='   a string with horizontal whitespace   '
#print('Original: ', streng)

# lstrip() fjerner blanktegn fra venstre side (starten av setningen)
#print('lstrip(): ', streng.lstrip())

# rstrip() fjerner blanktegn fra slutten av setningen
#print('rstrip(): ', streng.rstrip())

# strip() Fjerner blanktegn fra både venstre og høyre side av setningen (staren og slutten)
#print('strip(): ', streng.strip())


# Be bruker om en setning. Husk at vi ternger blanktegn i starten og/eller slutten av strengen.
#setning = input("Skriv en setning, ikke vær redd for å trykke knappen \"SPACE\" masse både før og etter setningen: ")

# Vi skriver ut setning for sammenligning
#print('Original setning:', setning)

# Så fjerner vi blanktegn før og etter setningen 
#renset = setning.strip()

# Resultat takk...
#print("Setning renset for blanktegn:", renset)


# Vi ber om input fra bruker
#input_bruker = "Kjære MOTTAKER, Vær snill å ta godt vare på vedlagt sjekk, den er for en verdi av SUM. Med Vennligst Hilsen, SENDER"

# Vi skriver til skjerm for sammenligning
#print('Original teks for sammenligning:')
#print(input_bruker)
#print()

# Vi erstatter de delene med store bokstaver
#input_bruker = input_bruker.replace("MOTTAKER", "Andreas")
#input_bruker = input_bruker.replace("SUM", "NOK 30000000.00")
#input_bruker = input_bruker.replace("SENDER", "Management")

# Og vi printer til skjerm
#print('Tekst etter erstattninger:')
#print(input_bruker)


# 🐍 En liten tekstgenerator hvor vi bruker .replace() for å fylle inn manglende ord
# Ideen: Vi starter med en mal, og bytter ut nøkkelord med det brukeren skriver inn

# Vi lager først malen
#mal = (
#    "Kjære <<TITTEL>> <<ETTERNAVN>>,\n\n"
#    "Mitt navn er <<PRINSENAVN>>, og jeg er den <<ROLLE>> i <<LAND>>. "
#    "Jeg kontakter deg angående en utestående arv på hele <<BELØP>>.\n\n"
#    "For å sikre overføringen trenger vi kun din <<INFO>>. "
#    "Vennligst svar innen <<DAGER>> dager.\n\n"
#    "Med vennlig hilsen,\n"
#    "Prins <<PRINSENAVN>>"
#)

# Vi spør brukeren om input til alle feltene vi trenger å erstatte
#tittel = input("Tittel (f.eks. Hr., Fr., Dr.): ")
#etternavn = input("Etternavn: ")
#prinsenavn = input("Navn på prinsen: ")
#rolle = input("Hva slags rolle har prinsen? (f.eks. arving): ")
#land = input("Navn på et land: ")
#beløp = input("Beløp på arven (f.eks. 5 millioner USD): ")
#info = input("Hva trenger vi fra 'offeret'? (f.eks. kontonummer): ")
#dager = input("Antall dager til svarfrist: ")

# Vi bruker .replace() til å erstatte hvert sted i malen
#epost = mal.replace("<<TITTEL>>", tittel)
#epost = epost.replace("<<ETTERNAVN>>", etternavn)
#epost = epost.replace("<<PRINSENAVN>>", prinsenavn)
#epost = epost.replace("<<ROLLE>>", rolle)
#epost = epost.replace("<<LAND>>", land)
#epost = epost.replace("<<BELØP>>", beløp)
#epost = epost.replace("<<INFO>>", info)
#epost = epost.replace("<<DAGER>>", dager)

# Så skriver vi ut resultatet
#print("\n📨 Her er den ferdige e-posten:\n")
#print(epost)


# Vi lager variabler for senere bruk
#beskrivelse_en = 'Beskrivelse 1'
#beskrivelse_to = 'Beskrivelse 2'
#pris_en = '3456.89'
#pris_to = '563.45'

# Kolonne 1 "left justified"
# Kolonne 2 "right justified"
# Vi bruker mellomrom til padding
#print(beskrivelse_en.ljust(20," "), pris_en.rjust(10," "), sep="")
#print(beskrivelse_to.ljust(20," "), pris_to.rjust(10," "), sep="")
#print("-" * 30)
#print()

# Kolonne I "right justified"
# Kolonne 2 "left justified
# Vi bruker mellomrom til padding
#print(beskrivelse_en.rjust(20," "), pris_en.ljust(10," "), sep="")
#print(beskrivelse_to.rjust(20," "), pris_to.ljust(10," "), sep="")
#print("-" * 30)
#print()

# Kolonne 1 "left justified"
# Kolonne 2 "right justified"
# . til padding
#print(beskrivelse_en.ljust(20,"."), pris_en.rjust(10,"."), sep="")
#print(beskrivelse_to.ljust(20,"."), pris_to.rjust(10,"."), sep="")
#print("-" * 30)
#print()

# Kolonne 1 "center justified"
# Kolonne 2 "center justified"
# - til padding
#print(beskrivelse_en.center(20,"-"), pris_en.center(10,"-"), sep="")
#print(beskrivelse_to.center(20,"-"), pris_to.center(10,"-"), sep="")



# Enkelt faktura-oppsett med tekstjustering og format
# Vi lager en tittel
#print("Invoice number:".rjust(43) + "0002")

# Så lager vi en linje som skiller seksjoner
#print("-" * 47)

# Her kommer linjene våre med ting, priser blir høyre justert
#print("Item 1".ljust(40) + "{:>7.2f}".format(500.00))
#print("Item 2".ljust(40) + "{:>7.2f}".format(1200.00))

# Linje igjen
#print("-" * 47)

# Totalsum
#print("Total".ljust(40) + "{:>7.2f}".format(1700.00))

# Endelig linje
#print("-" * 47)


# Vi lager og printer en variabel og printer
#input_streng = 'en to tre fire en to tre fire en to tre fire'
#print('Input streng: ', input_streng)
#print()

# Count kan brukes til å telle antall forekomster av en delstreng
#print('Antall på en: ', input_streng.count('en'))
#print('Antall av fem: ', input_streng.count('fem'))
#print()

# find brukes til å finne indeksen til den første forekomsten av delstrengen.
#print('Indeks til en: ', input_streng.find('en'))
#print('Indeks til to: ', input_streng.find('to'))
#print('Indeks til tre: ', input_streng.find('tre'))
#print('Indeks til fire: ', input_streng.find('fire'))
#print()

# find gir oss -1 i respons dersom delstrengen ikke er å finne.
#print('Indeks til fem: ', input_streng.find('fem'))
#print()

# startswith brukes for å finne ut om delstrengen er å finne helt i starten av strengen.
#print('starter med en? ', input_streng.startswith('en'))
#print('starter med to? ', input_streng.startswith('to'))
#print('starter med tre? ', input_streng.startswith('tre'))
#print('starter med fire? ', input_streng.startswith('fire'))
#print('starter med fem? ', input_streng.startswith('fem'))
#print()

# endswith brukes for å finne ut om delstrengen er å finne helt i enden av en streng
#print('ender med en? ', input_streng.endswith('en'))
#print('ender med to? ', input_streng.endswith('to'))
#print('ender med tre? ', input_streng.endswith('tre'))
#print('ender med fire? ', input_streng.endswith('fire'))
#print('ender med fem? ', input_streng.endswith('fem'))



# Vi definerer noen teststrenger
#test_strenger = ['aaaaa', '11111', '11a11']
#print('Teststrenger: ', test_strenger)
#print()

# isalpha – Sjekker om alle tegn er bokstaver
#print('isalpha (kun bokstaver): ')
#for streng in test_strenger:
#    print(f'{streng}: {streng.isalpha()}')
#print('-' * 30)
#print()

# isnumeric – Sjekker om alle tegn er numeriske (inkl. rare talltegn fra andre språk)
#print('isnumeric (kun tall): ')
#for streng in test_strenger:
#    print(f'{streng}: {streng.isnumeric()}')
#print('-' * 30)
#print()

# isdigit – Sjekker om alle tegn er siffer (0–9)
#print('isdigit (bare siffer): ')
#for streng in test_strenger:
#    print(f'{streng}: {streng.isdigit()}')
#print('-' * 30)
#print()

# isalnum – Sjekker om alle tegn er bokstaver eller tall
#print('isalnum (bokstaver og tall):')
#for streng in test_strenger:
#    print(f'{streng}: {streng.isalnum()}')
#print('-' * 30)
#print()

# islower – Sjekker om alle tegn er små bokstaver
#print('islower (små bokstaver):')
#print('aaaaa:', 'aaaaa'.islower())
#print('BBBBB:', 'BBBBB'.islower())
#print('-' * 30)
#print()

# isupper – Sjekker om alle tegn er store bokstaver
#print('isupper (store bokstaver):')
#print('aaaaa:', 'aaaaa'.isupper())
#print('BBBBB:', 'BBBBB'.isupper())
#print('-' * 30)
#print()

# istitle – Sjekker om strengen er i tittel-format
#print('istitle (tittel-format):')
#print('is this title case?:', 'is this title case?'.istitle())
#print('Is This Title Case?:', 'Is This Title Case?'.istitle())
#print('-' * 30)
#print()

# isspace – Sjekker om strengen kun inneholder mellomrom eller whitespace-tegn
#print('isspace (kun whitespace):')
#print('a:', 'a'.isspace())
#print("'  ':", "  ".isspace())
#print(r"'\\t\\t':", "\t\t".isspace())



# Ber brukeren om input
#bruker_input = input('Skriv inn en verdi: ')

# Kjører fire ulike str-test-metoder og viser resultatet
#print('\nResultater:')

#print('Er det bare bokstaver (isalpha)?      :', bruker_input.isalpha())
#print('Er det bare tall (isdigit)?           :', bruker_input.isdigit())
#print('Er det bokstaver eller tall (isalnum)?:', bruker_input.isalnum())
#print('Er det bare mellomrom (isspace)?      :', bruker_input.isspace())


#print("Addisjon:\t", "5 + 2 =", 5 + 2)
#print("Subtrahering:\t", "5 - 2 =", 5 - 2)
#print("Multiplisering:\t", "5 * 2 =", 5 * 2)
#print("Eksponent:\t", "5 ** 2 =", 5 ** 2)
#print("Dividering:\t", "5 / 2 =", 5 / 2)
#print("Heltal division:\t", "5 // 2 =", 5 // 2)
#print("Restdivisjon eller modulo:\t\t", "5 % 2 =", 5 % 2)


# Vi lager en variabel, og skriver til skjerm
#a = 5
#print('Den originale verdien av a:\t\t ', a)

# En forenklet måte å skrive at a = a + 2
#a += 2 
#print("Adder og tildel +=:\t\t\t", "a += 2 \t", "resulterer i at a =", a)

# Vi setter verdien i a tilbake til 5
#a = 5
# En forenklet måte å skrive at a = a - 2
#a -= 2
#print("Subtrakter og tildel -=:\t\t", "a -= 2 \t", "resulterer i at a =", a)

# Vi setter verdien i a tilbake til 5
#a = 5
# En forenklet måte å skrive at a = a * 2
#a *= 2
#print("Multipliser og tildel *=:\t\t", "a *= 2 \t", "resulterer i at a =", a)

# Vi setter verdien i a tilbake til 5
#a = 5
# En forenklet måte å skrive at a = a ** 2
#a **= 2
#print("Opphøy/eksponer og tildel **=:\t\t", "a **= 2\t","resulterer i at a =", a)

# Vi setter verdien i a tilbake til 5
#a = 5
# En forenklet måte å skrive at a = a / 2
#a /= 2
#print("Divider og tildel /=:\t\t\t", "a /= 2 \t","resulterer i at a =", a)

# Vi setter verdien i a tilbake til 5
#a = 5
# En forenklet måte å skrive at a = a // 2
#a //= 2
#print("Heltall-divider og tildel //=:\t\t", "a //= 2\t","resulterer i at a =", a)

# Vi setter verdien i a tilbake til 5
#a = 5
# En forenklet måte å skrive at a = a % 2
#a %= 2
#print("Modulo/rest-divisjon og tildel %=:\t", "a %= 2 \t","resulterer i at a =", a)


# Be brukeren om et tall og lagre det i en variabel. Legg merke til at vi bruker "float" for å tillate desimaler.
# verdi1 = float(input("Skriv inn et tall: "))

# Be om en ny verdi som skal legges til
# verdi2 = float(input("Skriv inn tallet du vil legge til det forrige: "))

# Bruk add and assign operatoren (+=) for å legge til verdi2 i verdi1
# verdi1 += verdi2

# Skriv ut det nye resultatet
# print(f"Summen etter å ha lagt til er: {verdi1}")



# #  "Er lik" operatør == Sjekker om 2 verdier er like.
# print("5 == 2\t", "Er lik?\t\t\t", 5 == 2)

# #  "Er ulik" operatør != Sjekker om 2 verdier er ulike.
# print("5 != 2\t", "Er ulik?\t\t\t", 5 != 2)

# #  Større enn operatøren > sjekker om verdien til venstre er høyere enn verdien til høyre.
# print("5 > 2\t", "Er 5 større enn 2?\t\t", 5 > 2)

# #  Mindre enn operatøren < sjekker om verdien til venstre er mindre enn vedrien til høyre.
# print("5 < 2\t", "Er 2 større enn 5?\t\t", 5 < 2)

# #  Større enn eller er lik operatøren >= sjekker om verdien til venstre er større enn eller lik den til høyre.
# print("5 >= 2\t", "5 er større enn eller lik 2?\t", 5 >= 2)

# #  Mindre enn eller er lik operatøren <= sjekker om verdien til venstre er mindre enn eller lik den til høyre.
# print("5 <= 2\t", "5 er mindre enn eller lik 2?\t", 5 <= 2)

# print("'2' == 'a'\t", "gir oss\t", '2' == 'a')
# print("'2' != 'a'\t", "gir oss\t", '2' != 'a')
# print("'2' > 'a'\t", "gir oss\t", '2' > 'a')
# print("'2' < 'a'\t", "gir oss\t", '2' < 'a')
# print("'2' >= 'a'\t", "gir oss\t", '2' >= 'a')
# print("'2' <= 'a'\t", "gir oss\t", '2' <= 'a')

# Vi tildeler verdier til 2 variabler vi skal bruke i regnestykket senere.
# a = 100
# b = 50
# print("'a == b+b\t", "Er lik?\t\t", a==b+b)


# Dette skriptet demonstrerer forskjellen mellom tildeling (=) og sammenligning (==)

# Vi tildeler verdier til to variabler
# a = 100    # Her bruker vi = for å tildele 100 til variabelen a
# b = 50     # Vi tildeler 50 til variabelen b

# # Vi bruker == for å sammenligne verdiene
# # Dette sjekker: Er a lik summen av b + b?
# print("a == b + b\t", "Er lik?\t", a == b + b)

# # Vi legger til et ekstra eksempel for klarhet
# c = 200
# d = 100

# print("c == d\t\t", "Er lik?\t", c == d)  # Dette vil gi False

# # Og vi kan også skrive ut verdiene for referanse
# print("\nVerdier:")
# print("a =", a)
# print("b =", b)
# print("c =", c)
# print("d =", d)

# a = True
# b = False
# print("Verdien av a er:", a)
# print("Verdien av b er:", b)
# print("NOT a:", "vi inverterer a med not, som gir oss:", "a =",not a) # not a, sier, inverter verdien av a
# print("NOT b:", "vi inverterer b med not, som gir oss:", "b =",not b) # not b, sier, inverter verdien av b


# # I theorien
# print("True og True =", True and True)
# print("True og False =", True and False)
# print("False og True =", False and True)
# print("False og False =", False and False)
# print()

# # I praksis
# print("(5 > 2) og (3 > 2) =", (5 > 2) and (3 > 2))
# print("(5 > 2) og (3 < 2) =", (5 > 2) and (3 < 2))
# print("(5 < 2) og (3 > 2) =", (5 < 2) and (3 > 2))
# print("(5 < 2) og (3 < 2) =", (5 < 2) and (3 < 2))



# # I theorien
# print("Sann eller sann =", True or True)
# print("Sann eller usann =", True or False)
# print("Usann eller sann =", False or True)
# print("Usann eller usann =", False or False)
# print()

# # I praksis
# print("(5 > 2) eller (3 > 2) =", (5 > 2) or (3 > 2))
# print("(5 > 2) eller (3 < 2) =", (5 > 2) or (3 < 2))
# print("(5 < 2) eller (3 > 2) =", (5 < 2) or (3 > 2))
# print("(5 < 2) eller (3 < 2) =", (5 < 2) or (3 < 2))




# if utrykk som skal evalueres:
# En mengde med kode: Handling å ta når evalueringen blir: True

# a = 5
# b = 2

# if a * b > 9:  # Legg merke til at utrykket ender med en -> : (også kalt kolon)
#     print("a * b (", a * b, ") er større enn 9") # Igjen, legg merke til innrykket i starten av linjen



# # Vi setter noen variabler, og skriver dem til skjerm
# a = 5
# b = 2
# print("Vi har satt to verdier. a =", a, "og b =", b)
# print()

# print("if evalueres til å være sann, og det er innrykk i andre linje:")
# if a * b > 9:
#     print("a * b (", a * b, ") er større enn 9")
#     print("Denne linjen vil kun skrive til skjerm dersom vi får tilbake True")

# print() # Bare ett mellomrom i linjeskift

# print("if evalueres til å være usann og det er innrykk i andre linje:")
# if a * b < 9:
#     print("a * b (", a * b, ") er større enn 9") # Legg merke til at dette ikke skrives til skjerm
#     print("Denne linjen vil kun skrive til skjerm dersom vi får tilbake True") # Legg merke til at dette ikke skrives til skjerm

# print()

# print("if evalueres til å være sann, og det er ikke innrykk i andre linje:")
# if a * b > 9:
#     print("a * b (", a * b, ") er større enn 9") # Dette skrives til skjerm
# print("Denne linjen vil kun skrive til skjerm dersom vi får tilbake True") # Rett før dette (dette ville printet uansett grunnet manglende innrykk)

# print()

# print("if evalueres til å være usann og det er ikke innrykk i andre linje")
# if a * b < 9:
#     print("a * b (", a * b, ") er mindre enn 9") # Dette skrives ikke til skjerm
# print("Denne linjen vil kun skrive til skjerm dersom vi får tilbake True") # Dette skal ikke skrives til skjerm, men fordi det ikke er innrykk.....


# # Vi definerer en variabel som forteller hvor mye drivstoff vi har
# drivstoff = 10

# if drivstoff > 10:
#     print("Keep on truckin'.")
# else:
#     print("For tung gasspedal, stopp og fyll tanken.")


# # Setter drivstoff variabel nivå
# drivstoff = 15

# if drivstoff > 20:                                                      # Her sier vi at hvis drivstoffnivået er på 20,
#     print("Kjør som ett oljet lyn.")                                    # så kan vi kjøre fort
# elif drivstoff > 10:                                                    # Men hvis nivået bare er 10,
#     print("Kjør økonomisk.")                                            # Så må vi kjøre sakte.
# else:                                                                   # Er nivået enda lavere
#     print("Håper du husket kortet, du trenger drivstoff.")              # Så må vi stoppe og fylle tanken.



# # Setter drivstoff variabel nivå
# drivstoff = 15

# if drivstoff > 20:                          # Her sier vi at hvis drivstoffnivået er på 20,
#     print("Kjør som ett oljet lyn.")        # så kan vi kjøre fort
# else:                                        # Men hvis nivået bare er 10.
#     if drivstoff > 10:                      # Så må vi kjøre sakte.
#         print("Kjør økonomisk.")            # Så må vi kjøre sakte.
#     else:                                   # Er nivået enda lavere
#         print("Håper du husket kortet, du trenger drivstoff.")  # Så må vi stoppe og fylle tanken.


# Beskrivelse: Vurderer prestasjonen basert på en verdi gitt av brukeren

# # Be brukeren om å skrive inn en verdi (vi bruker float, tilfelle bruker er vanskelig)
# verdi = float(input("Skriv inn poengsummen din (0-100): "))

# # Bruk if-elif-else for å vurdere prestasjonen
# if verdi > 90:
#     print("Utmerket prestasjon!")
# elif verdi < 40:
#     print("Prøv hardere nestegang")
# else:
#     print("Meh... ok. Men ikke bra.")


# # Dersom vi ønsker å sikre verdier innenfor ett område:

# verdi = float(input("Skriv inn poengsummen din (0-100): "))

# if verdi < 0 or verdi > 100:
#     print("Ugyldig poengsum. Poeng må være mellom 0 og 100.")
# elif verdi > 90:
#     print("Utmerket prestasjon!")
# elif verdi < 40:
#     print("Prøv hardere nestegang")
# else:
#     print("Meh... ok. Men ikke bra.")


# #Vi bestemmer variabler, og skriver til skjerm
# a = 10
# b = 15
# print("Vi har satt a = 10, og b = 15")
# print()

# print("Vi spør, er a større enn b?")
# print("a er større") if (a > b) else print("b er større")
# print()

# # or

# print("Vi sier, hvis a en minre enn b, print 5 til skjerm")
# c = 5 if (a < b) else 20
# print(c)


# print(type(3))
# print(type(7.6))
# print(type("Hello"))
# print(type(input("Please enter a value:")))



# a = "50"

# # isinstance blir tildelt verdien den skal teste, og data typen den skal testes mot.
# if isinstance(a,int):
#     print("a er en integer")
# elif isinstance(a,float):
#     print("a er ett flyt-nummer")
# elif isinstance(a,str):
#     print("a er en streng")


# # Vi lager en variabel med en flyttall-verdi
# a = 30.675
# print("Verdien av a er",a,"og er av typen", type(a))
# print("Casting a til integer ved å bruke a = int(a)")
# a = int(a)
# print()
# print("Verdien av a er", a, "og er av typen", type(a))
# print("casting til flyt-nummer ved å bruke = float(a)")
# a = float(a)
# print()
# print("Verdien av a er", a, "og er av typen", type(a))
# print("casting til streng ved å bruke = str(a)")
# a = str(a)
# print()
# print("Verdien av a er", a, "og er av typen", type(a))


# denne laget jeg selv, se neste.
# Write a script that requests a value from the user. Output its type. Now, cast it to another type of your choosing and output the type again.
# Vi ber brukeren gi oss en tall verdi, og lagrer den i en variabel, og skriver til skjerm
# brukernummer = input("Vær snill å sett inn numerisk verdi: ")
# print(brukernummer)
# print()

# brukernummer = float(brukernummer) # Vi konverterer til flyttall
# print("Vi har konvertert til flyttall:", brukernummer)

# # Ny og forbedret versjon etter ChatGPT fikk kloa i det. Tok det med for å vise en mer pedagogisk versjon.
# # Beskrivelse: Finner og viser type før og etter typekonvertering

# # Vi ber brukeren gi oss en tallverdi (som tekst til å begynne med)
# brukernummer = input("Vær snill å skriv inn en numerisk verdi: ")

# # Vi skriver verdien og hvilken datatype den har
# print("\nDu skrev inn:", brukernummer)
# print("Type før konvertering:", type(brukernummer))

# # Vi konverterer til flyttall (float)
# brukernummer = float(brukernummer)

# # Vi viser verdien og ny type etter konvertering
# print("\nEtter konvertering til float:")
# print("Verdi:", brukernummer)
# print("Type etter konvertering:", type(brukernummer))

# # Vi konverterer til integer (int)
# brukernummer = int(brukernummer)

# # Vi viser verdien og ny type etter konvertering
# print("\nEtter konvertering til integer:")
# print("Verdi:", brukernummer)
# print("Type etter konvertering:", type(brukernummer))

# # Vi konverterer tilbake til streng (str)
# brukernummer = str(brukernummer)
# print("\nEtter konvertering tilbake til streng:")
# print("Verdi:", brukernummer)
# print("Type etter konvertering:", type(brukernummer))

# # Bonus: Konverter til bool for moro skyld
# brukernummer_bool = bool(brukernummer)
# print("\nKonvertert til bool (sannhetsverdi):", brukernummer_bool)


# username = input("Please enter your username")
# password = input("Please enter your password")

# if (username == "student"):
#     if (password == "noroff"):
#         print("You have been logged in")
#     else:
#         print("The password is not correct")
# else:
#     print("The username is not correct")

# # Vi ber bruker skrive inn navnet på sin avdeling, og lagrer i var
# avdeling = input("Skriv inn avdelingen du hører til: ")

# # Vi tester om det bruker skriver inn stemmer med det som gir tilgang
# if (avdeling == "IT") or (avdeling == "Networking"):
#     print("Du har tilgang!")
# else:
#     print("Velkommen skulle du vært, men du har ikke tilgang...")



# # Beskrivelse: Utfører en boolsk AND-operasjon på to binære verdier fra brukeren

# def hent_binær_input(prompt):
#     while True:
#         verdi = input(prompt)
#         if verdi in ("0", "1"):
#             return int(verdi)
#         else:
#             print("Ugyldig input. Skriv inn kun 0 eller 1.")

# def main():
#     print("Vår logiske PLC (PLS) \"AND\" kalkulator!")

#     bin1 = hent_binær_input("Skriv inn 0 eller 1: ")
#     bin2 = hent_binær_input("Skriv inn 0 eller 1 igjen: ")

#     resultat = bin1 & bin2

#     print(f"\nResultat av AND mellom {bin1} og {bin2} er: {resultat}")

# # Kjør hovedfunksjonen kun hvis skriptet kjøres direkte
# if __name__ == "__main__":
#     main()



# # Beskrivelse: En enkel arbeidstidsvakt som sjekker om et gitt klokkeslett er innenfor arbeidstidene
# from datetime import datetime

# def main():
#     print("Velkommen til arbeidstidsvakten 3000™")

#     # Loop for å sikre korrekt tid
#     while True:
#         bruker_tid = input("Skriv inn klokkeslett i 24-timersformat (hh:mm). Ikke klem : mellom tallene: ")

#         try:
#             tid = datetime.strptime(bruker_tid, "%H:%M").time()
#             break  # Gyldig tid – vi bryter loopen
#         except ValueError:
#             print("Tosk, du skrev inn tid på feil format! Prøv igjen med HH:MM, som f.eks. 08:45 eller 20:15.")

#     # Definer arbeidstidene
#     start_tid = datetime.strptime("08:00", "%H:%M").time()
#     slutt_tid = datetime.strptime("17:00", "%H:%M").time()

#     # Sjekk om det er innenfor arbeidstid
#     if start_tid <= tid <= slutt_tid:
#         print("Det er fortsatt arbeidstid.")
#         print("Tilbake til jobb, din kontor nisse! Du har mer jobb å gjøre!")
#     else:
#         print("🌙 Det er *ikke* arbeidstid.")
#         print("Vær snill og stopp. Berør noe gress, lukt litt natur, klem et menneske. Lev livet ditt for pokker.")
#         print("Eller... Kjøp deg en is... det burde kurere den værste arbeidslyst...")

# if __name__ == "__main__":
#     main()


# # Aktivitet test fra studie
# print("1. Print the first menu option")
# print("2. Print the second menu option")
# print("3. Print the third menu option")
# print("4. Print the fourth menu option")
# print("")

# menuSelection = input("Please select a menu option : ")

# if (menuSelection == "1"):
#     print("The first option was selected")
# else:
#     print("Another option was selected ")


# Ny test fra boken
# try:
#     print("1. Print the first menu option")
#     print("2. Print the second menu option")
#     print("3. Print the third menu option")
#     print("4. Print the fourth menu option")
#     print("")

#     menuSelection = int(input("Please select a menu option : "))

#     if (menuSelection == 1):
#         print("The first option was selected")
#     elif (menuSelection == 2):
#         print("The second option was selected")
#     elif (menuSelection == 3):
#         print("The third option was selected")
#     elif (menuSelection == 4):
#         print("The fourth option was selected")
#     else:
#         print("An invalid selection was used by the end user")

# except:
#     print("Please enter a value between 1 and 4")


# total = 0

# print("if statement output:\n")

# if total < 5:
#     print("Total:",total)
#     total += 1

# total = 0

# print("\nwhile statement output:\n")

# while total < 99999999:
#     print("Total:",total)
#     total += 1



# user_choice = input("Enter q to exit or another key to continue: ")

# while user_choice != "q":
#     print("The user entered:",user_choice)
#     user_choice = input("Enter q to exit or another key to continue: ")

# print("\nThe user quit the loop.")

# utside_teller = 0

# while utside_teller < 3:
#     innside_teller = 0
#     while innside_teller < 3:
#         print("Utside teller:",utside_teller,"Innside teller:",innside_teller)
#         innside_teller+=1
#     utside_teller+=1


# a , b = 0 , 1
# while b<1000:
#     print(b)
#     a,b=b,a+b


# def main():
#     totalt_bestemt = 0
#     totalt_ubestemt = 0

#     print("Første del: Her skal du skrive inn 5 hel-tall.")
#     for i in range(5):
#         try:
#             verdi = float(input(f"Skriv inn verdi {i+1} av 5: "))
#             totalt_bestemt += verdi
#         except ValueError:
#             print("Ikke gyldig tall. Hopper over dette forsøket.")

#     print("\nAndre del: Skriv inn tall, kun negativt tall vil avslutte.")
#     while True:
#         try:
#             verdi = float(input("Skriv inn et tall: "))
#             if verdi < 0:
#                 break
#             totalt_ubestemt += verdi
#         except ValueError:
#             print("Ikke gyldig tall. Prøv igjen.")

#     print("\nResultat:")
#     print(f"Totalt fra første loop (5 tall): {totalt_bestemt}")
#     print(f"Totalt fra andre loop (til negativt tall): {totalt_ubestemt}")

# if __name__ == "__main__":
#     main()



# # Test fra stoffet
# # Vi starter med å lage lister, lagret i variabler
# måneder = ("Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember")
# antall_salg = [45,59,34,64,23,45,76,32,12,45,34,102]
# klasse_størelse = {"PRG":30,"NET":40,"NIX":37,"PRH":32,"NEU":46,"NIY":65,"PRI":15,"NEV":44,"NIZ":27,"PRJ":33,"NEW":66,"NIA":17}

# # Enkel iterasjon over en streng. Husk, var måneder er lagret med strenger
# for item in måneder:
#     print(item, end=" ")

# print()

# # Enkel iterasjon over integere
# for item in antall_salg:
#     print(item, end=" ")

# print()

# # Enkel iterasjon over en streng.. Dette er bare en liste med karakterer, og kan itereres over.
# for item in "The string":
#     print(item, end=" ")

# print()

#  # enumerate() tillater elementer i en data strultur å bli listet sammen med dens indeks nummer. Kjekt hvis man trenger å referere til en indeks.
# for item in enumerate(måneder):
#     print(item, end=" ")

# print()

#  # zip() tillater elementer fra flere data strukturer å bli iterert samtidig.
# for item in zip(måneder , antall_salg):
#     print(item, end=" ")

# print()

#  # Bruk "key", og "value" kombinasjoner for å iterere igjennom en ordboks (dictionary) items()
# for key, value in klasse_størelse.items():
#     print(key, ": ", value,sep="")

# # Bruk av zip() med enumerate() samtidig for å liste måneder og salg sammen:
# for i, (måned, salg) in enumerate(zip(måneder, antall_salg), start=1):
#     print(f"{i}. {måned}: {salg} salg")


# # Når range() bare får ett tall, tolkes det som "kjør fra 0 og opp til (men ikke med) dette tallet".
# # Altså: range(10) gir 0 til 9 (totalt 10 tall).
# print("range(20)", end=":\t\t  ")
# for item in range(20):
#     print(item, end=",")


# # Når range() får to verdier, er den første startverdien og den andre stoppverdien (ikke inkludert).
# # Altså: range(1, 10) starter på 1 og går til 9.
# print("\nrange(1, 20)", end=":\t\t  ")
# for item in range(1, 20):
#     print(item, end=",")


# # Når range() får tre verdier, er den tredje "stegstørrelsen".
# # Altså: range(1, 10, 2) betyr start på 1, hopp annenhver verdi, og stopp før 10.
# print("\nrange(1, 20, 2)", end=":\t  ")
# for item in range(1, 20, 2):
#     print(item, end=",")

# def main():
#     total = 0

#     for i in range(1, 101):  # Loop from 1 to 100 (inclusive)
#         total += i

#     print(f"Totalt etter 100 runder er: {total}")

# if __name__ == "__main__":
#     main()



# def main():
#     total = 0

#     for i in range(1, 101):  # Fra 1 til 100
#         print(f"Loop {i}: total = {total} + {i} = {total + i}")
#         total += i

#     print("\n------------------------------------")
#     print(f"Totalt etter 100 runder er: {total}")

# if __name__ == "__main__":
#     main()



# # a loop that should iterate from 1 to 10
# def main():
#     for ting in range(1,11):
#         print("Ting verdi:",ting)
#         if input("Enter q to quit or any other key to continue: ") == "q":
#             break

# if __name__ == "__main__":
#      main()


# def main():
#     total = 0
#     while total < 10:
#         total += 1
#         if total % 2 == 0:
#             print(total, " is divisible by 2.")
#         else:
#             continue

# if __name__ == "__main__":
#     main()


# def main():
#     # Vi starter med å lage den ytre loopen som går fra 1 til og med 5
#     # Husk, i og j er vanlige variabler, men brukes til dette av mange. Dette fordi "alle" vet hva som er ment når de ser det.
#     # Vi demonstrerer dette her ved å bruke indi og jade
#     for indi in range(1, 6):
#         print(f"\nYtre loop - Iterasjon {indi}")

#         # Vi lager en indre løkke som også går fra 1 til og med 5
#         for jade in range(1, 6):

#             # Vi bruker continue hvis j er 3
#             # Dette betyr at vi hopper OVER resten av koden i denne iterasjonen og går rett til neste
#             if jade == 3:
#                 print(f"  Indre loop - jade er {jade}, vi bruker 'continue' og hopper til neste iterasjon.")
#                 continue

#             # Vi bruker break hvis jade er 5
#             # Dette betyr at vi avslutter hele den indre løkken (hopper helt ut av den)
#             if jade == 5:
#                 print(f"  Indre loop - jade er {jade}, vi bruker 'break' og avslutter hele den indre loopen.")
#                 break

#             # Hvis ingen av de over er sanne, skriver vi ut j-verdien
#             print(f"  Indre loop - jade er {jade}, normal iterasjon.")

#     print("\nFerdig med alle looper.")

# if __name__ == "__main__":
#     main()



# # CalculateTotal.py
# # Vi bruker en for-løkke til å skrive ut tallene fra 1 til 10.
# # Her bruker vi 'indi' i stedet for den klassiske 'i' – husk, det er bare et navn på en variabel.
# def main():
#     for indi in range(1, 11):
#         print(f"Dette er tall: {indi}")

# if __name__ == "__main__":
#     main()



# # PrintPerfect.py
# # Vi lager en total-variabel og bruker en for-løkke til å summere tallene fra 1 til 100
# # Her bruker vi 'indi' som løkkevariabel igjen – helt vanlig navn i våre kreative Python-eventyr
# def main():
#     print()
#     total = 0

#     for indi in range(1, 101):
#         total += indi  # Legg til nåværende tall i totalen

#     print(f"Summen av tallene fra 1 til 100 er: {total}")

# if __name__ == "__main__":
#     main()



# # PostalCodes.py
# # Vi demonstrerer hvordan break og continue fungerer i en nøstet loop (loop inni loop)
# # i brukes som teller for den ytre loop
# # j brukes som teller for den indre loop
# def main():
#     for i in range(1, 4):  # Går fra 1 til 3
#         print(f"\nYtre loop - Iterasjon {i}")

#         for j in range(1, 6):  # Går fra 1 til 5
#             if j == 3:
#                 print(f"  Indre loop - j er {j}, vi bruker 'continue' og hopper over denne iterasjonen.")
#                 continue  # Hopper til neste runde i indre loop

#             if j == 5:
#                 print(f"  Indre loop - j er {j}, vi bruker 'break' og avslutter indre loop.")
#                 break  # Avslutter indre loop helt

#             print(f"  Indre løkke - jade er {j}, normal iterasjon.")

# if __name__ == "__main__":
#     main()



# # Dette scriptet kjører en while-loop helt til brukeren skriver "X"
# # Underveis spør vi brukeren om input og gjentar til ønsket slutt

# print()
# def main():
#     while True:
#         svar = input("Skriv noe (eller skriv 'x' for å avslutte): ")

#         if svar.lower() == "x": # Legg merke til, vi konverterer til små bokstaver, hva hvis vi skriver "X" (stor X). Svar, uendelig loop.
#             print("Du valgte å avslutte. Ha det bra!")
#             break  # Avslutter loop når brukeren skriver 'exit'

#         print(f"Du skrev: {svar}")

# if __name__ == "__main__":
#     main()


# Vi lager ett skript for å vise hva som skal til for å samle en type informasjon uten funksjoner eller looper.

# pris = 70

# navn = input("Vær snill å skriv inn ditt navn:  ")
# antall = int(input("Hvor mange enheter ønsker du å kjøpe?  "))
# total = antall * pris
# print(navn,", totalen for ",antall," enheter er: ",total, sep="")
# print()

# navn = input("Vær snill å skriv inn ditt navn:  ")
# antall = int(input("Hvor mange enheter ønsker du å kjøpe?  "))
# total = antall * pris
# print(navn,", totalen for ",antall," enheter er: ",total, sep="")
# print()

# name = input("Vær snill å skriv inn ditt navn:  ")
# antall = int(input("Hvor mange enheter ønsker du å kjøpe?  "))
# total = antall * pris
# print(name,", totalen for ",antall," enheter er: ",total, sep="")


# Vi lager en funksjon for å forenkle den samme oppgaven som vist rett over her.
#Vi definerer en variabel


# def main():
#     pris = 70

#     def kalkuler_person_total():  # Funksjon header, resten er det vi kaller brødtekst, eller innhold (function body).
#         navn = input("Vær snill å skriv inn ditt navn:  ")
#         antall = int(input("Hvor mange enheter ønsker du å kjøpe?  "))
#         total = antall * pris
#         print(navn,", totalen for ",antall," enheter er: ",total, sep="")

#         # Take note of the indent. If the statements were not indented, they would not form part of the function.
#         # Similarly to what we saw with the if statement.
    
#     kalkuler_person_total()
#     print()
#     kalkuler_person_total()
#     print()
#     kalkuler_person_total()

# if __name__ == "__main__":
#      main()    


# Videre forenkling av koden over

# def main():
#     def calculate_person_total():  # Function header, the rest is the function body
#         name = input("Please enter your name:  ")
#         amount = int(input("How many items do you wish to purchase?  "))
#         total = amount * price
#         print(name,", your total for ",amount," items at ", price, " each, is: ",total, sep="")

#     price = 70

#     while (input("Type 'y' to calculate sale details: ") == 'y'):
#         calculate_person_total()

# if __name__ == "__main__":
#      main()



# # Funksjoner
# # Enda en forbedring av koden over.

# def calculate_person_total(): 
#     name = input("Please enter your name:  ")
#     amount = int(input("How many items do you wish to purchase?  "))
#     total = amount * price
#     print(name,", your total for ",amount," items is: ",total, sep="")

# # Main script
    
# price = 70

# while (input("Type 'y' to calculate a user's details:  ") == 'y'):
#     calculate_person_total()
    
# print(total) # total only exists in the function



# Vi definerer en funksjon, men variabel navn i parenteser. Disse variabel navnene blir referert til som parameterne
# til funksjonen. Alle argumenter som sendes til funksjonnen blir mottatt i parametere i samme sekvens som de sendes.
# Parameterne tjener som lokal variabel

# def main():
#     def med_et_argument(først): 
#         print("Med ett argument: først - ", først)
    
#     def med_to_argumenter(først, andre):
#         print("Med to argumenter: først - ", først, "andre - ", andre)

# # Når man kaller på en funksjon, gi like mange argumenter som funksjonen har parametere.


#     med_et_argument(10) 
#     med_to_argumenter("et",2)

# if __name__ == "__main__":
#     main()


# def main():
#     def visning(første, andre, tredje, fjerde):
#         print("først:", første)
#         print("andre:", andre)
#         print("trefje:",tredje)
#         print("fjerde:",fjerde)
    
#     print("Kallt opp i rett sekvens:")
#     visning(1,2,3,4)
#     print()
#     print("Kallt opp ved å spesifisere parameter navn:")
#     visning(andre=2,fjerde=4,tredje=3,første=1)

# if __name__ == "__main__":
#     main()


# Funksjons parametere dildeles med standard verdier. Desom ingen argumenter sendes for disse
# parameterene, vil de defaulte til disse parameterene. Dette gjør parameterene valgfrie.

# def main():
#     def vis(første=1, andre=2, tredje=3, fjerde=4):
#         print("første:", første)
#         print("andre:", andre)
#         print("tredje:",tredje)
#         print("fjerde:",fjerde)
    
#     print("Send alle argumenter:")
#     vis(1,2,3,4)
#     print()
#     print("Send ingen argumenter:")
#     vis()
#     print()
#     print("Send kun det første argumentet:")
#     vis(88) # Her kan vi legge til mer enn det første ved å skrive f.eks. vis(88,77,66) Vi vil da få tre verdier endret.
#     print()
#     print("Send det første argumentet, og ett navngitt argument:")
#     vis(88,fjerde=99)

# if __name__ == "__main__":
#     main()



# # Her leker vi litt med kode. Tester funksjoner, og hvordan vi sender argumenter til egen
# # lagede funksjoner. Vi kan spesifisere hvilke verdier som skal endres underveis.

# def main():
#     def echo(bruker,språk,system):
#         print('Bruker:',bruker,'Språk:',språk,'Plattform:',system)
#         print()

#     echo(språk='Python', system='Windows 11',bruker='Vicky')
#     echo('Levi','C#','Linux Fedora')
#     echo(språk='C++', system='Mac OS',bruker='Andy')

#     def mirror(bruker='Carola',språk='TurboCAD'): #Her lager vi standardverdier.
#         print('\nBruker:',bruker,'Språk:',språk)

#     mirror() # → Bruker: Carola, Språk: TurboCAD
#     mirror(språk='Java') # Bare språk endres
#     mirror(bruker='Tony') # Kun bruker overskrives
#     mirror('Susy','Basic') # Alle overskrives

# if __name__ == "__main__":
#      main()




# def kitten(a):
#     # Dette er starten på funksjonen. Du sender inn et tall som 'a'

#     print(f'Før endring: id(a) = {id(a)}, verdi = {a}')
#     # Vi skriver ut ID-en til objektet 'a' peker på, og verdien (f.eks. 5)
#     # 'id()' viser hvor i minnet verdien ligger

#     a += 1
#     # Dette ser ut som "endre a", men:
#     # a += 1 er det samme som a = a + 1
#     # Python lager nå et **nytt int-objekt** med verdien 6
#     # og 'a' begynner å peke på det nye objektet
#     # Originale 'a' (som pekte på 5) forlates

#     print(f'Etter endring: id(a) = {id(a)}, verdi = {a}')
#     # Nå ser vi at ID-en har endret seg, fordi 6 er et annet objekt

# def main():
#         x = 5
#         # Vi definerer en variabel x, og setter den til 5

#         print(f'Før: id(x) = {id(x)}, verdi = {x}')
#         # Skriver ut ID og verdi før vi sender x til funksjonen

#         kitten(x)
#         # Vi sender inn x (5) til funksjonen
#         # Inne i funksjonen heter det 'a', men peker på samme objekt
#         # Men når a += 1 skjer, lages en ny verdi, og x påvirkes IKKE

#         print(f'Etter: id(x) = {id(x)}, verdi = {x}')
#         # Til slutt ser vi at x fortsatt er 5, og har samme ID som før
#         # Det viser at funksjonen ikke har endret x — bare jobbet med en kopi

# if __name__ == "__main__":
#     main()


# def main():
#     def function(val1='Verdi 1:',val2='Verdi 2:',val3='Verdi 3:',val4='Verdi 4:',val5='Verdi 5:'):
#         print(val1,val2,val3,val4,val5)

# #    function()

# if __name__ == "__main__":
#     main()
# #        print('Verdi 1:', val1,'Verdi 2:', val2,'Verdi 3:', val3,'Verdi 4:', val4, 'Verdi 5:', val5)
# #        function(val1='Brus', val2='Poppkorn', val3='Kick Lunch', val4='kino bilett', val5='Godt humør') # Vi setter standard verdier, i mitt hode, fordi det er best practice.
# #        print('Function = ',function)


# def calculator(kalk_type, første_verdi, andre_verdi):
#     if kalk_type == 1:
#         print("Addere verdier")
#         return første_verdi + andre_verdi
#     elif kalk_type == 2:
#         print()
#         print("Subtrahere values")
#         return første_verdi - andre_verdi
#     elif kalk_type == 3:
#         print()
#         print("Udefinert")
#         return
    
# print(calculator(1,20,10))
# print(calculator(2,20,10))
# print(calculator(3,20,10)) # The return statement returns nothing
# print(calculator(4,20,10)) # No return statement matches this calc_type


# def kalk_all(første_verdi, andre_verdi):
#     Addisjon = første_verdi + andre_verdi
#     Subtraksjon = første_verdi - andre_verdi
#     Dividering = første_verdi / andre_verdi
#     Multiplisering = første_verdi * andre_verdi
#     return Addisjon, Subtraksjon, Dividering, Multiplisering # alle 4 verdier returneres

# # Mottar verdiene separat
# første, andre, tredje, fjerde = kalk_all(20,10)
# print(første, andre, tredje, fjerde)
# # Mottar alle veriene samtidig
# verdier = kalk_all(30,15)
# print(verdier)


# # Funksjonen tar imot tre verdier (a, b, c), øker hver med 1, og returnerer alle tre
# def øk_alle_med_en(a, b, c):
#     # Øker hver verdi med 1
#     a += 1
#     b += 1
#     c += 1

#     # Returnerer alle tre verdiene som en "pakke" (tuple)
#     return a, b, c

# def main():
#     # Starter med tre testverdier – kunne også vært input fra bruker
#     verdi1 = 10
#     verdi2 = 20
#     verdi3 = 30

#     # Kaller funksjonen og pakker ut verdiene i tre separate variabler
#     ny1, ny2, ny3 = øk_alle_med_en(verdi1, verdi2, verdi3)

#     # Skriver ut resultatet på pen måte
#     print(f"Originale verdier: {verdi1}, {verdi2}, {verdi3}")
#     print(f"Økte verdier:     {ny1}, {ny2}, {ny3}")

# if __name__ == "__main__":
#     main()



# # Denne funksjonen tar imot tre tallverdier, øker hver med 1, og returnerer de nye verdiene
# def øk_alle_med_en(a, b, c):
#     a += 1
#     b += 1
#     c += 1
#     return a, b, c  # Returnerer alle tre som en tuple

# def main():
#     print("Funksjonstest: Vi øker tre tall med én hver\n")

#     # Vi ber brukeren skrive inn tre verdier – vi konverterer til heltall med int()
#     tall1 = int(input("Skriv inn første tall: "))
#     tall2 = int(input("Skriv inn andre tall: "))
#     tall3 = int(input("Skriv inn tredje tall: "))

#     # Vi kaller funksjonen og pakker ut de tre verdiene vi får tilbake
#     ny1, ny2, ny3 = øk_alle_med_en(tall1, tall2, tall3)

#     # Vi skriver ut resultatene
#     print("\nResultat etter økning:")
#     print(f"Før: {tall1}, {tall2}, {tall3}")
#     print(f"Etter: {ny1}, {ny2}, {ny3}")

#     # Bonus: Vi kan også vise summen av de nye verdiene
#     total = ny1 + ny2 + ny3
#     print(f"Sum av økte verdier: {total}")

# if __name__ == "__main__":
#     main()

# def adderings_metoden(første_verdi, andre_verdi):
#     return første_verdi + andre_verdi

# # Using the method
# print(adderings_metoden(30,15))
# print()

# # Doing the same with the lamda expression
# adderer = lambda første_verdi, andre_verdi: første_verdi + andre_verdi
# print(adderer(30,15))


# # Først definerer vi en navngitt funksjon
# def beregn_månedslønn(timesats, antall_timer):
#     # Vi ganger timesatsen med antall timer for å finne månedslønna
#     return timesats * antall_timer


# # Nå lager vi samme funksjon, men som en in-line funksjon (lambda)
# beregn_månedslønn_lambda = lambda timesats, antall_timer: timesats * antall_timer
# # (Ja, det der ser nesten ut som juks, men det er faktisk helt lov... og veldig Python 😎)


# # Nå demonstrerer vi hvordan begge funksjonene brukes:
# # La oss si vi tjener 250 kr per time og har jobbet 160 timer denne måneden

# # Bruk av navngitt funksjon
# månedslønn1 = beregn_månedslønn(250, 160)
# print("Månedslønn med navngitt funksjon:", månedslønn1)

# # Bruk av lambda-funksjon
# månedslønn2 = beregn_månedslønn_lambda(250, 160)
# print("Månedslønn med lambda-funksjon:", månedslønn2)

# MetricConverter.py

# verdi_en = 50
# verdi_to = 70

# if verdi_en > verdi_to:
#     print("Gjør noe")
# else:
#     pass

# print("Ytring etter if")


# print("Normal loop:  ", end="")
# for value in range(0,5):
#     print(value, end="")
# print()
# print("Looper med \"continue\":  ", end="")
# for value in range(0,5):
#     if value == 2:
#         print("#", end="")
#         continue
#     print(value, end="")
# print()
# print("Looper med \"pass\":  ", end="")
# for value in range(0,5):
#     if value == 2:
#         print("#", end="")
#         pass
#     print(value, end="")
# print()
# print("Looper med \"break\":  ", end="")
# for value in range(0,5):
#     if value == 2:
#         print("#", end="")
#         break
#     print(value, end="")



# def enkel_yield():                             # Definerer en funksjon som bruker yield
#     print("Første linje")                      # Skriver ut første linje
#     yield                                      # Pausepunkt – "gi kontrollen tilbake" til den som kaller
#     print("Andre linje")                       # Når funksjonen kjøres igjen, fortsetter her
#     yield                                      # Pausepunkt igjen
#     print("Tredje linje")                      # Når funksjonen kjøres igjen, fortsetter her

# første_test = enkel_yield()                    # Lager en generator-objekt av funksjonen

# next(første_test)                              # Kjører til første `yield`, skriver: "Første linje"
# next(første_test)                              # Kjører videre til andre `yield`, skriver: "Andre linje"
# next(første_test)                              # Kjører videre til slutt, skriver: "Tredje linje"
#                                                # Så kommer det ingen flere `yield` → StopIteration-feil

# print("Denne linjen vil ikke skrives ut")     # Denne blir IKKE kjørt, pga feilen over




# def increment():
#     i = 0
#     while True:   # Creates an infinite loop
#         yield i       # returns the value of i and sets next start point
#         i += 1

# incrementor = increment()
# print(next(incrementor))  # Runs to first yield statement
# print(next(incrementor))  # Runs to second yield statement
# print(next(incrementor))  # Runs to third yield statement
# print(next(incrementor))
# print(next(incrementor))
# print(next(incrementor))
# print(next(incrementor))
# print(next(incrementor))


# # next() may be called an infinite number of times




# def tell_opp():                           # Definerer en generatorfunksjon som teller opp fra 0
#     i = 0                                 # Starter med i = 0
#     while True:                           # Lager en uendelig løkke
#         yield i                           # Gir fra seg nåværende verdi av i, og husker stedet
#         i += 1                            # Øker i med 1 for neste gang funksjonen fortsetter

# # Lager to separate generatorer – de har hver sin egen telleverdi!
# opp_teller_en = tell_opp()               # Første generator, starter på 0
# opp_teller_to = tell_opp()               # Andre generator, starter også på 0 (egen kopi)
# opp_teller_tre = tell_opp()

# print("Første generator:")
# print(next(opp_teller_en))               # Starter første generator → skriver 0
# print(next(opp_teller_to))               # Fortsetter første generator → skriver 1
# print(next(opp_teller_tre))               # Starter første generator → skriver 0
# print(next(opp_teller_en))
# print(next(opp_teller_to))               
# print(next(opp_teller_tre))

# print("Andre generator:")
# print(next(opp_teller_to))               # Starter andre generator → skriver 0 (uavhengig!)




# def fibonacci(første_verdi, andre_verdi):
#     while True:
#         yield første_verdi
#         temp = første_verdi # Lagrer første_verdi midlertidig
#         første_verdi = andre_verdi # Fordi den vil overskrives her
#         andre_verdi = temp + andre_verdi # Bruker den lagrede midlertidige verdien (første_verdi ligger lagret i temp)

# fib = fibonacci(0,1)

# # Print the first 15 Fibonacci numbers

# for i in range(0,20):
#     print(next(fib),end=", ")






# def fibonacci(første_verdi=0, andre_verdi=1):
#     while True:
#         yield første_verdi
#         første_verdi, andre_verdi = andre_verdi, første_verdi + andre_verdi

# fib = fibonacci()

# # Skriver de første 20 verdiene til skjerm

# for i in range(20):
#     print(next(fib),end=", ")


    

# def mitt_spekter(original_verdi, tell_opp):
#     i = original_verdi
#     while True:
#         yield i
#         i += tell_opp

# øk_en = mitt_spekter(0,1)
# øk_to = mitt_spekter(0,5)

# print("Første generator, øk_en:  ", end="")
# for i in øk_en:
#     if i > 10:
#         break;
#     else:
#         print(i, end=", ")

# print()
# print("Andre generator, øk_to:  ", end="")
# for i in øk_to:
#     if i > 50:
#         break;
#     else:
#         print(i, end=", ")



# def mitt_spekter(original_verdi, tell_opp):
#     i = original_verdi
#     while True:
#         yield i
#         i += tell_opp

# tell_opp = mitt_spekter(0,1)
# print(type(tell_opp))




# def fi_generator():
#     a = b = 1
#     while True:
#         yield a
#         a,b=b,a+b
    
# fib=fi_generator()

# for i in fib:
#     if i > 100 :		# Her sier vi at hvis verdien i "i" er større enn 100
#         break		# Så skal vi avslutte
#     else :
#         print( "Generert:" , i )	#Her skriver vi til skjerm den endelige resultatet sist i ble lagret, som er FØR den kommer til 100.




# def morro_generator(verdier):
#     indeks = 0
#     while True:
#         yield verdier[indeks]                   # Return current value
#         indeks = (indeks + 1) % len(verdier)     # Wrap around to start when end is reached

# min_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']
# gen = morro_generator(min_liste)

# for _ in range(15):
#     print(next(gen), end=", ")


# verdi_a=10

# try:
#     print(verdi_b) # verdi_b har ikke blitt initialisert, og vil gi en runtime error.
# except:
#     print("Ops!!" \
#     "\nHer skjedde det noe feil." \
#     "\nKan være en feil 50" \
#     "\naka, feilen ligger 50 cm fra skjermen. ;)")


# verdi_a=10

# try:
#     print(verdi_b) # verdi_b har ikke blitt initialisert, og vil gi en runtime error.
# except NameError as msg:  # NameError exception blir håndtert, og dens detaljer lagres i msg ved å bruke "as" nøkkel ordet
                          
#     print("En feil har oppstått: ",msg )


# listen = [1,2,3,4] # En liste med 4 elementer

# try:
#     for i in range (0,5):  # En loop med 5 iterajoner
#         print(listen[i],end=",")
# except IndexError as msg:
#     print()
#     print("En feil har oppstått: ", msg)



# try:
#     a = int(input("Skriv inn ett nummer:  "))
# except ValueError as msg:
#     print("En feil har oppstått: ", msg)

# oppføringer = [2,3,4,5,6]
# try:
#     a = int(input("Skriv inn ett nummer:  "))
#     indeks = 0
#     while indeks < a:
#         print(oppføringer[indeks])
#         indeks+=1
# except (ValueError,IndexError) as msg:
#     print("En feil har oppstått: ", msg)



# oppføringer = [2,3,4,5,6]
# try:
#     a = int(input("Skriv inn ett nummer:  "))
#     indeks = 0
#     while indeks < a:
#         print(oppføringer[indeks])
#         indeks+=1
# except (ValueError,IndexError) as msg:
#     print("En feil har oppstått: ", msg)
# finally:
#     print("Denne blokken med kode vil alltid kjøre.")


# try:
#     a = 50
#     if a > 10:
#       # Lager et ValueError objekt med en egendefinert melding
#       # "raise" nøkkelordet sender error-en til except blokken
#       raise ValueError("Verdien er for høy")
# except ValueError as msg:
#     print("En feil har oppstått: ", msg)

