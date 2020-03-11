def capitalize(s):
    even, odd = [], []
    for count,letter in enumerate(s):
        if count % 2 == 0:
            even.append(letter.upper())
            odd.append(letter)
        else:
            odd.append(letter.upper())
            even.append(letter)
    return ["".join(even), "".join(odd)]


s = "abcdefg"
print(capitalize(s))