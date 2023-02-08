import argparse

from src.config import CONSTS, CONSTS_LIST


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
            "-f",
            "--file",
            help="name of file",
            required=False,
            default="../etc/data/repgrid1.csv",
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
        parser.add_argument(
            "-p",
            "--p",
            help="distance coefficient",
            required=False,
            default=2,
        )
        argument = parser.parse_args()
        CONSTS_LIST.update(
            {
                CONSTS.seed.name: argument.seed,
                CONSTS.dump.name: argument.dump,
                CONSTS.go.name: argument.go,
                CONSTS.file.name: argument.file,
                CONSTS.p.name: argument.p,
            }
        )
        print(argument)


if __name__ == "__main__":
    Main()
