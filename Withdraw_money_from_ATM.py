import random

#given
currency = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
total_notes_respectively = [random.randint(0,10) for _ in range(len(currency))]

#calculating total money:
totalMoneyInBank = 0
for a in range(len(currency)):
    totalMoneyInBank += currency[a] * total_notes_respectively[a]

print("The total money in this ATM is: ", totalMoneyInBank)    


amount_Out = int(input("Enter the amount of withdrawal: "))


if totalMoneyInBank >= amount_Out:
    numberOfNotes = []
    it_count = amount_Out

    for i, j in  enumerate(currency):
        if it_count // j <= total_notes_respectively[i]:
            numberOfNotes.append(it_count // j)
            it_count = it_count % j
        else:
            numberOfNotes.append(total_notes_respectively[i])
            it_count = it_count - total_notes_respectively[i] * currency[i]


    print("brrr brrr")
    print("\033[1mYou get:\033[0m")


    for j in range(len(currency)):
        if numberOfNotes[j] >= 1:
            print(f"₹{currency[j]} x {numberOfNotes[j]} ")
else:
    print("There is not enough money in the bank.")    

   




