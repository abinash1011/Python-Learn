def binary(n):
    if n == 0:
        return 0
    return n % 2 + 10 * binary(int(n / 2))

a = binary(70)
print(a)