import random
import string

def generateName():
    return ("").join(random.choices(string.ascii_letters, k=6))
