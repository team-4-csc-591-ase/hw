import os
from typing import Any, List

from src import utils
from src.cols import Cols
from src.rows import Rows


class Data:
    def __init__(self, src) -> None:
        self.cols = None
        self.rows: List[Any] = []
        if isinstance(src, str):
            self.parse_csv(src)
        else:
            if src is None:
                src = []
            for line in src:
                self.add(line)

    def add(self, element):
        if not self.cols:
            self.cols = Cols(element)

        else:
            row = Rows(element)
            self.rows.append(row.cells)
            for td in self.cols.x:
                # print('td.at', row.cells[td.at])
                td.add(row.cells[td.at])

            for td in self.cols.y:
                td.add(row.cells[td.at])

    """
        if self.cols:
            # if t.cells != None :
            t = Rows(element)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = Cols(element)
    """

    def parse_csv(self, file):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        f_path = os.path.join(path, "etc/data", file)
        with open(f_path, "r") as csv:
            lines = csv.readlines()
            for line in lines:
                split_line = line.replace("\n", "").rstrip().split(",")
                split_line = [utils.coerce(i) for i in split_line]
                self.add(split_line)


"""
obj = Data(CONSTS_LIST[CONSTS.file.name])
print(obj.cols)
"""
