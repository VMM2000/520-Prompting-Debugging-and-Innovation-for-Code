def find_Rotations(s):
    n = len(s)
    min_rotations = 0
    for rotation in range(n):
        if s[n - rotation - 1:] == s[n - rotation - 1:]:
            min_rotations = rotation + 1
            break
    return min_rotations