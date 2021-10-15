'''
File Created: Thursday, 14th October 2021 8:34:38 am
@Author: Abinash1011
-----
Last Modified: Thursday, 14th October 2021 8:54:09 am
Modified By: Abinash1011
-----
'''
class Employee:
    """
    Employee class
    """
    def __init__(self, id_no, name):
        self.id_no = id_no
        self.name = name

    def display(self):
        """
        display
        """
        print(f'id_no = {self.id_no}\nName = {self.name}')


if __name__ == "__main__":
    emp1 = Employee(1, "coder")
    emp1.display()
    del emp1.id_no
    try:
        print(emp1.id_no)
    except AttributeError:
        print("emp1.id_no is not defined")

    del emp1
    try:
        emp1.display()
    except NameError:
        print("emp1 is not defined")
