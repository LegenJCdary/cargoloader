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
