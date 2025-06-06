# brannstasjon.py

from brannmann import Brannmann

# Lager tre forskjellige brannmenn
f1 = Brannmann("Andreas", "Andresen", 1, 45)
f2 = Brannmann("Sandra", "Solstad", 2, 38)
f3 = Brannmann("Roger", "Røykdykker", 3, 50)

# Viser info om alle tre
f1.vis_info()
f2.vis_info()
f3.vis_info()

# Totalt antall brannmenn
print(f"Totalt antall brannmenn: {Brannmann.telling}")
