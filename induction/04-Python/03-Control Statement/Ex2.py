a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

if a > b and b > c:
    print("Decreasing order")
elif a < b and b < c:
    print("Increasing order")
else:
    print("Neither increasing or decreasing order")