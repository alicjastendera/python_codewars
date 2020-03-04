def validBraces(braces):
    old = ""

    while old != braces:
        old = braces
        braces = braces.replace("{}", "").replace("()", "").replace("[]", "")

    return braces == ""