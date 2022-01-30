from call.lexer.tokens import Token
from call.ast.types import Branch


# TODO: Do this later, first do ASTLine
class ASTGenerator:
    def __init__(self, tokens: list) -> None:
        self.tokens: list[Token]
        self.ast: list[Branch]
