# 12.Merge 2 Sorted Arrays
def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
    return nums1

nums1 = [1, 2, 3]
m = 3
nums2 = [4, 6, 8]
n = 3

result = merge(nums1, m, nums2, n)
print(result)
