class LexerError(Exception):
    __module__ = "builtins"
    def __init__(self, msg):
        self.msg = msg
        return
    def __str__(self):
        return self.msg

class dacode:
    def lexer(code):
        pos = 1
        line = 1
        col = 1
        typee = ""
        out = {}
        for c in code:
            if c in "1234567890":
                typee = "number"
            elif c == "+":
                typee = "plus"
            elif c == "\n":
                typee = "NL"
                line += 1
                col = 0
            else:
                raise LexerError("Error while running the compiler:\n"
                                + (code.split('\n')[line-1] if code.split('\n') else code) + "\n"
                                + "-"*(col-1) + "^")
            out[pos] = {c: typee}
            pos += 1
            col += 1
        return out
    def parser(lexed):
        pass
print(dacode.lexer("12+34"))
