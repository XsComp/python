# csvreader.py

# Fil 1: csvreader.py
import csv

try:
    with open("mycsv.csv", newline='', encoding='utf-8') as csvfile:
        leser = csv.reader(csvfile, delimiter=';')
        print("Innholdet i 'mycsv.csv':")
        for rad in leser:
            print(", ".join(rad))
except FileNotFoundError:
    print("Filen 'mycsv.csv' ble ikke funnet. Er du sikker på at den eksisterer?")