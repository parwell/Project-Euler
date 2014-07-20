# Factorial Digit Sum

total = 1

for i in range(1, 101):
    total *= i

total = str(total)
print(total)

sum_digits = total.split()

the_sum = 0

for i in sum_digits:
    the_sum += i

print(the_sum)
