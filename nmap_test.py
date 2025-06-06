import nmap

print("🧪 Starter enkel portskanning med nmap.PortScanner...\n")

# Initialiser skanneren
scanner = nmap.PortScanner()

# Mål og port(er)
target = '127.0.0.1'
ports = '22,80,443'

# Utfør skanning
scanner.scan(hosts=target, ports=ports)

# Skriv ut resultater
for host in scanner.all_hosts():
    print(f"\n📍 Skannet vert: {host}")
    print(f"  ↳ Status: {scanner[host].state()}")
    for proto in scanner[host].all_protocols():
        print(f"  ➕ Protokoll: {proto}")
        lport = scanner[host][proto].keys()
        for port in sorted(lport):
            state = scanner[host][proto][port]['state']
            print(f"    - Port {port}: {state}")

print("\n🎯 Ferdig!")
