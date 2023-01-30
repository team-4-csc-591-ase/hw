import math
import re
from pathlib import Path
from typing import Any, Callable, cast

from src.config import CONSTS, CONSTS_LIST


def get_project_root() -> str:
    return str(Path(__file__).parent.parent)


def o(t: dict) -> str:
    """

    Args:
        t: dict

    Returns: str

    """

    result = "{"
    keys = list(t.keys())
    keys.sort()
    for key in keys:
        result += " :" + str(key) + " " + str(t[key])

    result += "}"
    return result


# print t then return it
def oo(t: dict) -> dict:
    """

    Args:
        t: dict

    Returns: dict

    """
    print(o(t))
    return t


def settings(s: str) -> dict:
    """

    Args:
        s: String to be parsed

    Returns: Dictionary of options from parsed string

    """
    return dict(re.findall(r"\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s))


def rand(lo, hi) -> float:
    """
    Args: hi, lo

    Return : float
    """
    lo, hi = lo or 0, hi or 1
    seed: int = cast(int, CONSTS_LIST[CONSTS.seed.name])
    seed = (16807 * seed) % 2147483647
    return lo + (hi - lo) * seed / 2147483647


def rnd(n, n_places=3) -> float:
    """
    Args: n, n_places = 3

    Return : float
    """
    mult = pow(10, n_places)
    return math.floor(n * mult + 0.5) / mult


def csv(file_name: str, function: Callable):
    return True


def coerce(s: str) -> Any:
    """

    Args:
        s:

    Returns:

    """

    if s == "true":
        return True
    elif s == "false":
        return False
    # checks if number is an integer
    elif s.isnumeric():
        return int(s)
    # checks if in_str is a non-integer number
    elif re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$", s) is not None:
        return float(s)
    else:
        return s


def cosine(a, b, c):
    x1 = (a**2 + c**2 - b**2) / (2 * c)
    x2 = max(0, min(1, x1))
    y = (a**2 - x2**2) ** 0.5
    return x2, y


def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))


def any(t):
    return t[rint(0, len(t) - 1)]


def many(t, n):
    u = []
    for i in range(n):
        u.append(any(t))
    return u


def push(t, x):
    t.append(x)


def lt(x):
    def fun(a, b):
        return a[x] < b[x]


def map(t, fun):
    u = []
    for k, v in t.items():
        v, k = fun(v)
        u[k or (1 + len(u))] = v
    return u


def kap(t, fun):
    u = []
    for k, v in t.items():
        v, k = fun(k, v)
        u[k or (1 + len(u))] = v
    return u


def show(node, what, cols, nPlaces, lvl=0):
    if node:
        lvl = lvl or 0
        print("| " * lvl + str(len(node.data.rows) + " "))
        if not node.left or lvl == 0:
            print(o(node.data.stats("mid", node.data.cols.y, nPlaces)))
        else:
            print("")
        show(node.left, what, cols, nPlaces, lvl + 1)
        show(node.right, what, cols, nPlaces, lvl + 1)
