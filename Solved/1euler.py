# Multiples of 3 and 5


total = 0

for i in range(1, 1000):
    if i % 5 == 0 or i % 3 == 0:
        total += i
    elif i % 5 == 0 and i % 3 == 0:
        total -= i
    else:
        continue

print(total)
input()
