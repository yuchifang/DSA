# https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = list(words[0])
        for word in words[1::]:
            check = []
            for chr in word:
                if chr in ans:
                    check.append(chr)
                    ans.remove(chr)
            ans = check
        return ans




