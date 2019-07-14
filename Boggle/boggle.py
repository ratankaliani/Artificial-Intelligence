import sys,time, collections
start = time.time()
def safeMove(index,move,visited):
    if len(bgboard) == 16:
        #print("1")
        if index % 4 == 0 and move in [-1, -5, 3]:
            return False
        if index % 4 == 3 and move in [1, -3, 5]:
            return False
    if len(bgboard) == 25:
        if index % 5 == 0 and move in [-1, -6, 4]:
            return False
        if index % 5 == 4 and move in [1, -4, 6]:
            return False
    if len(bgboard) == 36:
        #print(3)
        if index % 6 == 0 and move in [-1, -7, 5]:
            return False
        if index % 6 == 5 and move in [1, -5, 7]:
            return False
    #print("should work"+str(index+move))
    #print(visited)
    if 0>(int(index+move)) or int(index+move)>15:
        #print(4)
        #print("unSafe")
        return False
    if int(index+move) in visited:
        return False
    return True
def findBoggleWords(board, position, visited, word):
    visited.add(position)
    #print(position)
    #print(board[position])

    if board[position]!='_':
        word+=board[position]
        # if len(board)==16:
        #     if len(word)>2 and word[0:3] not in firstLettersThree:
        #         return
        # else:
        #     if len(word)>3 and word[0:4] not in firstLettersFour:
        #         return

        # if word in scrabbleDict[word[0]]:
        #     boggleWords.add(word)
        #     print(word)
        if word in scrabbleSet:
            boggleWords.add(word)
        if (len(board) == 16):
            for move in fourways:
                if safeMove(position,move,visited):
                    if len(word)>2:
                        if word[0:3] in firstLettersThree:
                            findBoggleWords(board,position+move,visited,word)
                    else:
                        findBoggleWords(board, position + move, visited, word)
        if (len(board) == 25):
            for move in fiveways:
                if safeMove(position,move,visited):
                    if len(word)>3:
                        if word[0:4] in firstLettersFour:
                            findBoggleWords(board,position+move,visited,word)
                    else:
                        findBoggleWords(board, position + move, visited, word)
        if (len(board) == 36):
            for move in sixways:
                if safeMove(position,move,visited):
                    if len(word)>3:
                        if word[0:4] in firstLettersFour:
                            findBoggleWords(board,position+move,visited,word)
                else:
                    findBoggleWords(board, position + move, visited, word)
        word = word[:len(word)-1]
        visited.remove(position)
    else:
        for char in 'qwertyuiiopasdfghjklzxcvbnm':
            word.append(char)
            if word in scrabbleSet: boggleWords.add(word)
            if (len(board) == 16):
                for move in fourways:
                    if safeMove(position, move, visited):
                        findBoggleWords(board, position + move, visited, word)
            if (len(board) == 25):
                for move in fiveways:
                    if safeMove(position, move, visited):
                        findBoggleWords(board, position + move, visited, word)
            if (len(board) == 36):
                for move in sixways:
                    if safeMove(position, move, visited):
                        findBoggleWords(board, position + move, visited, word)
            word = word[:len(word) - 1]
            visited.remove(position)
def findWords(board):
    visited = set()
    word=""
    #print(board)
    for i in range(len(board)):
        #print("findWords"+str(i))
        findBoggleWords(board,i,visited,word)
bgboard=sys.argv[1].lower()
bgarray = []
i=0
while i<len(bgboard):
    if bgboard[i]=='2':
        bgarray.append(bgboard[i+1]+bgboard[i+2])
        i+=3
    elif bgboard[i]=='3':
        bgarray.append(bgboard[i+1:i+4])
        i+=4
    else:
        bgarray.append(bgboard[i])
        i+=1

#print(bgarray)
fourways = [-4,4,-1,1,-3,-5,3,5]
fiveways = [-5,5,-1,1,-4,-6,4,6]
sixways = [-6,6,-1,1,-5,-7,5,7]

with open("scrabble.txt") as f:
    data = [line.rstrip('\n') for line in f]
scrabbleSet = set()
scrabbleDict =collections.defaultdict(list)
firstLettersThree = set()
firstLettersFour = set()
for ind in data:
    updated = ind.lower()
    if len(bgarray)==16:
        if len(updated)>2:
            scrabbleSet.add(updated)
            scrabbleDict[updated[0].lower()].append(updated.strip("\n").lower())
            firstLettersThree.add(updated[0:3])
    else:
        if len(updated)>3:
            scrabbleSet.add(updated)
            scrabbleDict[updated[0].lower()].append(updated.strip("\n").lower())
            #firstLettersFour.add(updated[0:4])
#print(len(firstLettersThree))
#print(len(scrabbleSet))
#print(len(firstLettersFour))
sum = 0
#print(scrabbleDict.keys())
for i in scrabbleDict.keys():
    sum+=len(scrabbleDict[i])
#print(sum)
#print(len(scrabbleSet))
boggleWords = set()
findWords(bgarray)
print("Number of Words: "+str(len(boggleWords)))
print("Time "+str(time.time()-start))