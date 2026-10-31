n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
 a = n
 b = i
 while b != 0:
 a, b = b, a % b
 if a == 1:
 count += 1
print("Euler's Totient:", count)
