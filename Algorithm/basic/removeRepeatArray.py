num1 = [1, 2, 2, 1]
newList = []

for item in num1:
    if not item in newList:
        newList.append(item)
print(newList)
