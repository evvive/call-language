from call.types.types import Types, Value
from call.types.errors import TypeGenerationError


class TypeGenerator:
    def __init__(self, type: Types, value: Value) -> None:
        if type == Types.STR:
            value = str(value)
        elif type == Types.F64:
            self._f64()

        return

    def _f64(self):
        try:
            f64 = float(self.value.value)
        except ValueError:
            raise TypeGenerationError(self.type, self.value, "Invalid f64")
        finally:
            return f64
