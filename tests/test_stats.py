import os
import re

from src.config import CONSTS, CONSTS_LIST
from src.data import Data
from src.utils import get_project_root, o


def test_stats() -> None:
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path

    data = Data(f)
    expected_xmid = 1.5728643216080398
    expected_xdiv = 0.8020548777266148
    expected_ymid = 23.844221105527648
    expected_ydiv = 8.340720074222057
    actual_xmid = float(
        re.findall(r"\d+\.\d+", o(data.stats("mid", data.cols.x, 2)))[0]  # type: ignore
    )
    actual_xdiv = float(
        re.findall(r"\d+\.\d+", o(data.stats("div", data.cols.x, 3)))[0]  # type: ignore
    )
    actual_ymid = float(
        re.findall(r"\d+\.\d+", o(data.stats("mid", data.cols.y, 2)))[0]  # type: ignore
    )
    actual_ydiv = float(
        re.findall(r"\d+\.\d+", o(data.stats("div", data.cols.y, 3)))[0]  # type: ignore
    )

    print("xmid", o(data.stats("mid", data.cols.x, 2)))  # type: ignore
    print("xdiv", o(data.stats("div", data.cols.x, 3)))  # type: ignore
    print("ymid", o(data.stats("mid", data.cols.y, 2)))  # type: ignore
    print("ydiv", o(data.stats("div", data.cols.y, 3)))  # type: ignore

    assert expected_xmid == actual_xmid
    assert expected_xdiv == actual_xdiv
    assert expected_ymid == actual_ymid
    assert expected_ydiv == actual_ydiv
