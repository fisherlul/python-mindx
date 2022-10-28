from itertools import zip_longest


nums = [2,7,11,15]
class Solution:
    def twoSum(nums: list, target: int):
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                return [dictionary[nums[i]], i]
            else:
                dictionary[target - nums[i]] = i


print(Solution.twoSum(nums, 9))
