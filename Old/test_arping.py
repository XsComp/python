"""
arping_test.py
Bare tester arping for å se hvem som er våkne på nettverket vårt.
"""
import scapy.all as scapy

def main():
    print("🧠 Enkel arping-test – vi roper ut i nettverket og ser hvem som svarer!")
    ip_range = input("Skriv inn nettverksområde (f.eks. 192.168.1.0/24): ")
    
    print(f"\n[+] Kjører arping på {ip_range}...")
    answered, _ = scapy.arping(ip_range, verbose=0)

    if answered:
        print(f"[+] Fant {len(answered)} enhet(er) som svarte:")
        for sent, received in answered:
            print(f"  🔸 IP: {received.psrc} | MAC: {received.hwsrc}")
    else:
        print("[!] Ingen svarte... Enten er alle offline, eller så ignorerer de oss 🥲")

if __name__ == "__main__":
    main()