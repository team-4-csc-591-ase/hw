from src.utils import samples


def test_sample():
    for i in range(1, 11):
        print("", "".join(samples(["a", "b", "c", "d", "e"]).values()))
