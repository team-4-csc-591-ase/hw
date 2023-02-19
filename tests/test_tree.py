import os

from src.clustering import tree, show_tree
from src.config import CONSTS_LIST, CONSTS
from src.data import read
from src.utils import get_project_root


def test_tree():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = read(f)
    show_tree(tree(data))
