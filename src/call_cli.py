#!/bin/python3
from sys import argv

"""Print copyright message"""
def copyright() -> None:
    print("-- BEGIN COPYRIGHT --")
    print("Copyright 2022 Evvive & CALL Contributors")
    print("Licensed under BSD-Clause-3 License, see:")
    print("\thttps://github.com/evvive/call-language/blob/master/LICENSE")
    print("-- END COPYRIGHT --")

    return

def version() -> None:
    print("\nCALL v0.1-essential")

    return

"""Print help message"""
def help() -> None:
    version()
    print("\nHELP")
    print("  COMMAND:    DESCRIPTION\n")
    print("  help:       print this help message")
    print("  run [file]: run [file]")
    print("  repl:       start Read-Eval-Print-Loop")
    print("  version:    print version")
    print("  init:       init call-cli.py project")

"""Call Command Line Interface"""
def main(argv) -> int:
    copyright()
    argv = argv[1:]
    argc = len(argv)

    if argc == 0:
        print("\nInvalid command, use help command to see available commands")

        return 1
    elif argc == 1:
        if argv[0] == "help":
            help()
        elif argv[0] == "repl":
            print("\nTODO: REPL")
        elif argv[0] == "version":
            version()
        elif argv[0] == "init":
            print("\nTODO: init")
        else:
            print("\nInvalid command, use help command to see available commands")

            return 1
    elif argc == 2:
        if argv[0] == "run":
            print("\nTODO: run", argv[1])
        else:
            print("\nInvalid command, use help command to see available commands")

            return 1
    else:
        print("\nInvalid command, use help command to see available commands")

        return 1

    return 0

if __name__ == "__main__":
    exit_code = main(argv)

    exit(exit_code)
