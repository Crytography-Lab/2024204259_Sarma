from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
text = input("Enter text: ").encode()
# Encryption
cipher = AES.new(key, AES.MODE_EAX)
encrypted, tag = cipher.encrypt_and_digest(text)
LINK: To be added
print("Encrypted text:", encrypted.hex())
# Decryption
decipher = AES.new(key, AES.MODE_EAX,
nonce=cipher.nonce)
decrypted = decipher.decrypt(encrypted)
try:
 decipher.verify(tag)
 print("Decrypted text:", decrypted.decode())
except ValueError:
 print("Decryption failed")
