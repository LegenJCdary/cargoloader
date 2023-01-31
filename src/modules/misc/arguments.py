from argparse import ArgumentParser, Namespace
from re import fullmatch
from typing import Optional, Tuple, Union


class CliInput:

    restart_fmt = "yyyymmdd_HHMMSS"
    restart_fmt_len = len(restart_fmt)
    restart_fmt_pattern = r"^\d\d\d\d\d\d\d\d_\d\d\d\d\d\d$"
    short_args = "einr"
    short_args_len = len(short_args)
    short_args_pattern = rf"[{short_args}]*"

    def parse_arguments(self) -> Tuple:
        parser = ArgumentParser()

        parser.add_argument("--exclude", "-e", nargs="+", default=None, metavar=("DISK_SN_1",
                            "DISK_SN_2"), help="Provide list (serial numbers, space separated) of"
                            " containers to skip. Mutually exclusive with --include option.")
        parser.add_argument("--include", "-i", nargs="+", default=None, metavar=("DISK_SN_1",
                            "DISK_SN_2"), help="Provide list (serial numbers, space separated) of"
                            " containers to process (others will be skipped). Mutually exclusive"
                            " with --exclude option.")
        parser.add_argument("--no-verification", "-n", action="store_false", default="store_true",
                            dest="verification", help="Specify that you want to skip verification"
                            " step.")
        parser.add_argument("--restart", "-r", nargs=1, default=None, metavar=self.restart_fmt,
                            help="Start in restart mode. Required argument is previous upload start"
                            " timestamp.")

        return self.validate_arguments(parser.parse_args())

    def validate_arguments(self, arguments: Namespace) -> Tuple[bool, Union[str, bool], Union[list,
                                                                bool], Union[list, bool]]:
        verify_flag = arguments.verification
        restart_point = self.validate_restart(arguments.restart)
        exclude_list, include_list = self.validate_inex_lists(arguments.exclude, arguments.include)

        return verify_flag, restart_point, exclude_list, include_list

    def validate_restart(self, restart: Optional[str]) -> Union[str, bool]:
        try:
            restart_point = restart[0]
        except TypeError:
            return False

        if restart_point:
            if len(restart_point) != self.restart_fmt_len or not fullmatch(self.restart_fmt_pattern,
                                                                           restart_point):
                raise ValueError("[CRITICAL]: Restart timestamp has invalid format, use --help."
                                 " Program will exit now.")
            else:
                return restart_point
        else:
            raise IndexError("[CRITICAL]: Option --restart requires an argument, use --help."
                             " Program will exit now.")

    def validate_inex_lists(self, exclude: list, include: list) -> Tuple:
        if exclude and include:
            raise TypeError("[CRITICAL]: Mutually exclusive lists were provided, use --help."
                            " Program will exit now.")
        else:
            return self.validate_inex_list(exclude), self.validate_inex_list(include)

    def validate_inex_list(self, input_list: list) -> Union[list, bool]:
        try:
            first = input_list[0]
        except TypeError:
            return False

        if len(first) < self.short_args_len and fullmatch(self.short_args_pattern, first):
            raise TypeError("[CRITICAL]: Short options concatenation is not allowed. Program"
                            " will exit now.")
        else:
            return self.create_list(input_list)

    @staticmethod
    def create_list(input_list: list) -> list:
        output_list = []
        for sn in input_list:
            output_list.append(sn.upper())

        return output_list
