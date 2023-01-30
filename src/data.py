import math
from typing import Any, Callable, Dict, List, Union

from src import utils
from src.cols import Cols
from src.config import CONSTS
from src.rows import Rows


class Data:
    def __init__(self, src: str) -> None:
        self.cols: Union[Cols, None] = None
        self.rows: List[Any] = []
        self.n = 0
        if isinstance(src, str):
            self.parse_csv(src)
        else:
            if src is None:
                src = []
            for line in src:
                self.add(line)

    def add(self, element: List[str]) -> None:
        """

        Args:
            element: List[str]

        Returns: None

        """
        if not self.cols:
            self.cols = Cols(element)

        else:
            row = Rows(element)
            self.rows.append(row.cells)
            for td in self.cols.x:
                td.add(row.cells[td.at])

            for td in self.cols.y:
                td.add(row.cells[td.at])

    def parse_csv(self, file: str) -> None:
        """

        Args:
            file: String

        Returns: None

        """
        with open(file, "r") as csv:
            lines = csv.readlines()
            for line in lines:
                split_line = line.replace("\n", "").rstrip().split(",")
                split_line = [utils.coerce(i) for i in split_line]
                self.add(split_line)
                self.n += len(split_line)

    def stats(
        self, fun: Union[str, Callable], show_cols: Union[Cols, None], n_places
    ) -> Dict[str, int]:
        if show_cols is None:
            show_cols = self.cols.y  # type: ignore
        t: Dict[str, int] = {}
        for col in show_cols:  # type: ignore
            if isinstance(fun, str):
                v = getattr(col, fun)()
            else:
                v = fun(col)
            if isinstance(v, int):
                v = utils.rnd(v, n_places)
            t[col.name] = v
        return t

    def better(self, row1, row2):
        s1, s2, ys = 0, 0, self.cols.y
        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)

    def dist(self, row1, row2, cols):
        n, d = 0, 0
        for col in cols or self.cols.x:
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** CONSTS.p.name
        return (d / n) ** (1 / CONSTS.p.name)


    def clone(self, init):
        data = Data(list(self.cols.names))
        map(self.add, init or [])

        return data

    def sway(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows) ** CONSTS.min.name
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}

        if len(rows) > 2 * min:
            left, right, node.A, node.B, node.min = self.half(
                rows, cols, above
            )  # need to check if it's node.A or node['A']
            if self.better(node.B, node.A):
                left, right, node.A, node.B = right, left, node.B, node.A
            node.left = self.sway(left, min, cols, node.A)
        return node

