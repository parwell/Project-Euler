# Truncatable Primes
# Runtime -.--- seconds

import math
import time
start = time.time()


# Checks whether a number is prime
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    pivot = int(math.sqrt(n))+1
    for divisor in range(3, pivot, 2):
        if n%divisor == 0:
            return False
    return True


# Generates all the prime numbers up to an upper limit
def genPrimes(limit, start=2):
    primes = list(range(start,int(limit)))
    current = 3
    while True:
        if current >= limit:
            break
        if not isPrime(current):
            if current in primes:
                primes.remove(current)
        else:
            multiples = getMultiples(primes,current)
            if multiples:
                multiples.pop(0)
            for multiple in multiples:
                if multiple in primes:
                    primes.remove(multiple)
        current += 1
    return primes


# Finds multiples of a number in a list
def getMultiples(numbers,base):
    return [number for number in numbers if number % base == 0]


def isTruncatable(n):
    n = str(n)
    if len(n) == 1:
        return False
    for i in range(len(n)-1):
        x = n[:i+1]
        x = int(x)
        if not isPrime(x):
            return False
    for i in range(len(n)-1):
        x = n[i+1:]
        x = int(x)
        if not isPrime(x):
            return False
    return True

def findTruncs(amount):
    truncs = []
    primes = genPrimes(10000)
    start = 10000
    while len(truncs) < amount+1:
        for prime in primes:
            if isTruncatable(prime):
                truncs.append(prime)
                print(truncs)
        primes = genPrimes(start, start+100)
    return truncs

print(sum(findTruncs(11)))
print("%.3f" % (time.time()-start))
input()
