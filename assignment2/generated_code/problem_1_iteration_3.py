def similar_elements(tuple1, tuple2):
    similar_tuple = ()
    for elem in tuple1:
        if elem in tuple2:
            similar_tuple += (elem,)
    return tuple(similar_tuple)