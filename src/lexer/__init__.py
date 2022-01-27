from enum import Enum, auto
import string

class Tokens(Enum):
    # Basics
    KEYWORD  = auto()
    VARIABLE = auto()

    # Types
    STRING   = auto()
    NUMBER   = auto()
    ARRAY    = auto()
    NULL     = auto()

    # Other
    EXPR     = auto()

    # @classmethod
    # def __contains__(cls, item):
    #     return item in [v.value for v in cls.__members__.values()]

class LexLineError(Exception):
    def __init__(self, char_num: int, line: str, message: str):
        self.char     = list(line)[char_num]
        self.char_num = char_num
        self.message  = message
        self.line     = line

        return

class LexerError(Exception):
    def __init__(self, char_num: int, line: str, line_num: int, message: str):
        self.char     = list(line)[char_num]
        self.char_num = char_num
        self.line_num = line_num
        self.message  = message

        return

class Lexer:
    def __init__(self, code: str) -> None:
        self.code = code


    def lex(self):
        code = self.code.split("\n")

        for line_num, line in enumerate(code):
            print(f"Line {line_num}: {line}")
            try:
                self.lexline(line)
            except LexLineError as err:
                raise LexerError(err.char_num, err.line, line_num, f"LexLine: {err.message}")

    keyword_chars = [
        *string.ascii_lowercase,
        "_",
        "!",
        "-"
    ]

    def lexline(self, line: str):
        splitted      = list(line)
        tokens        = []
        first         = True
        variable      = False
        string        = False
        string_ignore = False

        for char_num, char in enumerate(splitted):
            if char == "\n":
                raise LexLineError(char_num, line, "Invalid \\n char")

            if char == ";": break

            if char == "@" and variable is False:
                variable = True
            elif char == "@" and variable is True:
                raise LexLineError(char_num, line, "Invalid variable (@) token")

            if char == '"' and string is False:
                print("STRING!")
                tokens.append({
                    "token": Tokens.STRING,
                    "value": ""
                })

                string = True

                continue

            if string is True:
                print("String is true", char)
                if char == "\\":
                    string_ignore = True

                    continue

                if string_ignore is True:
                    string_ignore = not string_ignore

                    tokens[len(tokens) - 1]["value"] += char

                    continue

                if char == '"':
                    print("END STRING!")
                    string = False

                    continue

                tokens[len(tokens) - 1]["value"] += char

                continue

            if variable is True:
                if first is True:
                    tokens.append({
                        "token": Tokens.VARIABLE,
                        "value": char
                    })
                elif tokens[len(tokens) - 1]["token"] != Tokens.VARIABLE:
                    tokens.append({
                        "token": Tokens.VARIABLE,
                        "value": char
                    })
                elif tokens[len(tokens) - 1]["token"] == Tokens.VARIABLE:
                    tokens[len(tokens) - 1]["value"] += char

            if char in self.keyword_chars and not variable:
                if first is True:
                    tokens.append({
                        "token": Tokens.KEYWORD,
                        "value": char
                    })
                elif tokens[len(tokens) - 1]["token"] != Tokens.KEYWORD:
                    tokens.append({
                        "token": Tokens.KEYWORD,
                        "value": char
                    })
                elif tokens[len(tokens) - 1]["token"] == Tokens.KEYWORD:
                    tokens[len(tokens) - 1]["value"] += char

            if char == " ":
                if tokens[len(tokens) - 1]["token"] == Tokens.KEYWORD:
                    first = True
                    continue
                elif tokens[len(tokens) - 1]["token"] == Tokens.VARIABLE:
                    first = True
                    continue

            if first is True:
                first = not first

        print(tokens)
