a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
m = int(input("Enter modulus: "))
if m > 0:
 print("Addition:", (a + b) % m)
LINK: To be added
 print("Subtraction:", (a - b) % m)
 print("Multiplication:", (a * b) % m)
 print("Power:", pow(a, b, m))
else:
 print("Modulus must be positive")
