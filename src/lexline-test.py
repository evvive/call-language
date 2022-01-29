from lexer.linelexer import LineLexer

line = """mpush 27\n"""

lexer = LineLexer(line)

lexer.analyze()
