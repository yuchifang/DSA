input1=int(input())

# for fibonacciSeries
def forfibonacciSeries(input1):
    if input1 == 0:
        return 0
    if input1 ==1 or input1 ==2:
        return 1
    count1 = 1
    count2 = 1 
    count3 = 0
    for item in range(2,input1):
        count3 = count1 + count2
        count1 = count2
        count2 = count3
    return count3

# print(forfibonacciSeries(input1))

def fibonacciSeriesRecursive(input1):
    if input1 ==0:
        return 0
    if input1 ==1 and input1 ==1 :
        return 1

    return fibonacciSeriesRecursive(input1-1) +fibonacciSeriesRecursive(input1-2)

print(fibonacciSeriesRecursive(input1))