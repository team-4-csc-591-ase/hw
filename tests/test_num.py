import logging
import sys
import traceback

sys.path.insert(0, "../src")


from num import *


def test_num():
    numobj = Num()

    numList = [1, 1, 1, 1, 2, 2, 3]

    for val in numList:
        numobj.add(val)

    return custom_assert_equals(
        11 / 7, numobj.mid(val), "Check Nums"
    ) and custom_assert_equals(0.787, round(numobj.div(val), 3), "Check Nums")


def custom_assert_equals(val1, val2, msg=""):
    if val1 != val2:
        logging.error()
        traceback.print_stack()
        return False
    else:
        return True
