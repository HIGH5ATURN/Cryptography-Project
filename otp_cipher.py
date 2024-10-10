import os

# Function to encrypt the plaintext
def one_time_pad_encrypt(plaintext):
    # Generate a random key of the same length as the plaintext
    key = os.urandom(len(plaintext))  # Generates a random key
    
    # Encrypt by XORing the plaintext with the key
    ciphertext = bytes([p ^ k for p, k in zip(plaintext.encode(), key)])
    
    return ciphertext, key

# Function to decrypt the ciphertext
def one_time_pad_decrypt(ciphertext, key):
    # Decrypt by XORing the ciphertext with the key
    decrypted_text = bytes([c ^ k for c, k in zip(ciphertext, key)])
    
    return decrypted_text.decode()  # Convert bytes back to string

# Menu-driven interface
if __name__ == "__main__":
    print("Welcome to the One-Time Pad Cipher!")

    while True:
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Get plaintext input from the user
            plaintext = input("Enter the plaintext to encrypt: ")

            # Encrypt the plaintext
            ciphertext, key = one_time_pad_encrypt(plaintext)
            print("\n--- Encryption Result ---")
            print(f"Generated key is (in bytes): {key}")

            print(f"Ciphertext (in bytes): {ciphertext}")


        elif choice == '2':
            # Get ciphertext and key from the user
            ciphertext = input("Enter the ciphertext (bytes): ")
            key = input("Enter the key (bytes): ")

            # Convert inputs from strings to bytes
            try:
                ciphertext = eval(ciphertext)
                key = eval(key)
                
                if not (isinstance(ciphertext, bytes) and isinstance(key, bytes)):
                    raise ValueError
            except:
                print("Error: Invalid input format. Please enter valid byte strings.")
                continue

            # Decrypt the ciphertext
            if len(ciphertext) != len(key):
                print("Error: The length of the ciphertext and key must be the same.")
            else:
                decrypted_text = one_time_pad_decrypt(ciphertext, key)
                print("\n--- Decryption Result ---")
                print(f"Decrypted text: {decrypted_text}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

