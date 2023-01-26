import math
import re
from typing import Any, Callable, cast

from src.config import CONSTS, CONSTS_LIST


# convert t to a string. sort named keys.
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
