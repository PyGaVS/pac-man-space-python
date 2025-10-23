import arcade

class Input():
    def __init__(self):
        self.history = ["N", "N", "N", "N"]
        print(self.history)
    
    def addInput(self, input):
        self.history.append(input)
        self.history = self.history[-4:]

        return self.checkSpecial()

    def checkSpecial(self):
        special = ""

        if self.history[-3] == self.history[-2] and self.history[-2] == self.opposite(self.history[-1]):
            special = "speed"

        return special

    def flip(self):
        pass
    
    def opposite(self, input):
        opposites = {
            "R": "L",
            "L": "R",
            "U": "D",
            "D": "U"
        }

        return opposites.get(input, None)
    
    def getHistory(self):
        symbols = {
            "R": "🡆",
            "L": "🡄",
            "U": "🡅",
            "D": "🡇"
        }

        str=""

        for input in self.history:
            str = str + " " + symbols.get(input, "⏹️")

        return str