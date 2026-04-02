# 1. Find largest and smallest element in an array

def min_max_no(arr):
    if len(arr) == 0:
        return None

    min = arr[0]
    max = arr[0]

    for num in arr:
        if num < min:
             min = num
        if num > max:
             max = num
    return min, max


arr = [10,12,6,8,15]
print(min_max_no(arr))

