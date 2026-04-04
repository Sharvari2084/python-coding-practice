# 5. Find duplicate elements
def duplicates(arr):
    seen = set()
    duplicates = set ()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

arr = [1,2,3,4,5,4,3,6,2]
result = duplicates(arr)
print("Duplicate elements:",result)
    
