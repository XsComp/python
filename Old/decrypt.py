# decrypt.py



from cryptography.fernet import Fernet

key_input = input("Enter your secret decryption key: ").strip().encode()

fernet = Fernet(key_input)
with open("encrypted_message.txt", "rb") as f:
    encrypted = f.read()

message = fernet.decrypt(encrypted).decode()
print("Decrypted message:", message)
