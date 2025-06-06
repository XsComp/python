# politibetjent_main.py

# Her tester vi ut Politibetjent-klassen vår

from politibetjent import Politibetjent  # Importerer helten vår

# Lager en ny politibetjent
betjent_1 = Politibetjent("Vicky", "Kananu", 38, 8)
betjent_2 = Politibetjent("Andreas", "Andresen", 45, 12)

# Legger til noen imponerende utmerkelser
betjent_1.legg_til_utmerkelse("Medalje for tapperhet i tjenesten")
betjent_1.legg_til_utmerkelse("Årets betjent 2023")
betjent_1.legg_til_utmerkelse("Diplom for eksemplarisk ledelse")

# Viser all info om betjentene våre
betjent_1.vis_info()
betjent_2.vis_info()