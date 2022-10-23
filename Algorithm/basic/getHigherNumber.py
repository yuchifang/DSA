# 給一串數字 將兩個數字交換位置 找出如何交換會讓數字最大

# 用基本迴圈
'''
9876 = 9876
3578 = 8573
102030405060708090 = 902030405060708010
991199 = 999191
498712301 = 948712301 
988588011 = 988885011
98769 = 99768
997788 = 998787
'''

input1 = [int(item) for item in input()]
# input1Length = len(input1)
# maxIndex = -1
# maxValue = -1

# changeIndex = -1
# changeValue = -1

# maxChangeIndex = -1

# for index in range(input1Length-1, -1, -1):
#     if input1[index] > maxValue:
#         maxValue = input1[index]
#         maxIndex = index
#         continue
#     if maxValue > input1[index]:  # 找到 位數最大且比 max 還小的值
#         maxChangeIndex = maxIndex
#         changeIndex = index
#         changeValue = input1[index]

# if changeValue != -1:
#     input1[changeIndex], input1[maxChangeIndex] = input1[maxChangeIndex], changeValue,
# print("".join(str(item) for item in input1))

# 兩兩陣列比對
# 由大排到小
data = sorted(input1, reverse=True)
inputLength = len(input1)
maxValue = 0
maxIndex = -1

changeIndex = -1
for index in range(inputLength):
    if input1[index] < data[index]:
        maxValue = data[index]
        changeIndex = index
        break

for index in range(inputLength-1, -1, -1):
    if input1[index] == maxValue:
        maxIndex = index
        break

if maxIndex != -1:
    input1[maxIndex], input1[changeIndex] = input1[changeIndex], maxValue
print("".join([str(item) for item in input1]))
