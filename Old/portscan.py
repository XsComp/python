# portscan.py


import nmap3  # Importerer nmap3-modulen for å bruke Nmap fra Python

nmap = nmap3.Nmap()  # Lager et Nmap-objekt som vi bruker til å skanne
ip = "85.166.100.132"  # IP-en vi ønsker å skanne

results = nmap.scan_top_ports(ip)  # Kjører skann av de vanligste portene

# Henter generell enhetsinformasjon fra skanneresultat
device_info = results.get(ip, {})  # Resultat for den aktuelle IP-en

# Behandler hostname – det er en liste, så vi må hente første element
hostname_list = device_info.get("hostname", [])  # Henter listen med hostname-info
hostname = hostname_list[0].get("name", "unknown") if hostname_list else "unknown"

# Behandler MAC-adresse (dette er en dict)
mac_info = device_info.get("macaddress")
mac = mac_info.get("addr", "unknown") if isinstance(mac_info, dict) else "unknown"

# Skriver overskriften
print("-" * 84)
print(f"{ip} device is up the device hostname is {hostname} with mac addres {mac}")
print("-" * 84)
print("Port\tState\t Protocol")
print("-" * 84)

# Løper gjennom porter og skriver ut pent
for port in device_info.get("ports", []):
    portid = port.get("portid", "N/A")       # Portnummer (f.eks. 22)
    state = port.get("state", "unknown")     # Tilstand (f.eks. open)
    protocol = port.get("protocol", "tcp")   # Protokoll (tcp/udp)

    # Skriver portinfo, pent formattert
    print(f"{portid:<5}\t{state:<7}\t{protocol}")
