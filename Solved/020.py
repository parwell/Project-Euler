# Factorial Digit Sum
# Runtime 0.000 seconds

import time
start = time.time()

total = 1

for i in range(1, 101):
    total *= i

total = str(total)
theSum = 0

for i in total:
    theSum += int(i)

print(theSum)
print("%.3f" % (time.time()-start))
input()
