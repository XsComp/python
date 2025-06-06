import nmap3            # For å bruke Nmap via Python
import ipaddress        # For å validere IP og nettverk
import re               # For å validere porter
import csv              # For å lagre resultatene
import os               # For å sjekke filstier

# Globalt resultat og skannetype
siste_resultat = None
siste_skann_type = None   # "network" eller "ports"

# ------------------ Valideringsfunksjoner ------------------

def is_valid_subnet(subnet):
    try:
        ipaddress.IPv4Network(subnet)
        return True
    except ValueError:
        return False

def is_valid_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False

def is_valid_ports(ports):
    return re.fullmatch(r"(\d{1,5})(,\d{1,5})*", ports) is not None

# ------------------ Menyvalg 1: Nettverksskann ------------------

def scan_network():
    global siste_resultat, siste_skann_type
    subnet = input("Skriv inn subnett (f.eks. 192.168.1.0/24): ").strip()
    if not is_valid_subnet(subnet):
        print("Ugyldig subnett. Tasteleif, eller kunnskap svikt?")
        return

    print("Skanner hjerne... dette gikk fort. Ingenting å finne. Alt normalt i bruker. Starter skanning av nettverk vennligst vent...")
    scanner = nmap3.NmapScanTechniques()
    siste_resultat = scanner.nmap_ping_scan(subnet)
    siste_skann_type = "network"

    print("Skanning fullført. Vi fant mer her enn mellom øra dine... Ting jeg fant:\n")
    for host, info in siste_resultat.items():
        if host in ["stats", "runtime", "task_results"]:
            continue
        if isinstance(info, list):
            info = info[0]
        mac = info.get("macaddress", {}).get("addr", "ukjent") if isinstance(info.get("macaddress"), dict) else "ukjent"
        state = info.get("state", {}).get("state", "ukjent")
        print(f"{host:<15}  {mac:<20}  {state}")

# ------------------ Menyvalg 2: Portskanning ------------------

def scan_device_ports():
    global siste_resultat, siste_skann_type
    ip = input("Skriv inn IP-adresse (f.eks. 192.168.1.10): ").strip()
    ports = input("Skriv inn porter (kommaseparert uten mellomrom, f.eks. 22,80,443,3389): ").strip()

    if not is_valid_ip(ip):
        print("Eeeh... hva var det der? Ikke en IP i hvert fall.... Gå litt skole, og prøv igjen.")
        return
    if not is_valid_ports(ports):
        print("Ugyldig perso.... jeg mener... ugyldige porter. Heh... prøve igjen?")
        return

    print("Skanner porter på enheten... Helluuuuu.... e det nokon heime!?! Jeg ville bare høre om jeg kunne låne litt sukker??!!")
    scanner = nmap3.NmapScanTechniques()
    scan_result = scanner.nmap_tcp_scan(ip, args=f"-p {ports}")

    siste_resultat = {ip: scan_result[ip]}  # NB: Vi pakker ut korrekt IP-nøkkel

    siste_skann_type = "ports"

    print(f"\nResultat for {ip}:")
    for port in scan_result.get("ports", []):
        port_id = port.get("portid", "?")
        state = port.get("state", "?")
        service = port.get("service", {}).get("name", "?")
        print(f"Port {port_id:<5}  Tilstand: {state:<6}  Tjeneste: {service}")

# ------------------ Menyvalg 3: Lagre til CSV ------------------

def save_results_to_csv():
    global siste_resultat, siste_skann_type
    if not siste_resultat:
        print("Åh... nei... ikke takk meg. Bokstavelig talt... Det er ingen resultat å lagre. Hvordan syns du dette gikk?")
        return

    path = input("Skriv inn filsti og fillnavn (f.eks. resultater.csv): ").strip()
    try:
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")

            if siste_skann_type == "network":
                writer.writerow(["IP", "MAC", "State"])
                for ip, info in siste_resultat.items():
                    if ip in ["stats", "runtime", "task_results"]:
                        continue
                    if isinstance(info, list):
                        info = info[0]
                    mac = info.get("macaddress", {}).get("addr", "ukjent") if isinstance(info.get("macaddress"), dict) else "ukjent"
                    state = info.get("state", {}).get("state", "ukjent")
                    writer.writerow([ip, mac, state])

            elif siste_skann_type == "ports":
                writer.writerow(["IP", "Port", "State", "Protocol", "Service"])
                for ip, data in siste_resultat.items():
                    if isinstance(data, list):
                        data = data[0]
                    for port in data.get("ports", []):
                        writer.writerow([
                            ip,
                            port.get("portid", ""),
                            port.get("state", ""),
                            port.get("protocol", ""),
                            port.get("service", {}).get("name", "")
                        ])

            else:
                print("Ukjent skannetype. Kan ikke lagre. Something whent bang in the night")
                return

        print(f"Resultatene ble lagret til '{path}'")

    except Exception as e:
        print(f"Det funka ikke... du vet hvordan dette funker... ikke sant?: {e}")

# ------------------ Hovedmeny ------------------

def main():
    while True:
        print("=" * 123)
        print("=" * 56, "Nmap Meny", "=" * 56)
        print("=" * 123)
        print("1. Skann et nettverk \(og mellom øra\).")
        print("2. Skann en enhet for åpne porter. Hvor hacker vennlig er du?")
        print("3. Lagre siste resultat til CSV, men bare hvis du lover at det er det siste... jeg er lei av å løpe igjennom nettverket...")
        print("4. Greit... bare dra... jeg trenger ikke deg like vell... sniff.... jeg mener... avslutt programmet.")
        choice = input("Velg et alternativ (1-4): ").strip()

        if choice == "1":
            scan_network()
        elif choice == "2":
            scan_device_ports()
        elif choice == "3":
            save_results_to_csv()
        elif choice == "4":
            print("Hulk... Min mor sa jeg ikke skulle stole på deg... hikst... alene igjen... Wuaæææææææææ")
            break
        else:
            print("Joda... du har 4 valg... 1, 2, 3, eller 4... Hvorfor ikke prøve g... jeg er helt enig.... eller 5... funker like bra!\nHva med å bare drite i å gjøre noe valg over hode? Det funker faktisk BEDRE!!! Sukk... ok...  Prøv igjen... Hvis du må...")

# ------------------ Kjører programmet ------------------

if __name__ == "__main__":
    main()
