# https://judge.ccclub.io/problem/201403

menuCost = {}
menuItem = {}
input1 = int(input())
for item in range(input1):
    data = input().split()
    menuCost[data[0]] = int(data[1])
    if len(data) < 3:
        continue
    menuItem[data[0]] = data[2::]


totalWantItem = []


def handleCost(wantItem: str):
    data = []
    if wantItem in menuItem:
        data = [handleCost(data) for data in menuItem[wantItem]]
    return menuCost[wantItem] + sum(data)


input2 = int(input())
for item in range(input2):
    data = input()
    newCount = handleCost(data)
    print(newCount)