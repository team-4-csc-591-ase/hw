from src.num import Num
from src.sym import Sym


class Col:
    def __init__(self, n, s):
        """

        Args:
            n:
            s:
        """
        self.col = Num(n, s) if s[0].isupper() else Sym(n, s)
        self.isIgnored = self.col.txt.endswith("X")
        self.isKlass = self.col.txt.endswith("!")
        self.isGoal = self.col.txt[-1] in ["!", "+", "-"]
