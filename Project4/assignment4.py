import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
first=sys.argv[1]
second=sys.argv[2]
def retrieveData(fileName, nomineesNames) :
    data = csv.reader(open(fileName))
    dataList = list(data)
    print(dataList)
    global states
    states=[]
    for i in dataList:
        states.append(i[0])
    states=states[1:]
    #print(states)
    global voteObama
    voteObama=[]
    for i in dataList:
        voteObama.append(i[3])
    voteObama=voteObama[-1]
    global voteRomney
    voteRomney=[]
    for i in dataList:
        voteRomney.append(i[4])
    voteRomney=voteRomney[-1]


    votesList = []
    for nomineeName in nomineesNames:
        countDataList = len(dataList[0])
        for i in range(countDataList):
            if (dataList[0][i] == nomineeName ) :
                for j in range(1, len(dataList)):
                    votesList.append(dataList[j][i])
    txtFile = open('retrievedData.txt', 'w')
    for item in votesList:
        txtFile.write("%s\n" % item)
    return votesList
    #print(votesList)
retrieveData(first,second)


def SumVotes(fileName, nomineesNames) :
    data = csv.reader(open(fileName))
    global dataList
    dataList = list(data)
    global votesList
    votesList = []

    for nomineeName in nomineesNames:
        sumOfVotes = 0
        countDataList = len(dataList[0])
        for i in range(countDataList):
            if (dataList[0][i] == nomineeName ) :
                for j in range(1, len(dataList)):
                   # print(dataList[j][i])
                    sumOfVotes += int(dataList[j][i])
                    #print(j)
                    #print(len(dataList))
                    if (j==(len(dataList)-1)) :
                        votesList.append(sumOfVotes)

    return votesList
    #print(votesList)
SumVotes(first,second)


#def compareVoteonBar():

votesList=votesList[0:len(votesList)-1]
percentages=[]
totalvote=sum(votesList)
for i in votesList:
    a=100*float(i)/float(totalvote)
    a="%.3f" %a
    percentages.append(a)
    percentages.sort(reverse=True)



objects =[float(percentages[0]),float(percentages[1]),float(percentages[2]),float(percentages[3])]
y_pos = np.arange(len(objects))
performance = percentages
mycolor='rbym'
plt.bar(y_pos,[float(x) for x in performance], align='center',color=mycolor, alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Nominees')
plt.ylabel('Vote percentages')
plt.savefig('CompVotePercs.pdf')
plt.close()

def DispBarPlot():

    varx = [i for i in states]
    votesObama =[i for i in voteObama]
    votesRomney =[i for i in voteRomney]

    x_pos1= [x-0.1 for x in range(len(varx))]
    x_pos2= [x for x in range(len(varx))]

    print(x_pos1)
    print(x_pos2)

    plt.bar(x_pos1,votesObama,width=0.1,align='center',color='b')
    plt.bar(x_pos2,votesRomney,width=0.1,align='center',color='r')
    plt.xticks(x_pos1,varx)
    plt.ylabel('Vote counts')
    plt.xlabel('States')
    plt.title('Comparative Demonstration')

plt.savefig("ComparativeVotes.pdf")

DispBarPlot()

numlist=[]
global aciklik
aciklik=[]
aciklikson=[]
def obtainHistogram(x):
    for s in range(10):
        top=0
        for i in x:

            if len(str(i))==1:
                i=int("%.2d" %i)
                a=i%10
                i=i//10

                if a==s:
                    top+=1
                if a!=s:
                    b=i%10
                    if b==s:
                        top+=1

            if len(str(i))!=1:
                c=i%10
                i=i//10
                if c==s:
                    top+=1
                if c!=s:
                    d=i%10
                    if d==s:
                        top+=1
            #print(top)
        aciklik.append(top/(len(x)*2))

    return aciklik

obtainHistogram([7, 24, 25, 180, 249, 326, 446, 446, 512, 552, 612, 618, 618, 714, 780, 839, 846, 890, 949, 951])

def calculateMSE(x,y):
    diffirence=[]
    list1=x
    list2=y
    for i in range(len(x)):
        g=(int(x[i])-int(y[i]))**2
        diffirence.append(g)
    b=sum(diffirence)
    return b

calculateMSE([4, 7, 2, 3], [5, 2, 9, 6])



def plotHistogram():
    t = np.arange(10)
    s =[10,50,70,40,6,3,5,78,62,30]
    plt.plot(t, s)

    plt.xlabel('Digits')
    plt.ylabel('Distribution')
    plt.title('Histogram of least sign,digits')
    plt.grid(True)
    plt.savefig("Histogram.pdf")
    plt.show()

plotHistogram()


plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.savefig('HistogramSample1.pdf')
plt.show()
plt.close()

plt.plot([5,6,7,8])
plt.ylabel('some numbers')
plt.savefig('HistogramSample2.pdf')
plt.show()
plt.close()

plt.plot([1,27,3])
plt.ylabel('some numbers')
plt.savefig('HistogramSample3.pdf')
plt.show()
plt.close()

plt.plot([5,6,7,3,7])
plt.ylabel('some numbers')
plt.savefig('HistogramSample4.pdf')
plt.show()
plt.close()

plt.plot([5,6,7])
plt.ylabel('some numbers')
plt.savefig('HistogramSample5.pdf')
plt.show()
plt.close()

txtFile = open('myAnswer.txt', 'w')
txtFile.write('x')


