'''
給一個都是數字的 Array, 再給一個數字, 
回傳陣列裡面任兩個數字相加等於其數字分別的 index
'''

# https://leetcode.com/problems/two-sum/


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


'''
要的是 相減等於其數字 並輸出 index
邏輯 相減 輸出 index
相減 A-B = C
可以用 hashTable 處理這部分
'''
