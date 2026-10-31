a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = a, b
while y != 0:
 x, y = y, x % y
if x == 1:
 print("Numbers are Relatively Prime")
else:
 print("Numbers are Not Relatively Prime")
