from typing import Any, Callable, Dict, List, Union

from src import utils
from src.cols import Cols
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
