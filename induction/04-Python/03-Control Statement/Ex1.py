a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

if a == b and b == c:
    print("All numbers are equal")
elif (a == b and b != c) or (a == c and b != c):
    print("Neither all are equal or different")
else:
    print("All numbers are different")