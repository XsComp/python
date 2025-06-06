from scapy.arch.windows import get_windows_if_list

target_mac = "68:54:5a:ac:53:3c"  # Wi-Fi MAC in lowercase with colons

for iface in get_windows_if_list():
    mac = iface.get("mac", "").lower()
    if mac == target_mac:
        print("🎯 MATCH FOUND!")
        print(f"Name       : {iface['name']}")
        print(f"Description: {iface['description']}")
        print(f"MAC        : {iface['mac']}")
        break
else:
    print("❌ No matching interface found.")