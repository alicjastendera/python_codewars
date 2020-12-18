def reverse(seq):  
    left_side = 0
    right_side = len(seq)-1
    while left_side < right_side:
        temporary = seq[left_side]
        seq[left_side] = seq[right_side]
        seq[right_side] = temporary

        left_side += 1
        right_side -= 1
    return seq