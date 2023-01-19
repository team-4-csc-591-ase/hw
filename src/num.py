import math
import sys


class Num:
    Seed = 937162211
    n, mu, m2 = 0, 0, 0
    lo, hi = sys.maxsize, -sys.maxsize

    def add(self, n):
        if n != "?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + (d / self.n)
            self.m2 = self.m2 + (d * (n - self.mu))
            self.lo = min(self.n, self.lo)
            self.hi = max(self.n, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return (self.m2 < 0 or self.n < 2) and 0 or pow((self.m2 / (self.n - 1)), 0.5)

    def rand(self, ho, li):
        lo, hi = self.lo or 0, self.hi or 1
        Seed = (16807 * self.Seed) % 2147483647
        return lo + (hi - lo) * Seed / 2147483647

    def rnd(self, n, nPlaces=3):
        mult = pow(10, nPlaces)
        return math.floor(n * mult + 0.5) / mult
