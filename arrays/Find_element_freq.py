# 6. Find frequency of elements
def find_freq(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq

arr = [1,1,2,2,3,4,4,4,5]
result = find_freq(arr)
print("Frequencies:")
for key, value in result.items():
    print(key, "->", value)
