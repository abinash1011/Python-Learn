'''
File Created: Thursday, 14th October 2021 8:34:38 am
@Author: Abinash1011
-----
Last Modified: Thursday, 14th October 2021 8:54:09 am
Modified By: Abinash1011
-----
'''
class Employee:
    def __init__(self, Id, name):
        self.Id = Id
        self.name = name

    def display(self):
        print(f'ID = {self.Id}\nName = {self.name}')

emp1 = Employee(1, "coder")
emp1.display()
del emp1.Id
try:
    print(emp1.Id)
except AttributeError:
    print("emp1.Id is not defined")

del emp1
try:
    emp1.display()
except NameError:
    print("emp1 is not defined")