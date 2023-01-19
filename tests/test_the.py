from unittest.mock import patch

from src.config import the
from src.misc_functions import oo, reformat, settings


@patch("builtins.print")
def test_the(mock_print) -> None:
    """

    Returns: None

    """
    options = reformat(settings(the))
    options["go"] = "all"
    oo(options)
    mock_print.assert_called_with("{ :dump False :go all :help False :seed 937162211}")
