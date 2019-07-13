import sys, time
import time
import math
from heapq import heappush, heappop
from tkinter import Tk, Canvas

def calcDistance(x1, y1, x2, y2): #(lattitude, longitude)
    radius = 3958.755866

    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)
    print(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
    y1 *= math.pi / 180
    x1 *= math.pi / 180
    y2 *= math.pi / 180
    x2 *= math.pi / 180

    return math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y2 - y1)) * radius

def findpath(dictionary, end, start, distance):
    parent = dictionary.get(end)
    array = []
    array.append(end)
    array.append(parent)
    while parent != start:
        parent = dictionary.get(parent)
        array.append(parent)
    length = len(array)-1
    array = array[::-1]
    print("Distance Traveled: " + str(distance) + " miles")

    #print("The number of cities: " + str(length))
    return(array)

def a_star_search(city1,city2,canvas, minY, minX):
    startX = dictNodes.get(city1)[0]
    startY = dictNodes.get(city1)[1]
    x1End = dictNodes.get(city2)[0]
    y1End = dictNodes.get(city2)[1]
    update = 0
    openS = []
    closedS = {}
    heappush(openS, (calcDistance(startX, startY,x1End,y1End),city1,0,None))
    while(len(openS) != 0):
        tup = heappop(openS)
        name = tup[1]
        d = tup[2]
        aList = dictEdges.get(name)
        if(name == city2):
            closedS[name] = tup[3]
            shortPath = findpath(closedS,city2, city1, tup[0])
            break
        for each in aList:
            y1 = dictNodes.get(name)[0]
            x1 = dictNodes.get(name)[1]
            y2 = dictNodes.get(each)[0]
            x2 = dictNodes.get(each)[1]
            coorY = ((float((y2)) - minY)*(-15))+750
            coorX = ((float((x2)) - minX)*(15))+250
            coorY1 = ((float((y1)) - minY)*(-15))+750
            coorX1 = ((float((x1)) - minX)*(15))+250
            aNewD = d + calcDistance(y1,x1,y2,x2)
            someD = calcDistance(y2,x2,y1End,x1End)
            if each in closedS:
                continue
            heappush(openS, (someD+aNewD,each, aNewD, name))

            canvas.create_oval(float(coorX)+2, float(coorY)+2, float(coorX)-2, float(coorY)-2, fill="red")
            closedS[name] = tup[3]
            canvas.create_oval(float(coorX1)+2, float(coorY1)+2, float(coorX1)-2, float(coorY1)-2, fill="green")
            if(update%1000 == 0):
                canvas.update()
            update+=1

    for x in range(0, len(shortPath)-2):
        coorX1 = ((float((dictNodes.get(shortPath[x])[0])) - minY)*(-15))+750
        coorY1 = ((float((dictNodes.get(shortPath[x])[1])) - minX)*(15))+250
        coorX2 = ((float((dictNodes.get(shortPath[x+1])[0])) - minY)*(-15))+750
        coorY2 = ((float((dictNodes.get(shortPath[x+1])[1])) - minX)*(15))+250
        canvas.create_line(coorY1, coorX1, coorY2, coorX2, fill="blue", width=2)
        if(update % 20 == 0):
            canvas.update()
        update+=1

startTime = time.clock()
romNodes = "usnodes.txt"
dictNodes = {}
rN = open(romNodes, "r").readlines()
for x in range(21782):
    line = rN[x]
    coorList = line.split(" ")
    # G.add_node(str(coorList[0]))
    dictNodes[coorList[0]] = (float(coorList[1]),float(coorList[2]))
romEdges = "usedges.txt"
rE = open(romEdges, "r").readlines()
dictEdges = {}
for line in rE:
    name1 = line.split()
    edge1 = (name1[0])
    edge2 = (name1[1])
    if edge1 not in dictEdges:
        dictEdges[edge1] = [edge2]
    else:
        dictEdges[edge1].append(edge2)
    if edge2 not in dictEdges:
        dictEdges[edge2] = [edge1]
    else:
        dictEdges[edge2].append(edge1)

#------------------This is to make the dictionary for the actual city names--------------------#

namesLookup = {}
rrNodeCity = "usfullnames.txt"
CityNames = open(rrNodeCity, "r").readlines()
count = 0
theCityNames = CityNames
for line in theCityNames:
    indvNames = line.split()
    if(len(indvNames) == 3):
        name = indvNames[1] + "_" +indvNames[2]
        namesLookup[name] = indvNames[0]
        count +=1
    else:
        namesLookup[indvNames[1]] = indvNames[0]
cityOne = sys.argv[1]
cityTwo = sys.argv[2]
totald = 0
for item in dictNodes.keys():
    i = dictNodes[item]
    for edge in dictEdges[item]:
        v = dictNodes[edge]
        y1 = i[0]
        x1 = i[1]
        y2 = v[0]
        x2 = v[1]
        totald += calcDistance(x1, y1, x2, y2)
print("Total Miles of Railroad: "+str(totald))
theTK = Tk()
canvas = Canvas(theTK, width=1500,height=1500, background="white")
canvas.pack()

smallestX = 1000000000000
smallestY = 1000000000000
scaled = {}
for name in dictNodes:
    if (float(dictNodes[name][0]))<smallestY:
        smallestY = float(dictNodes[name][0])-1
    if (float(dictNodes[name][1]))<smallestX:
        smallestX = float(dictNodes[name][1])-1
coorX = 0
coorY = 0
for name in dictNodes:
    coorY = (((float(dictNodes[name][0])) - smallestY)*(-15))+750
    coorX = (((float(dictNodes[name][1])) - smallestX)*(15))+250
    scaled[name] = (coorY, coorX)

for name in dictNodes:
    allNeighbors = dictEdges[name]
    for neighbor in allNeighbors:
        canvas.create_line(scaled[name][1], scaled[name][0], scaled[neighbor][1], scaled[neighbor][0], fill="black", width=1)
a_star_search(namesLookup.get(cityOne),namesLookup.get(cityTwo),canvas, smallestY, smallestX)
print(str(time.clock()) + "s")
theTK.mainloop()



