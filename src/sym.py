import math
from typing import Any, Optional


class Sym:
    n = 0
    has: dict = {}
    most = 0
    mode = None

    def rnd(self, nPlaces) -> float:
        """
        Args: n, nPlaces = 3

        Return : float
        """
        mult = math.pow(10, 3)
        return math.floor((self.n * mult) + 0.5) / mult

    def add(self, x) -> None:
        """
        Args: x

        Return : None
        """
        if x != "?":
            self.n = self.n + 1
            if x in self.has:
                y = self.has[x]
            else:
                y = 0
            self.has[x] = 1 + y
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self, x) -> Optional[Any]:
        """
        Args: x

        Return : int
        """
        return self.mode

    def div(self, x) -> float:
        """
        Args: x

        Return : float
        """

        def fun(p):
            return p * (math.log2(p))

        e = 0
        for k, v in self.has.items():
            e = e + fun(v / self.n)
        return -e
