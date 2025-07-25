def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1 
    mid = (left + right) // 2
    if arr[mid] == target: 
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:                  
        return binary_search_recursive(arr, target, left, mid - 1)
sorted_strings = ["apple", "apricot", "cherry", "berry", "fig", "grape"]
target_string = "cherry"
result = binary_search_recursive(sorted_strings, target_string)
print(result)
