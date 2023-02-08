import re
from typing import List, Union

from src.num import Num  # type: ignore
from src.sym import Sym  # type: ignore


class Cols:
    def __init__(self, names: List[str]):
        self.names = names
        self.all = list()
        self.klass = None
        self.x = list()
        self.y = list()

        for c, s in enumerate(names):
            if re.match(r"^[A-Z]+", s):
                col: Union[Num, Sym] = Num(c, s)
            else:
                col = Sym(c, s)
            self.all.append(col)

            if not re.match(r".*X$", s):
                if (
                    re.match(r".*\+$", s)
                    # or re.match(r".*\-$", s)
                    or re.match(r".*\!$", s)
                ):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.match("!$", s):
                    self.klass = col

    def add(self, row) -> None:
        """

        Args:
            row: int

        Returns: None

        """
        for _, names in enumerate(zip(self.x, self.y)):
            for i, col in enumerate(names):
                col.add(row.cells[i])
