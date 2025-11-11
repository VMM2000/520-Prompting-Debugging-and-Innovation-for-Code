import re

def find_char_long(string):
    pattern = '\x08\\w{4,}\x08'
    return re.findall(pattern, string)