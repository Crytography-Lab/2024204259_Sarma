from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
key = b'12345678'
text = input("Enter text: ").encode()
# Encryption
cipher = DES.new(key, DES.MODE_ECB)
encrypted = cipher.encrypt(pad(text, 8))
print("Encrypted text:", encrypted.hex())
# Decryption
decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(encrypted), 8)
print("Decrypted text:", decrypted.decode())
