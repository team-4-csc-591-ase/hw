from src.data import Data
from src.utils import get_project_root
import os
from src.config import CONSTS, CONSTS_LIST
from src.utils import show


def test_optimize():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = Data(f)
    show(data.sway(), "mid", data.cols.y, 1)
    assert True
