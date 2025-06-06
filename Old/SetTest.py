# SetTest.py

# Trinn 1: Definer ett sett med min favoritt fast food
min_fav_mat = {"pizza", "burger", "wrap", "sushi", "kebab"}

# Trinn 2: Definer ett sett med en venns favoritt fast foods
venns_fav_mat = {"sushi", "biff", "pizza", "nudles", "kebab"}

# Trinn 3: Legg til enda en fast food til settet ditt
min_fav_mat.add("gyros")

# Trinn 4: Finn kryssningen mellom begge sett (delta favoritter)
delt_fav_mat = min_fav_mat.intersection(venns_fav_mat)

# Trinn 5: Vis de delta favoritt mat typene
print("Delte favoritter fastfood:")
for food in delt_fav_mat:
    print("-", food)

