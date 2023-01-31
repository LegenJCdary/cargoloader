import logging


class Loggers:

    main_name = "cargoloader_main_logger"
    main_fmt = "%(asctime)s [%(levelname)s]: %(message)s"

    def __init__(self):
        self.logger = self.define_main_logger()

    def define_main_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.main_name)
        logger.setLevel(logging.DEBUG)

        return logger
