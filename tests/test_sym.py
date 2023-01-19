import logging
import traceback

from src import sym


def test_sym():
    symobj = sym.Sym()

    symlist = ["a", "a", "a", "a", "b", "b", "c"]
    for x in symlist:
        symobj.add(x)

    return custom_assert_equals(
        "a", symobj.mid(x), "Check Sym"
    ) and custom_assert_equals(1.379, round(symobj.div(x), 3), "Check Sym")


def custom_assert_equals(val1, val2, msg=""):
    if val1 != val2:
        logging.error()
        traceback.print_stack()
        return False
    else:
        return True
