from math import sqrt
for i in range(1, 50):
    sq_rt = int(sqrt(i))
    if sq_rt*sq_rt == i:
        print(i)
