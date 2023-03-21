# import numpy as np
#
# from src.utils import bootstrap, cliffsDelta, gaussian
#
#
# def test_bootmu():
#     a, b = [], []
#     for i in range(1, 100 + 1):
#         a.append(gaussian(10, 1))
#     print("", "mu", "sd", "cliffs", "boot", "both")
#     print("", "--", "--", "------", "----", "----")
#     for mu in np.linspace(10, 11, 11):
#         b = []
#         for i in range(1, 100 + 1):
#             b.append(gaussian(mu, 1))
#         cl = cliffsDelta(a, b)
#         bs = bootstrap(a, b)
#         print("", mu, 1, cl, bs, cl and bs)
