from argparse import ArgumentParser, Namespace
from re import fullmatch
from typing import Optional, Tuple, Union


class CliInput:

    restart_fmt = "yyyymmdd_HHMMSS"
    restart_fmt_len = len(restart_fmt)
    restart_fmt_pattern = r"^\d\d\d\d\d\d\d\d_\d\d\d\d\d\d$"

    def parse_arguments(self) -> Tuple:
        parser = ArgumentParser()

        parser.add_argument("--no-verification", "-n", action="store_false", default="store_true",
                            dest="verification", help="Specify that you want to skip verification"
                            " step.")
        parser.add_argument("--restart", "-r", nargs=1, default=None, metavar=self.restart_fmt,
                            help="Start in restart mode. Required argument is previous upload start"
                            " timestamp.")

        return self.validate_arguments(parser.parse_args())

    def validate_arguments(self, arguments: Namespace) -> Tuple[bool, Union[str, bool]]:
        verify_flag = arguments.verification
        restart_point = self.validate_restart(arguments.restart)

        return verify_flag, restart_point

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
