import os
import platform
import requests
import webbrowser

# Funksjon som åpner bildet via riktig metode for operativsystemet
def åpne_bilde(filsti):
    if platform.system() == "Windows":
        os.startfile(filsti)  # Windows
    elif platform.system() == "Darwin":
        os.system(f"open '{filsti}'")  # macOS
    else:
        os.system(f"xdg-open '{filsti}'")  # Linux

# Henter info om en hunderase fra theDogAPI
def hent_hund_info(rase):
    url = f"https://api.thedogapi.com/v1/breeds/search?q={rase}"
    response = requests.get(url)
    return response.json()

# Henter info om en katterase fra theCatAPI
def hent_katt_info(rase):
    url = f"https://api.thecatapi.com/v1/breeds/search?q={rase}"
    response = requests.get(url)
    return response.json()

# Henter bilde-URL basert på rase-ID og dyretype
def hent_bilde_url(dyretype, breed_id):
    bilde_api = f"https://api.the{dyretype}api.com/v1/images/search?breed_ids={breed_id}"
    bilde_response = requests.get(bilde_api)
    if bilde_response.ok and bilde_response.json():
        return bilde_response.json()[0]["url"]
    return None

# Skriver ut utvalgt informasjon fra rasens data
def vis_dyreinfo(data, dyretype):
    print("\nInformasjon:")
    print(f"Navn: {data.get('name', 'Ukjent')}")
    print(f"Opprinnelse: {data.get('origin', 'Ukjent')}")
    print(f"Temperament: {data.get('temperament', 'Ikke spesifisert')}")
    print(f"Levetid: {data.get('life_span', 'Ukjent')}")
    if dyretype == "dog":
        print(f"Bred for: {data.get('bred_for', 'Ukjent')}")
    else:
        print(f"Beskrivelse: {data.get('description', 'Ingen beskrivelse')}")

# Viser hovedmenyen og styrer hovedflyten
def hovedmeny():
    while True:
        print("\n--- Dyreoppslag ---")
        print("1. Hundeinformasjon")
        print("2. Katteinformasjon")
        print("3. Avslutt")
        valg = input("Velg et alternativ (1-3): ").strip()

        if valg == "1":
            behandle_rase("dog")
        elif valg == "2":
            behandle_rase("cat")
        elif valg == "3":
            print("Ha en fin dag videre! 🐾")
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

# Meny for å vise detaljer og bilde, eller returnere
def behandle_rase(dyretype):
    søk = input(f"Skriv inn navnet på en {dyretype}-rase: ").strip()
    if dyretype == "dog":
        resultater = hent_hund_info(søk)
    else:
        resultater = hent_katt_info(søk)

    if not resultater:
        print(f"Ingen treff for {søk}. Prøv igjen.")
        return

    valgt = resultater[0]
    while True:
        print("\nHva ønsker du å gjøre?")
        print("1. Vis detaljer")
        print("2. Vis bilde")
        print("3. Gå tilbake")
        under_valg = input("Velg et alternativ (1-3): ").strip()

        if under_valg == "1":
            vis_dyreinfo(valgt, dyretype)
        elif under_valg == "2":
            bilde_url = hent_bilde_url(dyretype, valgt["id"])
            if bilde_url:
                print(f"Åpner bilde: {bilde_url}")
                webbrowser.open(bilde_url)
            else:
                print("Fant ikke bilde for denne rasen.")
        elif under_valg == "3":
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

# Programstart
hovedmeny()
