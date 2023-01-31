from argparse import ArgumentParser, Namespace
from typing import Tuple


class CliInput:

    def parse_arguments(self) -> Tuple:
        parser = ArgumentParser()

        parser.add_argument("--no-verification", "-n", action="store_false", default="store_true",
                            dest="verification", help="Specify that you want to skip verification"
                            " step.")

        return self.validate_arguments(parser.parse_args())

    @staticmethod
    def validate_arguments(arguments: Namespace) -> Tuple[bool]:
        verify_flag = arguments.verification

        return verify_flag
