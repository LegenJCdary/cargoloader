import argparse
import modules.misc.utils as utils
from modules.outputs.logging import Loggers
from modules.configs.configs import Conf
from modules.mounting.mounting import Docked
from modules.partitioning.listing import ShippingList
from modules.threading.working import Workers
from modules.verification.verify import Verify


def main():
    init_params = utils.InitParams()
    logger = Loggers()
    configuration = Conf()
    docked = Docked()
    crates = ShippingList()

    workers = Workers()
    verify = Verify()


def parse_arguments():
    parser = argparse.ArgumentParser()
    pass


def cargoloader():
    return main(*parse_arguments())


if __name__ == "__main__":
    cargoloader()
