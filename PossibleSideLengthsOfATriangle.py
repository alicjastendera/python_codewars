from math import pow, sqrt

def side_len(x, y):
    possible_sides = []
    z = 1
    while x + y > z:
        if x + z > y and y + z > x:
            possible_sides.append(z)
        z = z + 1

    for z in possible_sides:
        sides = [x, y, z]
        sides.sort()
        if pow(sides[0], 2) + pow(sides[1], 2) == pow(sides[2], 2):
            possible_sides.remove(z)

    return possible_sides