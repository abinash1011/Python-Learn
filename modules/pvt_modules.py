'''
File Created: Tuesday, 12th October 2021 8:26:49 am
@Author: Abinash1011
-----
Last Modified: Tuesday, 12th October 2021 8:27:03 am
Modified By: Abinash1011
-----
'''
def add(*nums):
    """
    add(arg1, arg2, ...) -> returns arg1 + arg2 + ...
    """
    result = 0
    for num in nums:
        result += num
    return result


def intro(normal, **info):
    """
    Takes a kwarg param and returns values
    params:
    info : (kwargs)
    return
    info
    """
    return normal, info

if __name__ == "__main__":
    normal_called, intro_call = intro(1,key="value", layman='man')
    print(intro_call, normal_called)
