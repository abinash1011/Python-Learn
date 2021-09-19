lower = int(input("enter your lower limit: "))
upper = int(input("enter your upper limit: "))
if lower % 2 == 0:
    lower += 1
if lower == 1:
    lower += 1
if upper < lower:
    print("Upper should always be more than lower")
else:

    for i in range(lower, upper):
        if i == 2:
            print(i)
            continue
        counter = 0
        for j in range(2, i):
            if i % j == 0:
                counter += 1
                break
        if counter == 0:
            print(i)
