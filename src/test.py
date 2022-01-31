from call.lexer.linelexer import LineLexer
from call.ast.branchgenerator import BranchGenerator

line = 'mpush 0.24'

lexer = LineLexer(line)
lexer.analyze()

branch = BranchGenerator(lexer.tokens)
branch.generate()
