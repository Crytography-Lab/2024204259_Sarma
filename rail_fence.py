def encrypt(text, rails):
    fence = [""] * rails
    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join(fence)


def decrypt(text, rails):
    pattern = []
    row = 0
    direction = 1

    for i in range(len(text)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    result = [""] * len(text)
    index = 0

    for r in range(rails):
        for i in range(len(text)):
            if pattern[i] == r:
                result[i] = text[index]
                index += 1

    return "".join(result)


message = input("Enter message: ")
rails = int(input("Enter number of rails: "))

encrypted = encrypt(message, rails)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, rails)
print("Decrypted:", decrypted)
