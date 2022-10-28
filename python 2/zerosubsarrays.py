nums = [1,3,0,0,2,0,0,4]
class Solution:
    def zeroFilledSubarray(nums: list[int]) -> int:
        ans = 0
        count = 0
        for num in nums:
            if num != 0:
                count = 0
            else:
                count += 1
            ans += count
        return ans

print(Solution.zeroFilledSubarray(nums))