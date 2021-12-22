'''
File Created: Thursday, 4th November 2021 11:04:58 am
@Author: Abinash1011
-----
Last Modified: Thursday, 4th November 2021 11:08:55 am
Modified By: Abinash1011
-----
'''
import time
def gcd(num1, num2):
    '''
    find the greatest common divisor by using Euclidian algorithm.
    '''
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

start_time = time.time()
print(gcd(148545484, 1585845484))
end_time = time.time()
print((end_time - start_time)*1000)
print(time.time())
