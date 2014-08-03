# Self Powers
# Runtime 0.015 seconds

import time
start = time.time()

def selfPowerSum(n):
    total = 0
    for i in range(1, n):
        total += i ** i
    return total

answer = str(selfPowerSum(1000))
print(answer[-10:])
print("%.3f" % (time.time()-start))
input()
