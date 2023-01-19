import logging
import math
import traceback

from src import num


def test_rand():
    # Have to add seed
    num1, num2 = num.Num(), num.Num()
    for i in range(1, pow(10, 3)):
        num1.add(num1.rand(0, 1))
    for i in range(1, pow(10, 3)):
        num2.add(num2.rand(0, 1))
    m1, m2 = num1.rnd(num1.mid(), 10), num2.rnd(num2.mid(), 12)

    result = ((m2 - m1) * 100) / m1
    # assert custom_assert_equals(round(m1,2), round(m2,2), "Check Rand")
    # and custom_assert_equals(
    #     0.5, round(m1, 2), "Check Rand"
    # )
    assert result <= 5 and custom_assert_equals(
        0.5, math.floor(m1 * 10) / 10, "Check Rand"
    )


# def custom_assert_equals(val1, val2, msg=""):
#     if val1 != val2:
#         logging.error(msg)
#         traceback.print_stack()
#         return False
#     else:
#         return True
