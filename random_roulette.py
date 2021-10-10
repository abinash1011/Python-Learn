'''
File Created: Saturday, 9th October 2021 10:51:50 am
@Author: Abinash1011
-----
Last Modified: Sunday, 10th October 2021 10:42:28 am
Modified By: Abinash1011
-----
'''


import random

def get_roulette(roulette):
    """
    params
    -------
    roulette : (list [str])

    return
    -------
    __No return__

    doc
    ---
    - cum weight = weight of previous element + its own weight
    - let the relative weight of 5 elements are [5,10,20,30,35]
    - then there cum_weight will be [5,15,35,65,100]
    """
    result = random.choices(roulette, weights=[18, 18, 2], k=5)
    print(result)


colors = ["Red", "Black", "Green"]
get_roulette(colors)
