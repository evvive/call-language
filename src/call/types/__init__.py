from call.types.types import Types, Value
from call.types.errors import TypeGenerationError


class TypeGenerator:
    def __init__(self, type: Types, value: str) -> None:
        self.type = type
        self.value: Value = None

        if type == Types.STR:
            self.value = Value(Types.STR, value)
        elif type == Types.F64:
            self.value = self.f64(value)
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
        if value.value.strip().lower() == "true":
            return Value(Types.BOL, True)
        elif value.strip().lower() == "false":
            return Value(Types.BOL, False)
