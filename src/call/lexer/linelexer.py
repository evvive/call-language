from lexer.tokens import Token, Tokens, KEYWORD_CHARS, NUMBER_CHARS
from lexer.errors import LexLineError as Error


class LineLexer:
    def __init__(self, line: str) -> None:
        self.line: str = line
        self.tokens: list[Token] = []
        self.first = True

        self.variable = False
        self.string = False
        self.string_ignore = False
        self.expr = False
        self.end = False

        return

    def _append(self, token) -> None:
        self.tokens.append(token)

        return

    def _handle_expr(self, char_num: int, char: str) -> None:
        if char == "]":
            self.expr = False

            return

        self.tokens[len(self.tokens) - 1].value += char

        return

    def _handle_str(self, char_num: int, char: str) -> None:

        if char == "\\":
            self.string_ignore = True

            return

        if self.string_ignore is True:
            self.string_ignore = not self.string_ignore

            self.tokens[len(self.tokens) - 1].value += char

            return

        if char == '"':
            self.string = False

            return

        self.tokens[len(self.tokens) - 1].value += char

        return

    def _handle_variable(self, char_num: int, char: str):
        if self.first is True:
            self._append(Token(
                Tokens.VARIABLE,
                char
            ))
        elif self.tokens[len(self.tokens) - 1].token != Tokens.VARIABLE:
            self._append(Token(
                Tokens.VARIABLE,
                char
            ))
        elif self.tokens[len(self.tokens) - 1].token == Tokens.VARIABLE:
            self.tokens[len(self.tokens) - 1].value += char

        return

    def _handle_keyword(self, char_num: int, char: str) -> int:
        if self.first is True:
            self._append(Token(
                Tokens.KEYWORD,
                char
            ))

            return 0
        elif self.tokens[len(self.tokens) - 1].token != Tokens.KEYWORD:
            self._append(Token(
                Tokens.KEYWORD,
                char
            ))

            return 1
        elif self.tokens[len(self.tokens) - 1].token == Tokens.KEYWORD:
            self.tokens[len(self.tokens) - 1].value += char

            return 1

    def _handle_num(self, char_num: int, char: str) -> None:
        if self.first is True:
            self._append(Token(
                Tokens.NUMBER,
                char
            ))
        elif self.tokens[len(self.tokens) - 1].token != Tokens.NUMBER:
            self._append(Token(
                Tokens.NUMBER,
                char
            ))
        elif self.tokens[len(self.tokens) - 1].token == Tokens.NUMBER:
            self.tokens[len(self.tokens) - 1].value += char

    def _analyze_char(self, char_num: int, char: str) -> None:
        if char == "\n":
            raise Error(char_num,
                        self.line,
                        "Found \\n, invalid char"
                        )

        if char == ";" and self.string is False and self.expr is False:
            self.end = True

            return

        if char == '"' and self.string is False and self.expr is False:
            self._append(Token(
                Tokens.STRING
            ))

            self.string = True

            return

        if (char in NUMBER_CHARS and self.string is False
           and self.expr is False):
            self._handle_num(char_num, char)

        if char == "[" and self.expr is False and self.string is False:
            self._append(Token(
                Tokens.EXPR
            ))

            self.expr = True

            return

        if char == "]" and self.expr is False and self.string is False:
            raise Error(
                char_num,
                self.line,
                "Invalid ]"
            )

        if self.expr is True and self.string is False:
            self._handle_expr(char_num, char)

            return

        if self.string is True:
            self._handle_str(char_num, char)

            return

        if char == "@" and self.variable is False:
            self.variable = not self.variable

            return
        elif char == "@" and self.variable is True:
            raise Error(
                char_num,
                self.line,
                "Invalid variable (@) token"
            )

            return

        if self.variable is True and char in NUMBER_CHARS:
            raise Error(
                char_num,
                self.line,
                "Invalid variable!"
            )

        if self.variable is True:
            self._handle_variable(char_num, char)

        if char in KEYWORD_CHARS and not self.variable:
            status = self._handle_keyword(char_num, char)

            if status != 0:
                return

        if char == " " and self.string is False:
            self.variable = False
            self.first = True

            return
            if self.first is True:
                return

        if self.first is True:
            self.first = not self.first

            return

    def analyze(self) -> None:
        """
        Analyzes the given line
        """

        splitted = list(self.line)

        for char_num, char in enumerate(splitted):
            self._analyze_char(char_num, char)

            if self.end is True:
                break

        return
