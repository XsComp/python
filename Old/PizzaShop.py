# Script: PizzaShop.py

# Beskrivelse: Kalkulerer prisen på en pizza basert på kundens valg
print("Velkommen til \"C og venner\" Pizza!")

total = 0

# --- PIZZABUNN ---
print("\nVelg pizzabunn:")
print("1. Vanlig (Kr 10)")
print("2. Uten gluten (Kr 20)")
bunn_valg = input("Skriv 1 for med, 2 for uten: ")

if bunn_valg == "1":
    print("→ Valgt: Vanlig (Kr 10)")
    total += 10
elif bunn_valg == "2":
    print("→ Valgt: Uten gluten (Kr 20)")
    total += 20
else:
    print("Ugyldig valg. Standard: Vanlig (Kr 10)")
    total += 10

# --- STØRRELSE ---
print("\nVelg størrelse:")
print("1. Liten (Kr 130)")
print("2. Medium (Kr 140)")
print("3. Stor (Kr 150)")
storrelse_valg = input("Skriv 1 for liten, 2 for medium, 3 for stor: ")

if storrelse_valg == "1":
    print("→ Valgt: Liten (Kr 30)")
    total += 130
elif storrelse_valg == "2":
    print("→ Valgt: Medium (Kr 40)")
    total += 140
elif storrelse_valg == "3":
    print("→ Valgt: Stor (Kr 50)")
    total += 150
else:
    print("Ugyldig valg. Standard: Medium (Kr 40)")
    total += 140

# --- SAUS ---
print("\nVelg saus:")
print("1. Tomat (Kr 5)")
print("2. Hvitløk (Kr 10)")
print("3. Ingen saus (Kr 0)")
saus_valg = input("Skriv 1 for tomat, 2 for hvitløk, 3 for ingen: ")

if saus_valg == "1":
    print("→ Valgt: Tomatsaus (Kr 5)")
    total += 5
elif saus_valg == "2":
    print("→ Valgt: Hvitløksaus (Kr 10)")
    total += 10
elif saus_valg == "3":
    print("→ Ingen saus valgt (Kr 0)")
else:
    print("Ugyldig valg. Ingen saus valgt som standard (Kr 0)")

# --- TOPPING ---
print("\nVelg toppinger (skriv 'ja' for hver du vil ha):")

topping_valg = {
    "Ost": 5,
    "Sopp": 3,
    "Avokado": 7,
    "Ananas": 5,
    "Bacon": 7,
    "Kylling": 7,
    "Fisk": 6
}

for topping, pris in topping_valg.items():
    svar = input(f"Vil du ha {topping}? (Kr {pris}) (ja/nei): ").lower()
    if svar == "ja":
        print(f"→ Lagt til: {topping} (Kr {pris})")
        total += pris

# --- TOTAL ---
print("\n🧾 Totalsum for din pizza:", total, "kroner")
print("Takk for handelen og vel bekomme! 🍕")
