sum_squares = 0
square_sum = 0

for i in range(1, 101):
    i = i ** 2
    sum_squares += i

for i in range(1, 101):
    square_sum += i

square_sum = square_sum * square_sum

print(square_sum - sum_squares)
input()
