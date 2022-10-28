nums = [-1, -4, -2, 5, 3, 1]

nums.sort()
result = []
for i in range(len(nums)-2): 
    if i>0 and nums[i-1] == nums[i]:
        continue
    j = i + 1
    k = len(nums) - 1
    while j < k:
        Sum = nums[i] + nums[j] + nums[k]
        if Sum < 0:
            j += 1
        elif Sum > 0:
            k -= 1
        else:
            result.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1
    
print(result)
    