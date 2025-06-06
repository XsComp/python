from cryptography.fernet import Fernet

# Ask spy to enter the encryption key manually
key_input = input("Enter your secret encryption key: ").strip().encode()

# Create a Fernet object with the entered key
fernet = Fernet(key_input)

# Ask for the message to encrypt
message = input("Enter message to encrypt: ")

# Encrypt the message
enc_message = fernet.encrypt(message.encode())

# Save encrypted message to a file
with open("encrypted_message.txt", "wb") as f:
    f.write(enc_message)

# Confirm success
print("🔐 Message encrypted and saved to 'encrypted_message.txt'")