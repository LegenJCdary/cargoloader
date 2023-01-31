class Conf:

    def __init__(self, conf_path: str, conf_type: str):
        self.conf_type = conf_type
        self.conf_path = self.get_conf_path(conf_path)

    def parse_conf(self) -> dict:
        conf = self.load_conf()
        if self.validate_conf(conf) is None:
            return conf
