from enum import Enum, auto

class LexerTypes(Enum):
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

    @classmethod
    def __contains__(cls, item):
        return item in [v.value for v in cls.__members__.values()]

class Lexer:
    def __init__(self, code: str) -> None:
        self.code = code


    def lex(self):
        code = self.code.split("\n")

        for line_num, line in enumerate(code):
            print(f"Line {line_num}: {line}")
