from array import *

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
    
