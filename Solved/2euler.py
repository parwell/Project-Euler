# Even Fibonacci Numbers
# Runtime 0.000 seconds

import time
start = time.time()

def genFibs(limit):
    first = 1
    second = 2
    numbers = [1,2]
    current = 0
    while True:
        current = first + second
        if current >= limit:
            break
        numbers.append(current)
        first = second
        second = current
    return numbers

def getEvens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

    
numbers = getEvens(genFibs(4000000))
print(str(sum(numbers)))
print("%.3f" % (time.time()-start))
input()
