from array import *

arr1 = array('i', [58, 55, 8, 89, 82, 6, 31, 75, 42, 55])

for i in range(9):
    if arr1[0] >= arr1[1]:
        del arr1[1]
    else:
        del arr1[0]

print(arr1)