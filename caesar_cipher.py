def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Interactive version
if __name__ == "__main__":
    while True:
        # Display options to the user
        print("\nCaesar Cipher Tool")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift_value = int(input("Enter the shift value (integer): "))
            encrypted = caesar_cipher_encrypt(message, shift_value)
            print(f"Encrypted Message: {encrypted}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift_value = int(input("Enter the shift value (integer): "))
            decrypted = caesar_cipher_decrypt(message, shift_value)
            print(f"Decrypted Message: {decrypted}")

        elif choice == '3':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

