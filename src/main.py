from cargoloader.modules.misc.arguments import CliInput


def main(cli_options: dict) -> None:
    print("cargoloader initialized")


def cargoloader():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    cargoloader()
