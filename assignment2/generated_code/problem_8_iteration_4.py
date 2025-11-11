def find_Rotations(str1, str2):
    # Create a list to store the rotation matrices
    rotation_matrices = []
    
    # Create two lists to store the characters in the strings
    chars1 = list(str1)
    chars2 = list(str2)
    
    # Iterate over the characters in the strings
    for char1, char2 in zip(chars1, chars2):
        # Create the rotation matrix for the character
        rotation_matrix = [[0, 1], [1, 0]]
        
        # Add the rotation matrix to the list
        rotation_matrices.append(rotation_matrix)
    
    # Calculate the number of rotations required
    num_rotations = len(str1) - len(str2)
    
    return num_rotations
