'''
File Created: Sunday, 17th October 2021 11:11:48 am
@Author: Abinash1011
-----
Last Modified: Sunday, 17th October 2021 11:15:00 am
Modified By: Abinash1011
-----
'''

import time

class Remote():
    """
    class defining a remote control
    """
    def __init__(self):
        self.channels = ["HBO", "CNN", "BBC","ESPN"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            return False

        return self.channels[self.index]


if __name__ == "__main__":
    remotecontrol = Remote()
    itr = iter(remotecontrol)
    while True:
        CHANNEL = next(itr)
        if not CHANNEL:
            break
        time.sleep(0.5)
        print(CHANNEL)
