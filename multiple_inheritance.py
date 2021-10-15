'''
File Created: Friday, 15th October 2021 9:23:48 am
@Author: Abinash1011
-----
Last Modified: Friday, 15th October 2021 9:26:17 am
Modified By: Abinash1011
-----
'''

class Father():
    """
    father class -> BASE CLASS
    """
    @staticmethod
    def skills():
        """
        returns skills
        """
        return "gardening, programming"

    @staticmethod
    def job():
        """
        prints job of the father class
        """
        print("computer programmer")

class Mother():
    """
    mother class -> BASE CLASS
    """
    @staticmethod
    def skills():
        """
        returns skills of the father class
        """
        return ("cooking, art")

    @staticmethod
    def job():
        """
        prints job
        """
        print("housewife")

class Child(Father, Mother):
    """
    child class -> DERIVED CLASS
    """
    @staticmethod
    def skills():
        """
        prints skills
        """

        print(f"sports, {Father.skills()}, {Mother.skills()}")

    @staticmethod
    def job():
        """
        prints job of the child class
        """
        print("student")

if __name__ == "__main__":

    Zhongli = Father()
    print(Zhongli.skills())
    Childe = Child()
    Childe.skills()
    Childe.job()
