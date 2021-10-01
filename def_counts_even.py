def counts_even(x):
    counter = 0
    for i  in x:
        if i % 2 == 0:
            counter += 1
    return counter


a = counts_even([4, 2, 1, 6, 5, 9, 15, 18, 20])
print(a)