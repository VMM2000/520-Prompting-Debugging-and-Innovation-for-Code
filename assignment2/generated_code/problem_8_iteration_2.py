def find_Rotations(s):
    char_set = set(s)
    rotations = len(s) - len(char_set)
    return rotations