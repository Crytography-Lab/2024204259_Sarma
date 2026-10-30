text = input("Enter text: ").replace(" ", "").upper()
rails = int(input("Enter number of rails: "))
# Encryption
fence = [[] for _ in range(rails)]
row = 0
direction = 1
for ch in text:
 fence[row].append(ch)
 if row == 0:
 direction = 1
 elif row == rails - 1:
 direction = -1
 row += direction
encrypted = ""
for r in fence:
 encrypted += "".join(r)
print("Encrypted text:", encrypted)
# Decryption
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
# Put encrypted characters into rails
fence = [[] for _ in range(rails)]
index = 0
for r in range(rails):
 for i in range(len(pattern)):
 if pattern[i] == r:
 fence[r].append(encrypted[index])
 index += 1
# Read zig-zag
positions = [0] * rails
decrypted = ""
for r in pattern:
 decrypted += fence[r][positions[r]]
 positions[r] += 1
print("Decrypted text:", decrypted)
