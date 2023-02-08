from cargoloader.modules.misc.arguments import CliInput
from cargoloader.modules.misc import utils


def main(cli_options: dict) -> None:
    init_params = utils.InitParams()
    print("cargoloader initialized")
    print(f"with: {cli_options}")
    print(f"and: {init_params}")


def cargoloader():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    cargoloader()
