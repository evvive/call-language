from call.types.types import Types, Value


class TypeGenerationError(Exception):
    def __init__(self, type: Types, value: Value, message: str) -> None:
        self.type: Types = type
        self.value: Value = value
        self.message: str = message

        return
