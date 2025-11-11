import re

def find_char_long(string):
    # The regex pattern for words that are at least 4 characters long
    pattern = r'\w{4,}'
    # Use re.findall() to find all matches of the pattern in the string
    matches = re.findall(pattern, string)
    # Return the list of matches
    return matches
