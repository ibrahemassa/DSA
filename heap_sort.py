from list_heap import Heap

def heap_sort(heap:Heap, arr:list[int]) -> list[int]:
    for i in arr:
        heap.insert(i)

    sorted_arr = []
    for i in range(heap.size):
        sorted_arr.append(heap.pop())

    return sorted_arr

#----------Testing----------#
import random
heap = Heap()
x = [random.randint(0, 100) for _ in range(10)]
print(f'Unsorted: {x}')
x = heap_sort(heap, x)
print(f'Sorted: {x}')
