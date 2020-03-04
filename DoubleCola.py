def whoIsNext(names, r):
    counter = 0
    actualLen = len(names)
    turns = 0

    while counter<r:
        counter = counter + actualLen
        actualLen *= 2
        turns = turns +1

    if turns == 1 :
        return names[r-1]

    actualLen /=2 
    counter = counter-actualLen
    remainingChanges = r - counter
    remainingChanges = int(remainingChanges / (actualLen/len(names)))
    return names[remainingChanges]