def fmetric (a):
    feets = (a * 39.37) // 12 
    inches = (a * 39.37) % 12
    return(feets, inches)

def tmetric (feet, inch):
    inches = (feet * 12 + inch) * 0.0254
    return(inches)
    