import math

from src import query, update
from src.col import Col
from src.config import CONSTS, CONSTS_LIST
from src.lists import copy, lt
from src.query import div
from src.range import RANGE
from src.sym import Sym
from src.update import add, extend
from src.utils import itself

# def bins(cols, rowss):
#     out = []
#     for col in cols:
#         ranges = []
#         for y, rows in enumerate(rowss):
#             for row in rows:
#                 if isinstance(col, Col):
#                     col = col.col
#                 x = row[col.at]
#                 if x != "?":
#                     k = int(bin(col, float(x) if x != "?" else x))
#                     ranges[k] = ranges[k] if ranges[k] else RANGE(col.at, col.txt, x)
#                     extend(ranges[k], x, y)
#         ranges = sorted(map(itself, ranges))
#         out.append(ranges if col.isSym else merge_any(ranges))
#     return out


def bins(cols, rowss):
    """

    Args:
        cols:
        rowss:

    Returns:

    """

    def with1Col(col):
        n, ranges = withAllRows(col)

        ranges = sorted(map(itself, ranges), key=lambda x: x["lo"])
        if col.isSym:
            return ranges
        else:
            merge_any(
                ranges,
                n / (CONSTS_LIST[CONSTS.bins.name]),
                (CONSTS_LIST[CONSTS.d.name]) * div(col),
            )

    def withAllRows(col):
        if isinstance(col, Col):
            col = col.col

        def xy(
            x,
            y,
        ):
            nonlocal n
            if x != "?":
                n += 1
                k = bin(col, x)
                ranges[k] = ranges[k] or RANGE(col.at, col.txt, x)
                extend(ranges[k], x, y)

        for y, rows in enumerate(rowss):
            for _, row in enumerate(rows):
                xy(row[col.at], y)

        return n, ranges

    n, ranges = 0, {}
    print(list(map(with1Col, cols)))
    print(n, ranges)
    return list(map(with1Col, cols))


def bin(col, x):
    """

    Args:
        col:
        x:

    Returns:

    """
    if x == "?" or hasattr(col, "isSym"):
        return x
    tmp = (col.hi - col.lo) / (CONSTS_LIST[CONSTS.bins.name] - 1)
    return 1 if col.hi == col.lo else math.floor(x / tmp + 0.5) * tmp


def merge_any(ranges0, n_small, n_far):
    """

    Args:
        ranges0:

    Returns:

    """

    def no_gaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j - 1].hi
        t[0].lo = -math.inf
        t[-1].hi = math.inf
        return t

    ranges1, j = [], 0
    while j < len(ranges0):
        left, right = ranges0[j], ranges0[j + 1] if j + 1 < len(ranges0) else None
        if right:
            y = merge2(left.y, right.y, n_small, n_far)
            if y:
                j += 1  # next round, skip over right.
                left.hi, left.y = right.hi, y
        ranges1.append(left)
        j += 1
    return (
        no_gaps(ranges0)
        if len(ranges0) == len(ranges1)
        else merge_any(ranges1, n_small, n_far)
    )


# def merge2(col1, col2):
#     """
#
#     Args:
#         col1:
#         col2:
#
#     Returns:
#
#     """
#     new = merge(col1, col2)
#     if div(new) <= (div(col1) * col1.n + div(col2) * col2.n) / new.n:
#         return new


def merge2(col1, col2, n_small=None, n_far=None):
    """

    Args:
        col1:
        col2:

    Returns:

    """
    new = merge(col1, col2)
    if n_small:
        if col1.n < n_small or col2.n < n_small:
            return new
    if n_far:
        if not col1.isSym and abs(query.mid(col1) - query.mid(col2)) < n_far:
            return new

    if div(new) <= (div(col1) * col1.n + div(col2) * col2.n) / new.n:
        return new


def merge(col1, col2):
    """

    Args:
        col1:
        col2:

    Returns:

    """
    new = copy(col1)
    if col1.isSym:
        for x, n in col2.has.items():
            add(new, x, n)
    else:
        for n in col2.has.values():
            add(new, n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    return new
