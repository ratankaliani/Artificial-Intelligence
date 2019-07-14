import sys
dodecaDict = {0:{1,2,3,4,5},1:{0,2,5,6,7},2:{0,1,3,7,8},3:{0,2,4,8,9},4:{0,3,5,9,10},5:{0,1,4,10,6},6:{11,7,10,1,5},7:{11,6,8,1,2},8:{11,7,9,2,3},9:{11,8,10,3,4},10:{11,9,6,4,5},11:{6,7,8,9,10}}
def bruteForce(num):
 # returns a solved pzl or the empty string on failure
 newSet = set()
 newSet.add(0)
 for i in range(6, 11):
     temp = set()
     val = False
     for j in newSet:
         if i in dodecaDict[j]:
             val = True
     if not val:
         temp.add(i)
     newSet = newSet | temp
     if len(newSet) == num:
         return newSet
 return []

input = sys.argv[1]
#input = input("Enter number: ")
bf = bruteForce(int(input))
if int(input)==1:
    print({0})
elif(bf)==[]:
    print("No Solution!")
else:
    print(bruteForce(int(input)))