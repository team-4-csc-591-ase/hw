import argparse
import importlib.machinery
import os
import types
from inspect import getmembers, isfunction
from typing import Any, Callable, List, Tuple


class TestEngine:
    """
    Our custom CLI based Test Engine implementation
    """

    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="TestEngine")
        parser.add_argument(
            "-P",
            "--path",
            help="Provide path of the tests, example: tests/",
            required=True,
            default="",
        )
        parser.add_argument(
            "-I",
            "--ignore",
            help="Provide files to ignore, example: __pycache__",
            required=False,
            default="__pycache__",
        )
        argument = parser.parse_args()

        self.test_files: List[str] = []
        self.ignore_list: List[str] = []
        self.success: bool = True
        self.ignore_list = self.files_to_ignore(argument.ignore)

        print(f"Path provided: {argument.path}")
        print(f"Files to ignore: {self.ignore_list}")

        self.load_test_files(argument.path)

    @classmethod
    def files_to_ignore(cls, files: str) -> List[str]:
        """
        Generate a list of files that are supposed to be ignored by the test engine
        Args:
            files: "," separate file names

        Returns: List of file names

        """
        return files.split(",")

    @classmethod
    def load_tests(cls, module: Any) -> List[Tuple[str, Callable]]:
        """
        Takes a module, separates the filename and test functions starting with test_
        Args:
            module: Maybe a file name that contains all the

        Returns: List of tuple(function name, function/object reference)

        """
        return [
            m
            for m in getmembers(module)
            if isfunction(m[1]) and m[0].startswith("test_")
        ]

    @classmethod
    def load_module(cls, file: str) -> Any:
        """
        Take a file name, find its module in the test environment,
        execute the module and return the module
        Args:
            file: File name

        Returns: Module

        """
        loader = importlib.machinery.SourceFileLoader("test_environment", file)
        module = types.ModuleType("test_environment")
        loader.exec_module(module)
        return module

    def process_file(self, path: str) -> None:
        """
        Takes the path walk all over it and append the file names in the test_files list
        Args:
            path: Path of the test files

        Returns: None

        """
        if os.path.isfile(path):
            self.test_files.append(path)
        elif os.path.isdir(path):
            for nested_path in os.listdir(path):
                self.load_test_files(path + "/" + nested_path)

    def load_test_files(self, path: str) -> None:
        """
        Helper function for process file
        Args:
            path: File path

        Returns:

        """
        if path in self.ignore_list:
            return None
        self.process_file(path)

    def run_single_file(self, file: str) -> None:
        """
        Takes a single file name and

        Args:
            file: File name

        Returns:

        """
        mod = self.load_module(file)
        tests = self.load_tests(mod)
        for test in tests:
            (test_name, test_function) = test
            try:
                test_function()
                print(f"Running test {test_name} - success")
            except AssertionError:
                print(f"Running test {test_name} - failure")
                self.success = False

    def run(self) -> None:
        """
        Entry point of the test engine
        Returns: None

        """
        for test_file in self.test_files:
            print(f"Test files: {test_file}")
            self.run_single_file(test_file)

        if self.success:
            print("Tests succeeded ✅ ")
        else:
            print("Tests failed ❌ ")


TestEngine().run()
