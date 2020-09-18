import math


def prob(n, p):
    return p ** n

def infoMeasure(n, p):
    return - math.log(p ** n, 2)

def sumProb(n, p):
    result = 0
    for i in range (1, n + 1):
        result = result + p ** i
    return result

def approxEntropy(n, p):
    result = 0
    for i in range(1, n + 1):
        result = result - p ** i * math.log(p ** i, 2)
    return result