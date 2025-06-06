"""
network_discovery.py
Av: Andreas & C-mode, på koffein og ren nysgjerrighet
Formål: Skann ditt lokale nettverk for aktive verter og åpne porter.
OBS: Dette skal kun brukes på nettverk du har lov til å skanne. Vi er snille, ikke kriminelle.
"""

import scapy.all as scapy
import socket
import sys

# Vanlige porter vi sjekker - historisk sett populære og/eller usikre
COMMON_PORTS = [22, 23, 25, 80, 110, 143, 443]

# Velkomstbanner med sarkasme
def banner():
    print("""
==================================================
  🧠  Andreas & C-Mode Network Discovery Tool  📡
--------------------------------------------------
Vi skanner... fordi vi bryr oss... eller fordi vi er nysgjerrige.
==================================================
""")

# Henter nettverksrange fra brukeren eller kommandolinje
def get_target_range():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("Skriv inn nettverksområde (f.eks. 192.168.1.0/24): ")

# Bruker arping til å oppdage levende verter
def discover_hosts(ip_range):
    print(f"\n[+] Skanner etter aktive enheter i {ip_range}...")
    answered, _ = scapy.arping(ip_range, verbose=0)
    hosts = []
    for sent, received in answered:
        hosts.append(received.psrc)
    print(f"[+] Fant {len(hosts)} levende vert(er).\n")
    return hosts

# Sjekker vanlige porter på hver vert
def scan_ports(ip):
    print(f"[*] Skanner {ip} for åpne porter...")
    open_ports = []
    for port in COMMON_PORTS:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)  # kort timeout for effektivitet
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except Exception as e:
            print(f"[!] Feil under portskanning av {ip}:{port} -> {e}")
    return open_ports

# Spør brukeren hvordan de ønsker resultatene (kun etter alt er ferdig)
def get_output_method():
    print("\nHvordan vil du vise resultatene?")
    print("1. Bare skriv dem ut på skjermen (som et sivilisert menneske)")
    print("2. Lagre til fil")
    choice = input("Velg 1 eller 2: ")
    if choice == '2':
        file_name = input("Filnavn å lagre til: ")
        mode = input("Overskrive eller legge til? (w/a): ").lower()
        return ("file", file_name, mode)
    return ("screen", None, None)

# Viser eller skriver resultatene til fil/skjerm
def display_results(results, method, file_name=None, mode=None):
    output = []
    for ip, ports in results.items():
        ports_str = ", ".join(str(p) for p in ports) if ports else "Ingen åpne porter (eller de er sjenerte)."
        output.append(f"Vert {ip} - Åpne porter: {ports_str}")

    if method == "screen":
        print("\n--- Skanneresultater ---")
        for line in output:
            print(line)
    else:
        try:
            with open(file_name, mode) as f:
                f.write("\n--- Skanneresultater ---\n")
                for line in output:
                    f.write(line + "\n")
            print(f"[+] Resultater lagret i {file_name}!")
        except Exception as e:
            print(f"[!] Klarte ikke å skrive til fil: {e}")

# Hovedfunksjonen - den store dirigenten
def main():
    banner()
    ip_range = get_target_range()

    # 1. Finn aktive enheter først
    live_hosts = discover_hosts(ip_range)

    # 2. Portskann dem alle og lagre resultatene
    results = {}
    for ip in live_hosts:
        results[ip] = scan_ports(ip)

    # 3. Først nå spør vi hvordan brukeren ønsker resultatene
    method, file_name, mode = get_output_method()
    display_results(results, method, file_name, mode)

if __name__ == '__main__':
    main()
