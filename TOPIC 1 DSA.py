def find_max(arr):
    largest = arr[0]
    
    for arr in arr:
        if arr > largest:
            largest = arr
            
    return largest

numbers = [15, 8, 42, 19, 3]
print(find_max(numbers))