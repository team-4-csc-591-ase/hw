import math
import sys
from typing import cast

from src.config import CONSTS


class Num:
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

    def div(self) -> float:
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

    def rand(self, lo, hi) -> float:
        """
        Args: hi, lo

        Return : float
        """
        lo, hi = lo or 0, hi or 1
        seed: int = cast(int, CONSTS.seed.value)
        seed = (16807 * seed) % 2147483647
        return lo + (hi - lo) * seed / 2147483647

    def rnd(self, n, n_places=3) -> float:
        """
        Args: n, n_places = 3

        Return : float
        """
        mult = pow(10, n_places)
        return math.floor(n * mult + 0.5) / mult
