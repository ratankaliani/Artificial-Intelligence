import sys,time, collections
with open("scrabble.txt") as f:
    data = [line.rstrip('\n') for line in f]
with open("common4") as f1:
    data1 = [line1.rstrip('\n') for line1 in f1]
    data2 = set()
    for xy in data1:
        solo = xy.split(" ")
        for word in solo:
            data2.add(word)
# print(len(data2))

bruh = set(data)
matrixL = ["" for y in range(4)]
matrixL[0] = "TWDLFBSPHM"
matrixL[1] = "AILEYHNRUO"
matrixL[2] = "TAOSKENMLR"
matrixL[3] = "KTEDSNMPYL"
possPhrases = set()
#recursive

def recur(arr, num, str):

    for char in arr[num]:
        tempstr = str[:]
        tempstr+=char
        if len(tempstr)==len(arr):
            if tempstr.lower() in data2:
                possPhrases.add(tempstr.lower())
                # print(1)
        else:
            recur(arr,num+1,tempstr)
recur(matrixL,0,"")
possP = list(possPhrases)
possP.sort()
print(len(possP))
for w in possP:
    print(w)




