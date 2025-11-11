def similar_elements(tuple1, tuple2):
    return [x for (x, y) in zip(tuple1, tuple2) if x == y]