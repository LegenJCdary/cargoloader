from json import loads
from jsonschema import validate
from logging import Logger
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


class OperatorConf(Conf):

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "operator")


class ProjectConf(Conf):

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "project")


class ApplicationConf(Conf):

    def __init__(self):
        super().__init__(global_vars.application_conf, "application")


class MergedConf:

    def __init__(self, logger: Logger, options: dict):
        self.logger = logger
        self.options = options
        self.operator = OperatorConf(options["operator_conf"]).parse_conf()
        self.project = ProjectConf(options["project_conf"]).parse_conf()
        self.application = ApplicationConf().parse_conf()
        self.final = self.create_final_conf()

    def nested_dict_iter(self, nested, all_keys: list, parent_key: str):
        for key, value in nested.items():
            if isinstance(value, abc.Mapping):
                yield from self.nested_dict_iter(value)
            else:
                all_keys.append(".".join[parent_key, key])

        return all_keys

    @staticmethod
    def breadcrumb(json_dict_or_list):
        if isinstance(json_dict_or_list, dict):
            for k, v in json_dict_or_list.items():
                p = breadcrumb(v)
                if p:
                    return [k] + p
        elif isinstance(json_dict_or_list, list):
            lst = json_dict_or_list
            for i in range(len(lst)):
                p = breadcrumb(lst[i])
                if p:
                    return [str(i)] + p

    def get_conf_keys(self) -> None:
        self.application_keys = self.breadcrumb(self.application)
        self.admin_keys = self.breadcrumb(self.admin)
        self.operator_keys = self.breadcrumb(self.operator)

    def check_conflicts(self) -> dict:
        failed = 0
        for key in self.conflicts:
            if key in self.operator_keys:
                if key in self.admin_keys or self.application_keys:
                    self.logger.error()
            else:
                if key in self.admin_keys and self.application_keys:
                    self.logger.error()
