from src.col import Col  # type: ignore
from src.num import Num  # type: ignore
from src.sym import Sym  # type: ignore


class Cols:
    def __init__(self, ss):
        self.cols = {"names": ss, "all": [], "x": [], "y": []}
        for i in ss:
            col = self.cols["all"].append(Col(i))
            if not col["isIgnored"]:
                if col["isKlass"]:
                    col["isKlass"] = col
                if col["isGoal"]:
                    col.y.append(col)
                else:
                    col.x.append(col)
