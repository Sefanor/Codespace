def isPrime(n):
    if n <= 1:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False

    return True

for n in range(0,21):
    print(f"Is {n} a prime? {isPrime(n)}")