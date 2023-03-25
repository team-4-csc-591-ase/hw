import os

from src.clustering import show_tree, tree
from src.config import CONSTS, CONSTS_LIST
from src.data import Data
from src.utils import get_project_root


def test_tree():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = Data(f)
    show_tree(tree(data))
