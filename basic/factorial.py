input1=int(input())
# for
def forfactorial(input1):
    if input1 ==0:
        return input1
    answer = 1
    for item in range(1,input1+1):            
        answer*=item
    return answer
# print(forfactorial(input1))


# recursive
def recursivefactorial(input1):
    if input1 == 0:
        return 0
    if input1-1 ==0:
        return 1
    return input1*recursivefactorial(input1-1)
print(recursivefactorial(input1))

