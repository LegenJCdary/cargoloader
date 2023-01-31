from json import loads
from jsonschema import validate

from . import schemas


class Conf:

    def __init__(self, conf_path: str, conf_type: str):
        self.conf_type = conf_type
        self.conf_path = self.get_conf_path(conf_path)

    def parse_conf(self) -> dict:
        conf = self.load_conf()
        if self.validate_conf(conf) is None:
            return conf

    def validate_conf(self, conf: dict) -> None:
        return validate(instance=conf, schema=getattr(schemas, self.conf_type))

    def load_conf(self) -> dict:
        with open(self.conf_path, "r", encoding="utf-8") as fh:
            return loads(fh.read())
