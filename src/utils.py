import copy
import json
import math
import re
from pathlib import Path
from typing import Any, cast

from src.config import CONSTS, CONSTS_LIST


def get_project_root() -> str:
    """
    Get absolute path of the project
    Returns: Path in string format

    """
    return str(Path(__file__).parent.parent)


def o(t):
    """

    Args:
        t:

    Returns:

    """
    if type(t) != dict and type(t) != list:
        return str(t)

    def fun(k, v):
        if str(k).find("_") != 0:
            v = o(v)
            return ":" + str(k) + " " + o(v)

        else:
            return False

    array = []
    if type(t) == dict:
        for key in t:
            output = fun(key, t[key])
            if output:
                array.append(output)
            array.sort()
    elif type(t) == list:
        array = t
    return "{" + " ".join(str(val) for val in array) + "}"


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
    """

    Args:
        a:
        b:
        c:

    Returns:

    """
    den = 1 if c == 0 else 2 * c
    x1 = (a**2 + c**2 - b**2) / den
    x2 = max(0, min(1, x1))
    y = abs((a**2 - x2**2)) ** 0.5
    return x2, y


def rint(lo, hi):
    """

    Args:
        lo:
        hi:

    Returns:

    """
    return math.floor(0.5 + rand(lo, hi))


def any(t):
    """

    Args:
        t:

    Returns:

    """
    return t[rint(0, len(t) - 1)]


def many(t, n):
    """

    Args:
        t:
        n:

    Returns:

    """
    u = []
    for i in range(n):
        u.append(any(t))
    return u


def push(t, x):
    """

    Args:
        t:
        x:

    Returns:

    """
    t.append(x)


def lt(x):
    """

    Args:
        x:

    Returns:

    """

    def fun(a, b):
        return a[x] < b[x]


def map(t, fun):
    """

    Args:
        t:
        fun:

    Returns:

    """
    u = []
    for k, v in enumerate(t):
        v, k = fun(v)
        u[k or (1 + len(u))] = v
    return u


def kap(t, fun):
    """

    Args:
        t:
        fun:

    Returns:

    """
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        u[k or (1 + len(u))] = v
    return u


def show(node, what=0, cols=0, n_places=0, lvl=0):
    """

    Args:
        node:
        what:
        cols:
        n_places:
        lvl:

    Returns:

    """
    if node:
        string = "|.." * lvl
        if node["left"] is None:
            print(string, o(last(last(node["data"].rows).cells)))
        else:
            string1 = "%.f" % (rnd(100 * node["c"]))
            print(string, string1)
        show(node["left"], what, cols, n_places, lvl + 1)
        show(node["right"], what, cols, n_places, lvl + 1)


def last(t):
    """

    Args:
        t:

    Returns:

    """
    return t[-1]


def dofile(file):
    """

    Args:
        file:

    Returns:

    """
    file = open(file, "r", encoding="utf-8")
    text = (
        re.findall(r"(?<=return )[^.]*", file.read())[0]
        .replace("{", "[")
        .replace("}", "]")
        .replace("=", ":")
        .replace("[\n", "{\n")
        .replace(" ]", " }")
        .replace("'", '"')
        .replace("_", '"_"')
    )
    file.close()
    file_json = json.loads(re.sub(r"(\w+):", r'"\1":', text)[:-2] + "}")
    return file_json


def repgrid(file, Data=None):
    """

    Args:
        file:
        Data:

    Returns:

    """
    t = dofile(file)
    rows = repRows(t, transpose(t["cols"]), Data)
    cols = repCols(t["cols"], Data)
    show(rows.cluster(), "mid", rows.cols.all, 1)
    show(cols.cluster(), "mid", cols.cols.all, 1)
    repPlace(rows)


def repRows(t, rows, Data=None):
    """

    Args:
        t:
        rows:
        Data:

    Returns:

    """
    rows = copy.deepcopy(rows)
    for j, s in enumerate(rows[len(rows) - 1]):
        rows[0][j] = rows[0][j] + ":" + s
    rows.pop()
    for n, row in enumerate(rows):
        if n == 0:
            row.append("thingX")
        else:
            u = t["rows"][len(t["rows"]) - n]
            row.append(u[len(u) - 1])
    return Data(rows)


def repPlace(data, n=20):
    """

    Args:
        data:
        n:

    Returns:

    """
    g = [[" " for _ in range(n + 1)] for i in range(n + 1)]
    maxy = 0
    print()
    for r, row in enumerate(data.rows):
        c = chr(65 + r)
        print(c, row.cells[-1])
        x, y = int(row.x * n // 1), int(row.y * n // 1)
        maxy = max(maxy, y + 1)
        g[y + 1][x + 1] = c
    print()
    for y in range(maxy):
        print(*g[y])


def transpose(t):
    """

    Args:
        t:

    Returns:

    """
    transposed = []
    for i in range(len(t[0])):
        transposed.append([row[i] for row in t])
    return transposed


def repCols(cols, Data):
    """

    Args:
        cols:
        Data:

    Returns:

    """
    cols = copy.copy(cols)
    for i, col in enumerate(cols):
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
        for j in range(1, len(col)):
            col[j - 1] = col[j]
        col.pop()
    s = []
    for i in range(len(cols[0])):
        s.append("Num" + str(i))
    cols.insert(0, s)
    cols[0][len(cols[0]) - 1] = "thingX"
    return Data(cols)
