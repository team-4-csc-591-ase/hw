from src.config import CONSTS, CONSTS_LIST
from src.data import Data


def test_data():
    data = Data(CONSTS_LIST[CONSTS.file.name])
    assert (
        len(data.rows) == 398
        and data.cols.y[0].w == -1
        and data.cols.x[1].at == 1
        and len(data.cols.x) == 4
    )
    """
    for i in data.cols.names:
        oo(i)
    return True
    """
