
def encrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    text += 'X' * (rows * cols - len(text))

    table = []
    for i in range(rows):
        table.append(text[i*cols:(i+1)*cols])

    result = ""

    for k in sorted(key):
        col = key.index(k)
        for row in table:
            result += row[col]

    return result


def decrypt(text, key):
    cols = len(key)
    rows = len(text) // cols

    table = [[''] * cols for _ in range(rows)]

    pos = 0
    for k in sorted(key):
        col = key.index(k)
        for row in range(rows):
            table[row][col] = text[pos]
            pos += 1

    result = ""
    for row in table:
        result += ''.join(row)

    return result


text = input("Enter message: ").replace(" ", "").upper()
key1 = input("Enter first key: ")
key2 = input("Enter second key: ")


encrypted = encrypt(encrypt(text, key1), key2)
print("Encrypted:", encrypted)


decrypted = decrypt(decrypt(encrypted, key2), key1)
print("Decrypted:", decrypted)

