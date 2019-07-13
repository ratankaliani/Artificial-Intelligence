import sys
import math,random

import itertools
import time
from tkinter import Tk, Canvas
def rgbToHex(val):
    # if '#%02x%02x%02x' % (int(val*255), int(val*255), 0)=="#10010000":
    #     print(val)
    val1=val
    if val1>1:
        val1=1
    return '#%02x%02x%02x' % (int(val1*255), int(val1*255), 0)
newTK = Tk()
canvas1 = Canvas(newTK, width=700,height=700, background="black")
canvas1.pack()
arrValues=[]
flyPoints = []
start=time.time()
for x in range(100):
    coorX = random.uniform(10,690)
    coorY = random.uniform(10,690)
    #canvas1.create_oval(float(coorX) + 3, float(coorY) + 3, float(coorX) - 3, float(coorY) - 3, fill="#4c4c00")
    # canvas1.create_oval(float(coorX) + 3, float(coorY) + 3, float(coorX) - 3, float(coorY) - 3, fill=)
    arrValues.append([coorX,coorY])
    flyPoints.append(random.uniform(0,1))
    for point in range(len(arrValues)):

        canvas1.create_oval(float(arrValues[point][0]) + 3, float(arrValues[point][1]) + 3,
                            float(arrValues[point][0]) - 3, float(arrValues[point][1]) - 3,
                            fill="#4c4c00")
newTK.update()
#time.sleep(1)

# time.sleep(1)
# for y in range(100):
#     canvas1.create_oval(float(arrValues[y][0]) + 3, float(arrValues[y][1]) + 3, float(arrValues[y][0]) - 3, float(arrValues[y][1]) - 3, fill="#FFFF00")
    #arrValues.append([coorX,coorY,random.uniform(0,1)])
# canvas1.update()
# newTK.bind("<KeyPress>", lambda e:newTK.destroy())
# newTK.focus_force()
# threshold = 1
# flyCount=100
# bumpAmt=0.1
# deltat=0.1
# tau=1

def recur(deltat,tau,bumpAmt,threshold,yeet):
    #print(max(flyPoints))
    temp=0
    for poi in range(len(arrValues)):

        flyPotential=flyPoints[poi]
        flyPotential+=(deltat*(1-flyPotential))/tau
        flyPoints[poi]=flyPotential

        if flyPotential>threshold:

            for p1 in range(len(arrValues)):
                flyPoints[p1]+=bumpAmt
        count=0
        #canvas1.delete(all)
        for point in range(len(arrValues)):

            if flyPoints[point]>threshold:
                temp=1
                canvas1.create_oval(float(arrValues[point][0]) + 3, float(arrValues[point][1]) + 3,
                                    float(arrValues[point][0]) - 3, float(arrValues[point][1]) - 3,
                                    fill="yellow")
                canvas1.update()
                flyPoints[point]=0
                count+=1


        if temp == 1:
            #canvas1.update()
            print("exec")
            #time.sleep(.1)
            #print("going back")
            for p1 in range(len(arrValues)):

                canvas1.create_oval(float(arrValues[point][0]) + 3, float(arrValues[point][1]) + 3,
                                    float(arrValues[point][0]) - 3, float(arrValues[point][1]) - 3,
                                    fill="#4c4c00")
                print("turned back")
            canvas1.update()
        temp=0
        # if poi%yeet==0:
        #     canvas1.update()
        # if yeet%15==0:
        #     canvas1.update()
            #                             float(arrValues[point1][0]) - 3, float(arrValues[point1][1]) - 3, fill="#4c4c00")
        #     if flyPoints[point]>threshold:
        #         temp=1
        #
        #
        #         canvas1.create_oval(float(arrValues[point][0]) + 3, float(arrValues[point][1]) + 3,
        #                             float(arrValues[point][0]) - 3, float(arrValues[point][1]) - 3, fill="yellow")
        #
        #         count+=1
        #         flyPoints[point]=0
        # if temp==1:
        #     canvas1.update()
        #     time.sleep(.15)
        #     for point1 in range(len(arrValues)):
        #         temp = 0
        #         canvas1.create_oval(float(arrValues[point1][0]) + 3, float(arrValues[point1][1]) + 3,
        #                             float(arrValues[point1][0]) - 3, float(arrValues[point1][1]) - 3, fill="#4c4c00")
        #
        #
        #
        #     canvas1.update()
        #print(count)
        canvas1.delete()
        if count>0:
            print(count)
        if count==100:
            #newTK.update()
            print("Time: " + str(time.time()-start))
            #return 0
        #newTK.update()

tempT=1
val=0
while val!=1:
    print("max: "+str(tempT))
    val = recur(0.001,1,0.1,0.999,tempT)
    tempT+=1
newTK.mainloop()