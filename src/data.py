from typing import Any, List, Union

from src import lists, update, utils
from src.cols import Cols
from src.config import CONSTS, CONSTS_LIST


class Data:
    """
    The Data Class
    """

    def __init__(self) -> None:
        self.cols: Union[Cols, None] = None
        self.rows: List[Any] = []
        self.n = 0

    def read(self, file_name):
        """

        Args:
            file_name:

        Returns:

        """
        data = Data()
        utils.csv(file_name, lambda t: update.row(data, t))
        return data

    def stats(self, what: str, cols: Union[Cols, None], n_places: int):
        """

        Args:
            what:
            cols:
            n_places:

        Returns:

        """

        def fun(col):
            """

            Args:
                col:

            Returns:

            """
            _callable = getattr(col, what)
            return col.rnd(_callable(), n_places), col.txt

        return lists.kap(cols, fun)

    def dist(self, row1, row2, cols=None):
        """

        Args:
            row1:
            row2:
            cols:

        Returns:

        """
        n, d = 0, 0
        for _, col in enumerate(cols or self.cols.x):
            n = n + 1
            d = (
                d
                + col.dist(row1.cells[col.at], row2.cells[col.at])
                ** CONSTS_LIST[CONSTS.p.name]
            )
        return (d / n) ** (1 / CONSTS_LIST[CONSTS.p.name])

    def clone(self, data, ts=None):
        """

        Args:
            data:
            ts:

        Returns:

        """
        data1 = update.row(Data(), data.cols.names)
        for t in ts or []:
            update.row(data1, t)
        return data1

    def clone2(self, init={}):
        data = Data([self.cols.names])
        _ = list(map(data.add, init))
        return data

    def around(self, row1, rows=None, cols=None):
        """

        Args:
            row1:
            rows:
            cols:

        Returns:

        """

        def distance(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        rows = rows or self.rows
        sorted_rows = sorted(list(map(distance, rows)), key=lambda x: x["dist"])

        return sorted_rows

    def cluster(self, rows=None, cols=None, above=None):
        """

        Args:
            rows:
            cols:
            above:

        Returns:

        """
        rows = rows or self.rows
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows) >= 2:
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
        """
        Args:
            rows:
            cols:
            above:

        Returns:

        """

        def project(row):
            """

            Args:
                row:

            Returns:

            """
            x, y = utils.cosine(distD(row, A), distD(row, B), c)
            row.x = row.x or x
            row.y = row.y or y
            return {"row": row, "x": x, "y": y}

        def distD(row1, row2):
            """

            Args:
                row1:
                row2:

            Returns:

            """
            return self.dist(row1, row2, cols)

        rows = rows or self.rows
        A = above or utils.any(rows)
        B = self.furthest(A, rows)["row"]
        c = distD(A, B)

        left, right, nums, mid = [], [], 0, None
        for tmp in sorted(list(map(project, rows)), key=lambda x: x["x"]):
            nums += 1
            if nums <= len(rows) / 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])

        return left, right, A, B, mid, c

    def furthest(self, row1, rows, cols=None):
        """

        Args:
            row1:
            rows:
            cols:

        Returns:

        """
        t = self.around(row1, rows, cols)
        return t[-1]
