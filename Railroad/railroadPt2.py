import sys, time
import time
import math
from tkinter import Tk, Canvas
from heapq import heappush, heappop

def calcDistance(x1, y1, x2, y2): #(lattitude, longitude)
    lat1, lon1, lat2, lon2 = x1, y1, x2, y2
    radius = 3958.755866

    angle1 = float(lat1) * (math.pi / 180)
    angle2 = float(lat2) * (math.pi / 180)
    theta = (float(lat2) - float(lat1)) * (math.pi / 180)
    zeta = (float(lon2) - float(lon1)) * (math.pi / 180)
    a = math.sin(theta / 2) * math.sin(theta / 2) + math.cos(angle1) * math.cos(angle2) * math.sin(zeta / 2) * math.sin(zeta / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c

def findpath(dictionary, end, start, distance):
    parent = dictionary[end]
    array = []
    array.append(end)
    array.append(parent)
    while parent != start:
        parent = dictionary[parent]
        array.append(parent)
    length = len(array)-1
    array = array[::-1]
    print("Distance Traveled: " + str(distance) + " miles")
    #print("The number of cities: " + str(length))
    return(array)

def a_star_search(city1,city2,canvas, minY, minX):
    startX = nodes[city1][1]
    startY = nodes[city1][0]
    x1End = nodes[city2][1]
    y1End = nodes[city2][0]
    update = 0
    openS = []
    closedS = {}
    heappush(openS, (calcDistance(startX, startY,x1End,y1End),city1,0,None))
    while(len(openS) != 0):
        tup = heappop(openS)
        name = tup[1]
        d = tup[2]
        aList = dictEdges[name]
        if(name == city2):
            closedS[name] = tup[3]
            shortPath = findpath(closedS,city2, city1, tup[0])
            break
        for each in aList:
            y1 = nodes[name][0]
            x1 = nodes[name][1]
            y2 = nodes[each][0]
            x2 = nodes[each][1]
            coorY = ((float((y2)) - minY)*(-15))+750
            coorX = ((float((x2)) - minX)*(15))+250
            coorY1 = ((float((y1)) - minY)*(-15))+750
            coorX1 = ((float((x1)) - minX)*(15))+250
            if each in closedS:
                continue
            aNewD = d + calcDistance(y1,x1,y2,x2)
            someD = calcDistance(y2,x2,y1End,x1End)

            heappush(openS, (someD+aNewD,each, aNewD, name))
            #heappush(openS, (someD, each, someD+aNewD, name))
            canvas.create_oval(float(coorX)+3, float(coorY)+3, float(coorX)-3, float(coorY)-3, fill="red")
            closedS[name] = tup[3]
            canvas.create_oval(float(coorX1)+2, float(coorY1)+2, float(coorX1)-2, float(coorY1)-2, fill="green")
            if(update%30000 == 0):
                canvas.update()
            update+=1

    for x in range(0, len(shortPath)-2):
        coorX1 = ((float((nodes[shortPath[x]][0])) - minY)*(-15))+750
        coorY1 = ((float((nodes[shortPath[x]][1])) - minX)*(15))+250
        coorX2 = ((float((nodes[shortPath[x+1]][0])) - minY)*(-15))+750
        coorY2 = ((float((nodes[shortPath[x+1]][1])) - minX)*(15))+250
        canvas.create_line(coorY1, coorX1, coorY2, coorX2, fill="blue", width=2)
        if(update % 20 == 0):
            canvas.update()
        update+=1

startTime = time.clock()
cityOne = sys.argv[1]
cityTwo = sys.argv[2]
nodes = {}
rN = open("usnodes.txt", "r").readlines()
for x in range(21782):
    line = rN[x]
    coorList = line.split(" ")
    nodes[coorList[0]] = (float(coorList[1]),float(coorList[2]))
rE = open("usedges.txt", "r").readlines()
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

names = {}
CityNames = open("usfullnames.txt", "r").readlines()
count = 0
theCityNames = CityNames
for line in theCityNames:
    indvNames = line.split()
    if(len(indvNames) == 3):
        name = indvNames[1] + "_" +indvNames[2]
        names[name] = indvNames[0]
        count +=1
    else:
        names[indvNames[1]] = indvNames[0]



theTK = Tk()
canvas = Canvas(theTK, width=1500,height=1500, background="white")
canvas.pack()

smallestX = 10000000
smallestY = 10000000
scaled = {}
for name in nodes:
    if (float(nodes[name][0]))<smallestY:
        smallestY = float(nodes[name][0])-1
    if (float(nodes[name][1]))<smallestX:
        smallestX = float(nodes[name][1])-1
coorX = 0
coorY = 0
for name in nodes:
    coorY = (((float(nodes[name][0])) - smallestY)*(-15))+750
    coorX = (((float(nodes[name][1])) - smallestX)*(15))+250
    scaled[name] = (coorY, coorX)

for name in nodes:
    allNeighbors = dictEdges[name]
    for neighbor in allNeighbors:
        canvas.create_line(scaled[name][1], scaled[name][0], scaled[neighbor][1], scaled[neighbor][0], fill="black", width=1)
a_star_search(names[cityOne],names[cityTwo],canvas, smallestY, smallestX)
print(str(time.clock()) + "s")
theTK.mainloop()



