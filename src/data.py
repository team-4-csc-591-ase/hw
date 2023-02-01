import math
from typing import Any, List, Union

from src import utils
from src.cols import Cols
from src.config import CONSTS, CONSTS_LIST
from src.rows import Rows


class Data:
    def __init__(self, src: Union[str, List[str]]) -> None:
        self.cols: Union[Cols, None] = None
        self.rows: List[Any] = []
        self.n = 0
        if isinstance(src, str):
            self.parse_csv(src)
        else:
            if src is None:
                src = []
            self.add(src)
            # for line in src:
            #     self.add(line)

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

    # def stats(
    #     self, fun: Union[str, Callable], show_cols: Union[Cols, None], n_places
    # ) -> Dict[str, int]:
    #     if show_cols is None:
    #         show_cols = self.cols.y  # type: ignore
    #     t: Dict[str, int] = {}
    #     for col in show_cols:  # type: ignore
    #         if isinstance(fun, str):
    #             v = getattr(col, fun)()
    #         else:
    #             v = fun(col)
    #         if isinstance(v, int):
    #             v = utils.rnd(v, n_places)
    #         t[col.name] = v
    #     return t

    def stats(self, what: str, cols: Union[Cols, None], n_places: int):
        def fun(k, col):
            callable = getattr(col, what)
            return col.rnd(callable(), n_places), col.txt

        return utils.kap(cols, fun)

    def better(self, row1, row2):
        s1, s2, ys = 0, 0, self.cols.y
        for col in ys:
            x = col.norm(row1[col.at])
            y = col.norm(row2[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)

    def dist(self, row1, row2, cols=None):
        n, d = 0, 0
        for _, col in enumerate(self.cols.x or cols):
            n = n + 1
            d = d + col.dist(row1[col.at], row2[col.at]) ** CONSTS_LIST[CONSTS.p.name]
        return (d / n) ** (1 / CONSTS_LIST[CONSTS.p.name])

    def clone(self, init=None):
        if init is None:
            init = []
        data = Data(self.cols.names)
        _ = list(map(data.add, init))
        return data

    def sway(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows) ** CONSTS_LIST[CONSTS.min.name]
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}

        if len(rows) > 2 * min:
            left, right, node["A"], node["B"], node["min"], _ = self.half(
                rows, cols, above
            )
            if self.better(node["B"], node["A"]):
                left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
            node["left"] = self.sway(left, min, cols, node["A"])
        if "left" not in node:
            node["left"] = None
        if "right" not in node:
            node["right"] = None
        return node

    def around(self, row1, rows=None, cols=None):
        if rows is None:
            rows = self.rows

        def distance(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        sorted_rows = sorted(map(distance, rows), key=lambda x: x["dist"])

        return sorted_rows

    def cluster(self, rows=None, min_size=None, cols=None, above=None):
        if rows is None:
            rows = self.rows
        min_size = min_size or (len(rows)) ** CONSTS_LIST[CONSTS.min.name]
        if cols is None:
            cols = self.cols.x
        node = {"data": self.clone(rows)}  # xxx cloning
        if len(rows) > 2 * min_size:
            left, right, node["A"], node["B"], node["mid"], _ = self.half(
                rows, cols, above
            )
            node["left"] = self.cluster(left, min_size, cols, node["A"])
            node["right"] = self.cluster(right, min_size, cols, node["B"])
        if "left" not in node:
            node["left"] = None
        if "right" not in node:
            node["right"] = None
        return node


    def half(self, rows=None, cols=None, above=None):
        def distD(row1, row2):
            return self.dist(row1, row2, cols)

        def project(row):
            return {
                "row": row,
                "dist": utils.cosine(distD(row, A), distD(row, B), c),
            }

        if rows is None:
            rows = self.rows

        some = utils.many(rows, CONSTS_LIST[CONSTS.Sample.name])
        A = above or utils.any(some)
        B = self.around(A, some)[int(CONSTS_LIST[CONSTS.Far.name] * len(rows))]["row"]
        c = distD(A, B)
        left, right, mid = [], [], None
        for n, tmp in enumerate(
            sorted(list(map(project, rows)), key=lambda x: x["dist"])
        ):
            if n <= len(rows) / 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c
