import logging


class Loggers:

    main_name = "cargoloader_main_logger"
    console_fmt = "\n%(asctime)s [%(levelname)s]: %(message)s"

    def __init__(self):
        self.logger = self.define_main_logger()

    def define_main_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.main_name)
        logger.setLevel(logging.DEBUG)
        return logger

    def add_console_handler(self) -> None:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(self.console_fmt))
        self.logger.addHandler(handler)
