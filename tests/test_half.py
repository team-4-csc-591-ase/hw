from src.data import Data
from src.utils import get_project_root, o
import os
from src.config import CONSTS, CONSTS_LIST


def test_half():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = Data(f)
    left, right, A, B, mid, c = data.half()
    print(len(left), len(right), len(data.rows))
    print(o(A.cells), c)
    print(o(mid.cells))
    print(o(B.cells))
    assert True
