# Sum Square Difference
# Runtime 0.000 seconds

import time
start = time.time()

sumSquares = 0
squareSum = 0

for i in range(1, 101):
    i = i ** 2
    sumSquares += i

for i in range(1, 101):
    squareSum += i

squareSum *= squareSum

print(squareSum - sumSquares)
print("%.3f" % (time.time()-start))
input()
