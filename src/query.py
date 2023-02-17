import math

from src.config import CONSTS, CONSTS_LIST
from src.lists import kap, per


def div(col):
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
    if not col.isSym and not col.ok:
        col.has.sort()
    col.ok = True
    return col.has


def mid(col):
    if col.isSym:
        return col.mode
    else:
        return per(has(col), 0.5)


def stats(data, fun=None, cols=None, n_places=2):
    cols = cols or data.cols.y
    tmp = kap(cols, lambda k, col: (round((fun or mid)(col), n_places), col.txt))
    tmp["N"] = len(data.rows)
    return tmp, list(map(mid, cols))


def norm(num, n):
    return n if n == "?" else (n - num.lo) / (num.hi - num.lo + 1 / float("inf"))


def value(has, nB=1, nR=1, sGoal=True):
    b, r = 0, 0
    for x, n in enumerate(has):
        if x == sGoal:
            b = b + n
        else:
            r = r + n
    b, r = b / (nB + 1 / float("inf")), r / (nR + 1 / float("inf"))
    return (b**2) / (b + r)


def dist(data, t1, t2, cols=None):
    def dist1(col, x, y):
        if x == "?" and y == "?":
            return 1
        if col.isSym:
            if x == y:
                return 0
            else:
                return 1
        else:
            x, y = norm(col, x), norm(col, y)

            if x == "?":
                if y < 0.5:
                    x = 1
                else:
                    x = 0
            if y == "?":
                if x < 0.5:
                    y = 1
                else:
                    y = 0
            return abs(x - y)

    d, n = 0, 1 / float("inf")
    cols = cols or data.cols.x
    for col in cols:
        n += 1
        d += dist1(col, t1[col.at], t2[col.at]) ** CONSTS_LIST[CONSTS.p.name]

    return (d / n) ** (1 / CONSTS_LIST[CONSTS.p.name])


def better(data, row1, row2):
    s1, s2, ys = 0, 0, data.cols.y
    for _, col in enumerate(ys):
        x = norm(col, row1[col.at])
        y = norm(col, row2[col.at])

        s1 = s1 - math.exp(col.w * (x - y) / len(ys))
        s2 = s2 - math.exp(col.w * (y - x) / len(ys))

    return s1 / len(ys) < s2 / len(ys)
