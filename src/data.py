from src import utils


class Data:
    def __init__(self, src) -> None:
        self.cols = None
        self.rows = []
        self.n = 0
        if isinstance(src, str):
            self.parse_csv(src)

    def parse_csv(self, src):
        file_path = src
        with open(file_path, "r") as csv:
            lines = csv.readlines()
            for line in lines:
                split_line = line.split(",")
                split_line = [utils.coerce(i) for i in split_line]
                self.n += len(split_line)
