# https://judge.ccclub.io/problem/180041
# input
# input 表示 有幾個 左括弧 有幾個括號
# 找出符合的

input1 = int(input())

printStr = ""
count = 0
# 合法括號窮舉


def isValid(count, input1, printStr, left, right):

    if count == input1:
        print(printStr)
        return

    if left > right:
        printStr += ")"
        count += 1
        isValid(count, input1, printStr, left, right+1)

    if left < input1//2:
        printStr += "("
        count += 1
        isValid(count, input1, printStr, left+1, right)


isValid(count, input1*2, printStr, 0, 0)
