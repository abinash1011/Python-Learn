def fib(n):
    if n == 2 or n == 1:
        return 1
    if n >= 3:
        return fib(n - 1) + fib(n - 2)


a = fib(6)
print(a)