import re
def fake_bin(x):
    x = re.sub("[1-4]","0",x)
    return re.sub("[5-9]", "1", x)