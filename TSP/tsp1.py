import sys
import math
import msvcrt
import itertools
from tkinter import Tk, Canvas
from pynput.keyboard import Key,Controller
class location():
    def __init__(self, latitude,longitude):
        self.lat = latitude
        self.lon = longitude

class swap():
    def __init__(self, st,en):
        self.s = st
        self.e = en

    def __eq__(self, other):
        return self.s == other.s and self.e == other.e

    def __str__(self):
        return str(self.s)+" "+str(self.e)
def printPath(hP,canv):
    for i in range(len(hP)):
        #print(hP)
        canv.create_line(converted[int(hP[i%len(hP)])][0], converted[int(hP[i%len(hP)])][1], converted[int(hP[(i + 1)%len(hP)])][0], converted[int(hP[(i + 1)%len(hP)])][1], fill="red",width=2)
    for pos in locationDict.keys():
        # print((str(locationDict[pos].lat)+" "+str(locationDict[pos].lon)))
        if len(locationDict.keys()) < 40:
            # print((str(locationDict[pos].lat)+" "+str(locationDict[pos].lon)))
            coorX = ((float((locationDict[pos].lon)) - minY) * (750)) - 500
            coorY = ((float((locationDict[pos].lat)) - minX) * (-400)) + 1070
        else:
            coorX = ((float((locationDict[pos].lon)) - minY) * (240)) - 20
            coorY = ((float((locationDict[pos].lat)) - minX) * (-150)) + 900

        canv.create_oval(float(coorX) + 3, float(coorY) + 3, float(coorX) - 3, float(coorY) - 3, fill="black")
        # totalDistance+=pairWiseDistances[i][i+1]
def findDistance(hPath):
    totalD =0
    for x in range(len(hPath)):
        # totalD+=pairWiseDistances[int(hPath[int(x%38)])][int(hPath[(x+1)%38])]
        totalD+=dbp(int(hPath[(x+1)%len(hPath)]),int(hPath[int(x%len(hPath))]))
    return totalD
def findDistanceU(hPath):
    totalD = 0
    for x in range(0,len(hPath)-1):
        # totalD+=pairWiseDistances[int(hPath[int(x%38)])][int(hPath[(x+1)%38])]
        totalD += dbp(int(hPath[(x + 1) % len(hPath)]), int(hPath[int(x % len(hPath))]))
    return totalD
def dbp(p1,p2):
    return pairWiseDistances[int(p1)][int(p2)]
def permsPath(currentPath):
    tempPath = currentPath
    length=7
    swaps =[]
    swapped=[]
    for x in range(0,len(tempPath)):
        #print(tempPath)
        #print(findDistance(tempPath))
        if (x+length)<len(tempPath):
            permSection = tempPath[x:(x+length)%len(tempPath)]

        else:

            permSection = tempPath[x:]+tempPath[:((x+length)%len(tempPath))]
            #print(permSection)
        possPermutations=list(itertools.permutations(permSection))
        #print(len(possPermutations))
        #print("past ehre")
        min=tempPath
        savedPerm=permSection
        
        for perm in possPermutations:
            endP = (x+length)%len(tempPath)
            tPath = [int(tempPath[(x-1)%len(tempPath)])]+list(perm)+[int(tempPath[endP])]

            if (x+length) < len(tempPath):
                minSection = min[x:(x+length)]
            else:
                minSection = min[x:]+min[:(x+length)%len(min)]
            minTing = [int(min[(x-1)%len(min)])]+minSection+[int(min[(x+length)%len(min)])]

            if findDistanceU(tPath)<findDistanceU(minTing):



                savedPerm = list(perm)
                if (x + length) < len(tempPath):
                    min=tempPath[:x]+list(perm)+tempPath[(x+length):]

                else:
                    min=list(perm)[:(x+length)%len(min)]+tempPath[(x+length)%len(min):x]+list(perm)[(x+length)%len(min):]

        minDist = findDistance(min)

        if minDist<findDistance(tempPath):
            #print("swipper")
            if (x + length) < len(tempPath):
                #print(tempPath)
                #print(savedPerm)
                swaps.append(swap(tempPath[x:(x + length)], list(savedPerm)))
                swapped.append(list(savedPerm))
                tempPath=min
            else:

                swaps.append(swap(tempPath[x:] + tempPath[:(x + length) % len(tempPath)], list(savedPerm)))
                swapped.append(list(savedPerm))
                tempPath = min
            #print(minDist)

        print(x)


    return tempPath, swaps




