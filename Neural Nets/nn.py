import sys,re,random
class nn:
    def __init__(self,layers):

def extractNNSpecs():
    args = sys.argv[1:]  # command line arguments
    if len(args) < 1 or re.compile("^\\d+$").search(args[-1]) is not None:
        args += [sys.argv[0] + "..\\..\\XOR.txt"]  # append the ...
    fileLoc = args[-1]  # training set location
    aTraining = open(fileLoc, "r").read().splitlines()  # make a list of the training set
    aInitial, aFinal = [], []  # We'll separate the input and output
    for idx in range(len(aTraining)):  # For each training set item
        strIn, strOut = aTraining[idx].split("=>")  # separate it into input and output
        #  print ("'{}' ==> '{}'".format(strIn, strOut))
        aInitial.append([float(mynum) for mynum in re.split("\\s+,?\\s*|\\s*,?\\s+", strIn.strip())] + [
            1.0])  # trailing element is bias
        aFinal.append([float(mynum) for mynum in re.split("\\s+,?\\s*|\\s*,?\\s+", strOut.strip())])
    # Fix the number of nodes per each layer
    aLayerCt = [len(aInitial[0])] + [int(n) for n in args[:-1]] + [len(aFinal[0])]

    return aInitial, aFinal, aLayerCt
def generateWeights():
    listWeights = []
    for x in range(9):
        listWeights.append(random.uniform(-1,1))
    return listWeights
def dotProd(l1,l2):
    if len(l1) != len(l2):
        return 0
    return sum(i[0] * i[1] for i in zip(l1, l2))
def printnn(weights, outputs, gradient, error, inputs, values):
    return
def forwardProp(nn,weights):


