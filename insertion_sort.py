def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


x = [7, 3, 4, 1, 8, 5, 99, 0, 4]
print(f'Unsorted list: {x}')
insertion_sort(x)
print(f'Sorted list: {x}')