import heapq

def heap_queue_largest(numbers):
    heap = []
    for num in numbers:
        heapq.heappushpop(heap, num)
    return heap