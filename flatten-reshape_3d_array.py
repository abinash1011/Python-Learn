import numpy as np

arr1 = np.array([
                    [22, 5, 16, 11, 4, 9],
                    [6, 48, 24, 55, 25, 44]
                ])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2, 2, 3)
print(arr3)
