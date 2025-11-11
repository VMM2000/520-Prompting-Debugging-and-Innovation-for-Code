def similar_elements(list1, list2):
    # Create dictionaries to store the frequency of elements in both lists
    dict1 = {}
    dict2 = {}
    
    # Count the frequency of elements in list1 and list2
    for element in list1:
        dict1[element] = dict1.get(element, 0) + 1
    for element in list2:
        dict2[element] = dict2.get(element, 0) + 1
    
    # Find the elements that have the same frequency in both lists
    similar_elements = []
    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            similar_elements.append(key)
    
    # Return the similar elements
    return similar_elements
