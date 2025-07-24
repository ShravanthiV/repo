def next_greater_element(nums):
    result = [-1] * len(nums)  
    stack = []  
    
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            result[index] = num  
        stack.append(i) 
    return result
arr = [4, 5, 2, 25]
print(next_greater_element(arr))
