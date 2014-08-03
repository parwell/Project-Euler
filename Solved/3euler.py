# Largest Prime Factor
# Runtime 0.005 seconds

import math
import time
start = time.time()

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
print("%.3f" % (time.time()-start))
input()
