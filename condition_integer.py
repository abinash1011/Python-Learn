num = int(input("Enter an Integer: "))
if num >= 1:
    print("Your number is a positive integer")
    if num > 0 and num < 100:
        print("Your number lies between 1 and 100")
elif num == 0:
    print("Zero is neither positive nor negative")
else:
    print("Your number is a negative integer")
