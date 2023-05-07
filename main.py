def fibonacci(n):
    if n < 0:
        raise ValueError("n tem que ser maior do que zero")
    if type(n) != int:
        raise ValueError("n tem que ser inteiro")
    fib = [0,1]
    if n == 0:
        return fib[0]
    for i in range(2,n+1):
        fib.append(fib[-1] + fib[-2])
    return fib.pop()