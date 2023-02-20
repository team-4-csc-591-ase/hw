from src.sym import Sym


class RANGE:
    def __init__(self, at=None, txt=None, lo=None, hi=None):
        """

        Args:
            at:
            txt:
            lo:
            hi:
        """
        self.at = at
        self.txt = txt
        self.lo = lo
        self.hi = lo if lo else hi if hi else lo
        self.y = Sym()
