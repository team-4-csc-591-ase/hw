import os

from src import utils
from src.config import CONSTS, CONSTS_LIST
from src.utils import get_project_root


def test_position():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    t = utils.dofile(f)
    rows = utils.repRows(t, utils.transpose(t["cols"]))
    rows.cluster()
    utils.repPlace(rows)
    assert True
