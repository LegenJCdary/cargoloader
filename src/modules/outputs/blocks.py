from logging import Logger

from ..configs.configs import MergedConf
from ..misc.utils import InitParams, get_exec_modes


class Blocks:

    def __init__(self, logger: Logger):
        self.logger = logger

    def log_dict_elements(self, dictionary: dict) -> None:
        for key, val in dictionary.items():
            val_string = " ".join(val) if isinstance(val, (list, dict)) else val
            self.logger.debug(f"\t{key}\t\t{val_string}")

    def log_starting_messages(self, init_params: InitParams, cli_options: dict) -> None:
        self.logger.info(f"Welcome to cargoloader {init_params.caller_name}!")
        self.logger.info(f"Starting at {init_params.start_point} on {init_params.hostname}.")
        self.logger.debug("Command line options are:")
        self.log_dict_elements(cli_options)
        self.logger.info(f"Running following modes: {get_exec_modes(cli_options)}.")

    def log_loaded_configs(self, config: MergedConf) -> None:
        self.logger.debug("Application configuration:")
        self.log_dict_elements(config.application, 0)
        self.logger.debug("")
        self.logger.debug("Project configuration:")
        self.log_dict_elements(config.project, 0)
        self.logger.debug("")
        self.logger.debug("Operator configuration:")
        self.log_dict_elements(config.operator, 0)
        self.logger.debug("")
        self.logger.debug("Final configuration:")
        self.log_dict_elements(config.final, 0)
        self.logger.debug("")
