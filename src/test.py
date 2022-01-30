from lexer.linelexer import LineLexer

line = 'a @b 2555 555 5555 [344] 2"24string"'

lexer = LineLexer(line)

lexer.analyze()
