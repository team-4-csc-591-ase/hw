import sys


class Num:
    def __init__(self, at=None, txt=None, name: str = "") -> None:
        self.n, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = sys.maxsize, -sys.maxsize
        self._name = name
        if at:
            self.at = at
        else:
            self.at = 0
        if txt:
            self.txt = txt
        else:
            self.txt = ""
        if "-" in self.txt:
            self.w = -1
        else:
            self.w = 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def add(self, n) -> None:
        """
        Args: n
        Return : None
        """
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + (d / self.n)
            self.m2 = self.m2 + (d * (n - self.mu))
            self.lo = min(self.n, self.lo)
            self.hi = max(self.n, self.hi)

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
            return round(x, n)

    def norm(self, n) -> float:
        """

        Args:
            n: int

        Returns: float

        """
        if n == "?":
            return n
        else:
            return (n - self.lo) / (self.hi - self.lo + 1e-32)

    def dist(self, n1, n2) -> int:
        """

        Args:
            n1: int
            n2: int

        Returns: int

        """
        if n1 == "?" and n2 == "?":
            return 1
        n1 = self.norm(n1)
        n2 = self.norm(n2)

        if n1 == "?":
            if n2 < 0.5:
                n1 = 1
            else:
                n1 = 0

        if n2 == "?":
            if n1 < 0.5:
                n2 = 1
            else:
                n2 = 0

        return abs(n1 - n2)
