from src.config import CONSTS, CONSTS_LIST
from src.utils import csv


def test_csv():
    n = 0

    def fun(t):
        nonlocal n
        n += len(t)

    csv(CONSTS_LIST[CONSTS.file.name], fun)
    return n == 8 * 399
