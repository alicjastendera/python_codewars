import string
def alphabet_position(text):
    positions =[]
    for sign in text:
        if sign.isalpha():
            position = string.ascii_lowercase.index(sign.lower())
            positions.append(str(position + 1))
    return " ".join(positions)


alphabet_position("The sunset sets at twelve o' clock.")
