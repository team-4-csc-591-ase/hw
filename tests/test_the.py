from unittest.mock import patch

from src.config import CONSTS_LIST
from src.utils import oo


@patch("builtins.print")
def test_the(mock_print) -> None:
    """

    Returns: None

    """
    options = CONSTS_LIST.copy()
    oo(options)
    mock_print.assert_called_with(
        "{ :dump False "
        ":file ../etc/data/auto93.csv "
        ":go data "
        ":help False "
        ":seed 937162211}"
    )
