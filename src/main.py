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
            print("Executing file")
            filename = argv[1]

    formatter = Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s")

    # TODO: Change this to work in windows and to check dirs
    logger = Logger(__name__, "./log/main.log", formatter, log)

    try:
        logger.print(ErrType.INFO, "Starting logger...")
    except LoggerError as err:
        print(f"Logger error! {err.message}")

        return 1

    code = ""
    f    = None

    try:
        logger.print(ErrType.INFO, "Reading file...")
        f = open(filename, "r")
        code = f.read()
    except FileNotFoundError:
        if filename == "": filename = "nothing"
        logger.print(ErrType.FATAL, f"Given file ({filename}) is invalid")

    finally:
        if f is not None:
            f.close()
        else:
            return 1

        if code == "": logger.print(ErrType.FATAL, "File not given!")

        logger.print(ErrType.INFO, "Starting Lexer...")
        lexer = Lexer(code)

        lexer.lex()

        logger.print(ErrType.INFO, f"Ending process with status 0")

        return 0

if __name__ == "__main__":
    exit_code = main(argv)
    exit(exit_code)
