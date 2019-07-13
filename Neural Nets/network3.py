import numpy as np
import sys,re
def extractNNSpecs():
    args = sys.argv[1:]  # command line arguments
    if len(args) < 1 or re.compile("^\\d+$").search(args[-1]) is not None:
        args += [sys.argv[0] + "..\\..\\XOR.txt"]  # append the ...
    fileLoc = args[-1]  # training set location
    aTraining = open(fileLoc, "r").read().splitlines()  # make a list of the training set
    aInitial, aFinal = [], []  # We'll separate the input and output
    for idx in range(len(aTraining)):  # For each training set item
        strIn, strOut = aTraining[idx].split("=>")  # separate it into input and output
        aInitial.append([float(mynum) for mynum in re.split("\\s+,?\\s*|\\s*,?\\s+", strIn.strip())] + [
            1.0])
        aFinal.append([float(mynum) for mynum in re.split("\\s+,?\\s*|\\s*,?\\s+", strOut.strip())])
    aLayerCt = [len(aInitial[0])] + [int(n) for n in args[:-1]] + [len(aFinal[0])]

    return aInitial, aFinal, aLayerCt
def makeNPArr():
    specs = extractNNSpecs()
    xorInputOutput = {}
    inputs = []
    outputs = []
    for x in range(len(specs[0])):
        #xorInputOutput[(specs[0][x][0], specs[0][x][1], specs[0][x][2])] = specs[1][x][0]
        inputs.append([specs[0][x][0], specs[0][x][1],specs[0][x][2]])
        outputs.append([specs[1][x][0]])
    #print(inputs)
    #print(outputs)
    return inputs,outputs
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))

i,o = makeNPArr()
#print(i)
#print(o)
X = np.array(i)

y = np.array(o)

np.random.seed(1)


syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for j in range(1000000):


    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    #print(l2)

    #print(syn1.T)
    #print(l1)
    #print(l2)
    l2_error = y - l2
    #print(y)
    #print(l2)
    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))
        #print(syn0)
        #print(l1[1][2])
        #print(l1)

    l2_delta = l2_error * nonlin(l2, deriv=True)


    l1_error = l2_delta.dot(syn1.T)


    l1_delta = l1_error * nonlin(l1, deriv=True)
    #print(syn0.T)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
    #print(l2_delta)
    #print(l1_delta)
    #print(l1.T)
    #print(l0.T)
