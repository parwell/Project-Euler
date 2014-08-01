# Factorial Digit Sum

total = 1

for i in range(1, 101):
    total *= i

total = str(total)
theSum = 0

for i in total:
    theSum += int(i)

print(theSum)
input()
