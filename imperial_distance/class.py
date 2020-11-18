from mathl import core

class Thing ():
    def __init__ (self):
        return()


class Element ():
    def __init__ (self, name, symbol, number, a):
        self.name = name
        self.symbol = symbol
        self.number = number
        self.a = a
    def dump(self):
        print(self.name)
        print(self.symbol)
        print(self.number)

hydrogen = Element("Hydrogen", "H", 1, 5)


aFeet = 3
aInch = 5
bFeet = 2
bInch = 8
factor = 0.5

class Distance ():
    def __init__(self, afeet, ainch, bfeet, binch):
        self.afeet = afeet
        self.bfeet = bfeet
        self.ainch = ainch
        self.binch = binch

    def summ(self):
        plus = core.sum(self.afeet, self.ainch, self.bfeet, self.binch)
        return(plus)
    
    def deff(self):
        minus = core.diff(self.afeet, self.ainch, self.bfeet, self.binch)
        return(minus)

    def mul(self, factor):
        umn = core.mul(self.afeet, self.ainch, factor)
        return(umn)

    
    def div(self, factor):
        dl = core.div(self.afeet, self.ainch, factor)
        return(dl)

calc = Distance(aFeet, aInch, bFeet, bInch)

print(calc.summ())
print(calc.deff())
print(calc.mul(factor))
print(calc.div(factor))

class Volume ():
    def __init__ (self, xfeet, xinch, yfeet, yinch, zfeet, zinch):
        self.xfeet = xfeet
        self.yfeet = yfeet
        self.zfeet = zfeet
        self.xinch = xinch
        self.yinch = yinch
        self.zinch = zinch

    def sfloor (self):
        sffloor = (self.xfeet * 12 + self.xinch) * (self.yfeet * 12 + self.yinch) // 12
        sifloor = (self.xfeet * 12 + self.xinch) * (self.yfeet * 12 + self.yinch) % 12
        return(sffloor, sifloor)
    
    def swall (self):
        sfwall = ((self.xfeet * 12 + self.xinch) * (self.zfeet * 12 + self.zinch) + ((self.yfeet * 12 + self.yinch) * (self.zfeet * 12 + self.zinch)) ) * 2 // 12
        siwall = ((self.xfeet * 12 + self.xinch) * (self.zfeet * 12 + self.zinch) + ((self.yfeet * 12 + self.yinch) * (self.zfeet * 12 + self.zinch)) ) * 2 % 12
        return(sfwall, siwall)
    
    def sceiling (self):
        sfceiling = (self.xfeet * 12 + self.xinch) * (self.yfeet * 12 + self.yinch) // 12
        siceiling = (self.xfeet * 12 + self.xinch) * (self.yfeet * 12 + self.yinch) % 12
        return(sfceiling, siceiling)
    
    def vroom (self):
        vfroom = (self.xfeet * 12 + self.xinch) * (self.yfeet * 12 + self.yinch) * (self.zfeet * 12 + self.zinch) // 12
        viroom = (self.xfeet * 12 + self.xinch) * (self.yfeet * 12 + self.yinch) * (self.zfeet * 12 + self.zinch) % 12
        return (vfroom, viroom)

vol = Volume(6, 4, 3, 2, 5, 6)

# print(vol.sfloor())
# print(vol.swall())
# print(vol.sceiling())
# print(vol.vroom())

class Transport ():
    def __init__(self, mass, power, wheels):
        self.mass = mass
        self.power = power
        self.wheels = wheels
    
class Car (Transport):
    # name = "Машина"
    # sits = 4

    def set_sits(self, sit):
        self.sits = sit
    
    def info (self,name):
        self.name = name
        
class Bus (Transport):
    name = "Автобус"
    sits = 24
    stands = 26
    way = "11 мамршрут"

    def bus (self,sits,stands,way):
        self.sits = sits
        self.stands = stands
        self.way = way
    
    def info (self, name):
        self.name = name

class Truck (Transport):
    name = "Грузовик"
    cargo = 2300

    def truck (self, cargo):
        self.cargo = cargo
    
    def info (self,name):
        self.name = name

v1 = Transport(1200, 120, 4)
v2 = Bus(2100, 430, 6)
v3 = Truck(3400, 850, 6)

spisok = [v1, v2, v3]

for i in spisok:
    print()