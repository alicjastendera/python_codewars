def in_array(array1, array2):
    return sorted(list(set([part for word in array2 for part in array1 if part in word])))
