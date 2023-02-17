import re
from typing import List, Union

from src.num import Num  # type: ignore
from src.sym import Sym  # type: ignore


class Col:
    def __init__(self, names: List[str]):
        for c, s in enumerate(names):
            if re.match(r"^[A-Z]+", s):
                col: Union[Num, Sym] = Num(c, s)
            else:
                col = Sym(c, s)

            if re.match(r".*!$", col.txt):
                col.isKlass = True

            if re.match(r".*X$", col.txt):
                col.isIgnored = True

            if re.match(r".*\+$", s) or re.match(r".*\-$", s) or re.match(r".*\!$", s):
                col.isGoal = True
