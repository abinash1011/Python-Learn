import numpy as np

#aliasing
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1
print(arr2)
print(id(arr1))
print(id(arr2))

#shalllow copy
arr3 = np.array([1, 2, 3, 4, 5])
arr4 = arr3.view()
print(arr4)
print(id(arr3))
print(id(arr4))

#deep copy
arr5 = np.array([1, 2, 3, 4, 5])
arr6 = arr5.copy()
print(arr5)
print(arr6)
print(id(arr5))
print(id(arr6))
arr5[2] = 9
print(arr5)
print(arr6)
print(id(arr5))
print(id(arr6))
