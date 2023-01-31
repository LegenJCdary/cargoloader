import modules.misc.utils as utils
from typing import Union
from modules.misc.arguments import CliInput
from modules.outputs.logging import Loggers
from modules.configs.configs import Conf
from modules.mounting.mounting import Docked
from modules.partitioning.listing import ShippingList
from modules.threading.working import Workers
from modules.verification.verify import Verify


def main(verify_flag: bool, restart_point: Union[str, bool], exclude_list: [list, bool],
         include_list: [list, bool]) -> None:
    init_params = utils.InitParams()
    logger = Loggers()
    configuration = Conf()
    docked = Docked()
    crates = ShippingList()

    workers = Workers()
    verify = Verify()


def cargoloader():
    return main(*CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    cargoloader()
