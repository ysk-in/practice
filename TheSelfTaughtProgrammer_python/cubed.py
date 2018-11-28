import math


def pow3(val):
    try:
        return math.pow(val, 3)
    except BaseException as e:
        print("pow3 failed. e=" + str(e))
