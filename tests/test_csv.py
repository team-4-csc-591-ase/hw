from src.config import CONSTS
from src.utils import csv


def test_csv():
    n = 0

    def fun(t):
        nonlocal n
        n += len(t)

    csv(CONSTS.file.name, fun)
    return n == 8 * 399
