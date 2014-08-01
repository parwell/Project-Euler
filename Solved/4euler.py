import time
start = time.time()

def findProducts():
    products = []
    for x in range(100,1000):
        for y in range(100,1000):
            products.append(x*y)
    return products

def isPalindrome(number):
    return str(number) == str(number)[::-1]

def getPalindromes(numbers):
    palindromes = []
    for number in numbers:
        if isPalindrome(number):
            palindromes.append(number)
    return palindromes

print(max(getPalindromes(findProducts())))
print("%.3f" % (time.time()-start))
input()
