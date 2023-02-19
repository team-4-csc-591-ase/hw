import os

from src.config import CONSTS, CONSTS_LIST
from src.data import read, clone
from src.query import stats
from src.utils import get_project_root, oo


def test_clone():
    """
    Not required for HW 4
    Returns:

    """
    project_root = get_project_root()
    file_path=os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data1 = read(f)
    data2 = clone(data1, data1.rows)
    oo(stats(data1))
    oo(stats(data2))

