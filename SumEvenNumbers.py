def sum_even_numbers(seq): 
    sum = 0
    for i in seq:
        if i % 2 == 0: sum = sum + i
    return sum
