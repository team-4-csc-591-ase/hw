import os

from src.clustering import half
from src.config import CONSTS, CONSTS_LIST
from src.data import Data
from src.query import stats
from src.utils import get_project_root, o


def test_half():
    """
    Not required for HW4
    Returns:

    """
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = Data().read(f)
    left, right, A, B, c, _ = half(data)
    print(len(left), len(right))
    l, r = data.clone(data, left), data.clone(data, right)
    print("l", o(stats(l)))
    print("r", o(stats(r)))
