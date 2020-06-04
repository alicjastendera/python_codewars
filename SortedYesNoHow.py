def is_sorted_and_how(arr):
    is_ascending = False
    is_descending = False

    for i in range(len(arr)-1):
        if arr[i] - arr[i+1] < 0:
            is_ascending = True
        if arr[i] - arr[i+1] > 0:
            is_descending = True

    if is_ascending is True and is_descending is False:
        return "yes, ascending"
    
    if is_ascending is False and is_descending is True:
        return "yes, descending"

    return "no"
