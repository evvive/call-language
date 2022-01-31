from call.lexer.tokens import Token, Tokens
from call.ast.types import Branch, Instructions
from call.ast.errors import BranchError
from call.types import TypeGenerator
from call.types.errors import TypeGenerationError
from call.types.types import Types


class BranchGenerator:
    """
    Generates the branch for one line
    """

    def __init__(self, tokens: list) -> None:
        self.tokens: list[Token] = tokens
        self.ast: Branch

        return

    def generate(self) -> None:
        """
        Generates the branch
        """

        print("Generating AST...")
        self.instruction: Instructions

        if len(self.tokens) == 0:
            raise BranchError(self.tokens, self.tokens[0], "Empty line")

        if self.tokens[0].token != Tokens.KEYWORD:
            raise BranchError(
                    self.tokens,
                    self.tokens[0],
                    "1st token should be ALWAYS a keyword"
                    )

        instruction = self.tokens[0].value.lower().strip()

        if instruction not in Instructions:
            raise BranchError(
                    self.tokens,
                    self.tokens[0],
                    "Invalid instruction"
                    )

        if instruction == "mpush":
            print("MPUSH")
            if len(self.tokens) != 2:
                raise BranchError(
                        self.tokens,
                        self.tokens[0],
                        "mpush has invalid args"
                        )

            param = self.tokens[1]

            if param.token == Tokens.NUMBER:
                param_type = Types.F64
            elif param.token == Tokens.STRING:
                param_type = Types.STR
            elif param.token == Tokens.KEYWORD:
                if param.value.strip().lower() == "true" or param.value.strip().lower() == "false":
                    param_type = Types.BOL

            var = TypeGenerator(param_type, param.value)

            print(var)
