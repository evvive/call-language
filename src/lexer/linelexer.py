from lexer.tokens import Token
from lexer.errors import LexLineError as Error


class LineLexer:
    def __init__(self, line: str) -> None:
        self.line: str = line
        self.tokens: list[Token] = []
        self.first = True

        self.variable = False
        self.string = False
        self.expr = False

        return

    def _append(self, token: Token) -> None:
        self.tokens.append(token)

        return

    def _analyze_char(self, char_num: int, char: str) -> None:
        print(char)

        if char == "\n":
            raise Error(char_num,
                        char,
                        self.line,
                        "Found \\n, invalid char"
                        )

        return

    def analyze(self) -> None:
        """
        Analyzes the given line
        """

        splitted = list(self.line)

        for char_num, char in enumerate(splitted):
            self._analyze_char(char_num, char)

        return
