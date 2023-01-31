from datetime import datetime


class InitParams:

    def __init__(self):
        self.start_point = self.get_start_point()

    @staticmethod
    def get_start_point() -> str:
        return datetime.now().strftime("%Y%m%d_%H%M%S")
