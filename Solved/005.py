# Smallest Multiple
# Runtime 42.425 seconds

import time
import math
start = time.time()

def smallestMultiple():
    numbers = [20,19,18,17,16,15,14,13,12,11]
    current = 20
    while True:
        values = []
        for number in numbers:
            values.append(isMultiple(current,number))
        if False not in values:
            return current
        current += 20
    return current

def isMultiple(a,b):
    return a % b == 0

print(smallestMultiple())
print("%.3f" % (time.time()-start))
input()
