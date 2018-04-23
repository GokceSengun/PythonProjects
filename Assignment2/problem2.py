import sys
g=sys.argv[1]
homew= open(g, "r")
data=homew.readlines()
print("The total cost of each house :")
bulletList=[]
for line in data:
    aLine= line.split(" ")
    bulletList.append(aLine)
ResultList=[]
def calculateTotalCost(x):
    for i in x:
        total_cost=float(i[0])+(float(i[0])*(float(i[2])*10)+(float(i[1])*10))
        ResultList.append(total_cost)

    return ResultList




def displayCosts(x):
    displayList=calculateTotalCost(x)
    y=0
    a=0
    for i in displayList:
        a+=1
        print(str(a)+" house's total cost is "+str(ResultList[y]))
        y=y+1
    return displayList
#print(displayCosts())

def selectBestBuy(homeCostList):
    mini = ResultList[0]
    x = 1
    for i in ResultList[0:]:

            if i < mini:
                mini = i
                print(str("You should select ")+str(x)+str(". house whose total cost is ")+str(mini)+".")
            else:
                x +=1

    return (mini)




    #print ("house's total cost is " +str(homeCostList))

displayCosts(bulletList)
selectBestBuy(ResultList)

homew.close()
