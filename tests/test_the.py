from unittest.mock import patch

from src.config import _CONSTS, CONSTS
from src.utils import oo


@patch("builtins.print")
def test_the(mock_print) -> None:
    """

    Returns: None

    """
    options = _CONSTS.copy()
    options[CONSTS.go.name] = "all"
    oo(options)
    mock_print.assert_called_with("{ :dump False :go all :help False :seed 937162211}")
