class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictD = {}
        indexCount = 0
        for item in nums:
            if item in dictD:
                return [dictD[item], indexCount]
            else:
                dictD[target-item] = indexCount
            indexCount += 1
