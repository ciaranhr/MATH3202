
fib_d = {}

def fib(n):
    if n in fib_d:
        return fib_d[n]
    if n <= 2:
        fib_d[n]= 1
    else:
        fib_d[n] = fib(n-1) + fib(n-2)
    return fib_d[n]
    
print(fib(12))