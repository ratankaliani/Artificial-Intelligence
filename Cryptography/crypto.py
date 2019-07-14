import sys, re, collections,operator,math,time
start = time.time()
class dictWord():
    def __init__(self, word):
        if word in wordsData:
            self.freq = int(wordsData[word])
        else:
            self.freq=10000
        self.word = word

    def __lt__(self, other):
        return self.freq < other.freq

def translate(inputStr,translateSet):
    translatedList=[]
    for word in inputStr:
        newStr = ''
        if word=='i' or word=='a':
            newStr += word
        else:
            for letter in word:
                if letter in translateSet:
                    newStr += translateSet[letter]
                else:
                    newStr+=letter
        translatedList.append(newStr)
    return (' '.join(translatedList))
def hasher(word):
    seen = collections.defaultdict()
    current = 0
    finalWord = ""
    for c in word:
        if c not in seen:
            seen[c]=(str(current))
            current += 1
        finalWord+=(seen[c])
    return finalWord
def calcFreq(word):
    sum = 0
    for letter in word:
        sum+=wordFreq[letter]
    return sum/len(word)
def possibleCiphers(word):
    #print(hasher(word))
    #print(wordMapper[hasher(word)])
    return wordMapper[hasher(word)]

def solver(inputStr):
    #print(inputStr)
    bool=True
    for word in inputStr:
        if word not in scrabbleSet and len(word)>1:
            bool=False
    if bool:
        dictTrans={}
        for words in inputStr:
            for letter in words:
                dictTrans[letter]=letter
        return dictTrans
    else:
        finalTranslation = recur({},inputStr,0,max(3,len(inputStr)/3),0)
        return finalTranslation
def recur(currentTranslations, cryptList,properNouns,maxProperNouns,depth):
    #print("i have recurred")
    wordsLeft = cryptList
    if len(wordsLeft)==0:
        #print(currentTranslations)
        finalStr = translate(input,currentTranslations)
        for word in finalStr.split():
            if word not in scrabbleSet and len(word)>1:
                return
        return currentTranslations
    if properNouns>maxProperNouns:
        return
    currentWord = wordsLeft[0]

    if hasher(currentWord) in wordMapper.keys():
        possibleCipherList = possibleCiphers(wordsLeft[0])
        #print(possibleCipherList)
        for possCipher in possibleCipherList:
            cipherWord = possCipher.word
            # if cipherWord=='once':
            #     print(currentWord+cipherWord)
            newTranslations = dict(currentTranslations)
            alreadyTranslated = set(currentTranslations.keys())
            noBueno = True
            for i in range(len(cipherWord)):
                if len(newTranslations.values())!=len(set(newTranslations.values())):
                        #print("exec")
                        noBueno = False
                        break
                if cipherWord[i] not in newTranslations.values() and currentWord[i] in alreadyTranslated:
                    noBueno = False
                    break

                # print("did u reach here")
                newTranslations[currentWord[i]] = cipherWord[i]
            #print(newTranslations)
            # print("noBueno"+str(noBueno))
            # print(newTranslations)
            #print(wordsLeft)
            if not noBueno:
                continue
            #print(newTranslations)
            if depth%10==0:
                print(translate(input,newTranslations))
            finalSolutions = recur(newTranslations, wordsLeft[1:], properNouns, maxProperNouns,depth+1)

            # print("did u reach here?")
            # print(finalSolutions)
            if finalSolutions:

                # print(finalSolutions)
                return finalSolutions
            # print("didudothis")
            # print(wordsLeft[1:])

        return None
    else:
        #print("whyd u skip")
        skipProperNoun = recur(currentTranslations, wordsLeft[1:], properNouns + 1, maxProperNouns,depth+1)
        if skipProperNoun:
            return skipProperNoun
        return
    #print(possibleCipherList)
    #print("second recurrance")
    #print(currentWord)




wordFreq = {'a':8.12,
            "b":1.49,
            "c":2.71,
            "d":4.32,
            "e":12.02,
            "f":2.3,
            "g":2.03,
            "h":5.92,
            "i":7.31,
            "j":0.1,
            "k":0.69,
            'l':3.98,
            'm':2.61,
            'n':6.95,
            'o':7.68,
            'p':1.82,
            'q':0.11,
            'r':6.02,
            's':6.28,
            't':9.1,
            'u':2.88,
            'v':1.11,
            'w':2.09,
            'x':0.17,
            'y':2.11,
            'z':0.07}

input = sys.argv[1:]
for block in range(len(input)):
    input[block]=input[block].lower()
with open("wordss.txt") as f:
    wordsD = [line.rstrip('\n') for line in f]
wordsData = {}
for wLine in wordsD:
    wList = wLine.split()
    wordsData[wList[0]]=wList[1]

with open("scrabble.txt") as f:
    data = [line.rstrip('\n') for line in f]
scrabbleSet = set()
wordMapper = collections.defaultdict(list)
for l in data:
    word = l.lower()
    scrabbleSet.add(word)
    wordMapper[hasher(word)].append(dictWord(word))
#print(wordMapper["0123"])
# listStr = wordMapper["0123"]
# listStr.sort(key=operator.attrgetter('freq'))
# print(listStr)
for key in wordMapper.keys():
    #print(wordMapper[key])
    wordMapper[key].sort(key=operator.attrgetter('freq'))
    wordMapper[key].reverse()
#print("0123"+wordMapper["0123"])
cryptTranslations = solver(input)
#print(cryptTranslations)
#print(cryptTranslations)
#print("time: "+str(time.time()-start))
print(translate(input,cryptTranslations))
