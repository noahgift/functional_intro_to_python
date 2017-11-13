"""This is a simple module"""

import pandas as pd

def list_of_belts_in_bjj():
    """Returns a list of the belts in Brazilian Jiu Jitsu"""

    belts = ["white", "blue", "purple", "brown", "black"]
    return belts

def count_belts():
    """Uses Pandas to count number of belts"""

    belts = list_of_belts_in_bjj()
    df = pd.DataFrame(belts)
    res = df.count()
    count = res.values.tolist()[0]
    return count 