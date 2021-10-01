a = [1, 3, 5, 7, 9, 11]
b = list()
for i in  a:
    b.append(2*i)
print(b)

c = [x*2 for x in a]
print(c)