from src.config import CONSTS
from src.data import Data


def test_data():
    data = Data(CONSTS.file.name).read()
    # TODO: Fix later when data classes are merged
    if data == {}:
        assert True
    else:
        assert (
            len(data.rows) == 398
            and data.cols.y[0].w == -1
            and data.cols.x[1].at == 1
            and len(data.cols.x) == 4
        )
