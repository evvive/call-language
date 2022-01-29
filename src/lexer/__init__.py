from lexer.tokens import Token, Tokens, KEYWORD_CHARS
from lexer.errors import LexLineError, LexerError

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

    def lexline(self, line: str):
        splitted      = list(line)
        tokens: list[Token] = []
        first         = True
        variable      = False
        string        = False
        string_ignore = False
        expr          = False

        for char_num, char in enumerate(splitted):

            if tokens == []: first = True

            if char == "\n":
                raise LexLineError(char_num, line, "Invalid \\n char")

            if char == ";" and string is False and expr is False: break

            if char == '"' and string is False and expr is False:
                tokens.append(Token(Tokens.EXPR))

                string = True

                continue

            if char == '[' and expr is False and string is False:
                tokens.append(Token(Tokens.EXPR))

                expr = True

                continue

            if char == "]" and expr is False and string is False:
                raise LexLineError(char_num, line, "Invalid ]")

            if expr is True and string is False:
                if char == "]":
                    expr = False

                    continue

                tokens[len(tokens) - 1].value += char


                continue

            if string is True:
                if char == "\\":
                    string_ignore = True

                    continue

                if string_ignore is True:
                    string_ignore = not string_ignore

                    tokens[len(tokens) - 1].value += char

                    continue

                if char == '"':
                    string = False

                    continue

                tokens[len(tokens) - 1].value += char

                continue

            if char == "@" and variable is False:
                variable = True
            elif char == "@" and variable is True:
                raise LexLineError(char_num, line, "Invalid variable (@) token")


            if variable is True:
                if first is True:
                    tokens.append(Token(Tokens.VARIABLE, char))

                elif tokens[len(tokens) - 1].token != Tokens.VARIABLE:
                    tokens.append(Token(Tokens.VARIABLE, char))

                elif tokens[len(tokens) - 1].token == Tokens.VARIABLE:
                    tokens[len(tokens) - 1].value += char

            if char in KEYWORD_CHARS and not variable:
                if first is True:
                    tokens.append(Token(Tokens.KEYWORD, char))

                elif tokens[len(tokens) - 1].token != Tokens.KEYWORD:
                    tokens.append(Token(Tokens.KEYWORD, char))

                    continue
                elif tokens[len(tokens) - 1].token == Tokens.KEYWORD:
                    tokens[len(tokens) - 1].value += char

                    continue

            if char == " ":
                if first == True: continue

                if tokens[len(tokens) - 1].token == Tokens.KEYWORD:
                    first = True

                    continue
                elif tokens[len(tokens) - 1].token == Tokens.VARIABLE:
                    first = True

                    continue

            if first is True:
                first = not first

                continue

            # print("Invalid char '", char, "'")

        print(tokens)
