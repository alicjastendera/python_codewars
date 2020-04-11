def segments(m, a):
    answer = list(range(m+1))
    for x in range(m+1):
        for numbers in a:
            if numbers[0] <= x <= numbers[1]:
                answer.remove(x)
                break
    return answer
