# 5euler
# Runtime -.--- seconds

import time
start = time.time()

def smallestMultiple(limit):
    numbers = list(range(1,limit+1))
    current = limit*(limit-1)
    while True:
        values = []
        print(current)
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


print(smallestMultiple(10))
print("%.3f" % (time.time()-start))
input()
