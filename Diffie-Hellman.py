# Diffie-Hellman Key Exchange
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))
# Private keys
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))
# Public keys
A = pow(g, a, p)
B = pow(g, b, p)
print("Alice's public key:", A)
print("Bob's public key:", B)
# Shared secret keys
key_A = pow(B, a, p)
key_B = pow(A, b, p)
print("Alice's shared key:", key_A)
print("Bob's shared key:", key_B)
if key_A == key_B:
 print("Key Exchange Successful")
else:
 print("Key Exchange Failed")
