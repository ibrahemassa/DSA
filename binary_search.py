def b_search(nums, target, l=None, r=None):
    if l is None:
        l, r= 0, len(nums) - 1
    m = (l+r)//2
    if l <= r:
        if nums[m] >  target:
            return b_search(nums, target, l=l, r=m-1)
        elif nums[m] < target:
            return b_search(nums, target, l=m+1, r=r)
        elif nums[m] == target:
            return m
    return -1

x = [n for n in range(1, 10000000)]
print(b_search(x, 700648))