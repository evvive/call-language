from enum import Enum, unique
from sys import argv
from logger import Logger, LoggerError, ErrType
from logging import Formatter
from lexer import Lexer

@unique
class Colors(Enum):
    RED = "\033[31m",
    WHITE = "\033[0M",
    GREEN = "\033[32M",
    BLUE = "\033[34M",
    PINK = "\033[35M"

def main(argv) -> int:
    argc     = len(argv)
    log      = True
    filename = ""

    if argc == 2:
        if argv[1] == "help":
            print("Help")
        elif argv[1] == "nolog":
            print("WARNING: Disabling logger")
            log = False
        else:
            filename = argv[1]

    formatter = Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s")

    logger = Logger(__name__, "call.log", formatter, log)

    try:
        logger.print(ErrType.INFO, "Hello, World")
    except LoggerError as err:
        print(f"Logger error! {err.message}")

        return 1

    code = ""
    f    = None

    try:
        f = open(filename, "r")
        code = f.read()
    except FileNotFoundError:
        logger.print(ErrType.FATAL, f"Given file ({filename}) is invalid")
    finally:
        if f is not None:
            f.close()
        else:
            return 1

        if code == "": logger.print(ErrType.FATAL, f"File not given!")

        lexer = Lexer(code)

        lexer.lex()

        return 0

if __name__ == "__main__":
    exit_code = main(argv)
    exit(exit_code)
