class Conf:

    def __init__(self):
        pass

    def parse_conf(self, conf_path: str) -> dict:
        conf = self.load_conf(conf_path)
        if self.validate_conf(conf):
            return self.complete_conf(conf)

    @staticmethod
    def load_conf(conf_path: str) -> dict:
        pass

    def validate_conf(self, conf: dict) -> bool:
        pass

    def complete_conf(self, conf: dict) -> dict:
        pass
