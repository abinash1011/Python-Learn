LOST_IN_FOREST = "You are still lost in the forest"


print("try to get out of the forest")
print("###########################\n###########################\n#####      → ↑     ########\n#####  :o          ########\n#####      → ↓     ########\n###########################\n###########################")

counter = 0
res = input("go Left(L) or Right(R) : ")

while res == "L" or res == "l":
    counter += 1
    print(LOST_IN_FOREST , counter)
    print("try to get out of the forest")
    print("###########################\n###########################\n#####      → ↑     ########\n#####  :o          ########\n#####      → ↓     ########\n###########################\n###########################\n-----------------------------")
    res = input("go Left(L) or Right(R) : ")
    if counter == 2 or counter == 3:
        print(LOST_IN_FOREST)
        print("try to get out of the forest 2or3")
        print("###########################\n###########################\n#####      → ↑     ########\n#####  :'(         ########\n#####      → ↓     ########\n###########################\n###########################\n-----------------------------")
        res = input("go Left(L) or Right(R) : ")

    if counter == 4:
        print(LOST_IN_FOREST)
        print("try to get out of the forest 4")
        print("###########################\n###########################\n#####                ######\n##### (╯°□°）╯︵ ┻━┻ ######    \n#####                ######\n###########################\n###########################")
        print("You LOSE\n-----------------------------")
        counter += 1
        break

if res == "R" or res == "r":
    print("You are out of the forest\n         ヽ(^o^)ノ")
