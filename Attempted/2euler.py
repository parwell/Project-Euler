# Even Fibonacci Numbers

def gen_fib(maximum):
    a = 0
    b = 1

    cap = 0
    fibs = []
    
    while cap < maximum:
        fib = a + b
        fibs += str(fib)
        a = b
        b = a + b
        cap = fib

gen_fib(4000000)
print(sum(int(fibs)))
        
