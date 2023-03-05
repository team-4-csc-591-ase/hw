from src.cols import Cols
from src.config import CONSTS, CONSTS_LIST
from src.utils import rand, rint


def row(data, t):
    """

    Args:
        data:
        t:

    Returns:

    """
    if data.cols:
        data.rows.append(t)
        for cols in [data.cols.x, data.cols.y]:
            for col in cols:
                add(col.col, t[col.col.at])
    else:
        data.cols = Cols(t)
    return data


def add(col, x, n=1):
    """

    Args:
        col:
        x:
        n:

    Returns:

    """

    def sym(t: dict):
        t[x] = n + (t.get(x, 0))
        if t[x] > col.most:
            col.most, col.mode = t[x], x

    def num(t: list):
        col.lo, col.hi = min(x, col.lo), max(x, col.hi)
        if len(t) < CONSTS_LIST[CONSTS.Max.name]:
            col.ok = False
            t.append(x)
        elif rand() < CONSTS_LIST[CONSTS.Max.name] / col.n:
            col.ok = False
            t[rint(0, len(t) - 1)] = x

    if x != "?":
        col.n = col.n + n  # Source of variable 'n'
        if hasattr(col, "isSym") and col.isSym:
            sym(col.has)
        else:
            x = float(x)
            num(col.has)
        #   return col


def extend(range, n, s):
    """

    Args:
        range:
        n:
        s:

    Returns:

    """
    range.lo = min(n, range.lo)
    range.hi = max(n, range.hi)
    add(range.y, s)


def adds(col, t):
    """

    Args:
        col:
        t:

    Returns:

    """
    for value in t or []:
        add(col, value)
    return col
