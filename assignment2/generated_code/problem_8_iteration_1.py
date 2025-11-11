def find_Rotations(s):
    count = 0
    same_string = False
    while not same_string:
        count += 1
        same_string = True
        for i in range(len(s)):
            if s[i] != s[i + count]:
                same_string = False
                break
    return count