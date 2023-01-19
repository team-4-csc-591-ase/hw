import math
import re
from typing import cast

from src.config import _CONSTS, CONSTS


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


# def reformat(d: dict) -> dict:
#     """
#
#     Args:
#         d: Dict
#
#     Returns: Reformatted Dictionary
#
#     """
#     for key, val in d.items():
#         if val == "false":
#             d[key] = False
#         elif val == "true":
#             d[key] = True
#         elif val.isdigit():
#             d[key] = int(val)
#     return d
def rand(lo, hi) -> float:
    """
    Args: hi, lo

    Return : float
    """
    lo, hi = lo or 0, hi or 1
    seed: int = cast(int, _CONSTS[CONSTS.seed.name])
    seed = (16807 * seed) % 2147483647
    return lo + (hi - lo) * seed / 2147483647


def rnd(n, n_places=3) -> float:
    """
    Args: n, n_places = 3

    Return : float
    """
    mult = pow(10, n_places)
    return math.floor(n * mult + 0.5) / mult
