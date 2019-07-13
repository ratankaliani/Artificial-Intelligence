# import sys, random, math,re
# cellList = []
# backCellList = []
# weightedList = []
# gradientList  = []
# def extractNNSpecs():
#     args = sys.argv[1:]               # command line arguments
#     if len(args)<1 or re.compile("^\\d+$").search(args[-1]) is not None:
#         args += [sys.argv[0] + "..\\..\\XOR.txt"]   # append the ...
#     fileLoc = args[-1]                # training set location
#     aTraining = open(fileLoc, "r").read().splitlines()  # make a list of the training set
#     aInitial, aFinal = [], []         # We'll separate the input and output
#     for idx in range(len(aTraining)): # For each training set item
#         strIn, strOut = aTraining[idx].split("=>")  # separate it into input and output
#     #  print ("'{}' ==> '{}'".format(strIn, strOut))
#         aInitial.append([float(mynum) for mynum in re.split("\\s+,?\\s*|\\s*,?\\s+", strIn.strip())] + [1.0])   # trailing element is bias
#         aFinal.append([float(mynum) for mynum in re.split("\\s+,?\\s*|\\s*,?\\s+", strOut.strip())])
#     # Fix the number of nodes per each layer
#     aLayerCt = [len(aInitial[0])] + [int(n) for n in args[:-1]] + [len(aFinal[0])]
#     return aInitial, aFinal, aLayerCt
#
# def generateWeights():
#     weights = set()
#     for i in range(9):
#         weights.add(random.uniform(-1,1))
#     return weights
# def dotProd(l1,l2):
#     if len(l1) != len(l1):
#         return 0
#     return sum(i[0] * i[1] for i in zip(l1, l2))
# #Create a neural network for XOR. Find the weights of the network, the output that the
# #network gives, and the error for the output.

import sys, random, math, re


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


# tanh is better apparently


import math, sys, re, random, math


def sigmoid(x):
    calculated = 1 / (1 + math.exp((-1 * x)))
    return calculated

def dotProd(l1,l2):
    if len(l1) != len(l2):
        return 0
    return sum(i[0] * i[1] for i in zip(l1, l2))
def calculateErrorXor(xorInputOutput, weights):
    errorSquared = 0
    actualOutputs = {}
    for tupleinput in xorInputOutput:
        dotList = [tupleinput[0],tupleinput[1],tupleinput[2]]
        #bias = 1
        FirstRaw = [weights[0],weights[1],weights[2]]
        SecondRaw =[weights[3],weights[4],weights[5]]
        # FirstRaw = weights[:500]
        # SecondRaw = weights[500:1000]
        hiddenFirstRaw = dotProd(FirstRaw,dotList)
        hiddenSecondRaw = dotProd(SecondRaw,dotList)
        #print(hiddenFirstRaw)
        #print(hiddenSecondRaw)
       # hiddenFirstRaw = (first * weights[0] + second * weights[2] + bias * weights[4])
        #hiddenSecondRaw = (first * weights[1] + second * weights[3] + bias * weights[5])
        hiddenFirstCalculated = sigmoid(hiddenFirstRaw)
        hiddenSecondCalculated = sigmoid(hiddenSecondRaw)
        outputRaw = (hiddenFirstCalculated * weights[6] + hiddenSecondCalculated * weights[7])
        outputCalculated = sigmoid(outputRaw)
        finalOutput = outputCalculated * weights[8]
        expectedOut = xorInputOutput[tupleinput]
        errorSquared += (expectedOut - finalOutput) ** 2
        actualOutputs[(tupleinput[0],tupleinput[1])] = finalOutput
    return (errorSquared, actualOutputs)

#print(extractNNSpecs())
specs = extractNNSpecs()
xorInputOutput = {}
for x in range(len(specs[0])):
    xorInputOutput[(specs[0][x][0],specs[0][x][1],specs[0][x][2])] = specs[1][x][0]
#print(xorInputOutput)
#print(xorInputOutput)
# xorInputOutput = {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 0}
weights = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# weights = [0 for x in range(1003)]

def Error():
    temp = 1
    bestWeights = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    bestActualOutputs = {}
    bestError = 999999999
    count = 0
    while temp != 0:
        for index in range(len(weights)):
            weights[index] = random.uniform(-100, 100)
        error, outputs = calculateErrorXor(xorInputOutput, weights)
        #print(outputs)
        if error < bestError:
            #print(bestError)
            bestError = error
            bestWeights = weights
            bestActualOutputs = outputs
            # print("Error: " + str(bestError))
            # print("Inputs: " + str(xorInputOutput))
            # print("Outputs: " + str(bestActualOutputs))
            # print("Weights: " + str(bestWeights))
            right,wrong = 0,0
            for x in bestActualOutputs.keys():
                keything = (x[0],x[1],1.0)
                # print(x)
                # print(xorInputOutput.keys())
                out1=bestActualOutputs[x]
                out2 = xorInputOutput[keything]

                if (out1>1 and out2>1) or (1>out1>0 and 1>out2>0):
                    right+=1
                else:
                    wrong+=1
            if(0<int(right/10)<1000):
                print("Number Wrong: " + str(str(int(right/10))))
                return 1
            print("")
        # if count==1000000:
        #     print("Error: " + str(bestError))
        #     print("Outputs: " + str(bestActualOutputs))
        #     print("Weights: " + str(bestWeights))
        #     print("Number of Propogations: " + str(int(count/4)))
        #     print("")
        #     return 1
        # if count>400000 and bestError>0.2:
        #     print('o'+str(bestError))
        #     return Error()

        count+=1
x = Error()

