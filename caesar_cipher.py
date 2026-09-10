def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - 65 + key) % 26 + 65)
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - 65 - key) % 26 + 65)
        else:
            result += ch

    return result


text = input("Enter message: ")
key = int(input("Enter key: "))

encrypted = encrypt(text, key)
print("Encrypted:", encrypted)

print("Decrypted:", decrypt(encrypted, key))
