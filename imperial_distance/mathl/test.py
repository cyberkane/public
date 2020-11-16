import mathl.core as core

class Test_Calc:
    def __init__(self, afeet, ainch, bfeet, binch):
        self.afeet = afeet
        self.bfeet = bfeet
        self.ainch = ainch
        self.binch = binch

    def test1(self):
        if core.sum(self.afeet, self.ainch, self.bfeet, self.binch) == (6,1):
            return(True)
    
    def test2(self):
        if core.diff(self.afeet, self.ainch, self.bfeet, self.binch) == (0,9):
            return (True)

    def test3 (self, factor):
        if core.mul(self.afeet, self.ainch, factor) == (1.5, 2.5):
            return (True)
    
    def test4 (self, factor):
        if core.div(self.afeet, self.ainch, factor) == (6.0, 10.0):
            return (True)
