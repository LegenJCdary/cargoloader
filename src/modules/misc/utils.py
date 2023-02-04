from datetime import datetime
from os import getlogin
from pwd import getpwnam
from socket import gethostname
from typing import Tuple


class InitParams:

    def __init__(self):
        self.start_point = self.get_start_point()
        self.caller_uid, self.caller_gid = self.get_caller_id()
        self.hostname = self.get_hostname()

    @staticmethod
    def get_start_point() -> str:
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def get_caller_id() -> Tuple[int, int]:
        user = getpwnam(getlogin())
        return user.pw_uid, user.pw_gid

    @staticmethod
    def get_hostname() -> str:
        return gethostname()
