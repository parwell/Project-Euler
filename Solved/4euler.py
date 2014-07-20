products = []

for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if product not in products:
            if str(product) == str(product)[::-1]:
                products.append(product)

print("Largest palindrome: " + str(max(products)))
input()
