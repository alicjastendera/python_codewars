import re
def get_count(input_str):
    return len(re.findall("[aeiou]", input_str))
