import call.logging
from enum import Enum, unique


class LoggerError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

        return

    def __contains__(self, cls, item):
        return item in [v.value for v in cls.__members__.values()]


@unique
class ErrType(Enum):
    FATAL = 1
    ERROR = 2
    WARNING = 3
    INFO = 4


@unique
class StatusType(Enum):
    BEGIN = 1
    NORMAL = 2
    EXIT = 3


class Logger:
    red = "\033[31m"
    white = "\033[0M"
    green = "\033[32M"
    blue = "\033[34M"
    pink = "\033[35M"

    def __init__(self, name: str, log: bool) -> None:
        self.name = name
        self.log = log

        return

    def print(self, level, message: str, status) -> None:
        prefix = ""

        if status == StatusType.NORMAL:
            prefix = " |"
        elif status == StatusType.EXIT:
            prefix = "/ "
        elif status == StatusType.BEGIN:
            prefix = "\\ "
        else:
            raise LoggerError("Invalid status!")

        if self.log is False:
            return

        if level not in ErrType:
            raise LoggerError("Invalid level")
        else:
            if level == ErrType.FATAL:
                print(prefix, self.name, "FATAL:", message)
            elif level == ErrType.ERROR:
                print(prefix, self.name, "ERROR:", message)
            elif level == ErrType.WARNING:
                print(prefix, self.name, "WARNING:", message)
            elif level == ErrType.INFO:
                print(prefix, self.name, "INFO:", message)

            return
