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
        node=utils.repCols(utils.dofile(f)["cols"], Data).cluster(),
        what=0,
        cols=data.cols.all,
        n_places=0,
    )
