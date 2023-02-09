from json import loads
from jsonschema import validate
from typing import Union
import os

from . import schemas
from ..global_vars import global_vars


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

    def get_conf_path(self, conf_path: Union[str, bool]) -> str:
        if not conf_path:
            try:
                conf_path = self.get_conf_here()
                open(conf_path)
                return conf_path
            except FileNotFoundError:
                try:
                    conf_path = os.path.join(global_vars.application_dir, f"{self.conf_type}.conf")
                    open(conf_path)
                    return conf_path
                except FileNotFoundError:
                    raise FileNotFoundError(f"[CRITICAL]: {self.conf_type.capitalize()}"
                                            " configuration could not be obtained.")
        else:
            return conf_path

    def get_conf_here(self) -> str:
        for file in os.listdir(os.getcwd()):
            if file.endswith(f"{self.conf_type}.conf"):
                return os.path.join(os.getcwd(), file)

        return ""
