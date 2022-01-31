# from call.lexer.linelexer import LineLexer
# from call.ast.branchgenerator import BranchGenerator
from call.types import TypeGenerator
from call.types.types import Types
from call.types.errors import TypeGenerationError
from call.logger import Logger, ErrType, StatusType

# line = 'mpush 0.24'

# lexer = LineLexer(line)
# lexer.analyze()

# branch = BranchGenerator(lexer.tokens)
# branch.generate()

# BOOLEAN TEST
logger = Logger(__name__, True)
logger.print(ErrType.INFO, "logger started", StatusType.BEGIN)

b = TypeGenerator(Types.BOL, "true")
logger.print(ErrType.INFO, "(bool) test passed", StatusType.NORMAL)
try:
    b = TypeGenerator(Types.BOL, "flex")
except TypeGenerationError:
    logger.print(ErrType.INFO, "(bool2) test passed", StatusType.NORMAL)
    pass

# STRING TEST
s = TypeGenerator(Types.STR, "Flex Mark")
logger.print(ErrType.INFO, "(str) test passed", StatusType.NORMAL)

# F64 TEST
f = TypeGenerator(Types.F64, "0.646464646464")
logger.print(ErrType.INFO, "(f64) test passed", StatusType.NORMAL)

try:
    f = TypeGenerator(Types.F64, "0.64.64.64.64.64.")
except TypeGenerationError:
    logger.print(ErrType.INFO, "(f64_2) test passed", StatusType.NORMAL)
    pass

# AUTO-DETECT TEST
a = TypeGenerator.detect("0.2")
if a == Types.F64:
    logger.print(ErrType.INFO, "(autodetect) test passed", StatusType.NORMAL)

a = TypeGenerator.detect("hello")
if a == Types.STR:
    logger.print(ErrType.INFO, "(autodetect2) test passed", StatusType.NORMAL)

a = TypeGenerator.detect("true")
if a == Types.BOL:
    logger.print(ErrType.INFO, "(autodetect3) test passed", StatusType.NORMAL)

a = TypeGenerator.detect("not true")
if a == Types.STR:
    logger.print(ErrType.INFO, "(autodetect4) test passed", StatusType.NORMAL)

logger.print(ErrType.INFO, "all test passed!", StatusType.EXIT)
exit(0)
