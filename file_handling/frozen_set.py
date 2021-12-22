'''
File Created: Sunday, 17th October 2021 7:30:42 pm
@Author: Abinash1011
-----
Last Modified: Sunday, 17th October 2021 7:33:06 pm
Modified By: Abinash1011
-----
'''
liist = [1, 2, 3, 4, 2, 4, 3, 2, 4, 1]
print(type(liist))
liist.append(5)
print(liist)

tuuple = tuple(liist)
print(tuuple)
print(type(tuuple))

seett = set(tuuple)         #tuple to set
print(seett)
print(type(seett))
seett2 = set(liist)         #list to set
print(seett2)

fs = frozenset(liist)
print(fs)
print(type(fs))
