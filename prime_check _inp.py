number = int(input("enterYour number: "))
for j in range(2, int(number/2) + 1):
    if number % j == 0:
        print(number, "is  not a prime number")
        break
else:
    print(number, "is a prime number")
