def max_in_sliding_window(arr, window_size):
    if not arr or window_size <= 0 or window_size > len(arr):
        return []
    max_values = []
    for i in range(len(arr) - window_size + 1):
        current_window = arr[i:i + window_size]
        max_values.append(max(current_window))
    return max_values
max_in_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
