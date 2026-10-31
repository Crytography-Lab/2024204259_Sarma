from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
# Key Generation
key = DSA.generate(2048)
private_key = key
public_key = key.publickey()
print("DSA Keys Generated Successfully")
# Message
message = input("Enter message: ").encode()
# Hash the message
hash_value = SHA256.new(message)
# Create Digital Signature
signer = DSS.new(private_key, 'fips-186-3')
signature = signer.sign(hash_value)
print("Digital Signature:", signature.hex())
# Verify Digital Signature
hash_value = SHA256.new(message)
verifier = DSS.new(public_key, 'fips-186-3')
try:
 verifier.verify(hash_value, signature)
 print("Signature is valid")
except ValueError:
 print("Signature is invalid")
