a = int(input("Enter a: "))
m = int(input("Enter modulus: "))
if m > 1:
 if __import__('math').gcd(a, m) == 1:
 inverse = pow(a, -1, m)
 print("Multiplicative Inverse:", inverse)
 else:
 print("Multiplicative Inverse does not exist")
else:
 print("Modulus must be greater than 1")
