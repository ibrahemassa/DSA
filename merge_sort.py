def merge_sort(arr):
    if len(arr) <= 1:
        return
    l, r = 0, len(arr)
    m = (l+r)//2
    # print(f'Splitting: {arr}')
    left, right = arr[l:m], arr[m:r]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)

def merge(left, right, arr):
    i, l, r =0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            # print(f'merging: {left[l]}')
            arr[i] = left[l]
            l += 1
            i += 1
        else:
            arr[i] = right[r]
            # print(f'merging: {right[r]}')
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


x = [356, 97, 846, 215]
merge_sort(x)
print(x)