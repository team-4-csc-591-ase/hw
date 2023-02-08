import os

from src import utils
from src.config import CONSTS, CONSTS_LIST
from src.data import Data
from src.utils import get_project_root


def test_repcols():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    raw = utils.dofile(f)
    t = utils.repCols(raw["cols"], Data)
    for col in t.cols.all:
        print(vars(col))
    for row in t.rows:
        print(vars(row))

    # show(repCols(dofile(f)['cols'], Data).cluster(),"mid",data.cols.all,1)
    assert True
