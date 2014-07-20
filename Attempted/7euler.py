def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

test = 3
primes = 0

while primes < 10001:
    if is_prime(test):
        print(test)
        test += 1
        primes += 1
    else:
        continue

