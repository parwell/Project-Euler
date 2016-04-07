# Special Pythagorean Triplet
# Runtime 0.016 seconds

import time
start = time.time()

def findTriple(upper):
    triples =[]
    for a in range(1,upper+1):
        for b in range(a,upper+1):
            for c in range(b,a+b):
                if a**2 + b**2 == c**2:
                    if a + b + c <= 1000:
                        triple = [a,b,c]
                        if checkCriteria(triple):
                            i = 2
                            while True:
                                a *= i
                                b *= i
                                c *= i
                                if a + b + c == 1000:
                                    return [a,b,c]
                                a /= i
                                b /= i
                                c /= i
                                i += 1
    return 'Not found.'

def checkCriteria(triple):
    a = triple[0]
    b = triple[1]
    c = triple[2]
    return 1000 % (a + b + c) == 0

def multiplyTriple(triple):
    a = triple[0]
    b = triple[1]
    c = triple[2]
    return a * b * c

print(multiplyTriple(findTriple(400)))
print("%.3f" % (time.time()-start))
input()
