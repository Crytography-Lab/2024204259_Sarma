text = input("Enter text: ").replace(" ", "").upper()
key = input("Enter key: ").upper()
# Encryption
columns = len(key)
rows = (len(text) + columns - 1) // columns
# Add X as padding
text += "X" * (rows * columns - len(text))
matrix = []
for i in range(rows):
 matrix.append(list(text[i * columns:(i + 1) *
columns]))
order = sorted(range(columns), key=lambda x: key[x])
encrypted = ""
for col in order:
 for row in range(rows):
 encrypted += matrix[row][col]
print("Encrypted text:", encrypted)
# Decryption
matrix = [[""] * columns for _ in range(rows)]
index = 0
for col in order:
 for row in range(rows):
 matrix[row][col] = encrypted[index]
 index += 1
decrypted = ""
for row in range(rows):
 for col in range(columns):
 decrypted += matrix[row][col]
print("Decrypted text:", decrypted.rstrip("X"))
