import logging
from enum import Enum, unique

class LoggerError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

        return

@unique
class ErrType(Enum):
    FATAL   = logging.FATAL
    ERROR   = logging.ERROR
    WARNING = logging.WARNING
    INFO    = logging.INFO

class Logger:
    def __init__(self, name: str, logfile: str, format: logging.Formatter, log: bool) -> None:
        self.name    = name
        self.logfile = logfile
        self.format  = format
        self.log     = log

        self.logger  = logging.getLogger(self.name)

        self.create_handler()

        return

    _levels = [
        ErrType.FATAL,
        ErrType.ERROR,
        ErrType.WARNING,
        ErrType.INFO
    ]

    def create_handler(self) -> None:
        if self.log is False: return

        handler = logging.FileHandler(self.logfile)

        # Levels used by CALL
        handler.setLevel(logging.FATAL)
        handler.setLevel(logging.ERROR)
        handler.setLevel(logging.WARNING)
        handler.setLevel(logging.INFO)

        handler.setFormatter(self.format)

        self.logger.addHandler(handler)

        return

    def print(self, level, message: str) -> None:
        if self.log is False: return

        if level not in self._levels:
            raise LoggerError("Invalid level")
        else:
            if level == ErrType.FATAL:
               self.logger.fatal(message)
            elif level == ErrType.ERROR:
                self.logger.error(message)
            elif level == ErrType.WARNING:
                self.logger.warning(message)
            elif level == ErrType.INFO:
                self.logger.info(message)

            return
