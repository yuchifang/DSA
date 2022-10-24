# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 解法一
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)
        dict1 = {}
        dict2 = {}
        returnList = []
        for item in nums1:
            if item in dict1:
                dict1[item] += 1
            else:
                dict1[item] = 1

        for item in nums2:
            if item in dict2:
                dict2[item] += 1
            else:
                dict2[item] = 1

        for key2 in dict2:
            if key2 in dict1:
                if dict1[key2] > dict2[key2]:
                    for item in range(dict2[key2]):
                        returnList.append(key2)
                else:
                    for item in range(dict1[key2]):
                        returnList.append(key2)
        return returnList
# 解法二


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans
# 解法三


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans
