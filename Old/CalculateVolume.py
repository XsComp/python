# Script: CalculateVolume.py


# Beskrivelse: Beregner volumet av en rektangulær tank og øker det med 1% pga. utvidelse i plastikken
# Vi ber brukeren om mål i centi meter
lengde = float(input("Oppgi lengde på tanken i cm: "))
bredde = float(input("Oppgi bredde på tanken i cm: "))
hoyde  = float(input("Oppgi høyde på tanken i cm: "))

# Vi kalkulerer volumet (lengde * bredde * høyde)
volum = lengde * bredde * hoyde

# Vi øker volumet med 1% for å kompensere for utvidelse av tanken
volum_med_utvidelse = volum * 1.01

# Vi skriver ut resultatet
print("\nVolum uten kompensasjon:", volum, "kubikkcentimeter")
print("Volum med 1% kompensasjon:", volum_med_utvidelse, "kubikkcentimeter")
print()

# Vi konverterer til liter for lett leselighet
liter = volum / 1000
liter_med_utvidelse = volum_med_utvidelse / 1000
print("Volum uten kompensasjon:", liter, "liter")
print("Volum med 1% kompensasjon:", liter_med_utvidelse, "liter")
print()

# Vi konverterer til liter og runder av til 2 desimaler
liter = round(volum / 1000, 2)
liter_med_utvidelse = round(volum_med_utvidelse / 1000, 2)
print(f"Volum uten kompensasjon: {liter} liter")
print(f"Volum med 1% kompensasjon: {liter_med_utvidelse} liter")
print()