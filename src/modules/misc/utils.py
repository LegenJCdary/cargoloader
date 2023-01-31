from datetime import datetime
from os import getlogin
from pwd import getpwnam
from typing import Tuple


class InitParams:

    def __init__(self):
        self.start_point = self.get_start_point()
        self.caller_uid, self.caller_gid = self.get_caller_id()

    @staticmethod
    def get_start_point() -> str:
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def get_caller_id() -> Tuple[int, int]:
        user = getpwnam(getlogin())
        return user.pw_uid, user.pw_gid
