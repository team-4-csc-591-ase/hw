from unittest.mock import patch

from src.num import Num
from src.query import mid, div
from src.update import add
from src.utils import rand


@patch("builtins.print")
def test_nums(mock_print=None):
    """
    Args: None
    Returns: Bool

    """
    num1, num2 = Num(), Num()
    for i in range(10000):
        add(num1, rand())
    for i in range(10000):
        add(num2, rand() ** 2)
    print(1, round(mid(num1), 2), round(div(num1), 2))
    mock_print.assert_called_with(
        "1       0.5     0.3"
    )
    print(2, round(mid(num2), 2), round(div(num2), 2))
    mock_print.assert_called_with(
        "2       0.26    0.32"
    )
    assert 0.5 == round(mid(num1), 1) and mid(num1) > mid(num2)