def recurFindPath(hp):
    thp = hp
    for i in range(3):
        for node in range(len(hp)):
            #print(len(thp))
            for node1 in range(len(hp)):

                if node1!=node and node1!=((node+1)%len(hp)) and node1!=((node-1)%len(hp)):
                    if (dbp(thp[node],thp[(node+1)%len(hp)])+dbp(thp[node1],thp[(node1+1)%len(hp)]))>(dbp(thp[node],thp[node1])+dbp(thp[(node+1)%len(hp)],thp[(node1+1)%len(hp)])):
                        if node<node1:
                            sliced = thp[(node+1):(node1+1)]
                            tempthp=thp[:((node+1))]+sliced[::-1]+thp[((node1+1)):]
                        else:

                            sliced = thp[(node1+1):(node+1)]
                            tempthp=thp[:(node1+1)]+sliced[::-1]+thp[(node+1):]
                            #print(len(tempthp))
                        thp=tempthp
    return thp

def greedyPath(cur,vis,size):
    node=cur[-1]
    #print(str(len(cur))+" "+str(size))
    #print(len(orderedDistances[node]))
    #print(orderedDistances[node])

    copyList = cur
    copySet = vis
    #print(copySet)
    i = 0
    while orderedDistances[node][i] in copySet:
        #print("went up")
        i+=1


    copySet.add(orderedDistances[node][i])
    copyList.append(orderedDistances[node][i])
    for x in range(734):
        if x not in copyList and len(copyList)==733:
            copyList.append(x)
            copySet.add(x)
            #print(len(copyList))
    if len(copyList)<size:
        greedyPath(copyList,copySet,size)
    return copyList

def getDataFromGreed():
    return (greedyPath([0], {0}, len(hamiltonianCycle)))
def calcDistance(x1, y1, x2, y2): #(lattitude, longitude)
    radius = 6371

    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)
    #print(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
    y1 *= math.pi / 180
    x1 *= math.pi / 180
    y2 *= math.pi / 180
    x2 *= math.pi / 180
    # print("x1 "+str(x1))
    # print("y1 " + str(y1))
    # print("x2 " + str(x2))
    # print("y2 " + str(y2))
    val = math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y2 - y1)
    val = float(int(val*1000000000000))/1000000000000
    return math.acos(val) * radius
    # print(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y2 - y1))
    # return math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y2 - y1)) * radius
def inputData():
    with open("locations1.txt") as f:
        data = [line.rstrip('\n') for line in f]
    #print(data)
    #print(data)
    locationDict = {}
    for x in range(1,len(data)):
        vals=data[x].split()
        lat=vals[1]
        lon=vals[0]

        #print(vals)
        #print(lat+" "+lon)
        locationDict[(x-1)]=location(float(lat)/1000,float(lon)/1000)
    return locationDict

locationDict=inputData()
#print(len(locationDict.keys()))
minX = 1000000000000
minY = 1000000000000

for name in locationDict.keys():
    if (float(locationDict[name].lon))<minY:
        minY = float(locationDict[name].lon)-1
    if (float(locationDict[name].lat))<minX:
        minX = float(locationDict[name].lat)-1

