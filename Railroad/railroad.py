import sys
import time
import math
from tkinter import Tk, Canvas
top = Tk()
railroaddisplay = Canvas(top,width=1500,height=1500,background="white")
class Node:
	def __init__(self, label):
		self.label = label
		self.edges = []
		self.x = 0
		self.y = 0
		self.xAdjust = 0
		self.yAdjust = 0
def distanced(x1, x2, y1, y2):
	lat1, lon1, lat2, lon2 = x1, y1, x2, y2
	radius = 3958.755866

	angle1 = float(lat1) * (math.pi / 180)
	angle2 = float(lat2) * (math.pi / 180)
	theta = (float(lat2) - float(lat1)) * (math.pi / 180)
	zeta = (float(lon2) - float(lon1)) * (math.pi / 180)
	a = math.sin(theta / 2) * math.sin(theta / 2) + math.cos(angle1) * math.cos(angle2) * math.sin(zeta / 2) * math.sin(zeta / 2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	return radius * c
def xycoordinates(node):
	lat = nodes[node][0]
	lon = nodes[node][1]
#arg = sys.argv[1]
#print(arg)
t0 = time.time()
nodes = {}
with open("fullnames.txt", "r") as fff:
	for line in fff:
		nodes[line[0]] = Node(line)
with open("nodes.txt", "r") as f:
	for line in f:
		nodes[line[0]].x= line[2:9]
		nodes[line[0]].y= line[10:17]
with open("edges.txt", "r") as ff:
	for line in ff:
		nodes[line[0]].edges.append(nodes[line[2]])
		nodes[line[2]].edges.append(nodes[line[0]])
totald = 0.0
for item in nodes.keys():
	i = nodes[item]
	i.yAdjust = 7650 - (float(i.x) * 160)
	i.xAdjust = (float(i.y) * 170) - 3550
	y2 = i.yAdjust + 20
	x2 = i.xAdjust + 20

	railroaddisplay.create_oval(i.xAdjust, i.yAdjust, x2, y2,  fill = "blue")



	for edge in i.edges:
		v = nodes[edge.label[0]]
		if(v.xAdjust>0):
			railroaddisplay.create_line(i.xAdjust + 10, i.yAdjust + 10, v.xAdjust + 10, v.yAdjust + 10, fill = "red")
			totald+=distanced(i.x,v.x,i.y,v.y)
		railroaddisplay.create_text(i.xAdjust + 10, i.yAdjust, text = i.label)
	railroaddisplay.pack()
"""sum = 0
for x in range(len(edges)):
	distance = distanced(x)
	sum+=distance"""

t1 = time.time()
print("Total Time: " + str(t1 - t0))
print("Total Distance: " + str(totald) + " Miles")
top.mainloop()
