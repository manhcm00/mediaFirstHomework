import math

def numberOfCombinations(k,N):
    return (math.factorial(N) / (math.factorial(k) * math.factorial(N - k)))

def prob(n, p, N):
    return numberOfCombinations(n, N) * (p ** n) * ((1 - p) ** (N - n))

def infoMeasure(n, p, N):
    return - math.log(prob(n, p, N), 2)

def sumProb(N, p):
    '''
    tổng xác suất của phân bố binomial = tổng xích ma của [(tổ hợp chập k của N) * (p ** k) * ((1 - p) ** (N - k))]
                                        = 1
    '''
    result = 0
    for i in range(1, N + 1):
        result += prob(i, p, N)
    return result

def approxEntropy(N, p):
    '''
    :param N: Tổng số xu được tung (tổng số phép thử bernoulli)
    :param p: tham số, là xác suất của phép thử bernoulli (phép tung xu) tương ứng
    :return: entropy gần đúng với đầu vào là N và p
    '''
    result = 0.0
    for i in range(1, N + 1):
        result = result + prob(i, p, N) * infoMeasure(i, p, N)
    return result