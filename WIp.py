def string_times(str, n):
    return str * n

a = string_times('hi', 3)
print(a)

def greet(x):
    return "Hello " + x + "!"


b = greet("Bob")
print(b)


def first_last6(list):
    return list[0] == 6 or list[len(list)-1] == 6


c = first_last6([1, 5, 9, 6])
print(c)