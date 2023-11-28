def partition(arr, l, r):
    pivot = arr[l]
    pivot_i = l
    great, less = l+1, r
    
    while True:
        while great < r and arr[great] < pivot:
            great += 1

        while less >= 0 and arr[less] > pivot:
            less -= 1
        
        if great < less:
            arr[great], arr[less] = arr[less], arr[great]
        else:
            break

    arr[less], arr[pivot_i] = pivot, arr[less]
    return less



def quick_sort(arr, l, r):
    if r - l <= 0:
        return

    partition_p = partition(arr, l, r)
    quick_sort(arr, l, partition_p-1)
    quick_sort(arr, partition_p+1, r)



x = [7, 3, 4, 1, 8, 5, 99, 0, 4]
print(f'Unsorted list: {x}')
quick_sort(x, 0, len(x)-1)
print(f'Sorted list: {x}')
