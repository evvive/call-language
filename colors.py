from enum import Enum, unique

@unique
class Colors(Enum):
    RED   = "\033[31m",
    WHITE = "\033[0m",
    GREEN = "\033[32m",
    BLUE  = "\033[34m",
    PINK  = "\033[35m"
