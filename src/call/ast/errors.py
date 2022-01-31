from call.lexer.tokens import Token


class BranchError(Exception):
    def __init__(self, tokens: list, token: Token, message: str) -> None:
        self.tokens: list = tokens
        self.token: Token = token
        self.message = message

        return
