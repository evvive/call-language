from dataclasses import dataclass
from enum import Enum, unique, auto, EnumMeta


class _ContainsMetaClass(EnumMeta):
    """
    Adds __contains__ method to enum
    """

    def __contains__(cls, item):
        return item in [v.value for v in cls.__members__.values()]


@unique
class Instructions(Enum, metaclass=_ContainsMetaClass):
    """
    Instruction set for v0.1-essential
    with __contains__ method
    """

    # Stack operations
    MPUSH = "mpush"  # Push to master stack
    MPOP = "mpop"    # Pop to master stack
    PUSH = "push"    # Push to user stack
    POP = "pop"      # Pop to user stack


@unique
class CALLType(Enum):
    STR = auto()  # 'Hello, World'
    F64 = auto()  # .22222
    BOL = auto()  # true
    VAR = auto()  # @flex


@dataclass
class CALLValue:
    type: CALLType
    value = 0

    @classmethod
    def __init__(self, type: CALLType, value) -> None:
        """IMPORTANT: Exceptions must be handled by other"""
        if type == CALLType.STR:
            value = str(value)
        elif type == CALLType.F64:
            value = float(value)
        elif type == CALLType.BOL:
            value = bool(value)
        else:
            value = value  # NOTE: VAR type can't be casted to other

        return


@dataclass
class Branch:
    """
    CALL AST branch class
    """
    instr: Instructions
    params: list

    def __init__(self, instr: Instructions, params: list) -> None:
        self.instr = instr
        self.params = params

        return
