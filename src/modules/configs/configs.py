from json import loads


class Conf:

    def __init__(self):
        pass

    def parse_conf(self, conf_path: str) -> dict:
        conf = self.load_conf(conf_path)
        if self.validate_conf(conf):
            return self.complete_conf(conf)

    @staticmethod
    def load_conf(conf_path: str) -> dict:
        return loads(conf_path)

    def validate_conf(self, conf: dict) -> bool:
        pass

    def complete_conf(self, conf: dict) -> dict:
        pass


class OperatorConf(Conf):

    def __init__(self):
        pass


class AdminConf(Conf):

    def __init__(self):
        super().__init__()


class ApplicationConf(Conf):

    def __init__(self):
        super().__init__()


class MergedConfig(Conf):

    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.operator = OperatorConf
        self.admin = AdminConf
        self.application = ApplicationConf
