def condition(x):
    if isinstance(x, (int, float)) and x==0 and x is not False:
        return True
    else:
        return False


def move_zeros(array):
    return sorted(array, key = lambda x: True if isinstance(x, (int, float)) and x==0 and x is not False else False)        
