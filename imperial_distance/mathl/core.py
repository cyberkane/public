import math

def sum (aFeet,aInch,bFeet,bInch):
    aInches = (aFeet * 12 + aInch)
    bInches = (bFeet * 12 + bInch)
    a = abs(aInches + bInches) // 12
    b = abs(aInches + bInches) % 12
    return (a, b)

def diff (aFeet,aInch,bFeet,bInch):
    aInches = (aFeet * 12 + aInch)
    bInches = (bFeet * 12 + bInch)
    a = abs(aInches - bInches) // 12
    b = abs(aInches - bInches) % 12
    return (a, b)

def mul (aFeet,aInch,factor):
    aFeets = (aFeet * factor)
    aInches = (aInch * factor)
    a = abs (aFeets + abs(aInches) // 12)
    b = abs (aInches % 12)
    return (a, b)

def div (aFeet,aInch,factor):
    aFeets = aFeet * 12
    aInches = aInch
    a = abs(aFeets + aInches) / factor // 12
    b = int(aFeets + aInches) / factor % 12
    return (a, b)
