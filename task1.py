def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Encrypt the character and wrap around using modulo
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Non-alphabetic characters are unchanged
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    return caesar_encrypt(encrypted_message, -shift)  # Decrypting is just encrypting with negative shift

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Would you like to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            shift = int(input("Enter shift value (0-25): "))
            if choice == 'E':
                encrypted_message = caesar_encrypt(message, shift)
                print(f"Encrypted message: {encrypted_message}")
            elif choice == 'D':
                decrypted_message = caesar_decrypt(message, shift)
                print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please choose E, D, or Q.")

if __name__ == "__main__":
    main()