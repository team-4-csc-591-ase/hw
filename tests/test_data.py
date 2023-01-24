from data import Data
from src.config import CONSTS


def test_data():
    data = Data(CONSTS.file.name)
    return (
        len(data.rows) == 398
        and data.cols.y[0].w == -1
        and data.cols.x[1].at == 1
        and len(data.cols.x) == 4
    )
