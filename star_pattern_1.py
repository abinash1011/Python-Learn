max_star = int(input("Enter an odd number: "))

if max_star % 2 == 0:
    print(max_star, "is not an odd number")
else:
    for i in range(max_star, 0, -1):
        for j in range(i, max_star, 1):
            print(" ", end="")
        for k in range(i, 0, -1):
            print("* ", end="")
        print()