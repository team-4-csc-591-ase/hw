import os

from src.config import CONSTS, CONSTS_LIST
from src.contrast_sets import xpln
from src.data import Data
from src.optimization import sway
from src.utils import get_project_root

"""
  data=DATA(is.file)
  best,rest,evals = sway(data)
  rule,most= xpln(data,best,rest)
  print("\n-----------\nexplain=", o(showRule(rule)))
  data1= DATA(data,selects(rule,data.rows))
  print("all               ",o(stats(data)),o(stats(data,div)))
  print(fmt("sway with %5s evals",evals),o(stats(best)),o(stats(best,div)))
  print(fmt("xpln on   %5s evals",evals),o(stats(data1)),o(stats(data1,div)))
  top,_ = betters(data, #best.rows)
  top = DATA(data,top)
  print(fmt("sort with %5s evals",#data.rows) ,o(stats(top)), o(stats(top,div)))

"""


def test_xpln():
    project_root = get_project_root()
    file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
    f = str(project_root) + "/" + file_path
    data = Data().read(f)
    best, rest, evals = sway(data)
    rule, most = xpln(data, best, rest)
    print("\n-----------\nexplain=", data.showRule(rule))
    selects = data.selects(rule, data.rows)
    data_selects = [s for s in selects if s != None]
    data1 = data.clone(data_selects)
    print(
        "all               ",
        data.stats("mid", data.cols.y, 2),
        data.stats("div", data.cols.y, 2),
    )
    print(
        "sway with",
        evals,
        "evals",
        best.stats("mid", best.cols.y, 2),
        best.stats("div", best.cols.y, 2),
    )
    print(
        "xpln on",
        evals,
        "evals",
        data1.stats("mid", data1.cols.y, 2),
        data1.stats("div", data1.cols.y, 2),
    )
    top, _ = data.betters(len(best.rows))
    top = data.clone(top)
    print(
        "sort with",
        len(data.rows),
        "evals",
        top.stats("mid", top.cols.y, 2),
        top.stats("div", top.cols.y, 2),
    )

    assert True
