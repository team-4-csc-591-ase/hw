from src.data import Data
from src.utils import get_project_root, o, rnd
import os
from src.config import CONSTS, CONSTS_LIST


def test_around():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = Data(f)
    print(data.rows[1])
    print(0, 0, data.rows[1])

    for n, t in (data.around(data.rows[1])):
        if n%50 == 0:
            print(n, rnd(t.dist, 2), o(t.row))