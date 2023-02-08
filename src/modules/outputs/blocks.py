import logging

from ..misc.utils import InitParams, get_exec_modes


def log_starting_messages(logger: logging, init_params: InitParams, cli_options: dict) -> None:
    logger.info(f"Welcome to cargoloader {init_params.caller_name}!")
    logger.info(f"Starting at {init_params.start_point} on {init_params.hostname}.")
    logger.debug("Command line options are:")
    for key, val in cli_options.items():
        val_string = " ".join(val) if isinstance(val, (list, dict)) else val
        logger.debug(f"\t{key}\t\t{val_string}")
    logger.info(f"Running following modes: {get_exec_modes(cli_options)}.")
