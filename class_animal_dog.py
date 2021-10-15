'''
File Created: Thursday, 14th October 2021 7:38:43 pm
@Author: Abinash1011
-----
Last Modified: Thursday, 14th October 2021 7:40:06 pm
Modified By: Abinash1011
-----
'''
class Animal:
    """
    animal class
    """
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        """
        prints habitat
        """
        print(self.habitat)

class Dog(Animal):
    """
    class dog sub-class of animal class
    """
    def __init__(self):
        super().__init__("kennel")

doge = Dog()
doge.print_habitat()
