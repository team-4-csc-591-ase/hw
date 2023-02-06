import copy


def test_copy():
    t1 = {"a": 1, "b": {"c": 2, "d": [3]}}
    t2 = copy.deepcopy(t1)
    t2["b"]["d"][0] = 10000
    print("b4", t1, "\nafter", t2)
    assert True
