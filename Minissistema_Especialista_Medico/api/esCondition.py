class Condition:
    def __init__(self, symbol):
        self.symbol = symbol
        if symbol == "=":
            self.index = 1
        elif symbol == ">":
            self.index = 2
        elif symbol == "<":
            self.index = 3
        elif symbol == "!=":
            self.index = 4
        else:
            self.index = -1

    def __str__(self):
        return self.symbol

    def to_string(self):
        return self.symbol
