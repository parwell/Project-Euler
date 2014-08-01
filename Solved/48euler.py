# Self Powers

def selfPowerSum(n):
    total = 0
    for i in range(1, n):
        total += i ** i
    return total

answer = str(selfPowerSum(1000))
print(answer[-10:])
input()
