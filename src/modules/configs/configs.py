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
        self.interim = {}
        self.config = self.create_final_conf()

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

    def check_priorities(self) -> dict:
        pass

    def merge_coherent(self) -> dict:
        pass

    def create_final_conf(self) -> dict:
        self.get_conf_keys()
        self.check_conflicts()
        self.check_priorities()
        self.merge_coherent()

        validated = self.validate_conf(self.interim)
        return self.complete_conf(validated)
