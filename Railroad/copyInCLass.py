import sys, time, random
def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)
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
def sumdist(puzzle):
    count = 0
    index = 0
    for POS in puzzle:
        if POS != " ":
            count += abs(index // 4 - (ord(POS) - 65) // 4)
            count += abs(index % 4 - (ord(POS) - 65) % 4)
        index += 1
    return count
puzzle = sys.argv[1]
start = time.clock()
puzzle = puzzle[:puzzle.index("")]+" "+puzzle[puzzle.index("")+1:]
goal = "ABCDEFGHIJKLMNO_"
sumd = 0
num = 0
while time.clock()-start < 14:
    num+=1
    temp = sumdist(puzzle)
    sumd+=temp
    puzzle = random.choice(myOptions(puzzle))
print("Number of States: %s" % num) #726678 States
time = time.clock()-start
print("Time: %ss" % time) #14.00014 seconds
print("Puzzles per second: %s" % (num/time)) #51905.02 puzzles / second
print("Average Manhattan Distance: %s" % (sumd/num)) #37.56 steps