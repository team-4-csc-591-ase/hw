import sys


class Num:
    def __init__(self, at=None, txt=None) -> None:
        self.n, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = sys.maxsize, -sys.maxsize
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
