import math

def removNb(n):
    sum = (n * (n + 1)) / 2 + 1
    max = math.sqrt(sum)
    factor = 2
    factorsList = []

    for factor in range(2, n):
        if (sum % factor == 0) and (sum / factor <= n):
            if factor != sum/factor:
                numerList = [factor-1, sum / factor - 1]
                factorsList.append(numerList)
    return factorsList

removNb(26)