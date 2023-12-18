def interpolation_search(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = left + (right - left)*(target - arr[left]) // (arr[right] - arr[left])

        if mid > right or mid < left:
            return -1

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(interpolation_search(x, 4))
