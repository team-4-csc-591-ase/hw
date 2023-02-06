import os

from src import utils
from src.config import CONSTS, CONSTS_LIST
from src.utils import get_project_root


def reprows():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    t = utils.dofile(f)
    rows = utils.repRows(t, utils.transpose(t["cols"]))
    for col in rows.cols.all:
        print(vars(col))
    for row in rows.rows:
        print(vars(row))
