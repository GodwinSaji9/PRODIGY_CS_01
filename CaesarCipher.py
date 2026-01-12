def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_value = ord(char)

            if char.isupper():
                new_char = chr((ascii_value - 65 + shift) % 26 + 65)
            else:
                new_char = chr((ascii_value - 97 + shift) % 26 + 97)

            result += new_char
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1 or 2): ")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    print("Encrypted message:", encrypt(message, shift))
elif choice == "2":
    print("Decrypted message:", decrypt(message, shift))
else:
    print("Invalid choice")
