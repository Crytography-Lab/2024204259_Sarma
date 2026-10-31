a = int(input("Enter a: "))
p = int(input("Enter prime number p: "))
if p > 1:
 if a % p != 0:
 result = pow(a, p - 1, p)
 print("Result:", result)
 print("Fermat's Little Theorem Verified")
 else:
 print("a should not be divisible by p")
else:
 print("Enter a valid prime number")
