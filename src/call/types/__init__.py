from call.types.types import Types, Value
from call.lexer.tokens import Token, Tokens
from call.types.errors import TypeGenerationError


class TypeGenerator:
    def __init__(self, type: Types, value: str) -> None:
        self.type = type
        self.value: Value = None

        if type == Types.STR:
            self.value = Value(Types.STR, value)
        elif type == Types.F64:
            self.value = self.f64(value)
        elif type == Types.BOL:
            self.value = self.bol(value)
        else:
            raise TypeGenerationError(type, value, "Unknown type")

        return

    @staticmethod
    def f64(value: str):
        try:
            f64 = float(value)
        except ValueError:
            raise TypeGenerationError(Types.F64, value, "Invalid f64")

        return Value(Types.F64, f64)

    @staticmethod
    def bol(value: str) -> Value:
        if value.strip().lower() == "true":
            return Value(Types.BOL, True)
        elif value.strip().lower() == "false":
            return Value(Types.BOL, False)
        else:
            raise TypeGenerationError(Types.BOL, value, "Invalid bol")

    @staticmethod
    def detect(value: str) -> Value:
        try:
            t = TypeGenerator.bol(value).type
        except TypeGenerationError:
            t = None
            try:
                t = TypeGenerator.f64(value).type
            except TypeGenerationError:
                if t == Types.BOL:
                    return Types.BOL
                return Types.STR

            return Types.F64

        return Types.BOL

    @staticmethod
    def detect_token(token: Token) -> Value:
        t = None

        if token.token == Tokens.KEYWORD:
            t = TypeGenerator.bol(token.value).type
        elif token.token == Tokens.NUMBER:
            t = TypeGenerator.f64(token.value).type
        elif token.token == Tokens.STRING:
            t = Types.STR

        return t
