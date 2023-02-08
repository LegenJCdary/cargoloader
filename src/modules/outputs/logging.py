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
        handler.setFormatter(ColourFormatter(self.console_fmt))
        self.logger.addHandler(handler)


class ColourFormatter(logging.Formatter):

    def __init__(self, formatter):
        super().__init__()
        grey = "\x1b[0;38m"
        light_green = "\x1b[1;32m"
        yellow = "\x1b[0;33m"
        red = "\x1b[0;31m"
        light_red = "\x1b[1;31m"
        reset = "\x1b[0m"

        self.level_formats = {
            logging.DEBUG: light_green + formatter + reset,
            logging.INFO: grey + formatter + reset,
            logging.WARNING: yellow + formatter + reset,
            logging.ERROR: red + formatter + reset,
            logging.CRITICAL: light_red + formatter + reset
        }

    def format(self, record):
        log_fmt = self.level_formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
