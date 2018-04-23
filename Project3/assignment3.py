import sys
inFile=open(sys.argv[1],"r")
inFile2=open(sys.argv[2],"r")
inFile3=open(sys.argv[3],"r")
outFile=open("binarian_message.txt","w")
outFile2=open("computations.txt","w")
outFile3=open("message.txt","w")

dict={}
for line in inFile.readlines():
    line=line.rstrip("\n")
    input_items=line.split(' ');
    dict[input_items[0]]=input_items[1]
#print(dict["'baD"]) #sözlük yazar.
mydata=[]
def binarian_to_english(text):

    for word in text.readlines():
        word=word.rstrip('\n')
        #print(word)

        mylist=[]
        if not word.startswith("+"):
            if not word.startswith("#"):
                #print(word)
                aLine=word.split(' ');
                #print(aLine)
                for i in aLine:
                    if i in dict:
                        i=dict[i]
                        mylist.append(i)
                    #print(i)
                    else:
                        mylist.append(i)
                print(*mylist)
                print(*mylist, file=outFile)

        else:
            word=word.split(' ')
            #print(word)
            mydata.extend(word)
    #print(mydata)

numdict=[]
def binary_to_decimal():
    for x in mydata:
        if x.isdigit():
            numdict.append(x)
    #print(numdict)


def bin_to_deci(number):

    b = len(number)
    say = b
    last = 0
    for i in number:
        say = say -1
        son = float(i) * 2 **say
        last += son
    return last



dictreversed = {}
for k in dict:
    dictreversed[dict[k]] = k
#print(dictreversed)



def english_to_binarian(go):
    for let in go.readlines():
        let=let.rstrip('\n')
        #print(let)
        myMessage=[]
        letter=let.split(' ');
        #print(letter)

        for i in letter:
            i=i.replace(",","")
            i=i.replace(".","")

            if i in dictreversed:
                i=dictreversed[i]
                myMessage.append(i)

            elif i not in dictreversed:
                if i.lower() in dictreversed:
                    i=i.lower()
                    i=dictreversed[i]
                    myMessage.append(i)
                elif i.isdigit():
                    s=""
                    while int(i)>0 :
                        if int(i) %2 ==1 :
                            s="1"+s
                        else:
                            s="0"+s
                        i= int(i)//2
                    myMessage.append(s)


                else:

                    myMessage.append(i)

        print(*myMessage)
        print(*myMessage, file=outFile3)



english_to_binarian(inFile3)
binarian_to_english(inFile2)
binary_to_decimal()

print("Data about Binarian planet:")
print("Data about Binarian planet:", file=outFile2)
print("Distance from the Earth: %e" %(int(bin_to_deci(numdict[2])) * 9.4607e+12) +" km".format())
print("Distance from the Earth: %e" %(int(bin_to_deci(numdict[2])) * 9.4607e+12) +" km".format(),file=outFile2)
print("Planet temperature: "+ str(bin_to_deci(numdict[0]))+" degrees Celsius")
print("Planet temperature: "+ str(bin_to_deci(numdict[0]))+" degrees Celsius", file=outFile2)
print("Orbital speed "+ str(bin_to_deci(numdict[1]))+" km/s")
print("Orbital speed "+ str(bin_to_deci(numdict[1]))+" km/s", file=outFile2)

inFile.close()
inFile2.close()
inFile3.close()
outFile.close()
outFile2.close()
outFile3.close()
