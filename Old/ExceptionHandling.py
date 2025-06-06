# ExceptionHandling.py

# Vi ber om verdier, og sikrer koden for brukerfeil.


# try:
#     tall_1 = int(input("Skriv inn et tall: "))                  # Krever heltall, ref. int
#     tall_2 = int(input("Skriv inn et tall til: "))
    
#     produkt = tall_1 * tall_2
#     print(f"Resultatet av {tall_1} * {tall_2} er {produkt}.")   # Vi utfører utregning

# except ValueError as e:
#     print("Ugyldig input! Du må skrive inn hele tall (ingen komma, bokstaver eller punktum).")
# except TypeError:
#     print("Type-feil oppstod. Sjekk at begge verdier er av riktig type (ikke flyttall eller bokstaver).")
# except Exception as e:
#     print(f"Jeg vet ikke hva du gjorde, men ikke gjør det igjen: {e}")

# finally:
#     print(f"Oppgave utført, alle prosesser avsluttet.")