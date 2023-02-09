from logging import Logger

from ..misc.utils import InitParams, get_exec_modes


class Blocks:

    def __init__(self, logger: Logger):
        self.logger = logger
        
    def log_starting_messages(self, init_params: InitParams, cli_options: dict) -> None:
        self.logger.info(f"Welcome to cargoloader {init_params.caller_name}!")
        self.logger.info(f"Starting at {init_params.start_point} on {init_params.hostname}.")
        self.logger.debug("Command line options are:")
        for key, val in cli_options.items():
            val_string = " ".join(val) if isinstance(val, (list, dict)) else val
            self.logger.debug(f"\t{key}\t\t{val_string}")
        self.logger.info(f"Running following modes: {get_exec_modes(cli_options)}.")
