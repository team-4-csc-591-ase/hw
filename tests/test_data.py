import os

from src.config import CONSTS, CONSTS_LIST
from src.data import read
from src.query import div, mid, stats
from src.utils import get_project_root, oo


def test_data():
    """
    Returns:

    """
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = read(f)
    col = data.cols.x[1]
    print(col.lo, col.hi, mid(col), div(col))
    oo(stats(data))
