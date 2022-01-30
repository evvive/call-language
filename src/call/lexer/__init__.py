from call.lexer.errors import LexLineError, LexerError
from call.lexer.linelexer import LineLexer


class Lexer:
    def __init__(self, code: str) -> None:
        self.code = code

    def lex(self):
        code = self.code.split("\n")

        for line_num, line in enumerate(code):
            print(f"Line {line_num}: {line}")
            try:
                tokens = self.lexline(line)
            except LexLineError as err:
                raise LexerError(
                        err.char_num,
                        err.line,
                        line_num,
                        f"LexLine: {err.message}"
                )
            finally:
                print(tokens)

    def lexline(self, line: str):
        lexer = LineLexer(line)
        lexer.analyze()

        return lexer.tokens
