# from unittest.mock import patch
#
# from src.config import CONSTS, CONSTS_LIST
# from src.num import Num
# from src.query import has
# from src.update import add
#
#
# @patch("builtins.print")
# def test_some(mock_print=None):
#     CONSTS_LIST[CONSTS.Max.name] = 32
#     num1 = Num()
#     for i in range(10000):
#         add(num1, i)
#     CONSTS_LIST[CONSTS.Max.name] = 512
#     print(has(num1))
#     mock_print.assert_called_with(has(num1))
#     # mock_print.assert_called_with(
#     #     "{15 687 1545 2022 2324 2693 2758 2883 3247 3533 4067 4168"
#     #     " 4469 4570 5863 5907 5957 6147 6440 6727 7228 7517 7574 7598"
#     #     " 7765 7955 8311 8379 8538 9052 9189 9323}"
#     # )
