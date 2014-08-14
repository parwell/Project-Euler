# Multiples of 3 and 5
# Runtime 0.000 seconds

import time
start = time.time()

print(sum(i for i in range(1000) if (i%3==0) or (i%5==0)))
print("%.3f" % (time.time()-start))
input()
