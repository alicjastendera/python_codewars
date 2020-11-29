import operator
def meeting(s):
    names = s.upper().split(';')
    names = [v.split(':') for v in names]
    names_rev = [(y, x) for x,y in names]
    x = sorted(names_rev, key = operator.itemgetter(0, 1))
    return("".join("({}, {})".format(pair[0], pair[1]) for pair in x))
