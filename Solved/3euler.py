factors = []

number = 10086647

for i in range(2, number):
    if  number % i == 0:
        factors.append(i)
        number = i
        print(factors)


print(839)
print(71)
input()
