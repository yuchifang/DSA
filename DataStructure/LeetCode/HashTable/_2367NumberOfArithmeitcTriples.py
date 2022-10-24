# https://leetcode.com/problems/number-of-arithmetic-triplets/
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        totalCount = 0
        for item in nums:
            if item + diff in nums and item + diff*2 in nums:
                totalCount += 1
        return totalCount
