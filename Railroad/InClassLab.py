import sys
import time
from random import randint
puzzle = "ABCDEFGHIJKLMNO_"
numberSwitches = sys.argv[1]
#numberSwitches = input("LOL: ")
def manhattan(str, goal):
    sum = 0
    for letter in str:
        if(letter!="_"):
            x = str.index(letter)
            y = goal.index(letter)
            rowDiff = abs(rowGoal(x) - rowGoal(y))
            colDiff = abs(colGoal(x) - colGoal(y))
            sum += (colDiff + rowDiff)

    #return sum + count
    return sum
def rowGoal(num):
    return int(num / 4)
def colGoal(num):
    return int(num % 4)
def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)
def manhattanPos(puzzle):
    count = 0
    index = 0
    for POS in puzzle:
        if POS!=" ":
            count+=abs(index//4-(ord(POS)-65)//4)
            count+=abs(index%4-(ord(POS)-65)%4)
        index+=1
    return count
def myOptions(str):
    nextSpace = [{1, 4}, {0, 2, 5}, {1, 3, 6}, {2, 7}, {0, 5, 8}, {1, 4, 6, 9}, {2, 5, 7, 10}, {3, 6, 11}, {4, 9, 12},
                 {5, 8, 10, 13}, {6, 9, 11, 14}, {7, 10, 15}, {8, 13}, {12, 9, 14}, {13, 10, 15}, {11, 14}]
    myArr = []
    if len(str) == 16:
        loc = str.find("_")
        list = nextSpace[loc]
        for i in range(len(list)):
            for pos in list:
                myArr.append(swap(str, pos, loc))

        return myArr
    else:
        print("Your input does not match the required length for this command.")
def randomN(n):
    totalMan = 0

    state = puzzle
    for x in range(int(n)):
        options = myOptions(state)
        random = randint(0,len(options)-1)
        temp = options[random]
        totalMan+=manhattan(temp,puzzle)
        state = temp
        """currentMan = 0
        options = myOptions(state)
        random = randint(0,len(options)-1)
        temp = options[random]
        currentMan=manhattanPos(temp)
        print(currentMan)
        print(temp)
        totalMan+=currentMan
        state = temp"""
    return totalMan
t0 = time.time()
total = randomN(numberSwitches)
t1 = time.time()
print("The number of puzzles is: " + str(numberSwitches)) #290000 puzzles
print("The Manhattan distance between each state is: " + str(total/int(numberSwitches))) #36.8 is the avg distance
print("Puzzles per second is " + str(float(numberSwitches)/(t1-t0))) #19969 puzzles per second
print("The time to run is " + str(t1-t0)) #14.5 seconds