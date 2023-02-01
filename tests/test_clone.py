import os

from src.config import CONSTS, CONSTS_LIST
from src.data import Data
from src.utils import get_project_root


def test_clone():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data1 = Data(f)
    data2 = data1.clone(data1.rows)
    return (
        len(data1.rows) == len(data2.rows)
        and data1.cols.y[1].w == data2.cols.y[1].w
        and data1.cols.x[1].at == data2.cols.x[1].at
        and len(data1.cols.x) == len(data2.cols.x)
    )
