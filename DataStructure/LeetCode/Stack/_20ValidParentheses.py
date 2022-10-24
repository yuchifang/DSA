# https://leetcode.com/problems/valid-parentheses/

'''
"{[]}"
True
"()[]{}"
True
"){"
False
'''

class Solution:
    def isValid(self, s: str) -> bool:
        listStack = []
        newList=[*s]
        if len(newList) % 2 !=0: return False
        for item in newList:
            if len(listStack) == 0:
               listStack.append(item)
               continue
            if item ==")" and listStack[-1] == "(":
                listStack.pop()
                continue

            if item =="]"and listStack[-1] == "[":
                listStack.pop()
                continue

            if item =="}"and listStack[-1] == "{":
                listStack.pop()
                continue

            listStack.append(item)
        return len(listStack) ==0
