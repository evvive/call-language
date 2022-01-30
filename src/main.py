from sys import argv
from call.logger import Logger, LoggerError, ErrType, StatusType
from call.lexer import Lexer


def main(argv) -> int:
    argc = len(argv)
    log = True
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

    # TODO: Change this to work in windows and to check dirs
    logger = Logger(__name__, log)

    try:
        logger.print(ErrType.INFO, "Starting logger...", StatusType.BEGIN)
    except LoggerError as err:
        print(f"Logger error! {err.message}")

        return 1

    code = ""
    f = None

    try:
        logger.print(ErrType.INFO, "Reading file...", StatusType.NORMAL)
        f = open(filename, "r")
        code = f.read()
    except FileNotFoundError:
        if filename == "":
            filename = "nothing"

        logger.print(ErrType.FATAL, f"Given file ({filename}) is invalid", StatusType.EXIT)

    finally:
        if f is not None:
            f.close()
        else:
            return 1

        if code == "":
            return 1

        logger.print(ErrType.INFO, "Starting Lexer...", StatusType.NORMAL)
        lexer = Lexer(code)

        lexer.lex()

        logger.print(ErrType.INFO, "Ending process with status 0", StatusType.EXIT)

        return 0


if __name__ == "__main__":
    exit_code = main(argv)
    exit(exit_code)
