import math,random
file = open("XOR.txt","w")
for x in range(10000):
    xval = random.uniform(0,1.5)
    yval = random.uniform(0,1.5)
    comb = (xval**2+yval**2)**(1/2)
    file.write(str(xval)+" "+str(yval)+" => "+str(comb))
    file.write("\n")