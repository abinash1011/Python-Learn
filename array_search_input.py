'''
File Created: Sunday, 19th September 2021 7:50:02 pm
@Author: Abinash1011
-----
Last Modified: Thursday, 4th November 2021 11:08:13 am
Modified By: Abinash1011
-----
'''

from array import array
arr = array('i', [])
n = int(input("how many numbers do u want to enter?"))

for i in range(n):
    x = int(input("enter the number: "))
    arr.append(x)
print(arr)

f = int(input("search for which number: "))

k = 0
for l in arr:
    if l == f:
        print(k)
        break
    k += 1
