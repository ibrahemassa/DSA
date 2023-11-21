def merge_sort(arr):
    if len(arr) <= 1:
        return
    m = len(arr)//2
    left, right = arr[:m], arr[m:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)


def merge(left, right, arr):
    i = l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1
            i += 1
        else:
            arr[i] = right[r]
            r += 1
            i += 1
    while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1
    while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1


x = [356, 97, 846, 215, 213, 301]
merge_sort(x)
print(x)