from array import *

arr1 = array('i', [2, 4, 8, 16])
arr2 = array('i', [1, 1, 1, 1])
arr3 = array('i', [])

for i in range(4):
    sum = arr1[i] + arr2[i]
    arr3.append(sum)

print(arr3)