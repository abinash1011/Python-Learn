def BMI_Calculator(name, height, weight):
    BMI = weight / (height ** 2)
    print(BMI)
    if BMI < 25:
        return name + " is not over-weight"
    else:
        return name + " is over-weight"


bhai = BMI_Calculator("ashutosh", 1.95, 105)
print(bhai)
