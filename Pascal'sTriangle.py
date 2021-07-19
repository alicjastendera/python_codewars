from math import factorial


def v1_pascals_triangle(n):
    row, result = [1], []
    shift = [0]
    for _ in range(n):
        print(row)
        result.extend(row)
        row = [left + right for left, right in zip(row + shift, shift + row)]
    return result


def v2_pascals_triangle(n):
    row = []
    for i in range(n):
        for k in range(i + 1):
            element = factorial(i) / (factorial(k) * factorial(i - k))
            row.append(int(element))
    return row


def pascals_triangle(n):
    result = []
    for i in range(1, n+1):
        val = 1
        for j in range(1, i + 1):
            result.append(val)
            val = val * (i - j) // j
    return result
