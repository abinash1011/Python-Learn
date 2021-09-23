#sum of two matrices using 2-D array and loops

import numpy as np

arr1 = np.array([
                 [1, 2, 3],
                 [4, 5, 6]
                ])
arr2 = np.array([
                 [7, 8],
                 [9, 10],
                 [11, 12]
                ])
arr3 = arr1.flatten()
arr4 = arr2.flatten()

arr5 = []
for i in range(0,6,2):
    print(arr4[i])
    print(arr3[i/2])