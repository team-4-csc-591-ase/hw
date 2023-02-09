# import sys
from typing import Any


class Num:
    def __init__(self, at=0, txt="") -> None:
        self.n, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = float("inf"), float("-inf")
        # self._name = name
        # if at:
        self.at = at
        self.txt = txt

        if "-" in self.txt:
            self.w = -1
        else:
            self.w = 1

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, name):
    #     self._name = name

    def add(self, n) -> None:
        """
        Args: n
        Return : None
        """
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self) -> float:
        """
        Args: None
        Return : Float
        """
        return self.mu

    def div(self) -> float:
        """
        Args: None
        Return : bool
        """
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

    def rnd(self, x, n) -> float:
        if x == "?":
            return x
        else:
            return Num.rnd(self, x, n)

    def norm(self, n) -> str | float:
        """

        Args:
            n: int

        Returns: float

        """
        if isinstance(n, str) or n == "?":
            return n
        else:
            return (float(n) - self.lo) / (self.hi - self.lo + 1e-32)

    def dist(self, n1: Any, n2: Any) -> int:
        """

        Args:
            n1: int
            n2: int

        Returns: int

        """
        if (isinstance(n1, str) or n1 == "?") and (isinstance(n2, str) or n2 == "?"):
            return 1
        n1 = self.norm(n1)
        n2 = self.norm(n2)

        if isinstance(n1, str) or n1 == "?":
            if n2 < 0.5:
                n1 = 1
            else:
                n1 = 0

        if isinstance(n2, str) or n2 == "?":
            if n1 < 0.5:
                n2 = 1
            else:
                n2 = 0

        return abs(n1 - n2)
