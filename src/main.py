from cargoloader.modules.misc.arguments import CliInput
from cargoloader.modules.misc import utils
from cargoloader.modules.outputs import blocks, logging


def main(cli_options: dict) -> None:
    init_params = utils.InitParams()
    loggers = logging.Loggers(cli_options)
    logger = loggers.logger
    blocks.log_starting_messages(logger, init_params, cli_options)


def cargoloader():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    cargoloader()
