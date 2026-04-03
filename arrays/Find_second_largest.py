def second_largest(arr):
    if len(arr) < 2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == float('-inf'):
        return None
    return second
arr = [ 10,20,5,25,30]
result = second_largest(arr)

if result is not None:
    print("Second largest element:", result)
else:
    print("No second largest element found")