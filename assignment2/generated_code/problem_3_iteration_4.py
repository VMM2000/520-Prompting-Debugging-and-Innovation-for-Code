import heapq

def heap_queue_largest(numbers):
    return heapq.nlargest(len(numbers), numbers)
