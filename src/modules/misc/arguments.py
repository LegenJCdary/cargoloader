from argparse import ArgumentParser, Namespace


class CliInput:

    option_names = {
        "verification": ["--no-verification", "-n"]
    }

    def create_parser(self) -> ArgumentParser:
        parser = ArgumentParser()

        parser.add_argument(self.option_names["verification"][0], self.option_names["verification"]
                            [1], action="store_false", default=True, dest="verification", help=
                            "Specify that you want to skip verification step.")

        return parser

    def parse_arguments(self) -> dict:
        return self.validate_arguments(self.create_parser().parse_args())

    @staticmethod
    def validate_arguments(arguments: Namespace) -> dict:

        return {
            "verification": arguments.verification
        }
