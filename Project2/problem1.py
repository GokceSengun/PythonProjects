import sys
g=sys.argv[1]
homew= open(g, "r")
data=homew.readlines()
for aline in data:
    ListString= aline.split(";");
ListIntegers = map(int ,ListString)


def averageFirstThreeDigit(number):
    varSum = 0
    numberLength = str(number).__len__()
    while (number != 0):
        if (numberLength <=3 and numberLength !=0):
            varSum+= int(number) % 10
        number //= 10
        numberLength -= 1
    return (varSum/3)

def changeResultToList(result):
    threeDigitlist= list()
    for x in result:
        threeDigitlist.append(averageFirstThreeDigit(x))
    return threeDigitlist

def reverseList(listParam):
    size = len(listParam)
    index = size-1
    tempList = list()
    for i in range(size, 0, -1):
        tempList.append(listParam[index])
        index -=1
    return tempList

def avgFirstThreeDigit(params):
    resultlist = changeResultToList(params)
    #print (resultlist)
    return  reverseList(resultlist)

output=avgFirstThreeDigit(ListIntegers)
print(output)
homew.close()

