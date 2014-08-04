# Special Pythagorean Triplet
# Runtime 18.119s seconds

import time
start = time.time()

def genTriples(upper):
    triples =[]
    for a in range(1,upper+1):
        for b in range(a,upper+1):
            for c in range(b,a+b):
                if a**2 + b**2 == c**2:
                    if a + b + c <= 1000:
                        triple = [a,b,c]
                        triple.sort()
                        if triple not in triples:
                            triples.append(triple)
    return triples

def checkCriteria(triple):
    a = triple[0]
    b = triple[1]
    c = triple[2]
    return a + b + c == 1000

def findTriple(upper):
    triples = genTriples(upper)
    for triple in triples:
        if checkCriteria(triple):
            return triple
    return "Not found."

def multiplyTriple(triple):
    a = triple[0]
    b = triple[1]
    c = triple[2]
    return a * b * c

print(multiplyTriple(findTriple(400)))
print("%.3f" % (time.time()-start))
input()
