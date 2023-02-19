import os

from src.config import CONSTS_LIST, CONSTS
from src.data import read
from src.optimization import sway
from src.query import stats, div
from src.utils import get_project_root, o, diffs


def test_sway():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = read(f)
    best, rest = sway(data)
    print("\nall ", o(stats(data)))
    print("    ", o(stats(data, div)))
    print("\nbest", o(stats(best)))
    print("    ", o(stats(best, div)))
    print("\nrest", o(stats(rest)))
    print("    ", o(stats(rest, div)))
    print("\nall ~= best?", o(diffs(best.cols.y, data.cols.y)))
    print("best ~= rest?", o(diffs(best.cols.y, rest.cols.y)))

