'''
File Created: Monday, 11th October 2021 6:12:54 pm
@Author: Abinash1011
-----
Last Modified: Monday, 11th October 2021 6:28:33 pm
Modified By: Abinash1011
-----
'''
import random
import functools
data = random.sample(range(0, 99), 10)
print(data)

evens = list(filter(lambda n : n % 2 == 0, data))
print(evens)

doubles = list(map(lambda x : x * 2 ,evens))
print(doubles)

sum = functools.reduce(lambda a, b : a + b, doubles )
print(sum)
