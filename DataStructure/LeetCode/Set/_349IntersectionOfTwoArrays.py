# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        noRepeatOne = set(nums1)
        noRepeatSecond = set(nums2)
        answerList = []
        for item in noRepeatSecond:
            if item in noRepeatOne:
                answerList.append(item)
        return answerList



