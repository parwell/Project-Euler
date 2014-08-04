# Smallest Multiple
# Runtime 1001.763 seconds

import time
import math
start = time.time()

def smallestMultiple():
    numbers = [20,19,18,17,16,15,14,13,12,11]
    current = 1
    while True:
        values = []
        for number in numbers:
            values.append(isMultiple(current,number))
        if bigAnd(values):
            return current
        current += 1
    return current

def bigAnd(values):
	return False not in values

def isMultiple(a,b):
    return a % b == 0

print(smallestMultiple())
print("%.3f" % (time.time()-start))
input()
