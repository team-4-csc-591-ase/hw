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
        "{:Far 0.95 :Sample 512 :dump False :file auto93.csv "
        ":go data :help False :min 0.5 :p 2 :seed 937162211}"
    )
