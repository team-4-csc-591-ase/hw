from typing import List


class Num:
    def __init__(self, n=0, s="") -> None:
        """

        Args:
            n:
            s:
        """
        self.at = n
        self.txt = s
        self.n = 0
        self.ok = True
        self.has: List = []
        self.lo = float("inf")
        self.hi = float("-inf")
        self.w = -1 if s.endswith("-") else 1
        self.isSym = False
