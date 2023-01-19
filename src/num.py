import math
import sys


class Num:
    Seed = 937162211
    n, mu, m2 = 0, 0, 0
    lo, hi = sys.maxsize, -sys.maxsize

    """
    Args: n

    Return : None
    """

    def add(self, n) -> None:
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + (d / self.n)
            self.m2 = self.m2 + (d * (n - self.mu))
            self.lo = min(self.n, self.lo)
            self.hi = max(self.n, self.hi)

    """
    Args: None

    Return : Float
    """

    def mid(self) -> float:
        return self.mu

    """
    Args: None

    Return : bool
    """

    def div(self) -> bool:
        return (self.m2 < 0 or self.n < 2) and 0 or pow((self.m2 / (self.n - 1)), 0.5)

    """
    Args: hi, lo

    Return : float
    """

    def rand(self, lo, hi) -> float:
        lo, hi = self.lo or 0, self.hi or 1
        Seed = (16807 * self.Seed) % 2147483647
        return lo + (hi - lo) * Seed / 2147483647

    """
    Args: n, nPlaces = 3

    Return : float
    """

    def rnd(self, n, nPlaces=3) -> float:
        mult = pow(10, nPlaces)
        return math.floor(n * mult + 0.5) / mult
