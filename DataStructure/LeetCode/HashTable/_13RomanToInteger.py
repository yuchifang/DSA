# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        totalCount = 0
        dictNumeral = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # todo 解法 一
        # dictSpecialNumeral = {
        #     "IV": 4,
        #     "IX": 9,
        #     "XL": 40,
        #     "XC": 90,
        #     "CD": 400,
        #     "CM": 900
        # }

        # for specialNumber in dictSpecialNumeral:
        #     if specialNumber in s:
        #         s = s.replace(specialNumber, "")
        #         totalCount += dictSpecialNumeral[specialNumber]

        # for item in s:
        #     newNumber = dictNumeral[item]
        #     totalCount += newNumber
        # return totalCount
        # 解法 二
        sLength = len(s)
        for index in range(sLength):
            if index == sLength -1 or dictNumeral[s[index]]>=dictNumeral[s[index+1]]:
                totalCount+=dictNumeral[s[index]]
            else:
                totalCount-=dictNumeral[s[index]]
        return totalCount

