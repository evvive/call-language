from enum import Enum, unique
from sys import argv
from logger import Logger, LoggerError, ErrType
from logging import Formatter

@unique
class Colors(Enum):
    RED = "\033[31m",
    WHITE = "\033[0M",
    GREEN = "\033[32M",
    BLUE = "\033[34M",
    PINK = "\033[35M"

def main(argv) -> int:
    argc = len(argv)
    log  = True

    if argc == 2:
        if argv[1] == "help":
            print("Help")
        elif argv[1] == "nolog":
            print("WARNING: Disabling logger")
            log = False
        else:
            print("Invalid command")
            return 1

    formatter = Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s")

    logger = Logger(__name__, "call.log", formatter, log)

    try:
        logger.print(ErrType.INFO, "Hello, World")
    except LoggerError as err:
        print(f"Logger error! {err.message}")

        return 1
    finally:
        return 0

if __name__ == "__main__":
    exit_code = main(argv)
    exit(exit_code)
