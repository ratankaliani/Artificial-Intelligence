#Railroad Lab Part One
#Assignment: Get files from Railroad Section for Romania
#Whatever edges are given, build a graph using that information
#Display that graph in some manner

import time
from math import acos, sin, cos, pi
import sys
import tkinter as graphicsPack

class Vertex:
	def __init__(self, name):
		self.name = name
		self.edges = []
		self.x = 0
		self.y = 0
		self.xAdjust = 0
		self.yAdjust = 0

def calcd(y1,x1, y2,x2):
   y  = float(y1)
   x  = float(x1)
   yTwo  = float(y2)
   xTwo  = float(x2)

   R   = 3958.76 # miles = 6371 km

   y = y * pi/180.0
   x = x * pi/180.0
   yTwo = yTwo * pi/180.0
   xTwo = xTwo *  pi/180.0
   # approximate great circle distance with law of cosines
   return acos( sin(y)*sin(yTwo) + cos(y)*cos(yTwo)*cos(xTwo-x) ) * R

def graph():
	#vertices and names
	translate = open("fullnames.txt", "r")
	graph = {}
	for line in translate:
		graph[line[0]] = Vertex(line)
	#latitude longitude
	position = open("nodes.txt", "r")
	for line in position:
		temp = line.split(" ")
		ver = graph[line[0]]
		ver.x = float(temp[1])
		ver.y = float(temp[2])
	#edges
	edges = open("edges.txt", "r")
	for edge in edges:
		ind1 = edge[0]
		ind2 = edge[2]
		v1 = graph[ind1]
		v2 = graph[ind2]
		v1.edges.append(v2)
		v2.edges.append(v1)
	return graph

if __name__ == '__main__':
	start = time.time()
	Graph = graph()
	image = graphicsPack.Tk()
	canvas = graphicsPack.Canvas(width = 1500, height = 800)
	for item in Graph.keys():
		#6371 km is 3959 miles
		i = Graph[item]
		i.yAdjust = 7650 - (i.x * 160)
		i.xAdjust = (i.y * 170) - 3550
		y2 = i.yAdjust + 20
		x2 = i.xAdjust + 20
		#x0, y0, x1, y1
		#canvas.create_oval(i.xAdjust, i.yAdjust, x2, y2, outline = "black", fill = "orange")
		Graph[item] = i

	edgesum = 0.0
	for item in Graph.keys():
		i = Graph[item]
		for edge in i.edges:
			v = Graph[edge.name[0]]
			canvas.create_line(i.xAdjust + 10, i.yAdjust + 10, v.xAdjust + 10, v.yAdjust + 10, fill = "hot pink")
			edgesum += float("%.3f"%(calcd(v.x, v.y, i.x, i.y)))
		#canvas.create_text(i.xAdjust + 10, i.yAdjust + 10, text = i.name[0])
	canvas.pack()
	edgesum /= 2

	print("Run Time: " + "%.4f"%(time.time() - start) + " seconds")
	print("Total Distance of Railroad Tracks: " + str(edgesum) + " miles")
	image.mainloop()
