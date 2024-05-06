from .baselog import BaseLog


class ServiceLog(BaseLog):
    def __init__(self):
        super().__init__("SERVICE")
