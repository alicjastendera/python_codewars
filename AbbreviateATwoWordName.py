def abbrev_name(data):
    name, surname = data.split() 
    return ('.'.join([list(name)[0], list(surname)[0]])).upper()