converted = []
pairWiseDistances = {}
orderedDistances = {}
for pos in locationDict.keys():
    if len(locationDict.keys())<40:
    #print((str(locationDict[pos].lat)+" "+str(locationDict[pos].lon)))
        coorX = ((float((locationDict[pos].lon)) - minY) * (750)) - 500
        coorY = ((float((locationDict[pos].lat)) - minX) * (-400)) + 1070
    else:
        coorX = ((float((locationDict[pos].lon)) - minY) * (240)) - 20
        coorY = ((float((locationDict[pos].lat)) - minX) * (-150)) +900
    # converted.append((coorX,coorY))
    # canvas.create_oval(float(coorX) + 3, float(coorY) + 3, float(coorX) - 3, float(coorY) - 3, fill="black")
    converted.append((coorX, coorY))
    dictDistances = {}

    for pos2 in locationDict.keys():
        dictDistances[pos2]=calcDistance(locationDict[pos].lat,locationDict[pos].lon,locationDict[pos2].lat,locationDict[pos2].lon)
    dic=sorted(dictDistances, key=dictDistances.get, reverse=False)
    #pairWiseDistances[pos]=dic
    pairWiseDistances[pos]=dictDistances
    orderedDistances[pos]=dic
#print(str(dbp(orderedDistances[0][0],0))+" "+str(dbp(orderedDistances[0][len(orderedDistances[0])-1],0)))
hamiltonianCycle = []
totalDistance = 0
for i in range(len(locationDict.keys())):
    # canvas.create_line(converted[i][0], converted[i][1], converted[i+1][0], converted[i+1][1], fill="red", width=2)
    #print(hamiltonianCycle)
    hamiltonianCycle.append(str(i))
    # totalDistance+=calcDistance(locationDict[i].lat,locationDict[i].lon,locationDict[i+1].lat,locationDict[i+1].lon)
    # totalDistance+=pairWiseDistances[i][i+1]
# canvas.create_line(converted[37][0], converted[37][1], converted[0][0], converted[0][1], fill="red", width=2)
# totalDistance+=calcDistance(locationDict[37].lat,locationDict[37].lon,locationDict[0].lat,locationDict[0].lon)
# totalDistance+=pairWiseDistances[37][0]
# hamiltonianCycle.append(str(37))
#print(hamiltonianCycle)
# printPath(hamiltonianCycle)
theTK = Tk()
canvas = Canvas(theTK, width=1250,height=800, background="white")
canvas.pack()

#print(greed)
#print(greed)
greed = getDataFromGreed()
#print(findDistance(greed))
# val = recurFindPath(hamiltonianCycle)
val = recurFindPath(greed)
#print(findDistance(val))
printPath(hamiltonianCycle,canvas)
theTK.bind("<KeyPress>", lambda e:theTK.destroy())
theTK.mainloop()
newTK = Tk()
canvas1 = Canvas(newTK, width=1250,height=800, background="white")
canvas1.pack()
printPath(val,canvas1)
newTK.bind("<KeyPress>", lambda e:newTK.destroy())
newTK.focus_force()
newTK.mainloop()
nTK = Tk()
#print(findDistance(val))

val1=permsPath(val)
val2=recurFindPath(val1[0])
canvas2 = Canvas(nTK, width=1250,height=800, background="white")
canvas2.pack()
printPath(val1[0],canvas2)
nTK.bind("<KeyPress>", lambda e:nTK.destroy())
nTK.focus_force()
nTK.mainloop()

# print(converted)
print("Tangled")
print(([int(x) for x in hamiltonianCycle]))
print(findDistance(hamiltonianCycle))
#
print("Untangled")
print([int(y) for y in val])
print(findDistance(val))
#
#
print("Untangled with Perms")
print([int(x) for x in val1[0]])

#print(findDistance(val1[0]))
print(findDistance(val2))
#greed2 = getDataFromGreed()
# print("swaps")
# #print(val1[1])
# #print(val1[1])
# #print(val1[2])
print("swaps")
for swapVal in val1[1]:
    print(str(swapVal.s)+""+str(swapVal.e))