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
            # if src is None:
            #     src = []
            # self.add(src)
            if isinstance(src[0], str):
                self.add(src)
            else:
                for line in src:
                    self.add(line)

    def add(self, element: Any) -> None:
        """

        Args:
            element: List[str]

        Returns: None

        """
        # if not self.cols:
        #     self.cols = Cols(element)
        #
        # else:
        #     row = Rows(element)
        #     self.rows.append(row.cells)
        #     for td in self.cols.x:
        #         td.add(row.cells[td.at])
        #
        #     for td in self.cols.y:
        #         td.add(row.cells[td.at])

        # if self.cols:
        #     element = element if hasattr(element, "cells") else Rows(element)
        #     self.rows.append(element)
        #     self.cols.add(element)
        if self.cols:
            if isinstance(element, list):
                element = Rows(element)
            self.rows.append(element)
            self.cols.add(element)
        else:
            self.cols = Cols(element)

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

    def dist(self, row1, row2, cols=None):
        n, d = 0, 0
        for _, col in enumerate(cols or self.cols.x):
            n = n + 1
            d = (
                d
                + col.dist(row1.cells[col.at], row2.cells[col.at])
                ** CONSTS_LIST[CONSTS.p.name]
            )
        return (d / n) ** (1 / CONSTS_LIST[CONSTS.p.name])

    def clone(self, init=None):
        if init is None:
            init = []
        data = Data(self.cols.names)
        _ = list(map(data.add, init))
        return data

    def around(self, row1, rows=None, cols=None):
        rows = rows or self.rows

        def distance(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        sorted_rows = sorted(list(map(distance, rows)), key=lambda x: x["dist"])

        return sorted_rows

    def cluster(self, rows=None, cols=None, above=None):
        rows = rows or self.rows
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}  # xxx cloning
        if len(rows) > 2:
            left, right, node["A"], node["B"], node["mid"], node["c"] = self.half(
                rows, cols, above
            )
            node["left"] = self.cluster(left, cols, node["A"])
            node["right"] = self.cluster(right, cols, node["B"])
        if "left" not in node:
            node["left"] = None
        if "right" not in node:
            node["right"] = None
        return node

    def half(self, rows=None, cols=None, above=None):
        def distD(row1, row2):
            return self.dist(row1, row2, cols)

        def project(row):
            x, y = utils.cosine(distD(row, A), distD(row, B), c)
            row.x = row.x or x
            row.y = row.y or y
            return {"row": row, "x": x, "y": y}

        rows = rows or self.rows

        # some = utils.many(rows, CONSTS_LIST[CONSTS.Sample.name])
        A = above or utils.any(rows)
        # B = self.around(A, some)[int(CONSTS_LIST[CONSTS.Far.name] * len(rows))]["row"]
        B = self.furthest(A, rows)["row"]  # self.furthest(A, rows)
        c = distD(A, B)
        left, right, mid = [], [], None
        for n, tmp in enumerate(
            sorted(list(map(lambda row: project(row), rows)), key=lambda x: x["x"])
        ):
            if n <= len(rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])

        return left, right, A, B, mid, c

    def furthest(self, row1, rows, cols=None):
        t = self.around(row1, rows, cols)
        return t[len(t) - 1]
