from typing import Any, List, Union

from src import update, utils
from src.cols import Cols


class Data:
    """
    The Data Class
    """

    def __init__(self) -> None:
        self.cols: Union[Cols, None] = None
        self.rows: List[Any] = []
        self.n = 0

    def read(self, file_name, rows=None):
        """

        Args:
            file_name:

        Returns:

        """
        data = Data()

        # add = lambda t: update.row(self, t)
        # def add(t):
        def add(t):
            update.row(self, t)

        if isinstance(file_name, str):
            utils.csv(file_name, lambda t: update.row(data, t))
        else:
            self.cols = Cols(file_name.cols.names)
            if rows:
                for row in rows:
                    add(row)
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
