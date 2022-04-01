
def fibonacci_tab(n):
    fib = [0 for i in range(n + 1)]
    fib[0] = 0
    fib[1] = 0
    fib[2] = 1

    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

print(fibonacci_tab(7))
