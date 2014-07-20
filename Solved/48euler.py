# Self Powers

def self_power(n):
    total = 0
    for i in range(1, n):
        total += i ** i
    return total

the_sum = str(self_power(1000))
print(the_sum[-10:])
input()
