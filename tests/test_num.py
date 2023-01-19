import logging
import traceback

from src import num


def test_num():
    numobj = num.Num()

    numList = [1, 1, 1, 1, 2, 2, 3]

    for val in numList:
        numobj.add(val)

    return custom_assert_equals(
        11 / 7, numobj.mid(), "Check Nums"
    ) and custom_assert_equals(0.787, round(numobj.div(), 3), "Check Nums")


def custom_assert_equals(val1, val2, msg=""):
    if val1 != val2:
        logging.error(msg)
        traceback.print_stack()
        return False
    else:
        return True
