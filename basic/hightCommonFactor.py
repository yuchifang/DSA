# 210 % 45 = 30
# 45 % 30 = 15
# 30 % 15 = 2

input1 = [int(item) for item in input().split()]

def isValid(m,n):
    if n == 0:
        return m
    return isValid(n,m%n)


print(isValid(input1[0],input1[1]))
