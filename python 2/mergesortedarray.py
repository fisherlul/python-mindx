class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = m + n- 1
        k = n - 1
        count = 0

        if m > 0:
            while j > -1:
                count += 1
                if i == j and k < 0:
                    nums1[i] == nums2[k]
                    break
                if i < 0:
                    i = 0
                if nums1[i] > nums2[k]:
                    temp = nums1[j]
                    nums1[j] = nums1[i]
                    nums1[i] = temp
                    i -= 1
                    j -= 1
                elif nums1[i] <= nums2[k]:
                    nums1[j] = nums2[k]
                    k -= 1
                    j -= 1
            
        return nums1, count

a = Solution()
b, c = a.merge([4, 5, 6, 0, 0, 0], 3, [2, 2, 4], 3)