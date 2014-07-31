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

def primeFacs(number):
    factors = []
    current = 2
    while current <= number:
        if number % current == 0:
            number /= current
            factors.append(current)
        else:
            current += 1
    factors.sort()
    return factors


number = 600851475143
print(max(primeFacs(number)))
input()
