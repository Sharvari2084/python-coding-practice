# 7. Find Missing Number (1 to n)

def find_missing(arr,n):
    actual_sum = sum(arr)
    total_sum = n * (n+1)//2
    return total_sum - actual_sum

arr = [1,2,3,5]  # missing 4
n = 5

print("Missing number:",find_missing(arr,n))
    
