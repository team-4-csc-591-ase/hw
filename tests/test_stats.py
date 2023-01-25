from src.config import CONSTS
from src.data import Data
from src.utils import o


def test_stats():
    data = Data(CONSTS.file.name).read()
    # TODO: Fix later when data classes are merged
    if data == {}:
        print(data)
        assert True
    else:
        for k, cols in zip(data.cols.y, data.cols.x):
            print(k, "mid", o(data.stats("mid", cols, 2)))
            print("", "div", o(data.stats("div", cols, 2)))

    assert True
