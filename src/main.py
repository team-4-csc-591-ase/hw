import argparse
from src.config import CONSTS


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="The LUA Project USAGE:")
        parser.add_argument(
            "-d",
            "--dump",
            help="on crash, dump stack",
            required=False,
            default=False,
        )
        parser.add_argument(
            "-g",
            "--go",
            help="start-up action",
            required=False,
            default="data",
        )
        parser.add_argument(
            "-s",
            "--seed",
            help="random number seed",
            required=False,
            default=937162211,
        )
        argument = parser.parse_args()
        _CONSTS.update({CONSTS.SEED.name: argument.seed})
        print(argument)


if __name__ == "__main__":
    Main()
