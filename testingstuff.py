# class Solution:
#     def merge(nums1: list, m: int, nums2: list, n: int):
#         i = m-1

#         j = m+n-1

#         k = n-1

#         while i>= 0 and k>= 0:

#             if nums1[i] < nums2[k]:

#                 nums1[j] = nums2[k]

#                 k -= 1

#                 j -= 1

#             elif nums1[i] >= nums2[k]:

#                 nums1[j] = nums1[i]

#                 nums1[i] = nums2[k]

#                 i -= 1

#                 j -= 1

#         if k>=0:

#             nums1[:j+1] = nums2[:k+1]
        
#         return nums1


# class Solution:
#     from math import pow
#     def reverse(x: int) -> int:
#         x = [str(i) for i in str(x)]
#         x.sort(reverse=True)
#         if x[-1] == "0":
#             x.pop(-1)
#         if x[-1] == "-":
#             x.insert(0, "-")
#             x.pop(-1)
#         x = "".join(x)
#         return int(x)


# def valid_palindrome(s):
#     new_string = ''.join(char for char in s if char.isalnum())
#     new_string = new_string.lower()
#     if new_string == new_string[::-1]:
#         return True
#     else:
#         return False

s = "hello world 5 x 5"
import re
class Solution:
    def areNumbersAscending(s: str) -> bool:
        m = re.findall(r'\d+', s)
        for i in range(len(m)):
            m[i] = int(m[i])
        for i in range(len(m)-1):
            if m[i] >= m[i+1]:
                return False
        return True

print(Solution.areNumbersAscending(s))