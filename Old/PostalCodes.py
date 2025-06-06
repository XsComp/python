# PostalCodes.py


def main():
    # En ordbok (dictionary) med postnummer og stedsnavn
    postkoder = {
        "0010": "Oslo Sentrum",
        "5003": "Bergen",
        "7030": "Trondheim",
        "8006": "Bodø",
        "9008": "Tromsø",
        "1607": "Fredrikstad",
        "2609": "Lillehammer",
        "1707": "Sarpsborg",
        "3510": "Hønefoss",
        "4620": "Kristiansand",
        "1500": "Moss"
    }

    # Spør brukeren om et postnummer
    kode = input("Skriv inn et postnummer: ")

    if kode in postkoder:
        print(f"{kode} tilhører området: {postkoder[kode]}")
    else:
        print("Postnummeret finnes ikke i databasen.")

if __name__ == "__main__":
    main()
