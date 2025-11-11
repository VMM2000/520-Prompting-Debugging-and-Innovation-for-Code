import heapq

def heap_queue_largest(numbers, n):
    largest_numbers = heapq.nlargest(n, numbers)
    return largest_numbers