# GuessingGame.py


from Old.mymodules import create_time, output_local_time, calculate_difference, generate_random

print("Velkommen til Gjett Tallet-spillet!")
print("Jeg \"tenker\" på et tall mellom 0 og 10. Kan du gjette hva det er?")

spill_aktivt = True                                                                                                     # Brukes for å kontrollere om spillet skal fortsette
start_tid = create_time()                                                                                               # Registrerer starttidspunktet for spillet

total_runder = 0                                                                                                        # Teller antall runder som er spilt

while spill_aktivt:
    riktig_tall = generate_random(10)                                                                                   # Genererer et tilfeldig tall mellom 0 og 10
    try:
        bruker_input = input("\nGjett et tall mellom 0 og 10: ")                                                        # Leser brukerens rå input først
        gjetning = int(bruker_input)                                                                                    # Prøver å konvertere input til heltall
        total_runder += 1

        if gjetning == riktig_tall:
            print("Wow! Det der vaaar så flaks det!")
        else:
            print(f"Nope! Jeg tenkte på {riktig_tall}. Hihi!")

        fortsette = input("Vil du feile igjen? (ja/nei): ").lower()
        if fortsette != "ja":
            spill_aktivt = False

    except ValueError:
        print(f"Ser '{bruker_input}' ut som et tall for deg? Du hadde én jobb... én!!.")

slutt_tid = create_time()                                                                                               # Når spillet er slutt, registrer sluttidspunktet
varighet = calculate_difference(start_tid, slutt_tid)                                                                   # Kalkuler hvor lenge spillet varte

print(f"\nDu kastet nå bort {int(varighet)} sekunder og prøvde {total_runder} gang(er)."
      "Takk for spillet, men vi vet begge to at du hadde bedre ting å gjøre!")
output_local_time(slutt_tid)                                                                                            # Viser når spillet ble avsluttet


 

 