class LexLineError(Exception):
    def __init__(self, char_num: int, line: str, message: str):
        self.char     = list(line)[char_num]
        self.char_num = char_num
        self.message  = message
        self.line     = line

        return

class LexerError(Exception):
    def __init__(self, char_num: int, line: str, line_num: int, message: str):
        self.char     = list(line)[char_num]
        self.char_num = char_num
        self.line_num = line_num
        self.message  = message

        return
