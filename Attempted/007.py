def genPrimes(limit):
    primes = list(range(2,int(limit)))
    current = 3
    while True:
        if current >= limit:
            break
        for value in range(2, current):
            if current % value == 0:
                primes.remove(current)
                break
        current += 1
    return primes

primes = genPrimes(1000000)
print(primes[10001])
input()
