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
    value: any = 0
