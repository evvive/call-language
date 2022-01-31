from enum import Enum, unique
from dataclasses import dataclass


@unique
class Types(Enum):
    STR = "STR"
    F64 = "F64"
    BOL = "BOL"
    VAR = "VAR"


@dataclass
class Value:
    type: Types

    def __init__(self, type: Types, value: any):
        if type == Types.STR:
            self.type = Types.STR
            self.value: str = value
        elif type == Types.F64:
            self.type = Types.F64
            self.value: float = value
        elif type == Types.BOL:
            self.type = Types.BOL
            self.value: bool = value
