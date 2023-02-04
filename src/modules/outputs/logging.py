import logging
from logging import handlers as loghan


class Loggers:

    main_name = "cargoloader_main_logger"
    main_fmt = "%(asctime)s [%(levelname)s]: %(message)s"
    console_fmt = "\n%(asctime)s [%(levelname)s]: %(message)s"
    memory_cap = 10

    def __init__(self):
        self.logger = self.define_main_logger()

    def define_main_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.main_name)
        logger.setLevel(logging.DEBUG)

        return logger

    def add_memory_handler(self) -> None:
        handler = loghan.MemoryHandler(self.memory_cap, flushLevel=logging.DEBUG, flushOnClose=False
                                       )
        self.logger.addHandler(handler)

    def add_console_handler(self) -> None:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(self.console_fmt))
        self.logger.addHandler(handler)

    def add_syslog_handler(self) -> None:
        handler = loghan.SysLogHandler()
        handler.setFormatter(logging.Formatter(self.main_fmt))
        self.logger.addHandler(handler)

    def add_file_handler(self, log_path: str) -> None:
        handler = logging.FileHandler(log_path)
        handler.setFormatter(logging.Formatter(self.main_fmt))
        self.logger.addHandler(handler)

    def flush_memory_handler(self) -> None:
        pass


class ColourFormatter(logging.Formatter):

    def __init__(self, formatter):
        super().__init__()
        grey = "\x1b[0;38m"
        light_green = "\x1b[1;32m"
        yellow = "\x1b[0;33m"
        red = "\x1b[0;31m"
        light_red = "\x1b[1;31m"
        reset = "\x1b[0m"

        self.FORMATS = {
            logging.DEBUG: light_green + formatter + reset,
            logging.INFO: grey + formatter + reset,
            logging.WARNING: yellow + formatter + reset,
            logging.ERROR: red + formatter + reset,
            logging.CRITICAL: light_red + formatter + reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)