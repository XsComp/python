import time

def delay_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    delay_print("Initializing secure shell...")
    time.sleep(1)
    delay_print("Connecting to OmniCore Systems...")
    time.sleep(1)
    delay_print("Connection established. Welcome, ShadowRoot.")
    time.sleep(1)
    print("\nMission: Penetration Test – OmniCore Firewall\n")
    time.sleep(1)

def main_menu():
    delay_print("What would you like to do?")
    print("1. Scan network")
    print("2. Attempt login")
    print("3. Exit")

    choice = input("> ")

    if choice == "1":
        scan_network()
    elif choice == "2":
        attempt_login()
    elif choice == "3":
        delay_print("Disconnecting... Stay safe, ShadowRoot.")
    else:
        print("Invalid choice.")
        main_menu()

def scan_network():
    delay_print("\nRunning network scan...")
    time.sleep(1.5)
    delay_print("Host found: 192.168.1.45")
    delay_print("Open ports: 22 (SSH), 80 (HTTP)")
    delay_print("Vulnerability found: Weak SSH credentials\n")
    main_menu()

def attempt_login():
    delay_print("\nConnecting to 192.168.1.45 over SSH...")
    time.sleep(1)
    delay_print("Login prompt:")
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "omnicore123":
        delay_print("\nAccess granted.")
        delay_print("Welcome to OmniCore Internal Systems.")
        inside_system()
    else:
        delay_print("\nAccess denied. Too many failed attempts may trigger an alert.\n")
        main_menu()

def inside_system():
    delay_print("\nYou are now inside the target system.")
    delay_print("1. View system logs")
    delay_print("2. Extract password hash")
    delay_print("3. Exit system")

    choice = input("> ")

    if choice == "1":
        delay_print("\nSystem Logs:")
        delay_print("[INFO] User 'admin' logged in at 02:12 AM")
        delay_print("[WARNING] Unauthorized access attempt detected at 02:14 AM")
        inside_system()
    elif choice == "2":
        delay_print("\nExtracting password hash...")
        time.sleep(1)
        delay_print("Hash found: $6$rounds=5000$omni$abcdefghijk1234567890")
        delay_print("Mission accomplished. Disconnecting...\n")
    elif choice == "3":
        delay_print("Exiting system...")
    else:
        delay_print("Invalid choice.")
        inside_system()

# Start game
intro()
main_menu()
