import heapq

def heap_queue_largest(numbers):
    largest_numbers = heapq.nlargest(3, numbers)
    return largest_numbers