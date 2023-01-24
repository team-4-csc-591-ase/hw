from src.config import CONSTS
from src.data import Data
from src.utils import o


def test_stats():
    data = Data(CONSTS.file.name)

    for k, cols in zip(data.cols.y, data.cols.x):
        print(k, "mid", o(data.stats("mid", cols, 2)))
        print("", "div", o(data.stats("div", cols, 2)))

    return True
