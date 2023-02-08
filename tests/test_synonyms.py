import os

from src import utils
from src.config import CONSTS, CONSTS_LIST
from src.data import Data
from src.utils import get_project_root


def test_synonyms():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path
    data = Data(f)
    utils.show(
        utils.repCols(utils.dofile(f)["cols"], Data).cluster(), "mid", data.cols.all, 1
    )
    # utils.show(utils.repCols(utils.dofile(f)['cols']).cluster())
    return True
