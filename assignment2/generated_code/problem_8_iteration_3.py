def find_Rotations(s, k):
    if s == original_string:
        return 0
    original_string = s
    shortest_string = get_shortest_string(s)
    rotations = k - len(shortest_string)
    total_rotations = 0
    for i in range(len(s)):
        if s[i] == shortest_string[0]:
            total_rotations += 1
            s = s[1:] + s[0] + shortest_string
            rotations += 1
            s = s[1:]
    return total_rotations + rotations

def get_shortest_string(s):
    shortest_string = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1]
            if substring not in shortest_string:
                shortest_string = substring
    return shortest_string