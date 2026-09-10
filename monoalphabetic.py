alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =     "QWERTYUIOPASDFGHJKLZXCVBNM"


def encrypt(text):
    result = ""

    for ch in text.upper():
        if ch in alphabet:
            result += key[alphabet.index(ch)]
        else:
            result += ch

    return result


def decrypt(text):
    result = ""

    for ch in text.upper():
        if ch in key:
            result += alphabet[key.index(ch)]
        else:
            result += ch

    return result


text = input("Enter message: ")

encrypted = encrypt(text)
print("Encrypted:", encrypted)

print("Decrypted:", decrypt(encrypted))
