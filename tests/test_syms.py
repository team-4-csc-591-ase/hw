import logging
import traceback

from src import sym
from src.query import mid, div
from src.sym import Sym
from src.update import adds


def test_syms():
    """
    Args : None
    Returns: Bool

    """
    sym = Sym()
    sym = adds(sym, ['a', 'a', 'a', 'a', 'b', 'b', 'c'])
    print(mid(sym), round(div(sym), 2))
    assert 1.38 == round(div(sym), 2)
