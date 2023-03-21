from src.utils import RX, scottKnot, tiles


def test_five():
    for rx in tiles(
        scottKnot(
            [
                RX([0.34, 0.49, 0.51, 0.6, 0.34, 0.49, 0.51, 0.6], "rx1"),
                RX([0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9], "rx2"),
                RX([0.15, 0.25, 0.4, 0.35, 0.15, 0.25, 0.4, 0.35], "rx3"),
                RX([0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9], "rx4"),
                RX([0.1, 0.2, 0.3, 0.4, 0.1, 0.2, 0.3, 0.4], "rx5"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])
