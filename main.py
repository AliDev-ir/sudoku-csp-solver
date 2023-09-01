import datetime
import time
import math
def split(word):        #spliting every word into letters
    return [char for char in word]

def income(entery,hlist,vlist,block):       #setting horizentali, verticali and block lists
    temp = []
    temp1 = []
    for q in range(9):
        for j in range(9):
            temp1.append(entery[(j+ (q) * 9)])  # setting horizental list
        hlist.append(temp1)
        temp1 = []
    for y in range(9):
        for i in range(9):
            p = hlist[i]
            temp.append(p[y])
            p = []
        vlist.append(temp)  # setting vertical list
        temp = []

    temp1 = []
    for i in range(9):
        for j in range(3):
            if i > 1:
                temp1 = hlist[j + 3]
            else:
                temp1 = hlist[j]
            for x in range(3):
                if i % 3 != 0:
                    temp.append(temp1[x + 3])
                else:
                    temp.append(temp1[x])
        block.append(temp)  # setting blocks list
        temp = []
        temp1 = []

def C(hlist,vlist,block,X,D,entery): #setting Cnostrations list
    for i in range(9):
        temph = list(map(int, hlist[i]))    #converting hlist to int and using as temph
        for j in range(9):
            tempv = list(map(int, vlist[j]))    ##converting vlist to int and using as tempv
            if entery[i*9+j] == "0":
                X.append(list(set(D).difference(temph).difference(tempv)))      #finding costrations and placing it in every variable
                if X[-1] == [0]:
                    X.pop(-1)
                    X.append([])
            else:
                X.append([])

def duplicates(hlist, vlist, block):  # check if placing goes Wrong and there's duplicates in 3 lists.
    for i in range(len(hlist)):
        for j in range(len(hlist[i])):
            try:
                hlist[i].remove("0")
            except:
                continue
    for i in range(len(vlist)):
        for j in range(len(vlist[i])):
            try:
                vlist[i].remove("0")
            except:
                continue
    for i in range(len(block)):
        for j in range(len(block[i])):
            try:
                block[i].remove("0")
            except:
                continue

    for i in range(len(hlist)):
        if len(hlist[i]) != len(set(hlist[i])):
            return True

    for i in range(len(vlist)):
        if len(vlist[i]) != len(set(vlist[i])):
            return True

    for i in range(len(block)):
        if len(block[i]) != len(set(block[i])):
            return True

    return False

D = [0,1,2,3,4,5,6,7,8,9]       #Domin
X = []      #Constrations
hlist = []      #horizental list
vlist = []      #vertical list
block = []      #blocks
entery = []     #input

for x in range(9):      #getting input in lines and connecting them together.
    entery.append(split(input("")))
entery = [*entery[0],*entery[1],*entery[2],*entery[3],*entery[4],*entery[5],*entery[6],*entery[7],*entery[8]]
#some examples for copy
# 530070000 600195000 098000060 800060003 400803001 700020006 060000280 000419005 000080079
# 000000000 030000160 067035004 608120900 090080030 002079806 800690350 026000090 000000000

path = [ [] for i in range(81) ] #making a list and putting [] state in every value. [[],[],[],...]
income(entery,hlist,vlist,block)
C(hlist,vlist,block,X,D,entery)

for i in range(len(X)):     #single element X's are now done.
    if len(X[i]) == 1:
        entery[i] = str(X[i][0])
        X[i] = []

print("python is processing, pleas wait...")
x = -1
while x < 80:       #the main part of program.
    x += 1
    if entery[x] == "0":
        for i in range(len(X[x])):
            if str(X[x][i]) not in str(path[x]):      # if it wasnt in path then it will insert it.
                entery[x] = str(X[x][i])
                path[x].append(str(X[x][i]))

                hlist = []
                vlist = []
                block = []
                income(entery, hlist, vlist, block)

                if duplicates(hlist,vlist,block) == True: #this one checks if the numbers goes wrong it should goes back
                    entery[x] = "0"
                    x -= 1
                    break
                elif "0" not in entery:       #if there is no more 0; then its done.
                    hlist = []
                    vlist = []
                    block = []
                    income(entery, hlist, vlist, block)
                    for i in range(9):
                        for j in range(9):
                            print(f"{hlist[i][j]} ",end="")
                        print("")
                    exit(0)
                    break #has to not be there
                else:
                    break

            elif len(path[x]) >= len(X[x]):     #if non of possible number could fit in their place then go back to last fited number.
                path[x] = []
                for i in range(x-1,-1,-1):
                    if len(X[i]) > 1:
                        x = i
                        break
                entery[x] = "0"
                x -= 1
                break



