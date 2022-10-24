# https://leetcode.com/problems/valid-parentheses/

'''
"{[]}"
True
"()[]{}"
True
'''

class Solution:
    def isValid(self, s: str) -> bool:
        for item in range(0,len(s),2):
            if s[item] == "(" and s[item+1]!= ")":
                return False
                
            if s[item] == "[" and s[item+1]!= "]":
                return False
                    
            if s[item] == "{" and s[item+1]!= "}":
                return False
                
        return True
        