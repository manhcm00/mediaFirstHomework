import math

def numberOfCombinations(k,N):
    return (math.factorial(N) / (math.factorial(k) * math.factorial(N - k)))

def prob(n, p, r):
    return numberOfCombinations(r - 1, n - 1) * (p ** r) * ((1 - p) ** (n - r))

def infoMeasure(n, p, r):
    return - math.log(prob(n, p, r), 2)

def sumProb(N, p, r):
    result = 0
    for i in range(r, N + 1):
        result += prob(i, p, r)
    return result

def approxEntropy(N, p, r):
    '''
    :param N: Tổng số xu được tung (tổng số phép thử bernoulli)
    :param p: Xác suất của phép thử bernoulli (phép tung xu) tương ứng
    :param r: Số lần thành công (ngửa) mà đạt được thì dừng
    :return: entropy gần đúng với đầu vào là N, p và r
    '''
    result = 0
    for i in range(r, N + 1):
        result = result + prob(i, p, r) * infoMeasure(i, p, r)
    return result