import re

def find_char_long(string):
    pattern = '(?=.*[a-zA-Z]{4,})'
    matches = re.findall(pattern, string)
    return matches