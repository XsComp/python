from datetime import datetime

# Meldinger som brukes i valg 3 og 4
melding = [
    "Koding er gøy!",
    "Python er ikke kode, men en livsstil",
    "Vi lærer Python på den morsomme måten",
    "Vi koder... fordi vi kan!"
]

def guess_the_number():
    while True:
        try:
            gjett = int(input("Skriv inn ett tall: "))
            if gjett == 212:
                print("DU KLARTE DET! Det ER 212.")
                break  # Endelig fri!
            elif gjett < 212:
                print("Hrmpfh... for lavt. TA I LITT DA!!.")
            else:
                print("Oooh... det var litt mye... det finnes da mellom ting...")
        except ValueError:
            print("Ser det ut som ett helt vanlig tall for deg? Virkelig? Skal vi melde deg opp til grunnskolen på nytt kanskje?")

def calculate_time():
    tid_input = input("Skriv inn tid (HH:MM): ")
    try:
        tid_verdi = datetime.strptime(tid_input, "%H:%M").time()
        start = datetime.strptime("08:00", "%H:%M").time()
        slutt = datetime.strptime("17:00", "%H:%M").time()
        if start <= tid_verdi <= slutt:
            print("Innenfor jobbtid.")
        else:
            print("Din egen tid, bruk den på noe ikke jobb relatert.")
    except ValueError:
        print("Feil format. Du VET hvordan klokka funker, ikke sant? Bruk formatet HH:MM, 14:00 f.eks. Yeeez.")

def print_something():
    try:
        indeks = int(input("Skriv inn ett hel-tall mellom 0 og 3.. "))
        if 0 <= indeks < len(melding):
            print(melding[indeks])
        else:
            print("Den indeksen er utenfor rekkevidde.")
    except ValueError:
        print("Invalid bruker. Vet ikke hva ett hel-tall er. Tast inn hel-tall dust... google først hvis du må... Det må være mellom 0 and 3.")

def change_print_option():
    try:
        indeks = int(input("Hvilket meldingsnummer (0–3) ønsker du å endre? "))
        if 0 <= indeks < len(melding):
            ny_melding = input("Skriv inn ny beskjed: ")
            melding[indeks] = ny_melding
            print("\nOppdatert beskjed:")
            for i, msg in enumerate(melding):
                print(f"{i}: {msg}")
        else:
            print("Sorry, den indeksen er ikke gyldig (klaske panne). Velg ett nummer mellom 0 and 3, du vet... sånn som vi ba deg gjøre opprinnelig...")
    except ValueError:
        print("Men vær så snill da... skriv inn ett gyldig nummer.")

def main():
    while True:
        print("\n------------------------------")
        print("         Meny System          ")
        print("------------------------------")
        print("1. Gjett nummeret")
        print("2. Kalkuler tid")
        print("3. Print noe")
        print("4. Endre ett print valg")
        print("5. Forlat åstedet")
        print("------------------------------")

        choice = input("Hvilket valg vil du ha? ")

        if choice == "1":
            guess_the_number()
        elif choice == "2":
            calculate_time()
        elif choice == "3":
            print_something()
        elif choice == "4":
            change_print_option()
        elif choice == "5":
            print("Forlater applikasjonen. Ha en perfekt dag (uten ananas på Pizza... for seg selv er det greit... vi hater ikke ananas. Den bare hører ikke hjemme på Pizza! 🍕")
            break
        else:
            print("Ukjent valg. Sansynligvis det samme som din mor tenkte om abort... Om bare... Uansett, prøv igjen, og jeg mener, prøv denne gangen. Helst ved å bruke GYLDIGE tall..")

if __name__ == "__main__":
    main()