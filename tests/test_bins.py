# import os
#
# from src.config import CONSTS, CONSTS_LIST
#
# # from src.data import read
# from src.data import Data
# from src.discretization import bins
# from src.optimization import sway
# from src.query import value
# from src.utils import get_project_root, o, rnd
#
#
# def test_bins():
#     project_root = get_project_root()
#     file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
#     f = str(project_root) + "/" + file_path
#
#     data = Data().read(f)
#     best, rest = sway(data)
#     print("all", "", "", "", o({"best": len(best.rows), "rest": len(rest.rows)}))
#     b4 = None
#     for k, t in enumerate(bins(data.cols.x, {"best": best.rows, "rest": rest.rows})):
#         for range in t:
#             if range.txt != b4:
#                 print("")
#             b4 = range.txt
#             print(
#                 range.txt,
#                 range.lo,
#                 range.hi,
#                 rnd(value(range.y.has, len(best.rows), len(rest.rows), "best")),
#                 o(range.y.has),
#             )
