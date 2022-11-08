input1 = [int(item) for item in input().split()]
input2 = [int(item) for item in input().split()]
returnList =[]

index1 = 0
index2 = 0

while len(input1)!= 0 or len(input2)!= 0:
    if len(input1) == 0:
        returnList.extend(input2)
        break
    if len(input2) == 0:
        returnList.extend(input1)
        break

    if input2[index2]>input1[index1]:
        returnList.append(input1.pop(0))
    elif input2[index2]<input1[index1]:
        returnList.append(input2.pop(0))
    if len(input1) == 0:
        returnList.extend(input2)
        break
    if len(input2) == 0:
        returnList.extend(input1)
        break

print(" ".join(str(item) for item in returnList))