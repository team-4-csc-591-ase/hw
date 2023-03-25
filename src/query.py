import math

from src.col import Col
from src.config import CONSTS, CONSTS_LIST
from src.lists import kap, per


def div(col):
    """

    Args:
        col:

    Returns:

    """
    if hasattr(col, "isSym"):
        e = 0
        if isinstance(col.has, dict):
            for n in col.has.values():
                e = e - n / col.n * math.log(n / col.n, 2)
        else:
            for n in col.has:
                e = e - n / col.n * math.log(n / col.n, 2)
        return e
    else:
        return (per(has(col), 0.9) - per(has(col), 0.1)) / 2.58


def has(col):
    """

    Args:
        col:

    Returns:

    """
    if isinstance(col, Col):
        col = col.col
    if not hasattr(col, "isSym") and not col.ok:
        if isinstance(col.has, dict):
            col.has = dict(sorted(col.has.items(), key=lambda item: item[1]))
        else:
            col.has.sort()
    col.ok = True
    return col.has


def mid(col):
    """

    Args:
        col:

    Returns:

    """
    if hasattr(col, "isSym") and col.isSym:
        return col.mode
    else:
        return per(has(col), 0.5)


def stats(data, fun=None, cols=None, n_places=2):
    """

    Args:
        data:
        fun:
        cols:
        n_places:

    Returns:

    """

    def helper(k, col):
        if isinstance(col, list) or isinstance(col, tuple):
            col = col[1]
        if isinstance(col, Col):
            col = col.col
        return round((fun or mid)(col), n_places), col.txt

    try:
        cols = cols or data.cols.y
    except AttributeError:
        return None

    # tmp = kap(cols, lambda k, col: (round((fun or mid)(col), n_places), col.txt))
    temp = kap(cols, helper)
    temp["N"] = len(data.rows)
    # return temp, map(mid, cols)
    return temp


def norm(num, n):
    """

    Args:
        num:
        n:

    Returns:

    """
    return n if n == "?" else (n - num.lo) / (num.hi - num.lo + 1 / float("inf"))


def value(has, n_B=1, n_R=1, s_goal=True):
    """

    Args:
        has:
        n_B:
        n_R:
        s_goal:

    Returns:

    """
    b, r = 0, 0
    for x, n in has.items():
        if x == s_goal:
            b = b + n
        else:
            r = r + n
    b, r = b / (n_B + 1 / float("inf")), r / (n_R + 1 / float("inf"))
    return (b**2) / (b + r)


def dist(data, t1, t2, cols=None):
    """

    Args:
        data:
        t1:
        t2:
        cols:

    Returns:

    """

    # def dist1(col, x, y):
    #     if x == "?" and y == "?":
    #         return 1
    #     if hasattr(col, "isSym"):
    #         if x == y:
    #             return 0
    #         else:
    #             return 1
    #     else:
    #         x, y = norm(col, x), norm(col, y)
    #
    #         if x == "?":
    #             if y < 0.5:
    #                 x = 1
    #             else:
    #                 x = 1
    #         if y == "?":
    #             if x < 0.5:
    #                 y = 1
    #             else:
    #                 y = 1
    #         return abs(x - y)
    def sym(x, y):
        return 0 if x == y else 1

    def num(x, y):
        if x == "?":
            x = 1 if y < 0.5 else 1
        if y == "?":
            y = 1 if x < 0.5 else 1
        return abs(x - y)

    def dist1(col, x, y):
        if x == "?" and y == "?":
            return 1
        return (
            sym(x, y)
            if hasattr(col, "isSym") and col.isSym
            else num(norm(col, float(x)), norm(col, float(y)))
        )

    d, cols = 0, cols or data.cols.x
    for col in cols:
        d += (
            dist1(col.col, t1[col.col.at], t2[col.col.at]) ** CONSTS_LIST[CONSTS.p.name]
        )
    return (d / len(cols)) ** (1 / CONSTS_LIST[CONSTS.p.name])


def better(data, row1, row2):
    """

    Args:
        data:
        row1:
        row2:

    Returns:

    """
    s1, s2, ys = 0, 0, data.cols.y
    for _, col in enumerate(ys):
        x = norm(col.col, row1[col.col.at])
        y = norm(col.col, row2[col.col.at])

        s1 = s1 - math.exp(col.col.w * (x - y) / len(ys))
        s2 = s2 - math.exp(col.col.w * (y - x) / len(ys))

    return s1 / len(ys) < s2 / len(ys)


def betters(data, n=None):
    def quicksort(arr, cmp_func):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        left = []
        right = []

        for item in arr[1:]:
            if cmp_func(data, item, pivot):
                left.append(item)
            else:
                right.append(item)

        return quicksort(left, cmp_func) + [pivot] + quicksort(right, cmp_func)

    tmp = quicksort(data.rows, better)
    return tmp[:n], tmp[n:] if n else tmp
