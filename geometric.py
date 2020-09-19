import math


def prob(n, p):
    return (1 - p) ** (n - 1) * p

def infoMeasure(n, p):
    return - math.log(prob(n, p), 2)

def sumProb(n, p):
    '''
    tổng xác suất của phân bố geometric = p * ((1-p) ** 0 + (1-p)**1 + (1-p) ** 2 + ... + (1-p) ** (n-1))
                                        = p * (1 / (1 - (1-p)))
                                        = p * (1 / p) = 1
    '''
    result = 0
    for i in range(1, n + 1):
        result += prob(i, p)
    return result

def approxEntropy(n, p):
    '''
    :param n: Symbol mà ta đang cần tính xác suất
    :param p: Xác suất của phép thử bernoulli (phép tung xu) tương ứng
    :return: entropy gần đúng với đầu vào là n và p
    '''
    result = 0
    for i in range(1, n + 1):
        result = result + prob(i, p) * infoMeasure(i, p)
    return result
