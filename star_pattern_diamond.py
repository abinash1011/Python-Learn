'''
File Created: Sunday, 26th September 2021 11:05:39 am
@Author: Abinash1011
-----
Last Modified: Sunday, 17th October 2021 8:19:29 pm
Modified By: Abinash1011
-----
'''
num_rows = int(input("enter the no. of stars in middle row: "))

for i in range(0, num_rows):
    for j in range(0, num_rows - i - 1):
        print(end=" ")
    for k in range(0, i + 1):
        print("*", end=" ")
    print()

for i in range(num_rows-1, 0, -1):
    for j in range(num_rows - i, 0, -1):
        print(end=" ")
    for k in range(i, 0, -1):
        print("*", end=" ")
    print()
