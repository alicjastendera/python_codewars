import string
def scoobydoo(villian, villians):
    letters = (villian[-5:] + villian[0:-5])[::-1]
    even = letters[1::2]
    odd = letters[::2]
    new_even = [string.ascii_lowercase[x - 26] if x > 25 else string.ascii_lowercase[x] for x in 
                [string.ascii_lowercase.index(letter) + 5 for letter in even]]

    result = [None]*(len(villian))
    result[::2] = odd
    result[1::2] = new_even

    for _ in villians:
        if _.replace(" ", "").lower() == "".join(result):
            return _
