# Script: TimeCalculation.py



# Beskrivelse: Konverterer arbeidede minutter til arbeidsdager, timer og minutter
# Antakelse: 1 arbeidsdag = 7.5 timer (450 minutter)

# Be om antall minutter fra brukeren
total_minutter = int(input("Oppgi totalt antall minutter jobbet denne måneden: "))

# Antall minutter i en vanlig arbeidsdag
minutter_per_dag = 7.5 * 60  # 450 minutter

# Kalkuler antall hele arbeidsdager
arbeidsdager = int(total_minutter // minutter_per_dag)

# Finn resterende minutter etter hele dager
resterende_minutter_etter_dager = total_minutter % minutter_per_dag

# Kalkuler timer og minutter fra det som er igjen
resterende_timer = int(resterende_minutter_etter_dager // 60)
resterende_minutter = int(resterende_minutter_etter_dager % 60)

# Skriv resultatet ut i formatet: dager:timer:minutter
print("Format: arbeidsdager:timer:minutter")
print(f"\nResultat: {arbeidsdager}:{resterende_timer}:{resterende_minutter}")
