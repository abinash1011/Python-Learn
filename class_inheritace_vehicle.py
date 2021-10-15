'''
File Created: Thursday, 14th October 2021 10:19:52 am
@Author: Abinash1011
-----
Last Modified: Thursday, 14th October 2021 10:21:29 am
Modified By: Abinash1011
-----
'''
class Vehicle:
    """
    vehicle class
    """
    @staticmethod
    def general_usage():
        """
        prints general usage of class vehicle
        """
        print("General usage: transportation")

class Car(Vehicle):
    """
    sub class of vehicle class
    """
    def __init__(self):
        print("I'm a Car")
        self.wheels = 4
        self.has_roof = True

    @staticmethod
    def specific_usage():
        """
        prints specific usage of sub class car
        """
        print("Specific use: commute to work,vacation with family")


class Motorcycle(Vehicle):
    """
    sub class of vehicle class
    """
    def __init__(self):
        print("I'm a Motorcycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        """
        prints specific usage of sub class motorcycle
        """
        print(f"Specific use: road trip, racing, wheels : {self.wheels}")


if __name__ == "__main__":
    c_object = Car()
    c_object.general_usage()
    c_object.specific_usage()

    m_object = Motorcycle()
    m_object.general_usage()
    m_object.specific_usage()
