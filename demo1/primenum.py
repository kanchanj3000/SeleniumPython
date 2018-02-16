def Is_prime(n):
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return False


for n in range(1,500):
    if Is_prime(n) is None:
        print n
