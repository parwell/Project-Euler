# Summation of Primes

import math
import time
start = time.time()

# Generates all the prime numbers up to an upper limit
def genPrimes(limit):
    primes = list(range(2,int(limit)))
    current = 3
    while True:
        if current >= limit:
            break
        if not isPrime(current):
            if current in primes:
                primes.remove(current)
        else:
            multiples = getMultiples(primes,current)
            multiples.pop()
            for multiple in multiples:
                if multiple in primes:
                    primes.remove(multiple)
        current += 1
    return primes

# Finds multiples of a number in a list
def getMultiples(numbers,base):
    return [number for number in numbers if number % base == 0]

# Checks whether a number is prime
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    pivot = int(math.sqrt(n))+1
    for divisor in range(3, pivot, 2):
        if n % divisor == 0:
            return False
    return True

print(sum(genPrimes(2000000)))
print("%.3f" % (time.time()-start)+" seconds")
input()
