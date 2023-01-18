import sys
sys.path.insert(0, '../src')
from sym import *
import logging
import traceback

def test_sym():
    symobj = Sym()

    symlist = ["a", "a", "a", "a", "b", "b", "c"]
    for x in symlist:
        symobj.add(x)
    findMid = symobj.mid(x)
    divValue = symobj.rnd(testobj.div(x))
    return (custom_assert_equals("a", findMid, "Check Sym") and custom_assert_equals(1.379,round(testobj.div(x), 3), "Check Sym"))

def custom_assert_equals(val1, val2, msg=""):
    if val1 != val2:
        logging.error()
        traceback.print_stack()
        return False
    else:
        return True
