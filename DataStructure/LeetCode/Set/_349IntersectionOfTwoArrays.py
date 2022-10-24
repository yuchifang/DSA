'''
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

'''


def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
    returnArr = []
    for item in nums1:
        print("item1", item)
        print("x", nums1)
        print("y", nums2)
        if item in nums2:
            print("item2", item)
            returnArr.append(item)
            nums2.remove(item)
            nums1.remove(item)
    return returnArr


print(intersect("z", ["1", "2", "2", "1"], ["2", "2"]))
