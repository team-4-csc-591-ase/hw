# import csv
# import os
#
# from src.config import CONSTS, CONSTS_LIST
# from src.utils import get_project_root
#
#
# def test_csv() -> None:
#     project_root = get_project_root()
#     file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
#     f = str(project_root) + "/" + file_path
#
#     n = 0
#     with open(f, mode="r") as file:
#         csv_file = csv.reader(file)
#         for line in csv_file:
#             n += len(line)
#
#     assert n == 3192
