import logging


class Loggers:

    main_name = "cargoloader_main_logger"
    main_fmt = "%(asctime)s [%(levelname)s]: %(message)s"
    console_fmt = f"\n{main_fmt}"

    def __init__(self):
        self.logger = self.define_main_logger()
        self.configure_loggers()

    def define_main_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.main_name)
        logger.setLevel(logging.DEBUG)

        return logger

    def add_handlers(self) -> None:
        self.add_console_handler()

    def configure_loggers(self) -> None:
        self.add_handlers()

    def add_console_handler(self) -> None:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(self.console_fmt))
        self.logger.addHandler(handler)
