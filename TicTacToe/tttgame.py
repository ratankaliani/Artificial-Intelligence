import sys,time,msvcrt
if len(sys.argv)==1:
    token = "O"
    board = "........."
elif len(sys.argv)==2:
    token = sys.argv[1]
    board = "........."
elif len(sys.argv)==3:
    board = sys.argv[1]
    token = sys.argv[2]

constraintSets = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
def checkWinner(game):
    tmpConstraints = [[], [], [], [], [], [], [], []]
    for y in range(8):
        for z in constraintSets[y]:
            tmpConstraints[y].append(game[z])
    for z in tmpConstraints:
        if "." not in z:
            if "O" not in z:
                if token == 'O':
                    return -1
                else:
                    return 1
            elif "X" not in z:
                if token == 'X':
                    return -1
                else:
                    return 1
    if "." not in game:
        return 0
    else:
        return ""
def winnerPrint(game):
    output = checkWinner(game)
    if output != "":
        if output == 1:
            print("You Win!")
        elif output == -1:
            print("You Lose!")
        else:
            print("It's a Tie!")
        return 1
    return 0
def whoseMove(game):
    return 'X' if len("".join(game).split("."))%2==0 else 'O'
def freePositons(game):
    return {x for x in range(9) if game[x] == "."}
def partitionMoves(game):
    #print("".join([game[x]+"\n" if x%3==2 else game[x] for x in range(9)]))

    tmpConstraints = [[],[],[],[],[],[],[],[]]
    for y in range(8):
        for z in constraintSets[y]:
            tmpConstraints[y].append(game[z])
    player = whoseMove(game)
    for c in tmpConstraints:
        if "." not in c:
            if "X" not in c:
                if(player=="X"): return {},{""},{}
                else: return {""},{},{}
            elif "O" not in c:
                if(player=="O"): return {}, {""}, {}
                else: return {""},{},{}
    if "." not in game:
        return {},{},{""}
    good,bad,tie = set(),set(),set()
    #print(freePositons(game))
    for x in freePositons(game):
        char = whoseMove(game)
        newGame = list(game)
        newGame[x] = char
        tmpGood,tmpBad,tmpTie = partitionMoves("".join(newGame))
        if tmpGood: bad.add(x)
        elif tmpTie: tie.add(x)
        else: good.add(x)
    return good,bad,tie
if token == "X":
    oppToken = 'O'
else:
    oppToken = 'X'
print("\n".join([board[i:i+3] for i in range(0,9,3)])+"\n")
while "." in board:
    if whoseMove(board) == token:
        print("Move? ")
        index = int(msvcrt.getch())
        # index = int(input("Move? "))
        while index > len(board) or index < 0 or board[index]!=".":
            print(("Invalid Move!"))
            index = int(msvcrt.getch())
            # index = input("Invalid Move! Pick an index that is unfilled: ")
        newB = list(board)
        newB[index] = token
        board = "".join(newB)
    else:
        good,bad,tie = partitionMoves(board)
        if len(good) > 0:
            index = good.pop()
        elif len(tie) > 0:
            index = tie.pop()
        else:
            index = bad.pop()
        newB = list(board)
        newB[index] = oppToken
        board = "".join(newB)
    print("\n".join([board[i:i + 3] for i in range(0, 9, 3)]) + "\n")
    if winnerPrint(board) == 1:
        exit()
winnerPrint(board)

