def pendulum(values):
    lst = [None] * len(values)
    values = sorted(values)

    if len(values) % 2 == 1:
        position =  int(len(values)/2) # start position
    else:
        position =  int(len(values)/2) -1
    
    step = 1
    v = 1
    
    for i in values:
        lst[position] = i    
        position = position + step
        v = v * -1
        step = v * (abs(step) + 1)

    return lst
