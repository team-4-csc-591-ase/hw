class Sym:
    def __init__(self, n=0, s="") -> None:
        self.n = 0
        self.has: dict = {}
        self.most = 0
        self.mode = None
        self.at = n
        self.txt = s
        self.isSym = True

    # def rnd(self, x, n) -> float:
    #     """
    #     Args: x
    #     Return : int
    #     """
    #     return x
    #
    # def add(self, x) -> None:
    #     """
    #     Args: x
    #     Return : None
    #     """
    #     if x != "?":
    #         self.n = self.n + 1
    #         if x in self.has:
    #             y = self.has[x]
    #         else:
    #             y = 0
    #         self.has[x] = 1 + y
    #         if self.has[x] > self.most:
    #             self.most, self.mode = self.has[x], x
    #
    # def mid(self, x) -> Optional[Any]:
    #     """
    #     Args: x
    #     Return : int
    #     """
    #     return self.mode
    #
    # def div(self, x) -> float:
    #     """
    #     Args: x
    #     Return : float
    #     """
    #
    #     def fun(p):
    #         return p * (math.log(p, 2))
    #
    #     e = 0
    #     for k, v in self.has.items():
    #         e = e + fun(v / self.n)
    #     return -e
    #
    # def dist(self, s1: Any, s2: Any) -> int:
    #     """
    #
    #     Args:
    #         s1: Any
    #         s2: Any
    #
    #     Returns: int
    #
    #     """
    #     if s1 == "?" and s2 == "?":
    #         return 1
    #     if s1 == s2:
    #         return 0
    #     else:
    #         return 1
