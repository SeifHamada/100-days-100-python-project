import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction):
    if direction == "encode":
        def encrypt(original_text, shift_amount):
            encrypted_text = ""
            for letter in original_text:
                if letter not in alphabet:
                    encrypted_text += letter
                else:
                    position = alphabet.index(letter) + shift_amount
                    if letter == "z":
                        position = alphabet.index(letter) + (shift_amount - 26)
                    encrypted_text +=alphabet[position]
            print(f"The encrypted text is: {encrypted_text}")
        encrypt(text, shift)

    elif direction == "decode":
        def decrypt(original_text, shift_amount):
            decrypted_text = ""
            for letter in original_text:
                if letter not in alphabet:
                    decrypted_text += letter
                else:
                    position = alphabet.index(letter) - shift_amount
                    if letter == "a":
                        position = alphabet.index(letter) - (shift_amount - 26)
                    decrypted_text += alphabet[position]
            print(f"The decrypted text is: {decrypted_text}")
        decrypt(text, shift)

    else:
        print("Please type 'encode' or 'decode'")



while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        print("Goodbye")
        break