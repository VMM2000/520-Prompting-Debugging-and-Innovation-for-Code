import re

def find_char_long(string):
    pattern = '\\w{4,}'
    matches = re.findall(pattern, string)
    return matches