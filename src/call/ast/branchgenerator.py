from call.lexer.tokens import Token, Tokens
from call.ast.types import Branch, Instructions


class BranchGenerator:
    """
    Generates the branch for one line
    """

    def __init__(self, tokens: list) -> None:
        self.tokens: list[Token] = tokens
        self.ast: Branch

        return

    def _handle_keyword(self, token: Token) -> None:
        if token.value.strip() in Instructions:
            print("Recognized instruction")
            return

    """
    Handles every token
    """

    def _handle_token(self, token: Token) -> None:
        print("Token:", token.token, "\nValue:", token.value)

        if token.token == Tokens.KEYWORD:
            print("Keyword!")
            self._handle_keyword(token)

        return

    """
    Generates the branch
    """

    def generate(self) -> None:
        print("Generating AST...")
        for token in self.tokens:
            self._handle_token(token)
