import os

from src import query
from src.config import CONSTS, CONSTS_LIST
from src.contrast_sets import selects, show_rule, xpln
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
    data = Data(f)

    best, rest, evals = sway(data)
    rule, _ = xpln(data, best, rest)
    print("\n-----------\nexplain=", show_rule(rule))
    data1 = Data(data, selects(rule, data.rows))

    print("all               ", query.stats(data), query.stats(data, query.div))
    print(f"sway with   {evals} evals", query.stats(best), query.stats(best, query.div))
    print(
        f"xpln on     {evals} evals", query.stats(data1), query.stats(data1, query.div)
    )

    top, _ = query.betters(data, len(best.rows))
    top = Data(data, top)
    print(
        f"sort with {len(data.rows)} evals",
        query.stats(top),
        query.stats(top, query.div),
    )
