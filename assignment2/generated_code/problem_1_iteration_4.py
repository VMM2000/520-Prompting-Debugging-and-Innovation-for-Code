def similar_elements(list1, list2):
    set1 = set((tuple(i) for i in list1))
    set2 = set((tuple(i) for i in list2))
    intersection = set1.intersection(set2)
    return list(intersection)