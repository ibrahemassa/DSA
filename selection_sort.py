def selection_sort(arr):
    for i in range(len(arr)):
        min_num, min_index = arr[i], i

        for j in range(i+1, len(arr)):
            if arr[j] < min_num:
                min_num, min_index = arr[j], j

        arr[i], arr[min_index] = min_num, arr[i]


x = [7, 3, 4, 1, 8, 5, 99, 0, 4]
print(f'Unsorted list: {x}')
selection_sort(x)
print(f'Sorted list: {x}')
