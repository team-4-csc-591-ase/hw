import os

from src import utils
from src.config import CONSTS, CONSTS_LIST
from src.data import Data
from src.utils import get_project_root

# def test_repcols():
#     project_root = get_project_root()
#     file_path=os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
#     f = str(project_root) + "/" + file_path
#
#     raw = utils.dofile(f)
#     t = utils.repCols(raw["cols"], Data)
#     for col in t.cols.all:
#         print(vars(col))
#     for row in t.rows:
#         print(vars(row))
#
#     # show(repCols(dofile(f)['cols'], Data).cluster(),"mid",data.cols.all,1)
#     assert True


def test_repcols():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    x = utils.dofile(f)["cols"]
    t = utils.repCols(x, Data)

    for i in t.cols.all:
        allDict = i.__dict__
        allDict["a"] = allDict.__class__.__name__
        allDict["id"] = id(allDict)
        # print(utils.o(i.__dict__))
        d = dict(sorted(allDict.items()))
        print(d)

    print()
    for i in t.rows:
        rowDict = i.__dict__
        rowDict["a"] = rowDict.__class__.__name__
        rowDict["id"] = id(rowDict)
        # print(utils.o(i.__dict__))
        d = dict(sorted(rowDict.items()))
        print(d)
