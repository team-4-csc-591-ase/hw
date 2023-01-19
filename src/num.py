import sys


class Num:
    n, mu, m2 = 0, 0, 0
    lo, hi = sys.maxsize, -sys.maxsize

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
