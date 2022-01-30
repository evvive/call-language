from enum import Enum, auto, unique
from dataclasses import dataclass
from string import ascii_lowercase


@unique
class Tokens(Enum):
    """Token enum"""

    # Basics
    KEYWORD = auto()
    VARIABLE = auto()

    # Types
    STRING = auto()
    NUMBER = auto()
    ARRAY = auto()
    NULL = auto()

    # Other
    EXPR = auto()


KEYWORD_CHARS = [
    *ascii_lowercase,
    *["_", "!", "-"]
]

NUMBER_CHARS = [
    *[str(i) for i in range(10)],
    "."
]


@dataclass
class Token:
    """Token class"""
    token: Tokens
    value: str = ""

    def __init__(self, token: Tokens, value: str = "") -> None:
        self.token = token
        self.value = value

        return


LexerList = list[Token]
