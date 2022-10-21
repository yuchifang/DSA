'''
9876 = 9876
3578 = 8573
102030405060708090 = 902030405060708010
991199 = 999191
498712301 = 948712301 
988588011 = 988885011
98769 = 99768
997788 = 998787

498712301
'''
input1 = [int(item) for item in input()]
input1Length = len(input1)
maxIndex = -1
maxValue = -1

for index in range(input1Length-1,-1,-1):
    if input1[index] > maxValue:
        maxValue = input1[index]
        maxIndex = index

    if maxValue > input1[index]: # 找到 位數最大且比 max 還小的值
        pass
    # print(index)
