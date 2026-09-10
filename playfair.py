def make_matrix(key):
    key = key.upper().replace("J", "I")
    letters = ""

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in letters:
            letters += ch

    return [letters[i:i+5] for i in range(0, 25, 5)]


def find(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            result += a + "X"
            i += 1

        elif text[i] == text[i+1]:
            result += a + "X"
            i += 1

        else:
            result += a + text[i+1]
            i += 2

    return result


def encrypt(text, matrix):
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find(matrix, a)
        r2, c2 = find(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1+1)%5]
            result += matrix[r2][(c2+1)%5]

        elif c1 == c2:
            result += matrix[(r1+1)%5][c1]
            result += matrix[(r2+1)%5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


def decrypt(text, matrix):
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find(matrix, a)
        r2, c2 = find(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1-1)%5]
            result += matrix[r2][(c2-1)%5]

        elif c1 == c2:
            result += matrix[(r1-1)%5][c1]
            result += matrix[(r2-1)%5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
message = input("Enter message: ")

matrix = make_matrix(key)

print("\nMatrix:")
for row in matrix:
    print(row)

prepared = prepare(message)

encrypted = encrypt(prepared, matrix)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, matrix)
print("Decrypted:", decrypted)
