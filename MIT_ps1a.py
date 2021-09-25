total_cost = float(input("Enter the cost ofYour dream home: "))
portion_down_payment = 0.25 * total_cost

annual_salary = float(input("EnterYour annual salary: "))

portion_saved = float(input("Enter the percent ofYour salary to save, as a decimal: "))
portion_saved_salary = (annual_salary/12)*portion_saved

r = 0.04

current_saving = 0

month = 0

while current_saving <= portion_down_payment:
    current_saving += (current_saving * r/12 + portion_saved_salary)
    month = month + 1

print("No. of months: ", month)
