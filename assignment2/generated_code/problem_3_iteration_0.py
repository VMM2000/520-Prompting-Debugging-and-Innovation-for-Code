import heapq

def heap_queue_largest(numbers):
    heap = []
    for num in numbers:
        heapq.heappush(heap, num)
    while heap:
        largest = heapq.heappop(heap)
        print(largest)