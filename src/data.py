from typing import Any, List, Union

from src import update, utils
from src.cols import Cols


class Data:
    """
    The Data Class
    """

    def __init__(self, file_name, rows=None) -> None:
        self.cols: Union[Cols, None] = None
        self.rows: List[Any] = []
        self.n = 0

        def add(t):
            update.row(self, t)

        if isinstance(file_name, str):
            utils.csv(file_name, lambda t: update.row(self, t))
        else:
            self.cols = Cols(file_name.cols.names)
            if rows:
                for row in rows:
                    add(row)
