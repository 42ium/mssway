def vi(message, key, dirction):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""
    key_index = 0
    message = message.lower()
    for char in message:
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = (offset*dirction + alphabet.index(char)) % len(alphabet)
            final_message += alphabet[index]
    return final_message

def encrypt(message, key):
    return vi(message, key, 1)

def decrypt(message, key):
    return vi(message, key, -1)

def main():
    print("Welcome to Vigenere Cipher!")
    while True:
        input_message = input("Please choose one function : encrypt(1) decrypt(2) quit(3) ")
        if(input_message == "1"):
            message = input("Enter your message: ")
            key = input("Enter your key: ")
            print(encrypt(message, key))
        elif(input_message == "2"):
            message = input("Enter your message which you want to decrypt: ")
            key = input("Enter your key: ")
            print(decrypt(message, key))
        elif(input_message == "3"):
            print("Quitting...")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
