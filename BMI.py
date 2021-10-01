name = input("Enter your name: ")
weight = float(input("Enter your weight in kgs: "))
height_cms = float(input("enter your height in cms: "))

height = height_cms / 100

BMI = weight/(height ** 2)
print("BMI =", BMI)

if BMI >= 25:
    print(name + ", you are over-weight")
else:
    print(name + ", you are not over-weight")