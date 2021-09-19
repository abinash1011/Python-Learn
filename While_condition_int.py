num = None
while num is None:
    input_val = input("Enter an Integer: ")
    try:
        num = int(input_val)
    except ValueError:
        print("{input} is not an integer, please enter an integer only".format(
            input=input_val))

if num >= 1:
    print("Your number is a positive integer")
    if num > 0 and num < 100:
        print("Your number lies between 1 and 100")

elif num == 0:
    print("Zero is neither positive nor negative")
else:
    print("Your number is a negative integer")
