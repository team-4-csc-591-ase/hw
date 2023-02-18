class Num:
    def __init__(self, n=0, s="") -> None:
        self.at = n
        self.txt = s
        self.n = 0
        self.ok = True
        self.has: dict = {}
        self.lo = float("inf")
        self.hi = float("-inf")
        self.isKlass = False
        self.isIgnored = False
        self.isGoal = False

        if "-" in self.txt:
            self.w = -1
        else:
            self.w = 1
