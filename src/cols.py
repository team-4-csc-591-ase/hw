from src import Num  # type: ignore
from src import Sym  # type: ignore


class Cols:
    def __init__(self, t) -> None:
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None

        for name in t:
            if name[0].isupper():
                col = Num(t.index(name), name)
            else:
                col = Sym(t.index(name), name)

            self.all.append(col)

            if name[-1] != "X":
                if name[-1] == "!":
                    self.klass = name
                if name[-1] == "+" or name[-1] == "-" or name[-1] == "!":
                    self.y.append(name)
                else:
                    self.x.append(name)

    def add(self, row) -> None:
        """

        Args:
            row: int

        Returns: None

        """
        total_columns = self.x.copy() + self.y.copy()
        for col in total_columns:
            col.add(row.cells[col.at])
