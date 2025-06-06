from cryptography.fernet import Fernet

# Ask for the encryption/decryption key
key_input = input("Enter your secret key: ").strip()

# Ensure the input is treated as a proper byte key
try:
    fernet = Fernet(key_input.encode())
except Exception as e:
    print("Invalid key format. Fernet requires a base64-encoded 32-byte key.")
    exit()

# Function to encrypt a message and save it to a file
def encrypt_message():
    msg = input("Enter message to encrypt: ")
    encrypted = fernet.encrypt(msg.encode())
    with open("spy_message.txt", "wb") as f:
        f.write(encrypted)
    print("Encrypted message saved to spy_message.txt.")

# Function to decrypt a message from a file and print it
def decrypt_message():
    try:
        with open("spy_message.txt", "rb") as f:
            encrypted = f.read()
        decrypted = fernet.decrypt(encrypted).decode()
        print("\nDecrypted message:", decrypted)
    except Exception as e:
        print("Failed to decrypt:", e)

# Main menu function
def main():
    while True:
        print("\n--- SPY MENU ---")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            encrypt_message()
        elif choice == "2":
            decrypt_message()
        elif choice == "3":
            print("Mission complete. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
