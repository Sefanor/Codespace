sample_n = 6

def factorial(n):
    tot = 1
    for i in range(n,0,-1):
        tot *= i
    return tot


print(factorial(sample_n))
    