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
        "{:Far 0.95 :Halves 512 :Max 512 :Reuse True :Sample 512 :bins 16 :bootstrap 512 :cliff 0.4 "
        ":cliffs 0.147 :cohen 0.35 :conf 0.05 :dump False :file auto93.csv :go data :help False "
        ":min 0.5 :p 2 :rest 4 :seed 937162211 :width 40}"
    )
