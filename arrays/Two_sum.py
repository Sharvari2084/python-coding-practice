def two_sum(arr,target):
    hashmap = {}

    for i in range (len(arr)):
        num = target - arr[i]
        if num in hashmap:
            return [hashmap[num],i]

        hashmap[arr[i]] = i
    return []

arr = [2, 7, 11, 15]
target = 9

print("Indices:", two_sum(arr, target))
            
            
