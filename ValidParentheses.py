import re

def valid_parentheses(string):
    string = re.sub("[A-Za-z0-9]", "", string)
    old = ""
    while old != string:
        old = string
        string = string.replace("()", "")

    return string == ""
