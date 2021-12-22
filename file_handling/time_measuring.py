'''
File Created: Sunday, 17th October 2021 8:10:11 pm
@Author: Abinash1011
-----
Last Modified: Sunday, 17th October 2021 8:15:32 pm
Modified By: Abinash1011
-----
'''
import time
start_time = time.time()
print("hello")
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

end_time = time.time()
print((end_time - start_time)* 1000, "milliseconds")
