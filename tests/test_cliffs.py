# import math
#
# from src.utils import cliffs_delta, rand, rnd
#
#
# def test_cliffs():
#     assert (
#         True
#         if not cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3])
#         else False
#     )
#     assert (
#         True
#         if cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6])
#         else False
#     )
#     t1, t2 = [], []
#     for i in range(1000):
#         t1.append(rand())
#         t2.append(math.sqrt(rand()))
#     assert True if not cliffs_delta(t1, t1) else False
#     assert True if cliffs_delta(t1, t2) else False
#     diff, j = False, 1.0
#     while not diff:
#         t3 = list(map(lambda x: x * j, t1))
#         diff = cliffs_delta(t1, t3)
#         print(">", rnd(j), diff)
#         j *= 1.025
