# Filnavn listtest.py

# Trinn 1: Definer en tom liste
venner = []

# Trinn 2: Spør etter 10 navn fra bruker
print("Vær så snill å skriv inn 10 navn:")
for i in range(10):
    navn = input(f"Venn {i + 1}: ")
    venner.append(navn)

# Trinn 3: Sorter listen alfabetisk
venner.sort()
print(venner)

# Trinn 4: Reverser listen
venner.reverse()
print(venner)

# Trinn 5: Be om ett siste navn
ekstra_navn = input("Legg til ett navn til i listen: ")
venner.append(ekstra_navn)

# Step 6: Display the full list
print("\nHer er hele vennelisten:")
for venner in venner:
    print("-", venner)



