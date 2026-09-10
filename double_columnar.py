def encrypt(text, key):
    text = text.upper().replace(" ", "")

    
    result = ""

    for n in sorted(key):
        col = key.index(n)

        for i in range(col, len(text), len(key)):
            result += text[i]

    
    text = result
    result = ""

    for n in sorted(key):
        col = key.index(n)

        for i in range(col, len(text), len(key)):
            result += text[i]

    return result


def decrypt(text, key):
    cols = len(key)
    rows = len(text) // cols

    order = sorted(range(cols), key=lambda x: key[x])

   
    matrix = [""] * cols
    index = 0

    for col in order:
        matrix[col] = text[index:index + rows]
        index += rows

    result = ""

    for i in range(rows):
        for j in range(cols):
            result += matrix[j][i]

    
    text = result
    matrix = [""] * cols
    index = 0

    for col in order:
        matrix[col] = text[index:index + rows]
        index += rows

    result = ""

    for i in range(rows):
        for j in range(cols):
            result += matrix[j][i]

    return result


message = input("Enter message: ")
key = [3, 1, 4, 2]

encrypted = encrypt(message, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, key))
